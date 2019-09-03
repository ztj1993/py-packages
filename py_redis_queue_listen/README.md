# Redis 队列监听模块

## 说明
这是一个 Redis 队列监听模块，封装了相关的队列获取及处理。

## 安装
```
pip install py-ztj-redis-queue-listen
```

## 依赖
```
pip install py-ztj-redis-instance>=0.0.1
```

## 使用
```
from redis_queue_listen import RedisQueueListen

RQL = RedisQueueListen()
RQL.listen()
```
