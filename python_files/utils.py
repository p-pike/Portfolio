# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:06:12 2020

@author: ppike
"""

import datetime,pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Saving data to a pickle file
def save_to_pickle(data,filename):
    date = datetime.datetime.now()
    date = date.strftime('%Y-%m-%d_%H-%M')
    pickle.dump(data,open('pickle_files/'+filename+'_'+date+'.pickle','wb'))
    print(filename+'was saved in pickle_files/'+filename+'_'+date+'.pickle')
    
#loading data from pickle file   
def load_pickle(filepath):
    data  = pickle.load(open(filepath,'rb'))
    return data

#Plotting models scores 
def plot_scores(scores,names):
    sc = pd.DataFrame(index=names)
    sc['Score'] = scores

    sc.sort_values(by='Score',ascending=True,inplace=True)

    plot = plt.barh(y = np.arange(len(names)), width = sc['Score']*100, tick_label = sc.index)
    plt.axis(xmin = 60.0)
    plt.tight_layout()

    for i in plot.patches:
        plt.text(y=i.get_y()+0.2,x=i.get_width(),s='{}%'.format(round(i.get_width(),2)))
