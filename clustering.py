from sklearn.cluster import KMeans, DBSCAN
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.preprocessing import StandardScaler
import pandas as pd

def perform_clustering(df):
    # Sample for clustering
    df = df.sample(n=10000, random_state=0)
    coords = df[['lat', 'long']].values
    scaler = StandardScaler()
    coords_scaled = scaler.fit_transform(coords)

    # Hiérarchique
    Z = linkage(coords_scaled, method='ward')
    max_d = 0.5
    df['hierarchical_cluster'] = fcluster(Z, max_d, criterion='distance')

    # K-Means
    kmeans = KMeans(n_clusters=5, random_state=0)
    df['kmeans_cluster'] = kmeans.fit_predict(coords_scaled)

    # DBSCAN
    dbscan = DBSCAN(eps=0.05, min_samples=10)
    df['dbscan_cluster'] = dbscan.fit_predict(coords_scaled)

    return df
