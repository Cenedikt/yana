import pandas as pd
import pandas_gbq

from api_reddit_call import ApiRedditCall

from yana.params import *
class Data :

    def __init__ (self):
        self.api_call = ApiRedditCall()
        self.gcp_project_id = GCP_PROJECT_ID
        self.subbreddit = SUBREDDITS
        self.dataset_id_posts = DATASET_ID_POSTS
        self.dataset_id_comments = DATASET_ID_COMMENTS

    def save_posts (self) -> None:
        '''
        makes an api request to get Posts and saves the data into BiQuerry
        '''
        df = ApiRedditCall().get_posts(subreddit=self.subbreddit)

        pandas_gbq.to_gbq(df, f'{self.project_id}.{self.dataset_id_posts}."posts"', project_id=self.gcp_project_id, if_exists='')

    def load_posts(self)->pd.DataFrame:
        '''
        get the Posts from the BigQueery
        '''
        query = f'SELECT * FROM `{self.gcp_project_ID}.{self.dataset_id_posts}."posts"`'
        df = pandas_gbq.read_gbq(query, project_id=self.gcp_project_id)
        return df

    def get_post_id(self)->pd.DataFrame:
        '''
        get the Posts_id from the BigQueery
        '''
        query = f'SELECT id FROM `{self.gcp_project_ID}.{self.dataset_id_posts}."posts"`'
        df = pandas_gbq.read_gbq(query, project_id=self.gcp_project_id)
        return df

    def  save_comments(self) -> None:
        '''
        makes an api request to get comments and saves the data into BiQuerry
        '''
        self.get_post_id()

        df = ApiRedditCall().get_commets()

        pandas_gbq.to_gbq(df, f'{self.project_id}.{self.dataset_id_comments}."comments"', project_id=self.gcp_project_ID, if_exists='truncate')

    def load_comments(self)->pd.DataFrame:
        '''
        get the comments from the BigQueery
        '''
        query = f'SELECT * FROM `{self.gcp_project_ID}.{self.dataset_id_comments}."comments"`'
        df = pandas_gbq.read_gbq(query, project_id=self.gcp_project_id)
