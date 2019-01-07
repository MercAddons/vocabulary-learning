import tkinter as tk
from _sqlite3 import Row

class VocabularyView(object):
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
        
        self.wordLab = tk.Label(self.frame, text = 'Word')
        self.wordLab.grid(column = 1, row = 0, sticky = tk.W)
        
        self.translationLab = tk.Label(self.frame, text = 'Translation')
        self.translationLab.grid(column = 1, row = 1, sticky = tk.W)
        
        self.wordString = tk.StringVar()
        self.translationString = tk.StringVar()
        
        self.wordEntry = tk.Entry(self.frame, width = 20, textvariable = self.wordString)
        self.wordEntry.grid(column = 2, row = 0, padx = 10)

        self.translationEntry = tk.Entry(self.frame, width = 20, textvariable = self.translationString)        
        self.translationEntry.grid(column = 2, row = 1, padx = 10)
        
        
        self.checkButton = tk.Button(self.frame, text = "Check")
        self.checkButton.grid(column = 0, row = 2, pady = 10, sticky = tk.W)
        
        self.addButton = tk.Button(self.frame, text = 'Add word')
        self.addButton.grid(column = 1, row = 2, pady = 10, sticky = tk.W)
        
        self.changeButton = tk.Button(self.frame, text = 'Switch language')
        self.changeButton.grid(column = 2, row = 2, pady = 10, sticky = tk.W)
        
        self.restartButton = tk.Button(self.frame, text = "Restart")
        self.restartButton.grid(column = 3, row = 2, pady = 10, sticky = tk.W)
        
        self.resultString=tk.StringVar()
        self.resultLabel = tk.Label(self.frame, textvariable=self.resultString)
        self.resultLabel.grid(column=2, row=3, padx=10, sticky=tk.W)
        
        
    
    def getWordString(self):
        return self.wordString.get()
    
    def setWordString(self, word):
        self.wordString.set(word)

    def getTranslationString(self):
        return self.translationString.get()
    
    def setTranslationString(self, translation):
        self.translationString.set(translation)
        
    def setResultString(self, result):
        self.resultString.set(result)
        
        