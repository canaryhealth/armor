#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: Philip J Grabner <phil@canary.md>
# date: 2015/11/02
# copy: (C) Copyright 2015-EOT Canary Health, Inc., All Rights Reserved.
#------------------------------------------------------------------------------

import os, sys, setuptools
from setuptools import setup, find_packages

# require python 2.7+
if sys.hexversion < 0x02070000:
  raise RuntimeError('This package requires python 2.7 or better')

heredir = os.path.abspath(os.path.dirname(__file__))
def read(*parts, **kw):
  try:    return open(os.path.join(heredir, *parts)).read()
  except: return kw.get('default', '')

test_dependencies = [
  'nose                 >= 1.3.0',
  'coverage             >= 3.5.3',
]

dependencies = [
  'six                  >= 1.6.1',
  'FormEncode           >= 1.2.5',
]

extras_dependencies = {
}

classifiers = [
  'Development Status :: 1 - Planning',
  # 'Development Status :: 2 - Pre-Alpha',
  # 'Development Status :: 3 - Alpha',
  # 'Development Status :: 4 - Beta',
  # 'Development Status :: 5 - Production/Stable',
  # 'Development Status :: 6 - Mature',
  # 'Development Status :: 7 - Inactive',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'Environment :: Console',
  'Operating System :: OS Independent',
  'Topic :: Internet',
  'Topic :: Security',
  'Topic :: Software Development',
  'Topic :: Software Development :: Object Brokering',
  'Topic :: Utilities',
  'Natural Language :: English',
  'License :: OSI Approved :: MIT License',
  'License :: Public Domain',
]

setup(
  name                  = 'armor',
  version               = read('VERSION.txt', default='0.0.1').strip(),
  description           = 'A data validation and sanitization library',
  long_description      = read('README.rst'),
  classifiers           = classifiers,
  author                = 'Canary Health Inc',
  author_email          = 'oss-pypi@canary.md',
  url                   = 'http://github.com/canaryhealth/armor',
  keywords              = 'data normalize validate validation sanitize sanitization',
  packages              = find_packages(),
  include_package_data  = True,
  zip_safe              = True,
  install_requires      = dependencies,
  extras_require        = extras_dependencies,
  tests_require         = test_dependencies,
  test_suite            = 'armor',
  entry_points          = '',
  license               = 'MIT (http://opensource.org/licenses/MIT)',
)

#------------------------------------------------------------------------------
# end of $Id$
# $ChangeLog$
#------------------------------------------------------------------------------
