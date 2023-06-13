import pandas as pd
import numpy as np
from colorama import Fore, Style


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
        for index, row in data.iterrows():
            selftext = row['selftext']
            title = row['title']
            print(f'{index} {len(selftext)} {len(title)}')
            if selftext =='':
                if len(title) <= 72 :
                    df_ = data.drop(index)
            elif len(selftext) <= 72 :
                data = data.drop(index)

        print(f"✅ Data has been cleaned")
        data.author = data.author.map(lambda x : str(x))
        return data

    def preprocessor_comments(self, data: pd.DataFrame) -> pd.DataFrame:
        '''
        removes all comments where the lengt of the body is smaler than 72 chars and
        Params:
            data: takes a DataFrame as an input
        return : returns an DataFrame
        '''
        print(f'start cleaning data.....')
        for index, row in data.iterrows():
            body = row['body']
            if len(body) <= 72 :
                df_ = data.drop(index)
        df_.author = df_.author.map(lambda x : str(x))
        print(f"✅ Data has been cleaned")
        return df_

if __name__ == '__main__' :
    import pandas
    path='/home/cenedikt/code/Cenedikt/yana/yana/data/depression_dataset_reddit_cleaned.csv'

    df = pandas.read_csv(path)
    prep = Preprocessor()
    print(df)
    df = prep.preprocessor_post(df)
    print(df)
