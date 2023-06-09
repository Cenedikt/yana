import pandas as pd
import pandas_gbq
import os
from tqdm import tqdm

from yana.data_logic.api_reddit_call import ApiRedditCall
from yana.data_logic.preprocessor import Preprocessor

from yana.params import *
class Data :

    def __init__ (self):
        self.api_call = ApiRedditCall()
        self.prep = Preprocessor()
        self.gcp_project_id = GCP_PROJECT_ID
        self.dataset_id = BQ_DATASET
        self.table_posts = 'posts'
        self.table_comments = 'comments'

    def save_posts (self) -> None:
        '''
        makes an api request to get Posts and saves the data into BiQuerry
        '''
        print(f'start saving the Data.....')
        df = self.api_call.get_posts()
        df = self.prep.preprocessor_post(df)
        pandas_gbq.to_gbq(df, f'{self.gcp_project_id}.{self.dataset_id}.{self.table_posts}', project_id=self.gcp_project_id, if_exists='replace')
        print(f"✅ Data saved to bigquery")

    def load_posts(self)->pd.DataFrame:
        '''
        get the Posts from the BigQueery
        '''
        print(f'start loding the Posts from Bigquerry.....')
        query = f'SELECT * FROM `{self.gcp_project_id}.{self.dataset_id}.{self.table_posts}`'
        df = pandas_gbq.read_gbq(query, project_id=self.gcp_project_id)
        print(f"✅ Data has been to bigquery")
        return df

    def get_post_id(self)->pd.DataFrame:
        '''
        get the Posts_id from the BigQueery
        '''
        print(f'start loding the Posts:id from Bigquerry.....')
        query = f'SELECT id FROM `{self.gcp_project_id}.{self.dataset_id}.{self.table_posts}`'
        df = pandas_gbq.read_gbq(query, project_id=self.gcp_project_id)

        print(f"✅ Data has been loaded from bigquery")
        return df

    def  save_comments(self) -> None:
        '''
        makes an api request to get comments and saves the data into BiQuerry
        '''
        print(f'start saving the Data.....')
        df_post_id = self.get_post_id().iloc[0:300,:]
        df = pd.DataFrame()
        progress_bar = tqdm(total=df_post_id.shape[0], unit='iteration')

        for index, row in df_post_id.iterrows():
            id = row['id']
            df_ = self.api_call.get_commets(id)
            df = pd.concat([df,df_], ignore_index=True)
            progress_bar.update(1)
        df = self.prep.preprocessor_comments(df)
        progress_bar.close()
        print(f"✅ Comments has been scrapped ")
        pandas_gbq.to_gbq(df, f'{self.gcp_project_id}.{self.dataset_id}.{self.table_comments}', project_id=self.gcp_project_id, if_exists='replace')
        print(f"✅ Data saved to bigquery")


    def load_comments(self)->pd.DataFrame:
        '''
        get the comments from the BigQueery
        '''
        print(f'start loding the comments from Bigquerry.....')
        query = f'SELECT * FROM `{self.gcp_project_id}.{self.dataset_id}.{self.table_comments}`'
        df = pandas_gbq.read_gbq(query, project_id=self.gcp_project_id)

        print(f"✅ Data has been loaded from bigquery")
        return df

    def save_as_csv(self):
        '''
        creats csv from the data of the from bigQuerry
        '''
        prefix = '.csv'
        current_directory = os.path.abspath(os.path.dirname(__file__))
        path_posts = os.path.join(current_directory,'..','data','posts')+prefix
        path_comments = os.path.join(current_directory,'..','data', 'comments')+prefix
        df_posts = self.load_posts()
        df_comments = self.load_comments()

        df_posts.to_csv(path_posts, index=False)
        df_comments.to_csv(path_comments, index=False)

        return df_posts, df_comments
