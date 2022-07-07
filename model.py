#@title Install dependencies

import os
import yaml
import torch
from torch import package

    
def punctuation(s):
    torch.hub.download_url_to_file('https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml',
                               'latest_silero_models.yml',
                               progress=False)

    with open('latest_silero_models.yml', 'r',encoding="utf8") as yaml_file:
        models = yaml.load(yaml_file, Loader=yaml.SafeLoader)
    model_conf = models.get('te_models').get('latest')
# see avaiable languages
    available_languages = list(model_conf.get('languages'))
    print(f'Available languages {available_languages}')

# and punctuation marks
    available_punct = list(model_conf.get('punct'))
    print(f'Available punctuation marks {available_punct}')
    model_url = model_conf.get('package')

    model_dir = "downloaded_model"
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, os.path.basename(model_url))

    if not os.path.isfile(model_path):
      torch.hub.download_url_to_file(model_url,
                                   model_path,
                                   progress=True)

    imp = package.PackageImporter(model_path)
    model = imp.load_pickle("te_model", "model")
    example_texts = model.examples
    def apply_te(text, lan='en'):
       return model.enhance_text(text, lan)
    input_text =s
    print("ooooo")
    ##print(apply_te(input_text, lan='en'))
   
    