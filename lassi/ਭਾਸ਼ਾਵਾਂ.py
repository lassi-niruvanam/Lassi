from pkg_resources import resource_filename
import json

doc_json = resource_filename('lassi', 'ਭਾਸ਼ਾਵਾਂ.json')

with open(doc_json, encoding='utf8') as d:
    ਭਾਸ਼ਾਵਾਂ = json.load(d)
