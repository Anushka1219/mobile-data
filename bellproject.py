import pandas as pd
import plotly.figure_factory as px
import csv

df=pd.read_csv("mobiledata.csv")
fig=px.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"])
fig.show()

