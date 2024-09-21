import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from collections import defaultdict
from typing import List, Tuple, Dict, Iterable
from numpy.typing import NDArray
import heapq
import pprint
import math



def getClusters(points: Iterable, n_clusters: int)->defaultdict[str, List[Tuple[float,float]]]:
    """
     Perform K-means clustering. Get clusters with points
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(points)

    # 1. Create a dict of clusters
    clusters = defaultdict(list)
    for point, label in zip(points, kmeans.labels_):
        label = "c"+str(label)
        clusters[label].append(tuple(point))
    
    return clusters

def convertPointToID(point: Tuple[float, float], idToxy:Dict[int, Tuple[float, float]]):
    import math 
    thresh = 1e-4
    for k,v in idToxy.items():
        dist = math.dist(point, v)
        if dist < thresh:
            return k


def getClustersOfIds(clustersDict: defaultdict[List[Tuple[float,float]]], idToxy: Dict[int, Tuple[float, float]]):
    idClusters = defaultdict(list)

    for clusterKey, cluster in clustersDict.items():
        for point in cluster:
            id = convertPointToID(point, idToxy)
            idClusters[clusterKey].append(id)
    return idClusters

# 2. Each list element contains (x,y) coordinates of points in each cluster
# This is already done in the previous step

def edgePointsFromClusters(clusters:Dict[str, List[Tuple[float,float]]], idToxy)->List[Tuple[float,float]]:
    # 3. Find the point at the edge closest to other clusters for each cluster
    edge_point_ids = []
    travelled = set()
    idxes = dict()
    for cid,cluster in clusters.items():
        minCluster2Dist = []
        for cid2, cluster2 in clusters.items():
            if cid==cid2:
                continue
            if set(frozenset((cid,cid2))) in travelled:
                continue
                
            #calculate minimum distance in an array
            minDist = np.inf
            for i, p in enumerate(cluster):
                for j, p2 in enumerate(cluster2):
                    dist = math.dist(p,p2)
                    if dist < minDist:
                        minDist = dist
                        # id1 = convertPointToID(p, idToxy)#id1 from key cluster
                        # id2 = convertPointToID(p2, idToxy)#id2 from value cluster 
                        # # idxes[cid][cid2]=((id1,id2), round(minDist,2))
                        # idxes[frozenset((cid, cid2))]=((id1,id2), minDist)
                        minDist = round(minDist, 2)
                        heapq.heappush(minCluster2Dist, (minDist,((cid,cid2),(p,p2))))
            travelled.add(frozenset((cid, cid2)))
        if cid==cid2:
            continue
        mdist, m = heapq.heappop(minCluster2Dist) 
        print(mdist)
        print(m)
        key, (p1, p2) = m
        id1 = convertPointToID(p1, idToxy)
        id2 = convertPointToID(p2, idToxy)
        idxes[frozenset(key)] = ((id1, id2), mdist)
        # break
    return idxes
    # for i, cluster in clusters.items():
    #     other_points = np.array([p for j, c in clusters.items() for p in c if j != i])
    #     distances = cdist(np.array(cluster), other_points)
    #     closest_point_index = np.argmin(np.min(distances, axis=1))
    #     edge_points.append(cluster[closest_point_index])
    # return edge_points

# def edgePointsFromClustersByID(clusters:List[List[Tuple[float,float]]])->List[Tuple[float,float]]:



if __name__=="__main__":

    # Sample data: 25 random points
    np.random.seed(42)
    points = np.random.rand(25, 2) * 10

    clusters = getClusters(points=points, n_clusters=3)
    pprint.pprint(clusters) 


    edge_points = edgePointsFromClusters(clusters)
    pprint.pprint(edge_points)


    # Print results
    # for i, (cluster, edge_point) in enumerate(zip(clusters.keys(), edge_points)):
    #     print(f"Cluster {i + 1}:")
    #     print(f"  Points: {cluster[i]}")
    #     print(f"  Edge point closest to other clusters: {edge_point}")
    #     print()