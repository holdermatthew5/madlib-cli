from madlib_cli.madlib import check

def test_check():
    dictionary = {
        "one": "first"
    }
    assert check(dictionary) == "I the first and two three have four five's six sister and plan to steal her seven eight!"