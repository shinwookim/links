import yaml
import re


output_dir = 'docs'

template = open("template.html", "r").read()

with open("links.yml") as links:
    links = yaml.safe_load_all(links)
    for link in links:
        with open(f'{output_dir}/{link["short-link"]}.html', 'x') as f:
            f.write(re.sub("{{URL}}", link['url'], template))
            f.close()
