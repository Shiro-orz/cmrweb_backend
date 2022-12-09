import json 

def load_json(url):
    with open(url) as f:
        return json.load(f)
