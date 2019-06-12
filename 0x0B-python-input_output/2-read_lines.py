#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding='utf-8') as jfile:
        content = jfile.read()
        counter = text.count('\n')
        if nb_lines <= 0 or nb_lines >= counter:
            print(content, end='')
        else:
            splt = content.split('\n')
            while(len(splt) != nb_lines):
                splt.pop(-1)
            print('\n'.join(splt))
