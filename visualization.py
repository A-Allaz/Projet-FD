import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import folium

def visualize_geographical_distribution(df, output_file):
    fig = plt.figure(figsize=(10, 6))
    sns.scatterplot(x='long', y='lat', data=df, alpha=0.5, edgecolor=None, s=1)
    plt.title('Répartition géographique des photos')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    # plt.show()
    output_file.savefig(fig)

def visualize_word_cloud(df, output_file):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['cleaned_text']))
    fig = plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud des textes prétraités")
    # plt.show()
    output_file.savefig(fig)

def visualize_clusters(df, cluster_column, file_name):
    map_clusters = folium.Map(location=[45.75, 4.85], zoom_start=12)
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 
              'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 
              'lightgreen', 'gray', 'black', 'lightgray']
    for idx, row in df.iterrows():
        cluster_id = row[cluster_column]
        color = 'gray' if cluster_id == -1 else colors[cluster_id % len(colors)]
        folium.CircleMarker(location=[row['lat'], row['long']],
                            radius=5,
                            color=color,
                            fill=True).add_to(map_clusters)
    map_clusters.save(file_name)
