from pprint import pprint

###########

def parse_cdp_neighbors(st):
    device = st[:3]
    result = {}
    c = 0
    a=[]
    st = [i.strip() for i in st.split('\n')]
    for line in st:
        if c == 1:
            #print(line)
            for i in line.split('  '):
                if i != '':
                    a.append(i.strip())
                    count += 1
                if count == 6:
                    result[device+]
            
            print(a)
                
            '''
            line = [i for i in line.split('  ')]
            print(line)
            for i in line:
                if i == '': 
                    line.remove('')
            '''
            continue
        if line.startswith('Device'):
            c = 1
    #print(st)


f = open('sw1_sh_cdp_neighbors.txt', 'r')
st = ' '.join([i for i in f.readlines()])
pprint(parse_cdp_neighbors(st))
