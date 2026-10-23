# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 蓄水池采样
# 假设有一个不停吐出球的机器，每次吐出1号球、2号球、3号球...
# 有一个袋子只能装下10个球，每次机器吐出的球，要么放入袋子，要么永远扔掉
# 如何做到机器吐出每一个球之后，所有吐出的球都等概率被放进袋子里
class Code01_ReservoirSampling:
    __java_fields__ = {}
    class Pool:
        __java_fields__ = {'size': 'size', 'bag': 'bag'}
        # size：实例字段，在构造函数中初始化。
        # bag：实例字段，在构造函数中初始化。
        def _java_init_0(self, s):
            s = jcast('int', s)
            self.size = jcast('int', s)
            self.bag = jarray('int', [s])

        # 是否要i号球
        # size/i的几率决定要
        # 剩下的几率决定不要
        def pick(self, i):
            i = jcast('int', i)
            return jcast('boolean', (jcast('int', (jstatic('Math', 'random') * i)) < self.size))

        # 袋子里0...size-1个位置
        # 哪个空间的球扔掉，让i号球进来
        def where(self):
            return jcast('int', jcast('int', (jstatic('Math', 'random') * self.size)))

        def enter(self, i):
            i = jcast('int', i)
            if (i <= self.size):
                self.bag[jcast('int', (i - 1))] = jcast('int', i)
            else:
                if self.pick(i):
                    jset(self.bag, self.where(), i)

        def getBag(self):
            return self.bag

        def __init__(self, *args, _java_ctor=None):
            self.size = jcast('int', 0)
            self.bag = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_ReservoirSampling.Pool.Pool")


    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        # 一共吐出多少球
        n = jcast('int', 41)
        # 袋子大小多少
        m = jcast('int', 10)
        # 进行多少次实验
        testTimes = jcast('int', 10000)
        cnt = jarray('int', [jcast('int', jadd(n, 1))])
        k = jcast('int', 0)
        while (k < testTimes):
            pool = Code01_ReservoirSampling.Pool(m, _java_ctor=0)
            i = jcast('int', 1)
            while (i <= n):
                jcall(pool, 'enter', i)
                i = jcast('int', (i + 1))
            bag = jcall(pool, 'getBag')
            for num in bag:
                cnt[num] = jcast('int', (cnt[num] + 1))
            k = jcast('int', (k + 1))
        jprint(jadd(jadd(jadd(jadd('机器吐出到', n), '号球, '), '袋子大小为'), m), newline=True)
        jprint(jadd('每个球被选中的概率应该接近', jdiv(jcast('double', m), n)), newline=True)
        jprint(jadd(jadd('一共测试', testTimes), '次'), newline=True)
        i = jcast('int', 1)
        while (i <= n):
            jprint(jadd(jadd(jadd(jadd(i, '被选中次数 : '), cnt[i]), ', 被选中概率 : '), jdiv(jcast('double', cnt[i]), testTimes)), newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_ReservoirSampling.main([])
