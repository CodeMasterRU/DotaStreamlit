from pymongo import MongoClient
import os
import pandas as pd


client = MongoClient('localhost', 27017)
db = client['mydatabase']


def insert_document(collection, document):
    result = collection.insert_one(document)
    return result.inserted_id

def save_csv_files_to_mongodb(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                collection_name = os.path.basename(root)
                collection = db[collection_name]


                data = pd.read_csv(file_path)
                records = data.to_dict(orient='records')

          
                for record in records:
                    insert_document(collection, record)


data_directory = './DataTI/ti_data/'

save_csv_files_to_mongodb(data_directory)
