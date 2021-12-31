#%%
import pandas as pd
import matplotlib.pyplot as plt

# %%
df= pd.read_csv("FoodPrice_in_Turkey.csv")
df
#%%
df.info()

# %%
df_food = df.groupby(["ProductName"])["Price"].mean()
df_food

# %%
