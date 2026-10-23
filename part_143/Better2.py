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

# 替罪羊树的更好实现，Python版
# 本文件是不做词频压缩的替罪羊树实现，并且数据经过了加强
# 本节课的视频，做了重要更新，补充了很多说明
# 介绍了我设计的替罪羊树，对比经典的替罪羊树，有哪些独特性和便利性
# 说明了我设计的替罪羊树和经典替罪羊树，复杂度是一样的
# 注意如下实现中的注释文字
# 测试链接 : https://www.luogu.com.cn/problem/P6136
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Better2:
    __java_fields__ = {'MAXN': 'MAXN', 'cntn': 'cntn', 'root': 'root', 'key': 'key', 'ls': 'ls', 'rs': 'rs', 'alive': 'alive', 'aliveSiz': 'aliveSiz', 'ALPHA': 'ALPHA', 'top': 'top', 'father': 'father', 'side': 'side', 'collect': 'collect', 'collectSiz': 'collectSiz'}
    MAXN = 0
    cntn = 0
    root = 0
    key = None
    ls = None
    rs = None
    # 节点是否存活，删掉就算死亡
    alive = None
    # 子树的存活节点数量
    aliveSiz = None
    ALPHA = 0.0
    top = 0
    father = 0
    side = 0
    collect = None
    collectSiz = 0
    @staticmethod
    def init(num):
        num = jcast('int', num)
        jset(Better2.key, ((_java_obj_1 := Better2), (_java_key_2 := 'cntn'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        jset(Better2.ls, Better2.cntn, jset(Better2.rs, Better2.cntn, 0))
        Better2.alive[Better2.cntn] = jcast('boolean', True)
        Better2.aliveSiz[Better2.cntn] = jcast('int', 1)
        return jcast('int', Better2.cntn)

    # 汇总存活节点数量
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Better2.aliveSiz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd((1 if Better2.alive[i] else 0), Better2.aliveSiz[Better2.ls[i]])), Better2.aliveSiz[Better2.rs[i]])))

    @staticmethod
    def inorder(i):
        i = jcast('int', i)
        # 增加剪枝：整棵树上没有存活节点也跳过
        if ((i != 0) and (Better2.aliveSiz[i] != 0)):
            Better2.inorder(Better2.ls[i])
            if Better2.alive[i]:
                jset(Better2.collect, ((_java_obj_4 := Better2), (_java_key_5 := 'collectSiz'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], i)
            Better2.inorder(Better2.rs[i])

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            return jcast('int', 0)
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        h = jcast('int', Better2.collect[m])
        jset(Better2.ls, h, Better2.build(l, jcast('int', (m - 1))))
        jset(Better2.rs, h, Better2.build(jcast('int', jadd(m, 1)), r))
        Better2.up(h)
        return jcast('int', h)

    @staticmethod
    def rebuild():
        if (Better2.top != 0):
            Better2.collectSiz = jcast('int', 0)
            Better2.inorder(Better2.top)
            newRoot = jcast('int', Better2.build(1, Better2.collectSiz))
            if (Better2.father == 0):
                Better2.root = jcast('int', newRoot)
            else:
                if (Better2.side == 1):
                    Better2.ls[Better2.father] = jcast('int', newRoot)
                else:
                    Better2.rs[Better2.father] = jcast('int', newRoot)

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Better2.ALPHA * Better2.aliveSiz[i]) >= jstatic('Math', 'max', Better2.aliveSiz[Better2.ls[i]], Better2.aliveSiz[Better2.rs[i]])))

    # 返回头节点编号
    @staticmethod
    def _java_add_0(i, f, s, num):
        i = jcast('int', i)
        f = jcast('int', f)
        s = jcast('int', s)
        num = jcast('int', num)
        # 增加剪枝：整棵树上没有存活节点就算空树
        if ((i == 0) or (Better2.aliveSiz[i] == 0)):
            return jcast('int', Better2.init(num))
        if (num <= Better2.key[i]):
            jset(Better2.ls, i, Better2._java_add_0(Better2.ls[i], i, 1, num))
        else:
            jset(Better2.rs, i, Better2._java_add_0(Better2.rs[i], i, 2, num))
        Better2.up(i)
        if (not Better2.balance(i)):
            Better2.top = jcast('int', i)
            Better2.father = jcast('int', f)
            Better2.side = jcast('int', s)
        return jcast('int', i)

    @staticmethod
    def _java_add_1(num):
        num = jcast('int', num)
        Better2.top = jcast('int', jset(Better2, 'father', jset(Better2, 'side', 0)))
        Better2.root = jcast('int', Better2._java_add_0(Better2.root, 0, 0, num))
        Better2.rebuild()

    @staticmethod
    def small(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        # 增加剪枝：整棵树上没有存活节点，就算空树
        if ((i == 0) or (Better2.aliveSiz[i] == 0)):
            return jcast('int', 0)
        if (num <= Better2.key[i]):
            return jcast('int', Better2.small(Better2.ls[i], num))
        else:
            return jcast('int', jcast('int', jadd(jcast('int', jadd(Better2.aliveSiz[Better2.ls[i]], (1 if Better2.alive[i] else 0))), Better2.small(Better2.rs[i], num))))

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        return jcast('int', jcast('int', jadd(Better2.small(Better2.root, num), 1)))

    @staticmethod
    def _java_index_0(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (x <= Better2.aliveSiz[Better2.ls[i]]):
            return jcast('int', Better2._java_index_0(Better2.ls[i], x))
        else:
            less = jcast('int', jcast('int', jadd(Better2.aliveSiz[Better2.ls[i]], (1 if Better2.alive[i] else 0))))
            if (less < x):
                return jcast('int', Better2._java_index_0(Better2.rs[i], jcast('int', (x - less))))
        return jcast('int', Better2.key[i])

    @staticmethod
    def _java_index_1(x):
        x = jcast('int', x)
        return jcast('int', Better2._java_index_0(Better2.root, x))

    @staticmethod
    def pre(num):
        num = jcast('int', num)
        kth = jcast('int', Better2.rank(num))
        if (kth == 1):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        else:
            return jcast('int', Better2._java_index_1(jcast('int', (kth - 1))))

    @staticmethod
    def post(num):
        num = jcast('int', num)
        kth = jcast('int', Better2.rank(jcast('int', jadd(num, 1))))
        if (kth == jcast('int', jadd(Better2.aliveSiz[Better2.root], 1))):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        else:
            return jcast('int', Better2._java_index_1(kth))

    # 注意remove方法
    # 因为替罪羊树会重构，所以值相同的一批节点，重构时假设选出的头为h
    # 那么这批节点，有可能在h的左侧，也有可能在h的右侧
    # 所以删除时，如果h已经被删，还要继续寻找其他key值相同的节点
    # 此时只根据key值的大小关系，方向无法确定是左还是右
    # 所以先求出目标的排名，再按排名删除，这样移动方向是确定的
    @staticmethod
    def _java_remove_0(i, f, s, rank):
        i = jcast('int', i)
        f = jcast('int', f)
        s = jcast('int', s)
        rank = jcast('int', rank)
        lsiz = jcast('int', Better2.aliveSiz[Better2.ls[i]])
        if (rank <= lsiz):
            Better2._java_remove_0(Better2.ls[i], i, 1, rank)
        else:
            cur = jcast('int', (1 if Better2.alive[i] else 0))
            if (Better2.alive[i] and (rank == jcast('int', jadd(lsiz, cur)))):
                Better2.alive[i] = jcast('boolean', False)
            else:
                Better2._java_remove_0(Better2.rs[i], i, 2, jcast('int', (jcast('int', (rank - lsiz)) - cur)))
        Better2.up(i)
        if (not Better2.balance(i)):
            Better2.top = jcast('int', i)
            Better2.father = jcast('int', f)
            Better2.side = jcast('int', s)

    @staticmethod
    def _java_remove_1(num):
        num = jcast('int', num)
        rank1 = jcast('int', Better2.rank(num))
        rank2 = jcast('int', Better2.rank(jcast('int', jadd(num, 1))))
        if (rank1 != rank2):
            Better2.top = jcast('int', jset(Better2, 'father', jset(Better2, 'side', 0)))
            Better2._java_remove_0(Better2.root, 0, 0, rank1)
            Better2.rebuild()

    @staticmethod
    def main(args):
        in_ = Better2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        n = jcast('int', jcall(in_, 'nextInt'))
        m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        num = 0
        while (i <= n):
            num = jcast('int', jcall(in_, 'nextInt'))
            Better2._java_add_1(num)
            i = jcast('int', (i + 1))
        lastAns = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        op = 0
        x = 0
        while (i <= m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcast('int', (x ^ lastAns)))
            if (op == 1):
                Better2._java_add_1(x)
            else:
                if (op == 2):
                    Better2._java_remove_1(x)
                else:
                    if (op == 3):
                        lastAns = jcast('int', Better2.rank(x))
                        ans = jcast('int', jcast('int', (ans ^ lastAns)))
                    else:
                        if (op == 4):
                            lastAns = jcast('int', Better2._java_index_1(x))
                            ans = jcast('int', jcast('int', (ans ^ lastAns)))
                        else:
                            if (op == 5):
                                lastAns = jcast('int', Better2.pre(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
                            else:
                                lastAns = jcast('int', Better2.post(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Better2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Better2._java_add_0(*args)
        if _java_choice == 1:
            return Better2._java_add_1(*args)
        raise TypeError("No matching overload for Better2.add")

    @staticmethod
    def index(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Better2._java_index_0(*args)
        if _java_choice == 1:
            return Better2._java_index_1(*args)
        raise TypeError("No matching overload for Better2.index")

    @staticmethod
    def remove(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Better2._java_remove_0(*args)
        if _java_choice == 1:
            return Better2._java_remove_1(*args)
        raise TypeError("No matching overload for Better2.remove")


Better2.MAXN = jcast('int', 2000001)
Better2.cntn = jcast('int', 0)
Better2.root = jcast('int', 0)
Better2.key = jarray('int', [Better2.MAXN])
Better2.ls = jarray('int', [Better2.MAXN])
Better2.rs = jarray('int', [Better2.MAXN])
Better2.alive = jarray('boolean', [Better2.MAXN])
Better2.aliveSiz = jarray('int', [Better2.MAXN])
Better2.ALPHA = jcast('double', 0.7)
Better2.top = jcast('int', 0)
Better2.father = jcast('int', 0)
Better2.side = jcast('int', 0)
Better2.collect = jarray('int', [Better2.MAXN])
Better2.collectSiz = jcast('int', 0)

if __name__ == '__main__':
    Better2.main([])
