from yana.data_logic.data import Data
'''
scrapes all the post and comments and saves the on BigQuerry
'''
data = Data()

data.save_posts()

data.save_comments()
