import pytest
from lib.personal_diary import *
pd = Personal_Diary("Jack")

def test_make_snippet_long_string():
    assert pd.make_snippet("This message will get snipped because it is too long to show unabbreviated") == 'This message will get snipped...'
    
def test_make_snippet_short_string():
    assert pd.make_snippet("This message wont get snipped") == 'This message wont get snipped'

def test_make_snippet_empty_string():
    with pytest.raises(Exception) as e:
        pd.make_snippet('')
    assert str(e.value) == "No message passed" 

def test_add_entry():
    assert pd.add_entry('This is my first diary entry') == None

def test_list_entries():
    assert pd.list_entries() == [('04/02/2025','This is my first diary entry')]
 
def test_count_words_five_words():
    assert pd.count_words('This entry has 5 words') == 5

def test_count_words_empty_string():
    with pytest.raises(Exception) as e:
        pd.count_words('')
    assert str(e.value) == "empty string" 