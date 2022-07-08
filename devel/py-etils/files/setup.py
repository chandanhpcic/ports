#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['etils',
 'etils.array_types',
 'etils.ecolab',
 'etils.edc',
 'etils.enp',
 'etils.epath',
 'etils.epy',
 'etils.etqdm',
 'etils.etree']

package_data = \
{'': ['*'], 'etils.epath': ['docs/*']}

extras_require = \
{'all': ['etils[array-types]',
         'etils[ecolab]',
         'etils[edc]',
         'etils[enp]',
         'etils[epath]',
         'etils[epy]',
         'etils[etqdm]',
         'etils[etree]',
         'etils[etree-dm]',
         'etils[etree-jax]',
         'etils[etree-tf]'],
 'array-types': ['numpy'],
 'dev': ['pytest',
         'pytest-subtests',
         'pytest-xdist',
         'pylint>=2.6.0',
         'yapf',
         'chex'],
 'ecolab': ['jupyter', 'numpy', 'mediapy', 'etils[enp]'],
 'edc': ['etils[epy]'],
 'enp': ['numpy', 'etils[array-types]'],
 'epath': ['importlib_resources', 'zipp', 'etils[epy]'],
 'epath-no-tf': ['etils[epath]'],
 'epy': ['typing_extensions'],
 'etqdm': ['absl-py', 'tqdm', 'etils[epy]'],
 'etree': ['etils[array_types]', 'etils[epy]', 'etils[enp]', 'etils[etqdm]'],
 'etree-dm': ['dm-tree', 'etils[etree]'],
 'etree-jax': ['jax[cpu]', 'etils[etree]'],
 'etree-tf': ['tf-nightly', 'etils[etree]']}

setup(name='etils',
      version='%%PORTVERSION%%',
      description='Collection of common python utils',
      author=None,
      author_email='Conchylicultor <etils@google.com>',
      url=None,
      packages=packages,
      package_data=package_data,
      extras_require=extras_require,
      python_requires='>=3.7',
     )