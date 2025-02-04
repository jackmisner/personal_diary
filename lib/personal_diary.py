from datetime import date
import os

class Personal_Diary():
    def __init__(self, name):
        self.name = name
        self.diary = {}

    def make_snippet(self, string):
        first_five_words_list = []
        self.words_list = string.split()
        if len(self.words_list) == 0:
            raise Exception("No message passed")
        elif len(self.words_list) > 5:
            for i in range(5):
                first_five_words_list.append(self.words_list[i])
            return ' '.join(first_five_words_list)+'...'
        else:
            return ' '.join(self.words_list)
        
    def add_entry(self, string):
        self.string = string
        if self.diary.get(date.today().strftime("%d/%m/%Y")) == None:
            self.diary[date.today().strftime("%d/%m/%Y")] = string
        else:
            self.diary[date.today().strftime("%d/%m/%Y")] += ', ' + string
        
    def list_entries(self):
        return list(self.diary.items())

    def count_words(self, string):
        self.string = string
        if len(self.string.split()) == 0:
            raise Exception("empty string")
        else:
            return len(self.string.split())