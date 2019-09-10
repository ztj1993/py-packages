# PythonPackages
my python package list.

## 如何打包发布
```
echo "
TEST_USERNAME=not_set
TEST_PASSWORD=not_set
PYPI_USERNAME=not_set
PYPI_PASSWORD=not_set
" | tee ~/.py-pkg-build

docker run -it --rm -v $PWD:/app -e TEST_ENABLE=true --env-file ~/.py-pkg-build ztj1993/image:py-pkg-build
docker run -it --rm -v $PWD:/app -e PYPI_ENABLE=true --env-file ~/.py-pkg-build ztj1993/image:py-pkg-build
```

## 包列表

### [registry](py_registry) - 配置注册模块
Python 配置快速调用模块，解决 Json or Yaml 深层次配置调用问题
```
pip install py-ztj-registry
```

### [config_file](py_config_file) - 配置加载模块
Python 配置文件加载模块，解决 yaml, json 配置文件的快速加载
```
pip install py-ztj-configfile
```

### [redis_instance](py_redis_instance) - Redis 实例模块
Redis 实例模块
```
pip install py-ztj-redis-instance
```

### [mysql_instance](py_mysql_instance) - MySQL 实例模块
MySQL 实例模块
```
pip install py-ztj-mysql-instance
```


### [redis_queue_listen](py_redis_queue_listen) - Redis 队列监听模块
Redis 队列监听模块，封装了队列获取及处理
```
pip install py-ztj-redis-queue-listen
```
