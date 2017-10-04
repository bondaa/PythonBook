from jinja2 import Environment, FileSystemLoader
import yaml
import sys

router_info = { 'hostname': 'R1' }

TEMPLATE_DIR = 'templates'
template = 'cisco_base.txt'
vars_dict = router_info

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
                  trim_blocks=True, lstrip_blocks=True)
template = env.get_template(template)

print(template.render(vars_dict))