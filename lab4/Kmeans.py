from sklearn.cluster import KMeans
import numpy as np

data = np.array([[25, 50000], [30, 54000], [35, 58000], [40, 60000]])
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(data)
print("Cluster centers:", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)
##================================================

data = np.array([[1, 2], [2, 3], [3, 4], [8, 8], [9, 10], [10, 11]])
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
print("Nhãn phân cụm:", kmeans.labels_)
