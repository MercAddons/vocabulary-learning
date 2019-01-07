import sqlite_backend
import ingles_exceptions as ingles_exc

class VocabularyModel(object):
        
    def __init__(self):
        self._table_name = 'diccionary'
        self._connection = sqlite_backend.connect_to_db(sqlite_backend.DB_name)
        self._ids = sqlite_backend.restartIds(self._connection, self._table_name)
        self._idsFails = list()
        
    @property
    def connection(self):
        return self._connection
    
    @property
    def table_name(self):
        return self._table_name
    
    @property
    def ids(self):
        return self._ids
    
    def idsFails(self):
        return self._idsFails
    
    def updateIds(self):
        self._ids.clear()
        self._ids = self._idsFails[:]
        self._idsFails.clear()
    
    def setAddIdsFails(self, addId):
        print("addidsFails",addId)
        self._idsFails.append(addId)
        print("idsFails: ", self._idsFails)
    
    def createWord(self, word, translation):
        sqlite_backend.insert(self.connection, word, translation, table_name = self._table_name)
        self.restartIds()
        
    def restartIds(self):
        self._ids.clear()
        self._idsFails.clear()
        self._ids = sqlite_backend.restartIds(self.connection, self.table_name)
        
    def readWord(self, id_word):
        self.ids.remove(id_word)
        return sqlite_backend.select(self.connection, id_word, table_name = self._table_name)

    def getSize(self):
        return sqlite_backend.selectSize(self.connection, table_name = self._table_name)
    
    