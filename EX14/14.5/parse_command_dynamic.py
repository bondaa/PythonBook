import clitable
from pprint import *
output_str = 'output/sh_ip_int_br.txt'
dictn = {'Command': 'show ip int br', 'Vendor': 'Cisco'}

def parse_command_dynamic(dictn, output_str, index = 'index', template = 'template', printed = 'False'):
    out = []
    output_sh_ip_route_ospf = output_str
    cli_table = clitable.CliTable(index, template)

    cli_table.ParseCmd(output_sh_ip_route_ospf, dictn)

    data_rows = [list(row) for row in cli_table]
    header = list(cli_table.header)
    print('Formatted Table:\n', cli_table.FormattedTable())
    for row in data_rows:
        out.append(dict(zip(header,row)))
    return(out)
