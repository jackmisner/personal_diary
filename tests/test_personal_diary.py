import pytest
from lib.personal_diary import *
pd = Personal_Diary("Jack")

def test_make_snippet():
    result = pd.make_snippet("This message will get snipped because it is too long to show unabbreviated")
    assert result == 'This message will get snipped...'
    result = pd.make_snippet("This message wont get snipped")
    assert result == 'This message wont get snipped'
    # Testing that passing an empty string raises an Exception
    with pytest.raises(Exception) as e:
        pd.make_snippet('')
    error_message = str(e.value)
    assert error_message == "No message passed" 

def test_add_entry():
    result = pd.add_entry('This is my first diary entry')
    assert result == None

def test_list_entries():
    result = pd.list_entries()
    assert result == [('03/02/2025','This is my first diary entry')]

def test_count_words():
    result = pd.count_words('This entry has 5 words')
    assert result == 5
    with pytest.raises(Exception) as e:
        pd.count_words('')
    error_message = str(e.value)
    assert error_message == "empty string" 