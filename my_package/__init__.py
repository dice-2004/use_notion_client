import configparser
from notion_client import Client

def initialise_app():#clientをglobal化
    global client
    config = configparser.ConfigParser()
    config.read('./config.ini')
    api_key = config['DEFAULT']['API_KEY']
    client=Client(auth=api_key)
    return client

initialise_app()
