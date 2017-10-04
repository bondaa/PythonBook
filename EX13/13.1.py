from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

def generate_cfg_from_template(template_path, var_path, trim_blocks=True, lstrip_blocks=True):
    if template_path.find('/') > 0:
        TEMPLATE_DIR, template = template_path.split('/')
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
                    trim_blocks=trim_blocks, lstrip_blocks=lstrip_blocks)
    else:
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        env = Environment(loader=FileSystemLoader(curr_dir),
                    trim_blocks=trim_blocks, lstrip_blocks=lstrip_blocks)
        template = template_path
    template = env.get_template(template)
    vars_dict = yaml.load(open(var_path))
    return(template.render(vars_dict))

print(generate_cfg_from_template(sys.argv[1], sys.argv[2]))
