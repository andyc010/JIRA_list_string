# considered using unittest module, but using pytest instead
#import unittest

from ..JIRA_list_string import jiraListString

text_with_separator = ', '
testlist = ['one', 'two']
testoneitem = ['oneitem']

jira = jiraListString()

#def jiraListString():
#class testing_Program():


def test_twostrings():
    assert jira.add_separator_text(text_with_separator, testlist) == 'one, two'

def test_one_item():
    assert jira.add_separator_text(text_with_separator, testoneitem) == ''

def test_zero_items():
    assert jira.add_separator_text(text_with_separator, []) == ''
