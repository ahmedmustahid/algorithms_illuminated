import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# Sample data: 25 random points
np.random.seed(42)
points = np.random.rand(25, 2) * 10

# Perform K-means clustering
n_clusters = 3  # You can change this to the desired number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(points)

# 1. Create a list of clusters
clusters = [[] for _ in range(n_clusters)]
for point, label in zip(points, kmeans.labels_):
    clusters[label].append(tuple(point))

# 2. Each list element contains (x,y) coordinates of points in each cluster
# This is already done in the previous step

# 3. Find the point at the edge closest to other clusters for each cluster
edge_points = []
for i, cluster in enumerate(clusters):
    other_points = np.array([p for j, c in enumerate(clusters) for p in c if j != i])
    distances = cdist(np.array(cluster), other_points)
    closest_point_index = np.argmin(np.min(distances, axis=1))
    edge_points.append(cluster[closest_point_index])

# Print results
for i, (cluster, edge_point) in enumerate(zip(clusters, edge_points)):
    print(f"Cluster {i + 1}:")
    print(f"  Points: {cluster}")
    print(f"  Edge point closest to other clusters: {edge_point}")
    print()