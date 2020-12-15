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
