import praw
import pandas as pd

class API_get_comments:

    def __init__(self) -> None:
        pass

    def get_commets(post_id: str ) -> pd.DataFrame :
        '''
        gets all the comments from a post
        Params:
            post_id: takes the id of a post as a String
        Return: retursn a Dataframe with all the importen information of the Comment
        '''
        reddit = praw.Reddit(
            client_id= CLIENT_ID,
            client_secret= CLIENT_SECRET,
            user_agent= USER_AGENT,
        )

        post = reddit.submission(id=post_id)
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
