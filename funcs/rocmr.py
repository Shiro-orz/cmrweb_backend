from .utils import load_json
import json 

pr_url = './src/pr.json'
pr1000_url = './src/pr1000.json'

pr_urls = {
    'dcmh': './src/dcmh.json',
    'rocmr': './src/rocmr.json',
    'finetune': './src/Finetune.json',
    'distillation': './src/Distillation.json'
}

pr1000_urls = {
    'dcmh': './src/dcmh1000.json',
    'rocmr': './src/rocmr1000.json',
#     'finetune': './src/finetune.json',
#     'dis': './src/dis.json'
}

tasks = ['it', 'ti', 'ii', 'tt']

def get_pr_data(type):
    if type == 'pr':
        data = load_json(pr_url)
    elif type == 'pr1000':
        data = load_json(pr1000_url)
    else:
        data = {}
    return data


def get_data(models, json_url):
    data = load_json(json_url)

    

def create_data(val):
    if 'thousand' in val.keys() and val['thousand'] == 'true':
        urls = pr1000_urls
    else:
        urls = pr_urls
    res = {'it':{}, 'ti':{}, 'ii':{}, 'tt':{}}
    for method in val['methods'].keys():
        if val['methods'][method] == []:
            continue 
        data = load_json(urls[method])
        models = val['methods'][method]
        for task in tasks:
            for datatype in data[task].keys():
                if datatype not in res[task].keys():
                    res[task][datatype] = {}
                for model in models:
                   res[task][datatype][model] = data[task][datatype][model]
    return res
