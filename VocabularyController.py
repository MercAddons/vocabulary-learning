import VocabularyModel as Model
import VocabularyView as View
import random
import tkinter as tk

class VocabularyController:
    """Implement the app Controller"""
    
    def __init__(self):
        self.english = True
        self.id = ''
        self.root = tk.Tk()
        self.model = Model.VocabularyModel()
        self.view = View.VocabularyView(self.root)
        self.view.checkButton.config(command=self.checkWords)
        self.view.addButton.config(command=self.addWord)
        self.word = ''
        self.translation = ''
        self.showNewWord()
        self.view.changeButton.config(command = self.changeLanguage)
        self.view.restartButton.config(command = self.restartSystem)
    
    def restartSystem(self):
        self.model.restartIds()
        self.showNewWord()
        self.view.setResultString("Restarted system")
    
    def showNewWord(self):
        if self.english:
            self.view.setWordString(self.getWord(self.english))
            self.view.setTranslationString("")
        else:
            self.view.setTranslationString(self.getWord(self.english))
            self.view.setWordString("")
            
    def showWord(self):
        if self.english:
            self.view.setWordString(self.word)
            self.view.setTranslationString("")
        else:
            self.view.setTranslationString(self.translation)
            self.view.setWordString("")
                
    def changeLanguage(self):
        self.english = not self.english
        self.model.restartIds()
        self.showNewWord()
        self.view.setResultString("Language switched")
        
    def checkWords(self):
        word = self.view.getWordString() 
        translation = self.view.getTranslationString()
        if self.word == word and self.translation == translation:
            if not self.model._ids and not self.model._idsFails:
                self.view.setResultString("Well done! Click Restart")
            else:                
                self.view.setResultString("Correct")
                self.showNewWord()  
        else:
            self.view.setResultString("Incorrect. %s is %s" % (self.word, self.translation))
            self.model.setAddIdsFails(self.id)
            self.showNewWord()  
        
        
    def getWord(self, ingles=True):
        word = "" 
        if not self.model.ids:
            if self.model.idsFails:
                self.model.updateIds()
        if  self.model.ids:
            self.id = self.calculateId()
            words = self.model.readWord(self.id)
            self.word = words['word']
            self.translation = words['translation']
            if ingles:
                word = self.word
            else:
                word = self.translation
        return word
            
    def addWord(self):
        word = self.view.getWordString()
        translation = self.view.getTranslationString()
        if translation != "" and word != "":
            self.model.createWord(word,translation)
            self.view.setResultString("Word added %s - %s" % (word,translation))
            self.showNewWord()
        else:
            self.view.setResultString("The fields can\'t be empty")
            self.showWord()
        
    def calculateId(self):
        ids = self.model.ids
        return random.choice(ids)
    
    def run(self):
        self.root.title("Vocabulary")
        self.root.deiconify()
        self.root.mainloop()
        
if __name__ == "__main__":
    c = VocabularyController()
    c.run()
        