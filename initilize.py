from yana.models import Model1_1
from yana.data_logic.data import Data

data = Data()

df_posts, df_comments = data.save_as_csv()

model = Model1_1('best')

model.embed(df_posts, save=True)
