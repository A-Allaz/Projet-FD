import pandas as pd

def load_and_clean_data(file_path):
    # Charger les données
    df = pd.read_csv(file_path, sep=',', low_memory=False)

    # Nettoyage des noms de colonnes
    df.columns = df.columns.str.strip()

    # Remplacer les valeurs manquantes dans 'tags' par une chaîne vide
    df['tags'] = df['tags'].fillna('')

    # Suppression des colonnes inattendues
    expected_columns = ['id', 'user', 'lat', 'long', 'tags', 'title', 
                        'date_taken_minute', 'date_taken_hour', 'date_taken_day', 
                        'date_taken_month', 'date_taken_year', 'date_upload_minute', 
                        'date_upload_hour', 'date_upload_day', 'date_upload_month', 
                        'date_upload_year']
    df = df.loc[:, df.columns.isin(expected_columns)]

    # Suppression des doublons et lignes invalides
    df = df.drop_duplicates()
    df = df.dropna(subset=expected_columns)
    for col in ['id', 'lat', 'long', 'date_taken_minute', 'date_taken_hour', 
                'date_taken_day', 'date_taken_month', 'date_taken_year', 
                'date_upload_minute', 'date_upload_hour', 'date_upload_day', 
                'date_upload_month', 'date_upload_year']:
        df = df[pd.to_numeric(df[col], errors='coerce').notnull()]

    print(f"Nombre de lignes après nettoyage : {len(df)}")
    return df
