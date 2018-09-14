try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from collections import defaultdict
import os

__version__ = None
exec(open("peasnaker/_version.py").read())
assert __version__

# Build a list of all project modules, as well as supplementary files
main_package = "peasnaker"
extensions = {".aplx", ".boot", ".cfg", ".json", ".sql", ".template", ".xml",
              ".xsd"}
main_package_dir = os.path.join(os.path.dirname(__file__), main_package)
start = len(main_package_dir)
packages = []
package_data = defaultdict(list)
for dirname, dirnames, filenames in os.walk(main_package_dir):
    if '__init__.py' in filenames:
        package = "{}{}".format(
            main_package, dirname[start:].replace(os.sep, '.'))
        packages.append(package)
    for filename in filenames:
        _, ext = os.path.splitext(filename)
        if ext in extensions:
            package = "{}{}".format(
                main_package, dirname[start:].replace(os.sep, '.'))
            package_data[package].append(filename)

setup(
    name="peasnaker",
    version=__version__,
    description="Contains the wrapper of NEAT and hyper",
    url="https://github.com/such-a-git/peasnaker.git",
    license="GNU GPLv3.0",
    packages=packages,
    package_data=package_data,
    install_requires=[None]
)
