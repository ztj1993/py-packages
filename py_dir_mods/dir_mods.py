# -*- coding: utf-8 -*-
# Intro: 目录模块加载
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2019-11-07

import importlib
import pkgutil


class DirMods(object):
    """目录模块加载"""

    def __init__(self, path=None):
        self.mods = dict()
        self.load(path)

    def load(self, mod):
        if isinstance(mod, str):
            mod = importlib.import_module(mod)

        for _, file, _ in pkgutil.iter_modules(path=mod.__path__, prefix=mod.__name__ + '.'):
            self.mods[file] = importlib.import_module(file)

    def get(self, name):
        return self.mods.get(name)

    def all(self):
        return self.mods

    def group(self, var):
        mods = dict()
        for name, mod in self.mods.items():
            if not hasattr(mod, var):
                continue
            if not isinstance(mods.get(getattr(mod, var)), dict):
                mods[getattr(mod, var)] = dict()
            mods[getattr(mod, var)][name] = mod
        return mods
