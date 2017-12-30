from pkg_resources import resource_filename
import json

doc_json = resource_filename('lassi', 'ਜ਼ਬਾਨੋਂ.py')

with open(doc_json, encoding='utf8') as d:
    ਜ਼ਬਾਨੋਂ = json.load(d)
