import pandas as pd
import praw
from tqdm import tqdm

from yana.params import *

class ApiRedditCall :

    def __init__(self) -> None:
        self.reddit = praw.Reddit(
            client_id= CLIENT_ID,
            client_secret= CLIENT_SECRET,
            redirect_uri= REDIRECT_URI,
            user_agent= USER_AGENT,
        )
        self.subreddits = SUBREDDITS

    def get_posts(self) -> pd.DataFrame:
        '''
        creates an API request to Reddit and scrabbes the Subbredit
        Return: returns a Df with the important information of the post
        '''
        progress_bar = tqdm(total=len(self.subreddits), unit='iteration')

        posts = {}
        index = 0

        for subreddit in self.subreddits:
            try:
                subreddit_request = self.reddit.subreddit(subreddit)

                submissons = subreddit_request.top(limit=1000)

                columns=['id','author','title','subreddit','selftext','ups','permalink']

                for post in submissons :
                    posts[index]= [
                        post.id,
                        post.author,
                        post.title,
                        post.subreddit.display_name,
                        post.selftext,
                        post.ups,
                        post.permalink
                    ]
                    index +=1
                    progress_bar.update(1)
            except:
                progress_bar.update(1)

        df = pd.DataFrame.from_dict(posts,orient='index' ,columns=columns)
        progress_bar.close()
        print(f"✅ Post has been scrapped")

        return df

    def get_commets(self, post_id: str) -> pd.DataFrame :
        '''
        gets all the comments from a post
        Params:
            post_id: takes the id of a post as a String
        Return: retursn a Dataframe with all the importen information of the Comment
        '''
        comments = {}
        index = 0
        columns=['id','author','body','ups','post_id']
        try:
            post = self.reddit.submission(id=post_id)
            post.comments.replace_more(limit=10)

            for comment in post.comments.list():
                comments[index] = [
                    comment.id,
                    comment.author,
                    comment.body,
                    comment.ups,
                    comment.link_id
                    ]
                index +=1
        except:
            print(f'no comment for the post {post_id}')
        df = pd.DataFrame.from_dict(comments,orient='index' ,columns=columns)

        return df

    def get_used_requests(self)->int:
        used_requests = self.reddit.auth.limits['used']
        print(f"Used requests:", {used_requests})
        return used_requests
