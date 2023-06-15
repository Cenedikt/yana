import numpy as np
import pandas as pd
import requests
import json
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search, torch
import os
import openai

# Get the current directory path
current_dir = os.path.dirname(os.path.realpath(__file__))
print(current_dir)
# Define the relative path to your files
relative_path_embedding_pt = "./data/embedding.pt"
relative_path_posts = "./data/posts.csv"
relative_path_comments = "./data/comments.csv"

# Get the absolute path

absolute_path_embeddings = os.path.abspath(os.path.join(current_dir, relative_path_embedding_pt))
absolute_path_posts = os.path.abspath(os.path.join(current_dir, relative_path_posts))
absolute_path_comments = os.path.abspath(os.path.join(current_dir, relative_path_comments))
print(absolute_path_posts)


class Model1_1():
    '''This class is an adaptation of the SentenceTransformer library for our purposes'''

    # Here are the different transformers we can use; for now, we can use fast and best
    fast = 'sentence-transformers/all-MiniLM-L6-v2'
    best = 'sentence-transformers/all-mpnet-base-v2'

    # Model initialization
    def __init__(self, model = fast) -> None:
        self.model = SentenceTransformer(model)
        return None

    # EMBED
    def embed(self,data:pd.DataFrame|list|str, save = False):
        '''Method that embeds new text (either document corpus or queries) into the multidimensional vector space

        Args:
            - data: data to be embedded as pd.Series of strings, list of strings, or string
            - save: True if you want to save the embeddings tensor as .pt (default False)'''

        # If the input is a dataframe, this part extracts the relevant text to be embedded

        if type(data) == pd.DataFrame:
            df = data['selftext']#.astype('string')#data.apply(lambda row: row['selftext'] if pd.notnull(row['selftext']) and row['selftext'].strip() != '' else row['title'], axis=1)
        else:
            df = data



        embedded =  self.model.encode(df,show_progress_bar=True,convert_to_tensor=True)
        print('Your input has been embedded successfully!')



        if save == True:
           torch.save(embedded, absolute_path_embeddings) #USE ABSOLUTE PATHS, get using python methods (os.path.join)
           print('Embedding saved as yana/yana/data/embedding.pt')
        return embedded

    # SEARCH
    def search(self, query:str, corpus_embeddings = None, results:int = 3):
        '''This is our main search method. Takes query, returns closest matches.

        Args:
            - query: user input as string
            - corpus_embeddings: the vector embeddings of the corpus of text we want to search from as pytorch tensor
            - results: the number of matches to return (integer, default is 3)'''

        search_results = []

        if corpus_embeddings is None:
            data = absolute_path_embeddings

            corpus_embeddings = torch.load(data)

        query_embeddings = Model1_1.embed(self,query)
        pred = semantic_search(query_embeddings=query_embeddings, corpus_embeddings=corpus_embeddings,top_k=results)

        print(f'Your query was: {query}')
        print('\nHere are your closest matches:\n')

        with open(absolute_path_posts, 'r') as file:
            data = pd.read_csv(file)
            posts = data[['id','author','title','selftext','subreddit','ups']]

            for i,k in enumerate(pred[0]):
                #print(k)
                search_results.append(posts.iloc[k['corpus_id'],0:].to_dict())
                print(f"{i+1}: {posts.iloc[k['corpus_id'],0:]}")
                print('\n')

        print(query)
        return search_results



class Model1_2(Model1_1):
    '''This class an upgrade from Model1_1 that also performs additional operations on the search results'''

    # Here are the different transformers we can use; for now, we can use fast and best
    fast = 'sentence-transformers/all-MiniLM-L6-v2'
    best = 'sentence-transformers/all-mpnet-base-v2'

    def __init__(self, model = fast) -> None:
        self.model = SentenceTransformer(model)
        return None

    def query_llm(payload):
        data = json.dumps(payload)
        response = requests.request("POST","https://api-inference.huggingface.co/models/deepset/tinyroberta-squad2", headers = {"Authorization": "Bearer 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"}, json = payload)
        return response.json()

    def advice(self, user_query):
        '''This is the main function of the model: it performs a semantic search through Model1_1, and then looks for advice in the results'''

        # This is the prompt that will perform the advice inferrence from the context (the closest matches). It should be fixed, and we need to do prompt engineering to ensure the best results
        prompt = f"The user describes the following mental health struggle: {user_query}. Given this described struggle, you will look for possible advice to give to the user from the context data, which is composed of several related posts from mental health subreddits"
        #prompt = 'Summarize the following reddit posts'

        # Search for k closest matches
        model = Model1_1()
        search_results = model.search(query=user_query,results=3)

        # Retrieve comments of these posts and put them into the context

        ids = []
        for post in search_results:
            ids.append(f't3_{post["id"]}')



        with open(absolute_path_comments, 'r') as file:
            data = pd.read_csv(file)
            relevant_comments = data[data['post_id'].isin(ids)]
            relevant_comments_text = relevant_comments['body']
            context = ' '.join(relevant_comments_text)
            #print(data)


        if context != '':

            print(prompt)

            print('Initiating large language model...')

            openai.api_key = os.getenv("OPENAI_API_KEY")
            context_truncated = context[:5000]
            output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a mental health assistant with vast psychological knowledge, and your role is to assess a problem or struggle that the user will input, then look through the Reddit posts and comments that are given to you, and propose any advice or solutions that are mentioned by other users. Only use the content provided to provide advice."},
                {"role": "user",  "content": f"Here is my issue: {user_query}"},
                {"role": "assistant", "content": f"Here are the comments of posts that are similar to the user's issue:{context_truncated}"}
            ]
            )


            search_results.append({'advice': output.choices[0].message['content']})
        else:
            output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a mental health assistant with vast psychological knowledge, and your role is to assess a problem or struggle that the user will input. Since there are no comments from similar posts, you will provide a comforting message and suggest ways to get help."},
                {"role": "user",  "content": f"Here is my issue: {user_query}"},
            ]
            )

            search_results.append({'advice': output.choices[0].message['content']})
        return search_results
