from yana.ml_logic.models import Model1_1
from yana.ml_logic.data import Data

'''
creates all the importent files like csv and the emmbedet.pt file
'''
data = Data()

#it can be choosen between wast mode or best mode
model = Model1_1(mode='best')

df_posts, df_comments = data.save_as_csv()

model.embed(df_posts, save=True)
