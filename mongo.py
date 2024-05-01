import os
import pandas as pd
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['DataTI'] 


def save_to_mongodb(file_path, collection_name):

    data = pd.read_csv(file_path)
    

    data_dict = data.to_dict(orient='records')
    

    collection = db[collection_name]
    

    collection.insert_many(data_dict)
    print(f"Данные из файла {file_path} успешно сохранены в коллекцию {collection_name}")


for root, dirs, files in os.walk('DataTI/ti_data'):
    for file in files:
        if file.endswith('.csv'):

            collection_name = os.path.splitext(os.path.basename(file))[0] + '_' + os.path.basename(root)

            save_to_mongodb(os.path.join(root, file), collection_name)