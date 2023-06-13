from yana.models import Model1_1
from yana.models import Model1_2
import pandas as pd

posts = pd.read_csv('/Users/vladnicolescu/code/Cenedikt/yana/yana/data/posts.csv')
#posts = data['clean_text'].astype('string')
#posts
posts.head()

model = Model1_1()
query = 'I am sad'
model.search(query)
