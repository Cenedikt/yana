import pandas as pd
import numpy as np
from colorama import Fore, Style
from tqdm import tqdm

class Preprocessor:

    def __init__(self):
        self.hallo = 'hallo'

    def preprocessor_post(self, data: pd.DataFrame) -> pd.DataFrame:
        '''
        removes all post where the lengt of th ebody is smaler than 72 chars and
        if the body is emty if the title is smaler then 72 chars
        Params:
            data: takes a DataFrame as an input
        return : returns an DataFrame
        '''
        print(f'start cleaning data.....')
        progress_bar = tqdm(total=data.shape[0], unit='iteration')
        for index, row in data.iterrows():
            selftext = row['selftext']
            title = row['title']
            print(f'{index} {len(selftext)} {len(title)}')
            if selftext =='':
                if len(title) <= 72 :
                    data = data.drop(index)
            elif len(selftext) <= 72 :
                data = data.drop(index)
            progress_bar.update(1)
        progress_bar.close()
        data.author = data.author.map(lambda x : str(x))
        print(f"✅ Data has been cleaned")

        return data

    def preprocessor_comments(self, data: pd.DataFrame) -> pd.DataFrame:
        '''
        removes all comments where the lengt of the body is smaler than 72 chars and
        Params:
            data: takes a DataFrame as an input
        return : returns an DataFrame
        '''
        print(f'start cleaning data.....')
        progress_bar = tqdm(total=data.shape[0], unit='iteration')
        for index, row in data.iterrows():
            body = row['body']
            if len(body) <= 72 :
                data = data.drop(index)
            progress_bar.update(1)
        progress_bar.close()
        data.author = data.author.map(lambda x : str(x))
        print(f"✅ Data has been cleaned")
        return data
