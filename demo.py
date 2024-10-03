#print documents.json file
import json
with open('documents.json', 'rt') as f:
    docs_raw  = json.load(f)
    print(docs_raw)
