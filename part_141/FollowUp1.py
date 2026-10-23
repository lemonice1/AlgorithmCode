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

# AVL实现普通有序表，数据加强的测试，Python版
# 这个文件课上没有讲，测试数据加强了，而且有强制在线的要求
# 基本功能要求都是不变的，可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P6136
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class FollowUp1:
    __java_fields__ = {'MAXN': 'MAXN', 'cnt': 'cnt', 'head': 'head', 'key': 'key', 'height': 'height', 'left': 'left', 'right': 'right', 'count': 'count', 'size': 'size'}
    MAXN = 0
    cnt = 0
    head = 0
    key = None
    height = None
    left = None
    right = None
    count = None
    size = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        FollowUp1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(FollowUp1.size[FollowUp1.left[i]], FollowUp1.size[FollowUp1.right[i]])), FollowUp1.count[i])))
        jset(FollowUp1.height, i, jcast('int', jadd(jstatic('Math', 'max', FollowUp1.height[FollowUp1.left[i]], FollowUp1.height[FollowUp1.right[i]]), 1)))

    @staticmethod
    def leftRotate(i):
        i = jcast('int', i)
        r = jcast('int', FollowUp1.right[i])
        FollowUp1.right[i] = jcast('int', FollowUp1.left[r])
        FollowUp1.left[r] = jcast('int', i)
        FollowUp1.up(i)
        FollowUp1.up(r)
        return jcast('int', r)

    @staticmethod
    def rightRotate(i):
        i = jcast('int', i)
        l = jcast('int', FollowUp1.left[i])
        FollowUp1.left[i] = jcast('int', FollowUp1.right[l])
        FollowUp1.right[l] = jcast('int', i)
        FollowUp1.up(i)
        FollowUp1.up(l)
        return jcast('int', l)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        lh = jcast('int', FollowUp1.height[FollowUp1.left[i]])
        rh = jcast('int', FollowUp1.height[FollowUp1.right[i]])
        if (jcast('int', (lh - rh)) > 1):
            if (FollowUp1.height[FollowUp1.left[FollowUp1.left[i]]] >= FollowUp1.height[FollowUp1.right[FollowUp1.left[i]]]):
                i = jcast('int', FollowUp1.rightRotate(i))
            else:
                jset(FollowUp1.left, i, FollowUp1.leftRotate(FollowUp1.left[i]))
                i = jcast('int', FollowUp1.rightRotate(i))
        else:
            if (jcast('int', (rh - lh)) > 1):
                if (FollowUp1.height[FollowUp1.right[FollowUp1.right[i]]] >= FollowUp1.height[FollowUp1.left[FollowUp1.right[i]]]):
                    i = jcast('int', FollowUp1.leftRotate(i))
                else:
                    jset(FollowUp1.right, i, FollowUp1.rightRotate(FollowUp1.right[i]))
                    i = jcast('int', FollowUp1.leftRotate(i))
        return jcast('int', i)

    @staticmethod
    def _java_add_0(num):
        num = jcast('int', num)
        FollowUp1.head = jcast('int', FollowUp1._java_add_1(FollowUp1.head, num))

    @staticmethod
    def _java_add_1(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            jset(FollowUp1.key, ((_java_obj_1 := FollowUp1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
            jset(FollowUp1.count, FollowUp1.cnt, jset(FollowUp1.size, FollowUp1.cnt, jset(FollowUp1.height, FollowUp1.cnt, 1)))
            return jcast('int', FollowUp1.cnt)
        if (FollowUp1.key[i] == num):
            FollowUp1.count[i] = jcast('int', (FollowUp1.count[i] + 1))
        else:
            if (FollowUp1.key[i] > num):
                jset(FollowUp1.left, i, FollowUp1._java_add_1(FollowUp1.left[i], num))
            else:
                jset(FollowUp1.right, i, FollowUp1._java_add_1(FollowUp1.right[i], num))
        FollowUp1.up(i)
        return jcast('int', FollowUp1.maintain(i))

    @staticmethod
    def _java_remove_0(num):
        num = jcast('int', num)
        if (FollowUp1.rank(num) != FollowUp1.rank(jcast('int', jadd(num, 1)))):
            FollowUp1.head = jcast('int', FollowUp1._java_remove_1(FollowUp1.head, num))

    @staticmethod
    def _java_remove_1(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (FollowUp1.key[i] < num):
            jset(FollowUp1.right, i, FollowUp1._java_remove_1(FollowUp1.right[i], num))
        else:
            if (FollowUp1.key[i] > num):
                jset(FollowUp1.left, i, FollowUp1._java_remove_1(FollowUp1.left[i], num))
            else:
                if (FollowUp1.count[i] > 1):
                    FollowUp1.count[i] = jcast('int', (FollowUp1.count[i] - 1))
                else:
                    if ((FollowUp1.left[i] == 0) and (FollowUp1.right[i] == 0)):
                        return jcast('int', 0)
                    else:
                        if ((FollowUp1.left[i] != 0) and (FollowUp1.right[i] == 0)):
                            i = jcast('int', FollowUp1.left[i])
                        else:
                            if ((FollowUp1.left[i] == 0) and (FollowUp1.right[i] != 0)):
                                i = jcast('int', FollowUp1.right[i])
                            else:
                                mostLeft = jcast('int', FollowUp1.right[i])
                                while (FollowUp1.left[mostLeft] != 0):
                                    mostLeft = jcast('int', FollowUp1.left[mostLeft])
                                jset(FollowUp1.right, i, FollowUp1.removeMostLeft(FollowUp1.right[i], mostLeft))
                                FollowUp1.left[mostLeft] = jcast('int', FollowUp1.left[i])
                                FollowUp1.right[mostLeft] = jcast('int', FollowUp1.right[i])
                                i = jcast('int', mostLeft)
        FollowUp1.up(i)
        return jcast('int', FollowUp1.maintain(i))

    @staticmethod
    def removeMostLeft(i, mostLeft):
        i = jcast('int', i)
        mostLeft = jcast('int', mostLeft)
        if (i == mostLeft):
            return jcast('int', FollowUp1.right[i])
        else:
            jset(FollowUp1.left, i, FollowUp1.removeMostLeft(FollowUp1.left[i], mostLeft))
            FollowUp1.up(i)
            return jcast('int', FollowUp1.maintain(i))

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        return jcast('int', jcast('int', jadd(FollowUp1.small(FollowUp1.head, num), 1)))

    @staticmethod
    def small(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', 0)
        if (FollowUp1.key[i] >= num):
            return jcast('int', FollowUp1.small(FollowUp1.left[i], num))
        else:
            return jcast('int', jcast('int', jadd(jcast('int', jadd(FollowUp1.size[FollowUp1.left[i]], FollowUp1.count[i])), FollowUp1.small(FollowUp1.right[i], num))))

    @staticmethod
    def _java_index_0(x):
        x = jcast('int', x)
        return jcast('int', FollowUp1._java_index_1(FollowUp1.head, x))

    @staticmethod
    def _java_index_1(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (FollowUp1.size[FollowUp1.left[i]] >= x):
            return jcast('int', FollowUp1._java_index_1(FollowUp1.left[i], x))
        else:
            if (jcast('int', jadd(FollowUp1.size[FollowUp1.left[i]], FollowUp1.count[i])) < x):
                return jcast('int', FollowUp1._java_index_1(FollowUp1.right[i], jcast('int', (jcast('int', (x - FollowUp1.size[FollowUp1.left[i]])) - FollowUp1.count[i]))))
        return jcast('int', FollowUp1.key[i])

    @staticmethod
    def _java_pre_0(num):
        num = jcast('int', num)
        return jcast('int', FollowUp1._java_pre_1(FollowUp1.head, num))

    @staticmethod
    def _java_pre_1(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        if (FollowUp1.key[i] >= num):
            return jcast('int', FollowUp1._java_pre_1(FollowUp1.left[i], num))
        else:
            return jcast('int', jstatic('Math', 'max', FollowUp1.key[i], FollowUp1._java_pre_1(FollowUp1.right[i], num)))

    @staticmethod
    def _java_post_0(num):
        num = jcast('int', num)
        return jcast('int', FollowUp1._java_post_1(FollowUp1.head, num))

    @staticmethod
    def _java_post_1(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        if (FollowUp1.key[i] <= num):
            return jcast('int', FollowUp1._java_post_1(FollowUp1.right[i], num))
        else:
            return jcast('int', jstatic('Math', 'min', FollowUp1.key[i], FollowUp1._java_post_1(FollowUp1.left[i], num)))

    @staticmethod
    def clear():
        jstatic('Arrays', 'fill', FollowUp1.key, 1, jcast('int', jadd(FollowUp1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', FollowUp1.height, 1, jcast('int', jadd(FollowUp1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', FollowUp1.left, 1, jcast('int', jadd(FollowUp1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', FollowUp1.right, 1, jcast('int', jadd(FollowUp1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', FollowUp1.count, 1, jcast('int', jadd(FollowUp1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', FollowUp1.size, 1, jcast('int', jadd(FollowUp1.cnt, 1)), 0)
        FollowUp1.cnt = jcast('int', 0)
        FollowUp1.head = jcast('int', 0)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        num = 0
        while (i <= n):
            jcall(in_, 'nextToken')
            num = jcast('int', jcast('int', jget(in_, 'nval')))
            FollowUp1._java_add_0(num)
            i = jcast('int', (i + 1))
        lastAns = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        op = 0
        x = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', (jcast('int', jget(in_, 'nval')) ^ lastAns)))
            if (op == 1):
                FollowUp1._java_add_0(x)
            else:
                if (op == 2):
                    FollowUp1._java_remove_0(x)
                else:
                    if (op == 3):
                        lastAns = jcast('int', FollowUp1.rank(x))
                        ans = jcast('int', jcast('int', (ans ^ lastAns)))
                    else:
                        if (op == 4):
                            lastAns = jcast('int', FollowUp1._java_index_0(x))
                            ans = jcast('int', jcast('int', (ans ^ lastAns)))
                        else:
                            if (op == 5):
                                lastAns = jcast('int', FollowUp1._java_pre_0(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
                            else:
                                lastAns = jcast('int', FollowUp1._java_post_0(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
        FollowUp1.clear()
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return FollowUp1._java_add_0(*args)
        if _java_choice == 1:
            return FollowUp1._java_add_1(*args)
        raise TypeError("No matching overload for FollowUp1.add")

    @staticmethod
    def remove(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return FollowUp1._java_remove_0(*args)
        if _java_choice == 1:
            return FollowUp1._java_remove_1(*args)
        raise TypeError("No matching overload for FollowUp1.remove")

    @staticmethod
    def index(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return FollowUp1._java_index_0(*args)
        if _java_choice == 1:
            return FollowUp1._java_index_1(*args)
        raise TypeError("No matching overload for FollowUp1.index")

    @staticmethod
    def pre(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return FollowUp1._java_pre_0(*args)
        if _java_choice == 1:
            return FollowUp1._java_pre_1(*args)
        raise TypeError("No matching overload for FollowUp1.pre")

    @staticmethod
    def post(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return FollowUp1._java_post_0(*args)
        if _java_choice == 1:
            return FollowUp1._java_post_1(*args)
        raise TypeError("No matching overload for FollowUp1.post")


FollowUp1.MAXN = jcast('int', 2000001)
FollowUp1.cnt = jcast('int', 0)
FollowUp1.head = jcast('int', 0)
FollowUp1.key = jarray('int', [FollowUp1.MAXN])
FollowUp1.height = jarray('int', [FollowUp1.MAXN])
FollowUp1.left = jarray('int', [FollowUp1.MAXN])
FollowUp1.right = jarray('int', [FollowUp1.MAXN])
FollowUp1.count = jarray('int', [FollowUp1.MAXN])
FollowUp1.size = jarray('int', [FollowUp1.MAXN])

if __name__ == '__main__':
    FollowUp1.main([])
