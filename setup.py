#!/usr/bin/env python
from distutils.core import setup
import os

parent_directory = os.path.abspath(os.path.dirname(__file__))

meta_files = {
	'README.md': None,
	'CLASSIFIERS.txt': None,
}

for filename in meta_files:
	try:
		current_file = open(os.path.join(parent_directory, filename))
		meta_files[filename] = current_file.read()
		current_file.close()
	except IOError:
		raise IOError('{0} not found.'.format(filename))

classifiers = meta_files['CLASSIFIERS.txt'].split('\n')
classifiers.remove('')

setup(name='djynamite',
	  version='0.1',
	  description='Keeping your Django sites explosively interactive.',
	  long_description=meta_files['README.md'],
	  classifiers=classifiers,
	  author='Brandon R. Stoner',
	  author_email='monokrome@limpidtech.com',
	  url='http://github.com/LimpidTech/djynamite',
	  packages=['djynamite'],
	  keywords = 'web django client javascript',
)
