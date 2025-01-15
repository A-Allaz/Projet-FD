import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

# Charger le fichier CSV
file_path = 'flickr_data2.csv'
df = pd.read_csv(file_path, sep=',', low_memory=False)

# Nettoyage des noms de colonnes
df.columns = df.columns.str.strip()

# Aperçu des données
print("Aperçu des données :")
print(df.head())

# Remplacer les valeurs manquantes dans 'tags' par une chaîne vide
df['tags'] = df['tags'].fillna('')


# Suppression des lignes avec des colonnes en plus
expected_columns = ['id', 'user', 'lat', 'long', 'tags', 'title', 'date_taken_minute', 'date_taken_hour', 'date_taken_day', 'date_taken_month', 'date_taken_year', 'date_upload_minute', 'date_upload_hour', 'date_upload_day', 'date_upload_month', 'date_upload_year']
df = df.loc[:, df.columns.isin(expected_columns)]

# Suppression des doublons
df = df.drop_duplicates()

# Vérification et suppression des lignes avec des types de données non conformes
df = df.dropna(subset=expected_columns)  # Suppression des lignes avec des valeurs manquantes
for col in ['id', 'lat', 'long', 'date_taken_minute', 'date_taken_hour', 'date_taken_day', 'date_taken_month', 'date_taken_year', 'date_upload_minute', 'date_upload_hour', 'date_upload_day', 'date_upload_month', 'date_upload_year']:
    df = df[pd.to_numeric(df[col], errors='coerce').notnull()]

print(f"\nNombre de lignes après nettoyage : {len(df)}")

# Visualisation des données
print("\nVisualisation des données :")
df.hist(figsize=(20, 15))
plt.suptitle('Histogrammes des données')
plt.show()

# Analyse des tags
df['tags'] = df['tags'].fillna('')  # Remplacer les valeurs manquantes dans 'tags' par une chaîne vide
df['tags_list'] = df['tags'].apply(lambda x: x.split(','))  # Diviser les tags en listes

# Compter les occurrences des tags
all_tags = [tag for tags in df['tags_list'] for tag in tags]
tag_counts = Counter(all_tags)

# Top 10 des tags
top_tags = tag_counts.most_common(10)
print("\nTop 10 des tags les plus fréquents :")
for tag, count in top_tags:
    print(f"{tag}: {count}")

# Visualisation des tags les plus fréquents
top_tags_df = pd.DataFrame(top_tags, columns=['Tag', 'Count'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Tag', data=top_tags_df, palette='viridis', hue=None)
plt.title('Top 10 Tags les plus fréquents')
plt.xlabel('Nombre')
plt.ylabel('Tag')
plt.show()

# Visualisation géographique (scatterplot des coordonnées)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='long', y='lat', data=df, alpha=0.5, edgecolor=None)
plt.title('Répartition géographique des photos')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Exporter les données nettoyées (si nécessaire)
df.to_csv('flickr_cleaned.csv', index=False)