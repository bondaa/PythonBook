from pprint import pprint

###########

def parse_cdp_neighbors(st):
    device = [st[:st.find('>')]]
    result = {}
    c = 0
    a=[]
    count = 0
    st = [i.strip() for i in st.split('\n')]
    for line in st:
        if c == 1:
            for i in line.split('  '):
                if i != '':
                    a.append(i.strip())
                    count += 1
                if count == 6:
                    result[device[0] + ' ' + a[1]] = [a[0],a[5]]
                    count = 0
                    a.clear()
            continue
        if line.startswith('Device'):
            c = 1
    return(result)


f = open('sw1_sh_cdp_neighbors.txt', 'r')
st = ' '.join([i for i in f.readlines()])
pprint(parse_cdp_neighbors(st))
