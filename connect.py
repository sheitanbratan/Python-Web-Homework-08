from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'USER')
mongo_pass = config.get('DB', 'PASS')
db_name = config.get('DB', 'DB_NAME')

URI = (
    f'mongodb+srv://{mongo_user}:{mongo_pass}@homework08.mbxw22h.mongodb.net/'
             f'?retryWrites=true&w=majority&appName=Homework08'
)


def create_connection():
    """Creating connection with MongoDB"""
    connect(db=db_name, host=URI, ssl=True)
    print(f'Successfully connected to {db_name}')


