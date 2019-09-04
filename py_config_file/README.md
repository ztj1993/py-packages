# Python ConfigFile Package

## 说明
这是一个 Python 配置文件加载模块，主要解决 yaml, json 配置文件的快速加载。

## 依赖
```
pip install PyYAML==5.1.2
```

## 使用
```
import os.path
from configfile import ConfigFile


config_dir = os.path.dirname(os.path.abspath(__file__))
configfile = ConfigFile(config_dir)

# 加载配置文件
print(configfile.load('config'))

# 加载配置文件
print(configfile.load('config', '/srv/config'))
```

## 配置文件定期加载
```
import json
import time
import os.path

from framework.configfile.configfile import ConfigFile

timestamp1 = time.time()
timestamp2 = False

config_dir = os.path.dirname(os.path.abspath(__file__))
configfile = ConfigFile(config_dir)


def callback():
    global timestamp1
    global timestamp2
    if timestamp2 is False:
        timestamp2 = timestamp1
    else:
        timestamp2 = time.time()
    return json.dumps({"timestamp": timestamp2})


file_path = configfile.get_file_path('expire', configfile.json_suffix)
print(configfile.expire(file_path, callback, 3))
print(configfile.load('expire'))
time.sleep(1)
print(configfile.expire(file_path, callback, 3))
print(configfile.load('expire'))
time.sleep(3)
print(configfile.expire(file_path, callback, 3))
print(configfile.load('expire'))
```
