
import json


## Bildschirm-Dumps
print(json.dumps(clara_model_batch, indent = 2, ensure_ascii = False))

print(json.dumps(clara_model_batch['outputs'][i]['data']['concepts'], indent=2))

print(json.dumps(response['outputs'][0]['data']['embeddings'], sort_keys=True, indent=2))


#
clara_res = {'clara_model_gen': clara_model_batch, 'clara_model_color': clara_model_batch_col, 'clara_model_vec': clara_model_batch_vec}


## save file
with open('cache\\' + 'clara_model_batch_all_raw_utf8.json', 'w', encoding='utf8') as fp:
    json.dump(clara_res, fp, indent = 2, ensure_ascii = False)


## load from json file
with open('cache\\' + 'final_data.json', encoding='utf8') as data_file:
    full_r = json.load(data_file)


