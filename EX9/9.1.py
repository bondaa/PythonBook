from sys import argv
import re

with open(argv[1], 'r') as f:
    for line in f:
        a = re.search(argv[2],line)
        if a != None:
            print(line)

# '^\S*0/1' - For interfzce 0/1                     9.1
# '^\S*0/[1,3] ' - For interfzce 0/1 and 0/3        9.1a
# '0/[1,3] ' - 9.1b but shortest                    9.1b
