import pandas as pd
import praw

class ApiGetPosts :

    def __init__(self) -> None:
        pass

    def get_posts(subreddit: str, amount: int) -> pd.DataFrame:
        '''
        creates an API request to Reddit and scrabbes the Subbredit
        Params:
            subbredit: is an String and takes the name of a Subreddit
            amount: is an int and scrapes the amount of comments desc
        Return: returns a Df with the important information of the post
        '''
        reddit = praw.Reddit(
            client_id= CLIENT_ID,
            client_secret= CLIENT_SECRET,
            redirect_uri= REDIRECT_URI,
            user_agent= USER_AGENT,
        )

        subreddit_request = reddit.subreddit()
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
