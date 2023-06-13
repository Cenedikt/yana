import numpy as np
import pandas as pd
import requests
import json
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search, torch
import os

# Get the current directory path
current_dir = os.path.dirname(os.path.realpath(__file__))
# Define the relative path to your file
relative_path_embedding_pt = "./data/embedding.pt"
# Get the absolute path
relative_path_csv = "./data/depression_dataset_reddit_cleaned.csv"
absolute_path_csv = os.path.abspath(os.path.join(current_dir, relative_path_csv))
absolute_path = os.path.abspath(os.path.join(current_dir, relative_path_embedding_pt))


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
    def embed(self,data:pd.Series|list|str, save = False):
        '''Method that embeds new text (either document corpus or queries) into the multidimensional vector space

        Args:
            - data: data to be embedded as pd.Series of strings, list of strings, or string
            - save: True if you want to save the embeddings tensor as .pt (default False)'''

        # If the input is a dataframe, this part extracts the relevant text to be embedded

        if type(data) == pd.DataFrame:
            df = data.apply(lambda row: row['selftext'] if pd.notnull(row['selftext']) and row['selftext'].strip() != '' else row['title'], axis=1)



        embedded =  self.model.encode(df,show_progress_bar=True,convert_to_tensor=True)
        print('Your input has been embedded successfully!')



        if save == True:
            torch.save(embedded, absolute_path) #USE ABSOLUTE PATHS, get using python methods (os.path.join)
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
            data = absolute_path

            corpus_embeddings = torch.load(data)

        query_embeddings = Model1_1.embed(self,query)
        pred = semantic_search(query_embeddings=query_embeddings, corpus_embeddings=corpus_embeddings,top_k=results)

        print(f'Your query was: {query}')
        print('\nHere are your closest matches:\n')

        with open(absolute_path_csv, 'r') as file:
            data = pd.read_csv(file)
            posts = data['clean_text'].astype('string')

            for i,k in enumerate(pred[0]):
                #print(k)
                search_results.append(k['corpus_id'])
                print(f"{i+1}: {posts[k['corpus_id']]}")
                print('\n')

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


        model = Model1_1()
        search_results = model.search(query=user_query,results=10)
        context = ' '.join(search_results)

        print('Initiating large language model...')

        output = Model1_2.query_llm({
    	"inputs": {
    		"question": prompt,
    		"context": context
    	},
    })
        print(output)
        return output["answer"]
