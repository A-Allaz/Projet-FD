from sklearn.feature_extraction.text import TfidfVectorizer
from mlxtend.frequent_patterns import apriori, association_rules
from visualization import visualize_word_cloud
import pandas as pd

def analyze_text(df, output_file):
    # Nettoyage textuel
    df['cleaned_text'] = df['tags'].fillna('') + ' ' + df['title'].fillna('')
    visualize_word_cloud(df, output_file)

    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=1000)
    tfidf_matrix = vectorizer.fit_transform(df['cleaned_text'])
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    tfidf_df['kmeans_cluster'] = df['kmeans_cluster']

    # Top terms par cluster
    for cluster in tfidf_df['kmeans_cluster'].unique():
        cluster_data = tfidf_df[tfidf_df['kmeans_cluster'] == cluster].drop(columns=['kmeans_cluster'])
        top_terms = cluster_data.mean(axis=0).sort_values(ascending=False).head(10)
        print(f"Cluster {cluster}: {', '.join(top_terms.index)}")

def extract_association_rules(df):
    binary_matrix = (df['cleaned_text'] != '').astype(int)
    binary_df = pd.DataFrame(binary_matrix, columns=['cleaned_text'])
    frequent_itemsets = apriori(binary_df, min_support=0.01, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1.0)
    print(rules.head())
