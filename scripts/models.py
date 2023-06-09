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
    def __init__(self, model = fast) -> None:
        self.model = SentenceTransformer(model)
        return None

    # EMBED
    def embed(self,data:pd.Series|list|str, save = False):
        '''Method that embeds new text (either document corpus or queries) into the multidimensional vector space

        Args:
            - data: data to be embedded as pd.Series of strings, list of strings, or string
            - save: True if you want to save the embeddings tensor as .pt (default False)'''
        embedded =  self.model.encode(data,show_progress_bar=True,convert_to_tensor=True)
        print('Your input has been embedded successfully!')

        if save == True:
            torch.save(embedded,'../yana/data/embedding.pt') #USE ABSOLUTE PATHS, get using python methods (os.path.join)
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
            data = '../data/embedding.pt'
            corpus_embeddings = torch.load(data)

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

class Model1_2():
    '''This class an upgrade from Model1_1 that also performs additional operations on the search results'''

    # Here are the different transformers we can use; for now, we can use fast and best
    fast = 'sentence-transformers/all-MiniLM-L6-v2'
    best = 'sentence-transformers/all-mpnet-base-v2'
