# -*- coding: utf-8 -*-
# Python 3 算法实现；中文题意、算法说明与原课程顺序对应。
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 城池攻占，Python版
# 一共有n个城市，1号城市是城市树的头，每个城市都有防御值、上级城市编号、奖励类型、奖励值
# 如果奖励类型为0，任何骑士攻克这个城市后，攻击力会加上奖励值
# 如果奖励类型为1，任何骑士攻克这个城市后，攻击力会乘以奖励值
# 任何城市的上级编号 < 这座城市的编号，1号城市没有上级城市编号、奖励类型、奖励值
# 一共有m个骑士，每个骑士都有攻击力、第一次攻击的城市
# 如果骑士攻击力 >= 城市防御值，当前城市会被攻占，骑士获得奖励，继续攻击上级城市
# 如果骑士攻击力  < 城市防御值，那么骑士会在该城市牺牲，没有后续动作了
# 所有骑士都是独立的，不会影响其他骑士攻击这座城池的结果
# 打印每个城市牺牲的骑士数量，打印每个骑士攻占的城市数量
# 1 <= n、m <= 3 * 10^5，攻击值的增加也不会超过long类型范围
# 测试链接 : https://www.luogu.com.cn/problem/P3261
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_CityCapture1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'defend': 'defend', 'belong': 'belong', 'type': 'type', 'gain': 'gain', 'attack': 'attack', 'first': 'first', 'deep': 'deep', 'top': 'top', 'sacrifice': 'sacrifice', 'die': 'die', 'left': 'left', 'right': 'right', 'dist': 'dist', 'mul': 'mul', 'add': 'add'}
    MAXN = 0
    n = 0
    m = 0
    # 城市防御值
    defend = None
    # 上级城市编号
    belong = None
    # 奖励类型
    type = None
    # 奖励值
    gain = None
    # 骑士攻击力
    attack = None
    # 骑士第一次攻击的城市
    first = None
    # 城市在城市树中的深度
    deep = None
    # 城市拥有的骑士列表，用小根堆左偏树组织，最弱的骑士是头
    top = None
    # 每个城市牺牲人数统计
    sacrifice = None
    # 每个骑士死在了什么城市
    die = None
    # 左偏树需要
    left = None
    right = None
    dist = None
    # 懒更新信息，攻击力应该乘多少
    mul = None
    # 懒更新信息，攻击力应该加多少
    add = None
    @staticmethod
    def prepare():
        Code01_CityCapture1.dist[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code01_CityCapture1.m):
            jset(Code01_CityCapture1.left, i, jset(Code01_CityCapture1.right, i, jset(Code01_CityCapture1.dist, i, 0)))
            Code01_CityCapture1.mul[i] = jcast('long', 1)
            Code01_CityCapture1.add[i] = jcast('long', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CityCapture1.n):
            jset(Code01_CityCapture1.sacrifice, i, jset(Code01_CityCapture1.top, i, 0))
            i = jcast('int', (i + 1))

    @staticmethod
    def upgrade(i, t, v):
        i = jcast('int', i)
        t = jcast('int', t)
        v = jcast('long', v)
        if (t == 0):
            Code01_CityCapture1.attack[i] = jcast('long', jcast('long', jadd(Code01_CityCapture1.attack[i], v)))
            Code01_CityCapture1.add[i] = jcast('long', jcast('long', jadd(Code01_CityCapture1.add[i], v)))
        else:
            Code01_CityCapture1.attack[i] = jcast('long', jcast('long', (Code01_CityCapture1.attack[i] * v)))
            Code01_CityCapture1.mul[i] = jcast('long', jcast('long', (Code01_CityCapture1.mul[i] * v)))
            Code01_CityCapture1.add[i] = jcast('long', jcast('long', (Code01_CityCapture1.add[i] * v)))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if ((Code01_CityCapture1.mul[i] != 1) or (Code01_CityCapture1.add[i] != 0)):
            l = jcast('int', Code01_CityCapture1.left[i])
            r = jcast('int', Code01_CityCapture1.right[i])
            if (l != 0):
                Code01_CityCapture1.attack[l] = jcast('long', jcast('long', jadd(jcast('long', (Code01_CityCapture1.attack[l] * Code01_CityCapture1.mul[i])), Code01_CityCapture1.add[i])))
                Code01_CityCapture1.mul[l] = jcast('long', jcast('long', (Code01_CityCapture1.mul[l] * Code01_CityCapture1.mul[i])))
                Code01_CityCapture1.add[l] = jcast('long', jcast('long', jadd(jcast('long', (Code01_CityCapture1.add[l] * Code01_CityCapture1.mul[i])), Code01_CityCapture1.add[i])))
            if (r != 0):
                Code01_CityCapture1.attack[r] = jcast('long', jcast('long', jadd(jcast('long', (Code01_CityCapture1.attack[r] * Code01_CityCapture1.mul[i])), Code01_CityCapture1.add[i])))
                Code01_CityCapture1.mul[r] = jcast('long', jcast('long', (Code01_CityCapture1.mul[r] * Code01_CityCapture1.mul[i])))
                Code01_CityCapture1.add[r] = jcast('long', jcast('long', jadd(jcast('long', (Code01_CityCapture1.add[r] * Code01_CityCapture1.mul[i])), Code01_CityCapture1.add[i])))
            Code01_CityCapture1.mul[i] = jcast('long', 1)
            Code01_CityCapture1.add[i] = jcast('long', 0)

    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        if (Code01_CityCapture1.attack[i] > Code01_CityCapture1.attack[j]):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        Code01_CityCapture1.down(i)
        jset(Code01_CityCapture1.right, i, Code01_CityCapture1.merge(Code01_CityCapture1.right[i], j))
        if (Code01_CityCapture1.dist[Code01_CityCapture1.left[i]] < Code01_CityCapture1.dist[Code01_CityCapture1.right[i]]):
            tmp = jcast('int', Code01_CityCapture1.left[i])
            Code01_CityCapture1.left[i] = jcast('int', Code01_CityCapture1.right[i])
            Code01_CityCapture1.right[i] = jcast('int', tmp)
        Code01_CityCapture1.dist[i] = jcast('int', jcast('int', jadd(Code01_CityCapture1.dist[Code01_CityCapture1.right[i]], 1)))
        return jcast('int', i)

    @staticmethod
    def pop(i):
        i = jcast('int', i)
        Code01_CityCapture1.down(i)
        ans = jcast('int', Code01_CityCapture1.merge(Code01_CityCapture1.left[i], Code01_CityCapture1.right[i]))
        jset(Code01_CityCapture1.left, i, jset(Code01_CityCapture1.right, i, jset(Code01_CityCapture1.dist, i, 0)))
        return jcast('int', ans)

    @staticmethod
    def compute():
        Code01_CityCapture1.deep[1] = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code01_CityCapture1.n):
            Code01_CityCapture1.deep[i] = jcast('int', jcast('int', jadd(Code01_CityCapture1.deep[Code01_CityCapture1.belong[i]], 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CityCapture1.m):
            if (Code01_CityCapture1.top[Code01_CityCapture1.first[i]] == 0):
                jset(Code01_CityCapture1.top, Code01_CityCapture1.first[i], i)
            else:
                jset(Code01_CityCapture1.top, Code01_CityCapture1.first[i], Code01_CityCapture1.merge(Code01_CityCapture1.top[Code01_CityCapture1.first[i]], i))
            i = jcast('int', (i + 1))
        i = jcast('int', Code01_CityCapture1.n)
        while (i >= 1):
            while ((Code01_CityCapture1.top[i] != 0) and (Code01_CityCapture1.attack[Code01_CityCapture1.top[i]] < Code01_CityCapture1.defend[i])):
                jset(Code01_CityCapture1.die, Code01_CityCapture1.top[i], i)
                Code01_CityCapture1.sacrifice[i] = jcast('int', (Code01_CityCapture1.sacrifice[i] + 1))
                jset(Code01_CityCapture1.top, i, Code01_CityCapture1.pop(Code01_CityCapture1.top[i]))
            if (Code01_CityCapture1.top[i] != 0):
                Code01_CityCapture1.upgrade(Code01_CityCapture1.top[i], Code01_CityCapture1.type[i], Code01_CityCapture1.gain[i])
                if (Code01_CityCapture1.top[Code01_CityCapture1.belong[i]] == 0):
                    jset(Code01_CityCapture1.top, Code01_CityCapture1.belong[i], Code01_CityCapture1.top[i])
                else:
                    jset(Code01_CityCapture1.top, Code01_CityCapture1.belong[i], Code01_CityCapture1.merge(Code01_CityCapture1.top[Code01_CityCapture1.belong[i]], Code01_CityCapture1.top[i]))
            i = jcast('int', (i - 1))

    @staticmethod
    def main(args):
        io = Code01_CityCapture1.ReaderWriter(_java_ctor=0)
        Code01_CityCapture1.n = jcast('int', jcall(io, 'nextInt'))
        Code01_CityCapture1.m = jcast('int', jcall(io, 'nextInt'))
        Code01_CityCapture1.prepare()
        i = jcast('int', 1)
        while (i <= Code01_CityCapture1.n):
            jset(Code01_CityCapture1.defend, i, jcall(io, 'nextLong'))
            i = jcast('int', (i + 1))
        i = jcast('int', 2)
        while (i <= Code01_CityCapture1.n):
            jset(Code01_CityCapture1.belong, i, jcall(io, 'nextInt'))
            jset(Code01_CityCapture1.type, i, jcall(io, 'nextInt'))
            jset(Code01_CityCapture1.gain, i, jcall(io, 'nextLong'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CityCapture1.m):
            jset(Code01_CityCapture1.attack, i, jcall(io, 'nextLong'))
            jset(Code01_CityCapture1.first, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_CityCapture1.compute()
        i = jcast('int', 1)
        while (i <= Code01_CityCapture1.n):
            jcall(io, 'println', Code01_CityCapture1.sacrifice[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CityCapture1.m):
            jcall(io, 'println', jcast('int', (Code01_CityCapture1.deep[Code01_CityCapture1.first[i]] - Code01_CityCapture1.deep[Code01_CityCapture1.die[i]])))
            i = jcast('int', (i + 1))
        jcall(io, 'flush')
        jcall(io, 'close')

    # 读写工具类
    class ReaderWriter(jclass('PrintWriter')):
        __java_fields__ = {'buf': 'buf', 'bId': 'bId', 'bSize': 'bSize', 'eof': 'eof', 'c': 'c'}
        # buf：实例字段，在构造函数中初始化。
        # bId：实例字段，在构造函数中初始化。
        # bSize：实例字段，在构造函数中初始化。
        # eof：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            super().__init__(jget(System, 'out'))

        def getByte(self):
            if (self.bId >= self.bSize):
                try:
                    self.bSize = jcast('int', jcall(jget(System, 'in'), 'read', self.buf))
                except (JBreak, JContinue):
                    raise
                except Exception as _java_exception_1:
                    if jinstanceof(_java_exception_1, 'IOException'):
                        e = _java_exception_1
                        jcall(e, 'printStackTrace')
                    else:
                        raise
                if (self.bSize == jcast('int', (-1))):
                    self.eof = jcast('boolean', True)
                self.bId = jcast('int', 0)
            return jcast('byte', self.buf[((_java_obj_2 := self), (_java_key_3 := 'bId'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4]])

        # c：实例字段，在构造函数中初始化。
        def hasNext(self):
            if self.eof:
                return jcast('boolean', False)
            while ((jset(self, 'c', self.getByte()) <= 32) and (not self.eof)):
                None
            if self.eof:
                return jcast('boolean', False)
            self.bId = jcast('int', (self.bId - 1))
            return jcast('boolean', True)

        def next(self):
            if (not self.hasNext()):
                return None
            c = jcast('byte', self.getByte())
            while (c <= 32):
                c = jcast('byte', self.getByte())
            sb = jnew('StringBuilder')
            while (c > 32):
                jcall(sb, 'append', jcast('char', c))
                c = jcast('byte', self.getByte())
            return jcall(sb, 'toString')

        def nextInt(self):
            if (not self.hasNext()):
                return jcast('int', jget(Integer, 'MIN_VALUE'))
            sign = jcast('int', 1)
            c = jcast('byte', self.getByte())
            while (c <= 32):
                c = jcast('byte', self.getByte())
            if (c == jchar('-')):
                sign = jcast('int', jcast('int', (-1)))
                c = jcast('byte', self.getByte())
            val = jcast('int', 0)
            while ((c >= jchar('0')) and (c <= jchar('9'))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('byte', self.getByte())
            self.bId = jcast('int', (self.bId - 1))
            return jcast('int', jcast('int', (val * sign)))

        def nextLong(self):
            if (not self.hasNext()):
                return jcast('long', jget(Long, 'MIN_VALUE'))
            sign = jcast('int', 1)
            c = jcast('byte', self.getByte())
            while (c <= 32):
                c = jcast('byte', self.getByte())
            if (c == jchar('-')):
                sign = jcast('int', jcast('int', (-1)))
                c = jcast('byte', self.getByte())
            val = jcast('long', 0)
            while ((c >= jchar('0')) and (c <= jchar('9'))):
                val = jcast('long', jcast('long', jadd(jcast('long', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('byte', self.getByte())
            self.bId = jcast('int', (self.bId - 1))
            return jcast('long', jcast('long', (val * sign)))

        def nextDouble(self):
            if (not self.hasNext()):
                return jcast('double', jget(Double, 'NaN'))
            sign = jcast('int', 1)
            c = jcast('byte', self.getByte())
            while (c <= 32):
                c = jcast('byte', self.getByte())
            if (c == jchar('-')):
                sign = jcast('int', jcast('int', (-1)))
                c = jcast('byte', self.getByte())
            val = jcast('double', 0)
            while ((c >= jchar('0')) and (c <= jchar('9'))):
                val = jcast('double', jadd((val * 10), jcast('int', (c - jchar('0')))))
                c = jcast('byte', self.getByte())
            if (c == jchar('.')):
                mul = jcast('double', 1)
                c = jcast('byte', self.getByte())
                while ((c >= jchar('0')) and (c <= jchar('9'))):
                    mul = jcast('double', (mul * 0.1))
                    val = jcast('double', jadd(val, (jcast('int', (c - jchar('0'))) * mul)))
                    c = jcast('byte', self.getByte())
            self.bId = jcast('int', (self.bId - 1))
            return jcast('double', (val * sign))

        def __init__(self, *args, _java_ctor=None):
            self.buf = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.bId = jcast('int', 0)
            self.bSize = jcast('int', 0)
            self.eof = jcast('boolean', False)
            self.c = jcast('byte', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_CityCapture1.ReaderWriter.ReaderWriter")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CityCapture1.MAXN = jcast('int', 300001)
Code01_CityCapture1.n = jcast('int', 0)
Code01_CityCapture1.m = jcast('int', 0)
Code01_CityCapture1.defend = jarray('long', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.belong = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.type = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.gain = jarray('long', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.attack = jarray('long', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.first = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.deep = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.top = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.sacrifice = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.die = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.left = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.right = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.dist = jarray('int', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.mul = jarray('long', [Code01_CityCapture1.MAXN])
Code01_CityCapture1.add = jarray('long', [Code01_CityCapture1.MAXN])

if __name__ == '__main__':
    Code01_CityCapture1.main([])
