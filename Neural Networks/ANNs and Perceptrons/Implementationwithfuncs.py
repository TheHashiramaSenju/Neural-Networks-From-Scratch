import numpy as np 
import matplotlib.pyplot as plt
from sklearn.dataset import make_blobs
import seaborn as sns 

X, Y = make_blobs(n_samples=500, centers = 2, n_features = 2, random_state = 10)
print(X.shape, Y.shape)
output = (500,2), (500,)

sns.scatterplot(X[:,0],X[:,1],c=Y,cmap = plt.cm.Accent)