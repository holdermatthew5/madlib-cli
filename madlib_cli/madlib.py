import re

def intro():
    print('Hi! Welcome to my madlib! Please enter the type of word requested. It can be any word or number (depending on what\'s requested), but each word cannot contain numbers and each number cannot contain letters.')
    read(template)

# def dictionary():

def check(dictionary):
    file = open('template.txt', 'r')
    file = file.read()
    one = re.sub('one', dictionary["one"], file)
    return one

# def write():