"""
When installing modules with pip

Installing a modules with certain dependencies

Example:
=======
pip install faker-file[all]
zsh: no matches found: faker-file[all]

The error 'zsh: no matches found: faker-file[all]' occurs because the square brackets are interpreted by the shell. To avoid this, we can either escape the square brackets or use quotes around the package name.

Solution 1:
=========
pip install 'faker-file[all]'

Solution 2:
========
pip install faker-file\[all\]

"""
