import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dataAnalysis import dengue_dataAnalysis
from dataAnalysis import lepto_dataAnalysis

def pie(state,year,dataset):
    matplotlib.use('TkAgg')
    y = np.array([dataset.loc[state,year + 'Cases'],dataset.loc[state,year + 'Deaths']])
    mylabels = ["Cases", "Deaths"]                
    plt.pie(y, labels = mylabels)
    plt.legend()
    plt.title("CASES VS DEATHS")
    circle = plt.Circle(xy=(0,0),radius = .73,facecolor = 'white')
    plt.gca().add_artist(circle)
    plt.show()


def bar(state,year,dataset):
    matplotlib.use('TkAgg')
    y = np.array([dataset.loc[state,year + 'Cases'],dataset.loc[state,year + 'Deaths']])
    x = [year + ' Cases',year + ' Deaths']
    plt.bar(x,y)
    plt.title("CASES VS DEATHS")
    plt.show()


def hbar(state,year,dataset):
    matplotlib.use('TkAgg')
    y = np.array([dataset.loc[state,year + 'Cases'],dataset.loc[state,year + 'Deaths']])
    x = [year + ' Cases',year + ' Deaths']
    plt.barh(x,y)
    plt.title("CASES VS DEATHS")
    plt.show()


def scatter(state,year,dataset):
    matplotlib.use('TkAgg')
    y = np.array([dataset.loc[state,year + 'Cases'],dataset.loc[state,year + 'Deaths']])
    x = [year + ' Cases',year + ' Deaths']
    plt.scatter(x,y)
    plt.title("CASES VS DEATHS")
    plt.show()

print("charts")