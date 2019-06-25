# import block
import sys
import os
import site
import subprocess
import json
import platform
import yaml
from pip._internal.operations.freeze import freeze

v = platform.python_version()
el = os.path.abspath(os.path.dirname(sys.argv[0]))
spl = site.getsitepackages()
wpip = subprocess.getoutput("which pip")
instpacks = subprocess.getoutput("pip freeze")
pypath = sys.path
e = os.environ['VIRTUAL_ENV'].split('/')
env_name = e[len(e) - 1]
inst_packs = []
for requirements in freeze(local_only=True):
    inst_packs.append(requirements)


def info():
    print('1.Python version is:', v)
    print('2.Name of virtual environment:', env_name)
    print('3.Executable location is', el)
    print('4.Pip location:', wpip)
    print('5.PYTHONPATH:', ', '.join(pypath))
    print('6.Installed packages:', ', '.join(inst_packs))
    print('7.Site packages location:', ', '.join(spl))


info()

# add yaml
data = dict(
    Installed_packages=str(', '.join(inst_packs)),
    PYTHONPATH=str(', '.join(pypath)),
    Pip_location=wpip,
    Executable_location=str(el),
    Name_of_virtual_environment=str(env_name),
    Python_version=str(v),
)
with open('python_info.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

# add json
file = open("python_info.json", "w")
prints = json.dumps({
    "Installed_packages": str(', '.join(inst_packs)),
    "PYTHONPATH": str(', '.join(pypath)),
    "Pip_location": wpip,
    "Executable_location": str(el),
    "Name_of_virtual_environment": str(env_name),
    "Python_version": str(v),
}, indent=4)
file.write(prints)
