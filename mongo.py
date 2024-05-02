import os
import pandas as pd
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ti_data']

# Chemin vers le répertoire contenant les données
data_dir = 'ti_data'

# Parcourir les répertoires TI_year
for year_dir in os.listdir(data_dir):
    if os.path.isdir(os.path.join(data_dir, year_dir)):
        year = year_dir.split('_')[1]  # Extraire l'année du nom du répertoire
        year_collection = db[f"TI_{year}"]  # Créer une nouvelle collection pour l'année
        
        # Parcourir les fichiers CSV dans le répertoire de l'année
        for csv_file in os.listdir(os.path.join(data_dir, year_dir)):
            if csv_file.endswith('.csv'):
                csv_path = os.path.join(data_dir, year_dir, csv_file)
                df = pd.read_csv(csv_path)
                data_json = df.to_dict(orient='records')
                collection_name = os.path.splitext(csv_file)[0]
                year_collection[collection_name].insert_many(data_json)
                
                print(f"Données insérées dans la collection TI_{year}.{collection_name}")

print("Terminé !")


# import os
# import pandas as pd
# from pymongo import MongoClient


# client = MongoClient('localhost', 27017)
# db = client['DataTI'] 


# def save_to_mongodb(file_path, collection_name):

#     data = pd.read_csv(file_path)
    

#     data_dict = data.to_dict(orient='records')
    

#     collection = db[collection_name]
    

#     collection.insert_many(data_dict)
#     print(f"Данные из файла {file_path} успешно сохранены в коллекцию {collection_name}")


# for root, dirs, files in os.walk('DataTI/ti_data'):
#     for file in files:
#         if file.endswith('.csv'):

#             collection_name = os.path.splitext(os.path.basename(file))[0] + '_' + os.path.basename(root)

#             save_to_mongodb(os.path.join(root, file), collection_name)