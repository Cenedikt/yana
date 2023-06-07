import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

class Embedder():
    '''This class is an adaptation of the SentenceTransformer library for our purposes'''

    # Here are the different models we can use; for now, we can use fast and best
    fast = 'sentence-transformers/all-MiniLM-L6-v2'
    best = 'sentence-transformers/all-mpnet-base-v2'

    # Model initialization
    def __init__(self, model = best) -> SentenceTransformer:
        self = SentenceTransformer(model)
        return self

    def embed_corpus(self,data:pd.DataFrame|list):
        embedded_corpus =  self.encode(data,show_progress_bar=True,convert_to_tensor=True)
        print('All the posts have been embedded successfully!')
        return embedded_corpus
