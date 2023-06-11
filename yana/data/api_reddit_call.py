import pandas as pd
import praw

class ApiRedditCall :

    def __init__(self) -> None:
        self.reddit = reddit = praw.Reddit(
            client_id= CLIENT_ID,
            client_secret= CLIENT_SECRET,
            redirect_uri= REDIRECT_URI,
            user_agent= USER_AGENT,
        )

    def get_posts(self, subreddit: str, amount: int) -> pd.DataFrame:
        '''
        creates an API request to Reddit and scrabbes the Subbredit
        Params:
            subbredit: is an String and takes the name of a Subreddit
            amount: is an int and scrapes the amount of comments desc
        Return: returns a Df with the important information of the post
        '''

        subreddit_request = self.reddit.subreddit(subreddit)
        subreddit_request

        submissons = subreddit_request.top(limit=amount)

        index = 0
        posts = {}
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

        df = pd.DataFrame.from_dict(posts,orient='index' ,columns=columns)

        return df

    def get_commets(self, post_id: str ) -> pd.DataFrame :
        '''
        gets all the comments from a post
        Params:
            post_id: takes the id of a post as a String
        Return: retursn a Dataframe with all the importen information of the Comment
        '''
        post = self.reddit.submission(id=post_id)
        post.comments.replace_more(limit=None)

        comments = {}
        index = 0
        columns=['id','author','body','ups','post_id']

        for comment in post.comments.list():
            comments[index] = [
                comment.id,
                comment.author,
                comment.body,
                comment.ups,
                comment.link_id
                ]
            index +=1

        df = pd.DataFrame.from_dict(comments,orient='index' ,columns=columns)

        return df
