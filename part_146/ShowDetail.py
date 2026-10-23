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

# 提根操作的代码 + 长链高度变化的实验
# 分别去生成一字型长链和之字型长链
# 每一种长链都让最下方节点提根上去
# 然后看看长链的高度变化
class ShowDetail:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'father': 'father', 'left': 'left', 'right': 'right', 'size': 'size'}
    MAXN = 0
    # 整棵树的头节点编号
    head = 0
    # 分配了多少节点编号
    cnt = 0
    # key[i]    : 编号为i的节点的key
    key = None
    # father[i] : 编号为i的节点的父节点编号
    father = None
    # left[i]   : 编号为i的节点的左孩子编号
    left = None
    # right[i]  : 编号为i的节点的右孩子编号
    right = None
    # size[i]   : 以编号为i的节点做头的子树，一共有多少个节点
    # 这个数组和具体要实现的功能有关，属于常用信息
    size = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        ShowDetail.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(ShowDetail.size[ShowDetail.left[i]], ShowDetail.size[ShowDetail.right[i]])), 1)))

    # 判断编号为i的节点，是其父亲的什么儿子
    # 0代表左儿子，1代表右儿子
    @staticmethod
    def lr(i):
        i = jcast('int', i)
        return jcast('int', (1 if (ShowDetail.right[ShowDetail.father[i]] == i) else 0))

    # 编号为i的节点上升一步，在结构上做调整
    @staticmethod
    def rotate(i):
        i = jcast('int', i)
        f = jcast('int', ShowDetail.father[i])
        g = jcast('int', ShowDetail.father[f])
        soni = jcast('int', ShowDetail.lr(i))
        sonf = jcast('int', ShowDetail.lr(f))
        if (soni == 1):
            ShowDetail.right[f] = jcast('int', ShowDetail.left[i])
            if (ShowDetail.right[f] != 0):
                jset(ShowDetail.father, ShowDetail.right[f], f)
            ShowDetail.left[i] = jcast('int', f)
        else:
            ShowDetail.left[f] = jcast('int', ShowDetail.right[i])
            if (ShowDetail.left[f] != 0):
                jset(ShowDetail.father, ShowDetail.left[f], f)
            ShowDetail.right[i] = jcast('int', f)
        if (g != 0):
            if (sonf == 1):
                ShowDetail.right[g] = jcast('int', i)
            else:
                ShowDetail.left[g] = jcast('int', i)
        ShowDetail.father[f] = jcast('int', i)
        ShowDetail.father[i] = jcast('int', g)
        ShowDetail.up(f)
        ShowDetail.up(i)

    # 编号为i的节点提根，变成编号为goal的节点的儿子
    # 如果goal == 0，表示把编号为i的节点变成整棵树的头
    @staticmethod
    def splay(i, goal):
        i = jcast('int', i)
        goal = jcast('int', goal)
        f = jcast('int', ShowDetail.father[i])
        g = jcast('int', ShowDetail.father[f])
        while (f != goal):
            if (g != goal):
                if (ShowDetail.lr(i) == ShowDetail.lr(f)):
                    ShowDetail.rotate(f)
                else:
                    ShowDetail.rotate(i)
            ShowDetail.rotate(i)
            f = jcast('int', ShowDetail.father[i])
            g = jcast('int', ShowDetail.father[f])
        if (goal == 0):
            ShowDetail.head = jcast('int', i)

    # 构建一字型长链
    @staticmethod
    def build1(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        h = jcast('int', jcast('int', jadd(ShowDetail.cnt, 1)))
        i = jcast('int', l)
        last = jcast('int', 0)
        while (i <= r):
            jset(ShowDetail.key, ((_java_obj_1 := ShowDetail), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], i)
            ShowDetail.father[ShowDetail.cnt] = jcast('int', last)
            jset(ShowDetail.left, ShowDetail.cnt, jset(ShowDetail.right, ShowDetail.cnt, 0))
            ShowDetail.size[ShowDetail.cnt] = jcast('int', jcast('int', jadd(jcast('int', (r - i)), 1)))
            if (last != 0):
                ShowDetail.right[last] = jcast('int', ShowDetail.cnt)
            i = jcast('int', (i + 1))
            last = jcast('int', ShowDetail.cnt)
        return jcast('int', h)

    # 构建之字形长链
    @staticmethod
    def build2(l, r, fa):
        l = jcast('int', l)
        r = jcast('int', r)
        fa = jcast('int', fa)
        if (l > r):
            return jcast('int', 0)
        jset(ShowDetail.key, ((_java_obj_4 := ShowDetail), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], l)
        ShowDetail.father[ShowDetail.cnt] = jcast('int', fa)
        jset(ShowDetail.left, ShowDetail.cnt, jset(ShowDetail.right, ShowDetail.cnt, 0))
        h = jcast('int', ShowDetail.cnt)
        if (l < r):
            jset(ShowDetail.key, ((_java_obj_7 := ShowDetail), (_java_key_8 := 'cnt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], r)
            ShowDetail.father[ShowDetail.cnt] = jcast('int', h)
            jset(ShowDetail.left, ShowDetail.cnt, jset(ShowDetail.right, ShowDetail.cnt, 0))
            c = jcast('int', ShowDetail.cnt)
            ShowDetail.right[h] = jcast('int', c)
            jset(ShowDetail.left, c, ShowDetail.build2(jcast('int', jadd(l, 1)), jcast('int', (r - 1)), c))
            ShowDetail.up(c)
        ShowDetail.up(h)
        return jcast('int', h)

    # 返回以i为头的树的高度
    @staticmethod
    def height(i):
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        return jcast('int', jcast('int', jadd(jstatic('Math', 'max', ShowDetail.height(ShowDetail.left[i]), ShowDetail.height(ShowDetail.right[i])), 1)))

    @staticmethod
    def main(args):
        jprint('构建一字型长链', newline=True)
        jprint('最下方节点执行splay，观察高度变化', newline=True)
        ShowDetail.head = jcast('int', ShowDetail.build1(1, 1000))
        jprint(jadd('splay之前的链长度 : ', ShowDetail.height(ShowDetail.head)), newline=True)
        ShowDetail.splay(ShowDetail.cnt, 0)
        jprint(jadd('splay之后的链长度 : ', ShowDetail.height(ShowDetail.head)), newline=True)
        jprint('==================', newline=True)
        jprint('构建之字型长链', newline=True)
        jprint('最下方节点执行splay，观察高度变化', newline=True)
        ShowDetail.head = jcast('int', ShowDetail.build2(1, 1000, 0))
        jprint(jadd('splay之前的链长度 : ', ShowDetail.height(ShowDetail.head)), newline=True)
        ShowDetail.splay(ShowDetail.cnt, 0)
        jprint(jadd('splay之后的链长度 : ', ShowDetail.height(ShowDetail.head)), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


ShowDetail.MAXN = jcast('int', 100001)
ShowDetail.head = jcast('int', 0)
ShowDetail.cnt = jcast('int', 0)
ShowDetail.key = jarray('int', [ShowDetail.MAXN])
ShowDetail.father = jarray('int', [ShowDetail.MAXN])
ShowDetail.left = jarray('int', [ShowDetail.MAXN])
ShowDetail.right = jarray('int', [ShowDetail.MAXN])
ShowDetail.size = jarray('int', [ShowDetail.MAXN])

if __name__ == '__main__':
    ShowDetail.main([])
