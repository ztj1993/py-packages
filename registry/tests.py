# -*- coding: utf-8 -*-
# Intro: 配置模块单元测试
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2019-09-02

import time
import unittest

from registry import Registry


class TestRegistry(unittest.TestCase):

    def test_init(self):
        """测试初始化"""
        registry = Registry({'a': {'aa': 'aaa'}})
        self.assertEqual(registry.get(), {'a': {'aa': 'aaa'}})
        self.assertEqual(registry.get('a.aa'), 'aaa')

    def test_set(self):
        """测试设置配置项"""
        registry = Registry()
        registry.set('a', 'a')
        registry.set('b', [1, 2])
        registry.set('c.h', 'h')
        self.assertEqual(registry.get(), {
            'a': 'a',
            'b': [1, 2],
            'c': {
                'h': 'h'
            }
        })

    def test_flat(self):
        """测试扁平处理"""
        registry = Registry({
            'a': {
                'h': 'h',
                'i': 'i',
            }
        })
        self.assertEqual(registry.flat(), {
            'a.h': 'h',
            'a.i': 'i',
        })

    def test_merge(self):
        """测试合并配置"""
        registry = Registry({
            'a': {
                'h': 'h',
                'i': 'i',
            }
        })
        registry.merge({
            'a': {
                'g': 'g',
            }
        })
        self.assertEqual(registry.get(), {
            'a': {
                'h': 'h',
                'i': 'i',
                'g': 'g',
            }
        })

    def test_get(self):
        """测试获取配置项"""
        registry = Registry({'a': {'aa': 'aaa'}})
        self.assertEqual(registry.get(), {'a': {'aa': 'aaa'}})
        self.assertEqual(registry.get('a'), {'aa': 'aaa'})
        self.assertEqual(registry.get('a.aa'), 'aaa')
        self.assertEqual(registry.get('b', ['b']), ['b'])

    def test_append(self):
        """测试列表追加值"""
        registry = Registry({'a': {'b': ['c', 'd']}})
        registry.append('a.b', 'e')
        self.assertEqual(registry.get(), {'a': {'b': ['c', 'd', 'e']}})

    def test_default(self):
        """测试设置默认值"""
        registry = Registry({'a': 'aaa'})
        self.assertEqual(registry.default('a', 'bbb'), 'aaa')
        self.assertEqual(registry.get('a'), 'aaa')
        self.assertEqual(registry.default('c', 'ccc'), 'ccc')
        self.assertEqual(registry.get('c', 'ccc'), 'ccc')

    def test_load(self):
        """测试加载配置项"""
        d = {
            'a': 'a',
            'b': 1,
            'c': {
                'h': 'h',
            },
            'd': [1, 2],
            'e': True,
            'f': 1.1,
        }
        registry = Registry()
        registry.load(d)
        self.assertEqual(registry.get(), d)

    def test_hook(self):
        """测试钩子"""
        registry = Registry()

        def callback():
            registry.set('a', 'aaa')
            return True

        registry.set_hook('hook', 3, callback)
        time.sleep(1)
        registry.refresh_hook('hook')
        self.assertEqual(registry.get('a'), None)
        time.sleep(3)
        registry.refresh_hook('hook')
        self.assertEqual(registry.get('a'), 'aaa')


if __name__ == '__main__':
    unittest.main()
