import numpy as np 
import pandas as pd 
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def clusterization_list():
    headers = ['lat', 'lng']
    dataset = pd.read_csv("routes/file_cluster.csv", decimal=',', header=None)
    for col in dataset.columns[:1]:
        dataset[col] = dataset[col].astype(float)
    # del dataset[dataset.columns[2]]

    kmeans = KMeans(n_clusters=3, random_state=0).fit(dataset[dataset.columns[:1]])
    X_clustered = kmeans.fit_predict(dataset[dataset.columns[:1]])
    import pdb; pdb.set_trace()
    # plot_results(X_clustered, dataset)

    return X_clustered

def plot_results(X_clustered, dataset):

    LABEL_COLOR_MAP = {0 : 'red', 1 : 'blue', 2: 'green'}
    label_color = [LABEL_COLOR_MAP[l] for l in X_clustered]
    c1label = 'lat'
    c2label = 'lng'
    title = c1label + ' x ' + c2label
    plt.figure(figsize = (12,12))
    plt.scatter(dataset.iloc[:, 0],dataset.iloc[:, 1], c=label_color, alpha=0.3) 
    plt.xlabel(c1label, fontsize=18)
    plt.ylabel(c2label, fontsize=18)
    plt.suptitle(title, fontsize=20)
    plt.savefig(title + '.png')
    plt.show()
