from mapproxy.wsgiapp import make_wsgi_app
from string import Template
import os

# render config template from environment variables

template_file = open('mapproxy.yaml.tmpl', 'r')
template = Template(template_file.read())
template_file.close()
output = template.substitute(wms_url=os.environ['WMS_URL'])

target_file = open('mapproxy.yaml', 'w')
target_file.write(output)
target_file.close()

application = make_wsgi_app('mapproxy.yaml')
