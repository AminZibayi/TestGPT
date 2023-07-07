```python
import json
from forestry_api import ForestryAPI
from tina_cms_api import TinaCMSAPI

FORESTRY_DATA_DIR = "forestry_data"
TINA_CMS_DATA_DIR = "tinaCMS_data"

def extract_forestry_data(file_name):
    with open(f"{FORESTRY_DATA_DIR}/{file_name}", "r") as file:
        data = json.load(file)
    return data

def insert_tina_data(file_name, data):
    with open(f"{TINA_CMS_DATA_DIR}/{file_name}", "w") as file:
        json.dump(data, file)

def migrate_data(file_name):
    forestry_data = extract_forestry_data(file_name)
    insert_tina_data(file_name, forestry_data)

def main():
    forestry_api = ForestryAPI()
    tina_cms_api = TinaCMSAPI()

    file_names = ["posts.json", "pages.json", "settings.json"]

    for file_name in file_names:
        migrate_data(file_name)

    print("Migration completed successfully.")

if __name__ == "__main__":
    main()
```