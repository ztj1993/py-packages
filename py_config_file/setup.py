# -*- coding: utf-8 -*-
# Intro: 配置文件模块安装文件
# Author: Ztj
# Email: ztj1993@gmail.com
# Date: 2019-09-04

import os.path
import re

from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8')
readme = f.read()
f.close()

f = open(os.path.join(os.path.dirname(__file__), 'config_file.py'), encoding='utf8')
version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)
f.close()

setup(
    name='py-ztj-configfile',
    version=version,
    description='python configuration file loading package',
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=['configfile'],
    url='http://github.com/ztj1993/PythonPackages/blob/master/py_config_file',
    author='ZhangTianJie',
    author_email='ztj1993@gmail.com',
    keywords='configfile config json yaml',
    install_requires=['PyYAML'],
    license='MIT License',
)
