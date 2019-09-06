# Python Aria2 本地管理模块

### 说明
这是一个 aria2 本地服务管理模块。

## 安装
```
pip install py-ztj-aria2local
```

### 使用
```
import time
from py_aria2local.aria2local import Aria2Local

local = Aria2Local()
print('is_install', local.is_install())
print('start', local.start())
time.sleep(3)
print('is_running', local.is_running())
time.sleep(15)
print('stop', local.stop())
time.sleep(3)
print('is_running', local.is_running())
```
