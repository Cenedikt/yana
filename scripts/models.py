import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search, torch

class Model1_1():
    '''This class is an adaptation of the SentenceTransformer library for our purposes'''

    # Here are the different transformers we can use; for now, we can use fast and best
    fast = 'sentence-transformers/all-MiniLM-L6-v2'
    best = 'sentence-transformers/all-mpnet-base-v2'

    # Model initialization
    def __init__(self, model = best) -> None:
        self.model = SentenceTransformer(model)
        return None

    # Method that embeds new text (either document corpus or queries) into the multidimensional vector space

    def embed(self,data:pd.DataFrame|list|str, save = False):
        '''Method that embeds new text (either document corpus or queries) into the multidimensional vector space

        Args:
            - data: data to be embedded
            - save'''
        embedded =  self.model.encode(data,show_progress_bar=True,convert_to_tensor=True)
        print('Your input has been embedded successfully!')
        return embedded

    # Our MAIN search method
    def search(self, query:str, corpus_embeddings = None, results:int = 3):
        '''This is our main search method. Takes query, returns closest matches.

        Args:
            - query: user input as string
            - embedded_corpus: the vector embeddings of the corpus of text we want to search from as pytorch tensor
            - results: the number of matches to return (integer, default is 3)'''

        search_results = []

        if corpus_embeddings is None:
            with open('../yana/data/kaggle_embeddings.csv', 'r') as file:
                data = pd.read_csv(file)
                corpus_embeddings = torch.tensor(data.drop(columns=['Unnamed: 0']).values)

        query_embeddings = Model1_1.embed(self,query)
        pred = semantic_search(query_embeddings=query_embeddings, corpus_embeddings=corpus_embeddings,top_k=results)

        print(f'Your query was: {query}')
        print('\nHere are your closest matches:\n')

        with open('../yana/data/depression_dataset_reddit_cleaned.csv', 'r') as file:
            data = pd.read_csv(file)
            posts = data['clean_text'].astype('string')

            for i,k in enumerate(pred[0]):
                #print(k)
                search_results.append(posts[k['corpus_id']])
                print(f"{i+1}: {posts[k['corpus_id']]}")
                print('\n')

        return search_results
