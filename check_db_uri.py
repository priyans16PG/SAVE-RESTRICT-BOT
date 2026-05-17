from pymongo.uri_parser import parse_uri
import os
env = {}
with open('.env', 'r', encoding='utf-8') as f:
    for line in f:
        line=line.strip()
        if line and not line.startswith('#'):
            if '=' in line:
                k,v=line.split('=',1)
                env[k]=v
uri = env.get('DB_URI')
print('DB_URI=', uri)
print('\nParsing:')
print(parse_uri(uri))
