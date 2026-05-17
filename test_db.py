import os
from pymongo import MongoClient


def load_db_uri(env_path='.env'):
    if not os.path.exists(env_path):
        return None
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('DB_URI='):
                return line.split('=', 1)[1]
    return None


def main():
    uri = load_db_uri()
    if not uri:
        print('DB_URI not found in .env')
        return
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        dbs = client.list_database_names()
        print('Connected — databases:')
        for d in dbs:
            print(' -', d)
    except Exception as e:
        print('Connection failed:', str(e))


if __name__ == '__main__':
    main()
