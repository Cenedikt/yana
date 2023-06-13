import pandas as pd
import pandas_gbq
from colorama import Fore, Style

from yana.data.api_reddit_call import ApiRedditCall

from yana.params import *
class Data :

    def __init__ (self):
        self.api_call = ApiRedditCall()
        self.gcp_project_id = GCP_PROJECT_ID
        self.dataset_id = BQ_DATASET
        self.table_posts = 'posts'
        self.table_comments = 'comments'

    def save_posts (self) -> None:
        '''
        makes an api request to get Posts and saves the data into BiQuerry
        '''
        print(f'start saving the Data.....')
        df = ApiRedditCall().get_posts()

        pandas_gbq.to_gbq(df, f'{self.gcp_project_id}.{self.dataset_id}.{self.table_posts}', project_id=self.gcp_project_id, if_exists='replace')
        print(f"✅ Data saved to bigquery")

    def load_posts(self)->pd.DataFrame:
        '''
        get the Posts from the BigQueery
        '''
        query = f'SELECT * FROM `{self.gcp_project_ID}.{self.dataset_id}.{self.table_posts}`'
        df = pandas_gbq.read_gbq(query, project_id=self.gcp_project_id)
        return df

    def get_post_id(self)->pd.DataFrame:
        '''
        get the Posts_id from the BigQueery
        '''
        query = f'SELECT id FROM `{self.gcp_project_ID}.{self.dataset_id}.{self.table_posts}`'
        df = pandas_gbq.read_gbq(query, project_id=self.gcp_project_id)
        return df

    def  save_comments(self) -> None:
        '''
        makes an api request to get comments and saves the data into BiQuerry
        '''
        self.get_post_id()

        df = ApiRedditCall().get_commets()
        print(df)
        #pandas_gbq.to_gbq(df, f'{self.gcp_project_id}.{self.dataset_id}.{self.table_comments}', project_id=self.gcp_project_ID, if_exists='truncate')

    def load_comments(self)->pd.DataFrame:
        '''
        get the comments from the BigQueery
        '''
        query = f'SELECT * FROM `{self.gcp_project_ID}.{self.dataset_id}.{self.table_comments}`'
        df = pandas_gbq.read_gbq(query, project_id=self.gcp_project_id)
