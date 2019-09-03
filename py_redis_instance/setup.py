# -*- coding: utf-8 -*-
# Intro: Redis 实例模块安装文件
# Author: Ztj
# Email: ztj1993@gmail.com
# Date: 2019-09-04

import os.path
import re

from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8')
readme = f.read()
f.close()

f = open(os.path.join(os.path.dirname(__file__), 'redis_instance.py'), encoding='utf8')
version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)
f.close()

setup(
    name='py-ztj-redis-instance',
    version=version,
    description='python redis instance package',
    long_description=readme,
    long_description_content_type="text/markdown",
    py_modules=["redis_instance"],
    url='http://github.com/ztj1993/PythonPackages/blob/master/py_redis_instance',
    author='ZhangTianJie',
    author_email='ztj1993@gmail.com',
    keywords='redis',
    install_requires=['redis', 'py-ztj-registry'],
    license='MIT License',
)
