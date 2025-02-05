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
        
    def add_entry(self, title, contents):
        self.title = title
        self.contents = contents
        self.diary_entry = {title:contents}
        if self.diary.get(date.today().strftime("%d/%m/%Y")) == None:                         # If there is not already an entry for today's date
            self.diary[date.today().strftime("%d/%m/%Y")] = self.diary_entry                  # self.diary = {today's date:{title:contents}}
        else:                                                                                 # Today already has an entry in self.diary
            self.diary[date.today().strftime("%d/%m/%Y")].update(self.diary_entry)            # Append entry to existing entry for today

    def list_all_entries(self):
        return list(self.diary.items())
    
    def list_entry_from_given_date(self, date):
        return [entry for entry in self.diary.items() if entry[0] == date]

    def count_words_in_string(self, string):
        self.string = string
        if len(self.string.split()) == 0:
            raise Exception("empty string")
        else:
            return len(self.string.split())
        
    def count_words_in_entry(self, entry_title):
        entries_dict = list(self.diary.values())[0].items()
        for item in entries_dict:
            if item[0] == entry_title:
                entry_string = item[1]
        return self.count_words_in_string(entry_string)
        