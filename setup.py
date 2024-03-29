from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='dalen2',
      setup_requires=['setuptools_scm'],
      install_requires=requirements,
      use_scm_version={'write_to': 'dalen2/version.txt'},
      description="Project Description",
      packages=find_packages(),
      test_suite = 'tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/dalen2-run'],
      zip_safe=False)
