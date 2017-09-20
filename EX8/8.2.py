from pprint import pprint

###########

def parse_cdp_neighbors(st):
    device = st[:3]
    result = {}
    c = 0
    st = [i.strip() for i in st.split('\n')]
    for line in st:
        if c == 1:
            for i in range(len(line)-1):
                if i 
            '''
            line = [i for i in line.split('  ')]
            print(line)
            for i in line:
                if i == '': 
                    line.remove('')
            '''
            print(line)
            continue
        if line.startswith('Device'):
            c = 1
    #print(st)


f = open('sw1_sh_cdp_neighbors.txt', 'r')
st = ' '.join([i for i in f.readlines()])
pprint(parse_cdp_neighbors(st))
