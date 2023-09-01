import yaml
import re
import os

output_dir = 'docs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

template = open("template.html", "r").read()

with open("links.yml") as links:
    links = yaml.safe_load_all(links)
    for link in links:
        with open(f'{output_dir}/{link["short-link"]}.html', 'x') as f:
            f.write(re.sub("{{URL}}", link['url'], template))
            f.close()
