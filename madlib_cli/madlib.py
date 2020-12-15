import re

def intro():
    print('Hi! Welcome to my madlib! Please enter the type of word requested. It can be any word or number (depending on what\'s requested), but each word cannot contain numbers and each number cannot contain letters.')
    words = [
        input('Adjective'),
        input('Adjective'),
        input('First Name'),
        input('Past Tense Verb'),
        input('First Name'),
        input('Adjective'),
        input('Adjective'),
        input('Plural Noun'),
    ]
    template = read_template('template.txt')
    string = parse_template(template, words)
    merge(string)
    print(string)

def read_template(path):
    file = open(path, 'r')
    file = file.read()
    return file

def parse_template(template, words):
    regex = [
        'one',
        'two',
        'three',
        'four', 
        'five',
        'six',
        'seven', 
        'eight',
    ]
    string = template
    i = 0
    while i < len(words):
        string = re.sub(regex[i], words[i], string)
        i += 1
    return string

def merge(string, template):
    print(string)
    file = open(template, 'w')
    file = file.write(string)

if __name__ == '__main__':
    intro()