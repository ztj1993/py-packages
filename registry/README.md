# Python Registry Package

### 说明
这是一个 Python 配置快速调用模块，主要解决 Json or Yaml 深层次配置调用问题。

### 使用
```
from registry import Registry

registry = Registry()

registry.set('a', 'a')
registry.set('b', {'bb': 'bbb'})
registry.set('c.h', 'h')

print(registry.get())
print(registry.get('b.bb'))
```

### 加载字典
```
from registry import Registry

registry = Registry()

registry.load({'a': {'aa': 'aaa'}})
print(registry.get('a.aa'))
```

### 合并字典
```
from registry import Registry

registry = Registry()

registry.load({'a': {'a1': 'aaa1'}})
registry.merge('a', {'a2': 'aaa2' })
print(registry.get('a'))
```

### 设置默认值
```
from registry import Registry

registry = Registry()

registry.set('a', 'aaa')
registry.default('a', 'bbb')
registry.default('c', 'ccc')
print(registry.get('a'))
print(registry.get('c'))
```

### 钩子调用
```
import time
from registry import Registry

registry = Registry()

def callback():
    print('callback')

registry.set_hook('hook', 3, callback)
time.sleep(1)
registry.refresh_hook('hook')
time.sleep(3)
registry.refresh_hook('hook')
```
