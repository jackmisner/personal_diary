import pytest
from datetime import date
from lib.personal_diary import *
pd = Personal_Diary("Jack")

def create_2_entries_for_yesterday_and_2_entries_for_today():
    pd.diary = {'04/02/2025': {"Yesterday's 1st entry": 'This is my first diary entry', 'Second entry for yesterday': 'This is my second diary entry'}}
    pd.add_entry('Entry number 1 for today', 'I have been working on the diary program today')
    pd.add_entry('Entry number 2 for today', 'Continued working on the diary program')

def test_check_init_correctly_captures_name():
    assert pd.name == 'Jack'

def test_make_snippet_long_string():
    assert pd.make_snippet("This message will get snipped because it is too long to show unabbreviated") == 'This message will get snipped...'
    
def test_make_snippet_short_string():
    assert pd.make_snippet("This message wont get snipped") == 'This message wont get snipped'

def test_make_snippet_empty_string():
    with pytest.raises(Exception) as e:
        pd.make_snippet('')
    assert str(e.value) == "No message passed" 

def test_add_entry_to_empty_diary():
    assert pd.add_entry('First entry of today','This is my first diary entry') == None

def test_add_entry_existing_entry_for_today():
    assert pd.add_entry('First entry of today','This is my first diary entry') == None
    assert pd.add_entry('Second entry of today','This is my second diary entry') == None

def test_list_all_entries_single_entry():
    pd.diary = {}
    pd.add_entry('First entry of today','This is my first diary entry')
    assert pd.list_all_entries() == [(f'{date.today().strftime("%d/%m/%Y")}',{'First entry of today': 'This is my first diary entry'})]

def test_list_all_entries_multiple_entry():
    pd.diary = {}
    pd.add_entry('First entry of today','This is my first diary entry')
    assert pd.list_all_entries() == [(f'{date.today().strftime("%d/%m/%Y")}',{'First entry of today': 'This is my first diary entry'})]
    pd.add_entry('Second entry of today','This is my second diary entry')
    assert pd.list_all_entries() == [(f'{date.today().strftime("%d/%m/%Y")}',{'First entry of today': 'This is my first diary entry', 'Second entry of today': 'This is my second diary entry'})]

def test_list_all_entries_multiple_entry_over_multiple_days():
    create_2_entries_for_yesterday_and_2_entries_for_today()
    assert pd.list_all_entries() == [   ('04/02/2025',
                                            {
                                            "Yesterday's 1st entry": 'This is my first diary entry',
                                            'Second entry for yesterday': 'This is my second diary entry'
                                            }
                                        ),
                                        (
                                        '05/02/2025', 
                                            {
                                            'Entry number 1 for today': 'I have been working on the diary program today', 
                                            'Entry number 2 for today': 'Continued working on the diary program'
                                            }
                                        )
                                    ]

def test_list_entry_specific_day():
    pd.diary = {'04/02/2025':{"Yesterday's entry":'On Tuesday i started writing this program'}}
    pd.add_entry("Today's entry","On Wednesday i continued working on the diary program")
    assert pd.list_entry_from_given_date('04/02/2025') == [('04/02/2025', {"Yesterday's entry": 'On Tuesday i started writing this program'})]

def test_count_words_empty_string():
    with pytest.raises(Exception) as e:
        pd.count_words_in_string('')
    assert str(e.value) == "empty string" 

def test_count_words_five_words():
    assert pd.count_words_in_string('This entry has 5 words') == 5

def test_count_words_in_entry():
    pd.diary = {'04/02/2025':{"Yesterday's entry":'On Tuesday i started writing this program'}}
    pd.add_entry('First entry of today','This is my first diary entry')