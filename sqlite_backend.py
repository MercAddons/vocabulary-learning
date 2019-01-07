import sqlite3
from _sqlite3 import IntegrityError
import ingles_exceptions as ingles_exc

DB_name = 'vocabulary'

def connect_to_db(db=None):
    
    if db is None:
        mydb = ':memory:'
        print('New connection to in-memory SQLite DB...')
    else:
        mydb = '{}.db'.format(db)
        print('New connection to SQLite DB...')
    connection = sqlite3.connect(mydb)
    return connection

def insert(connection, word, translation, table_name):
    sql = "INSERT INTO {} ('word', 'translation') VALUES (?, ?)"\
        .format(table_name)
    try:
        connection.execute(sql,(word, translation))
        connection.commit()
    except IntegrityError as e:
        raise ingles_exc.WordAlreadyStored(
            '{}: "{}" already stored in table "{}"'.format(e,word,table_name))
        
def select(connection, id_word, table_name):
    sql = 'SELECT * FROM {} WHERE id="{}"'.format(table_name, id_word)
    c = connection.execute(sql)
    result = c.fetchone()
    if result is not None:
        return tuple_to_dict(result)
    else:
        raise ingles_exc.IdNotStored(
            'Can\'t read "{}" because it\'s not stored in table "{}"'.format(id_word,table_name))
     
def tuple_to_dict(result):
    rdict = dict()
    rdict['id'] = result[0]
    rdict['word'] = result[1]
    rdict['translation'] = result[2]
    return rdict

def selectSize(connection, table_name):
    sql = 'SELECT COUNT(*) FROM {}'.format(table_name)
    c = connection.execute(sql)
    result = c.fetchone()
    if result is not None:
        return result[0]
    else:
        raise ingles_exc.SizeNotFound(
            'The select of size doesn\'t work')
        
def restartIds(connection, table_name):
    size = selectSize(connection, table_name)
    ids = list(range(1,size+1))
    return ids
    