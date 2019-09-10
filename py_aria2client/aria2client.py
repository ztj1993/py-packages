# -*- coding: utf-8 -*-
# Intro: Aria2 客户端
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2019-09-10

import time

from aria2local import Aria2Local
from aria2rpc import Aria2Rpc


class Aria2Client(Aria2Local, Aria2Rpc):
    def __init__(self, **kwargs):
        self.state = kwargs.get('state', True)
        self.enable = kwargs.get('enable', False)
        Aria2Local.__init__(self, **kwargs)
        Aria2Rpc.__init__(self, **kwargs)

    def check_state(self):
        try:
            self.get_version()
            self.state = True
        except:
            self.state = False
        return self.state

    def check_wait(self, interval_time=60):
        while self.check_state() is False:
            time.sleep(interval_time)

    def wait_complete(self, gid, callback):
        """等待完成"""
        last_progress = 0
        while last_progress < 100:
            progress = self.get_progress(gid)
            if progress is None:
                return None
            if progress is False:
                return False
            if not progress == last_progress:
                callback(self, progress)
                last_progress = progress
            time.sleep(5)
        return True

    def get_progress(self, gid):
        """获取进度"""
        status = self.tell_status(gid)
        if status is None:
            return None
        if status.get('status') == 'active':
            if int(status.get('totalLength')) == 0:
                return 0
            if int(status.get('completedLength')) == 0:
                return 0
            return int((int(status.get('completedLength')) / int(status.get('totalLength'))) * 100)
        elif status.get('status') == 'complete':
            return 100
        else:
            return False

    def is_complete(self, gid):
        """是否下载完成"""
        status = self.tell_status(gid)
        if status.get('status') == 'active':
            return False
        if status.get('status') == 'complete':
            return True
        return None
