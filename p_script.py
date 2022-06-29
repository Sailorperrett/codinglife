import pandas as pd
import flask as Flask
from rhino3dm import *

df = pd.DataFrame({'Name': ['Sailor'], 'Job': [
    'Student']})


df1 = df.applymap(str.upper)

print(df1)
