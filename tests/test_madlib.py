from madlib_cli.madlib import read_template
from madlib_cli.madlib import parse_template
from madlib_cli.madlib import merge

def test_read_template():
    assert 'I the one and two three have four five\'s six sister and plan to steal her seven eight!' == read_template("madlib_cli/template.txt")
