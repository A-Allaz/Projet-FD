from data_cleaning import load_and_clean_data
from visualization import visualize_geographical_distribution, visualize_word_cloud, visualize_clusters
from clustering import perform_clustering
from text_analysis import analyze_text, extract_association_rules
import matplotlib.backends.backend_pdf

def main():
    pdf = matplotlib.backends.backend_pdf.PdfPages("output.pdf")
    
    # Charger et nettoyer les données
    df = load_and_clean_data('flickr_data2.csv')

    # Visualisation géographique initiale
    visualize_geographical_distribution(df, pdf)

    # Clustering
    df = perform_clustering(df)

    # Visualisation des clusters
    visualize_clusters(df, 'kmeans_cluster', 'kmeans_clusters.html')
    visualize_clusters(df, 'dbscan_cluster', 'dbscan_clusters.html')
    visualize_clusters(df, 'hierarchical_cluster', 'hierarchical_clusters.html')

    # Analyse textuelle
    analyze_text(df, pdf)

    # Extraction de règles d'association
    # extract_association_rules(df)

    pdf.close()
    
    print("Processus terminé !")

if __name__ == "__main__":
    main()
