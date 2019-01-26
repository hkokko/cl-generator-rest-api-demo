# Very simple example to call generator REST API in Python
# Hannu Kokko, 2019
import requests
import ast
import json

def generate(generatorJson):
    url = "https://generator.campaign-logger.com/"
# generatorJson needs to be in json format
    response = requests.post(url, json = generatorJson)
    return response

#read the generator from the generator file. It is expected to be in the json format that generator expects
with open('generators/generator.json') as json_data:
    generatorJson = json.load(json_data)

response = generate(generatorJson)


teksti = response.text
# force the printout to be text.
x = ast.literal_eval(teksti)

print(x['result'])

