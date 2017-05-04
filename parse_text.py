# A script for converting any text into a file with unique words in lexicographic order


import re

def parse(text,output_filename,):
    with open(text, 'r', encoding="utf-8") as file:
        contents = file.read()
        words = contents.split()
        sorted_list = sorted([word.lower() for word in words])
        file = open(output_filename, 'w')
        repl_list = []
        for word in sorted_list:
            sub = re.sub(r'\W+', '', word)
            sub = re.sub(r'\d+', '', sub)
            repl_list.append(sub)
        repl_list = sorted(set(repl_list))
        for i in repl_list:
            file.write(i+'\n')
        file.close()
