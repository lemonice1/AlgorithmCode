# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 组团买票找到了在线测试
# 逻辑和课上讲的一样，但是测试中设定的ki为负数
# 实现做了一些小优化，具体可以看注释
# 测试链接 : https://www.luogu.com.cn/problem/P12331
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_GroupBuyTickets2:
    __java_fields__ = {}
    class Game:
        __java_fields__ = {'ki': 'ki', 'bi': 'bi', 'people': 'people'}
        # ki：实例字段，在构造函数中初始化。
        # bi：实例字段，在构造函数中初始化。
        # people：实例字段，在构造函数中初始化。
        def _java_init_0(self, k, b):
            k = jcast('long', k)
            b = jcast('long', b)
            self.ki = jcast('long', k)
            self.bi = jcast('long', b)

        def earn(self):
            return jcast('long', jcast('long', (self.cost(jcast('int', jadd(self.people, 1))) - self.cost(self.people))))

        def cost(self, p):
            p = jcast('long', p)
            price = jcast('long', jcast('long', jadd(jcast('long', (self.ki * p)), self.bi)))
            if (price < 0):
                price = jcast('long', 0)
            return jcast('long', jcast('long', (p * price)))

        def __init__(self, *args, _java_ctor=None):
            self.ki = jcast('long', 0)
            self.bi = jcast('long', 0)
            self.people = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['long', 'long']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_GroupBuyTickets2.Game.Game")


    @staticmethod
    def main(args):
        in_ = Code03_GroupBuyTickets2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        n = jcast('int', jcall(in_, 'nextInt'))
        m = jcast('int', jcall(in_, 'nextInt'))
        heap = jnew('PriorityQueue', (lambda a, b: jstatic('Long', 'compare', jcall(b, 'earn'), jcall(a, 'earn'))))
        i = jcast('int', 0)
        while (i < m):
            cur = Code03_GroupBuyTickets2.Game(jcall(in_, 'nextLong'), jcall(in_, 'nextLong'), _java_ctor=0)
            # 初始增费<=0的项目直接忽略
            if (jcall(cur, 'earn') > 0):
                jcall(heap, 'add', cur)
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', 0)
        while ((i < n) and (not jcall(heap, 'isEmpty'))):
            try:
                cur = jcall(heap, 'poll')
                money = jcast('long', jcall(cur, 'earn'))
                if (money <= 0):
                    # 没有正向增费，那么可以结束了
                    raise JBreak(None)
                ans = jcast('long', jcast('long', jadd(ans, money)))
                cur.people = jcast('int', (cur.people + 1))
                if (jcall(cur, 'earn') > 0):
                    jcall(heap, 'add', cur)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_2 := self), (_java_key_3 := 'ptr'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def nextLong(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('long', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('long', jcast('long', jadd(jcast('long', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('long', (jcast('long', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_GroupBuyTickets2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_GroupBuyTickets2.main([])
