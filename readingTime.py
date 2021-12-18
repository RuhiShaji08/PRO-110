import pandas as pd
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
#fig=ff.create_distplot([data],["result"],show_hist=False)
#fig.show()

def randomMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean
    

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_mean = randomMean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()



