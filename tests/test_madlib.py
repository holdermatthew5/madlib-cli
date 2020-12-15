from madlib_cli.madlib import read_template
from madlib_cli.madlib import parse_template
from madlib_cli.madlib import merge

def test_read_template():
    assert 'I the one and two three have four five\'s six sister and plan to steal her seven eight!' == read_template("madlib_cli/template.txt")

def test_parse_template():
    words = [
        'onet',
        'twot',
        'threet',
        'fourt', 
        'fivet',
        'sixt',
        'sevent', 
        'eightt',
    ]
    file = open('madlib_cli/template.txt', 'r')
    file = file.read()
    print(parse_template(file, words))
    assert parse_template(file, words) == 'I the onet and twot threet have fourt fivet\'s sixt sister and plan to steal her sevent eightt!'

def test_merge():
    string = 'I the onet and twot threet have fourt fivet\'s sixt sister and plan to steal her sevent eightt!'
    merge(string, 'madlib_cli/bare_template.txt')
    file = open('madlib_cli/bare_template.txt', 'r')
    file = file.read()
    assert file == string