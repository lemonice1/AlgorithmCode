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

# 树的序
# 给定一个长度为n的数组arr，表示依次插入数字，会形成一棵搜索二叉树
# 也许同样的一个序列，依次插入数字后，也能形成同样形态的搜索二叉树
# 请返回字典序尽量小的结果
# 1 <= n <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P1377
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_TreeOrder:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'left': 'left', 'right': 'right', 'stack': 'stack', 'n': 'n'}
    MAXN = 0
    arr = None
    left = None
    right = None
    stack = None
    n = 0
    @staticmethod
    def build():
        i = jcast('int', 1)
        top = jcast('int', 0)
        pos = jcast('int', 0)
        while (i <= Code03_TreeOrder.n):
            pos = jcast('int', top)
            while ((pos > 0) and (Code03_TreeOrder.arr[Code03_TreeOrder.stack[pos]] > Code03_TreeOrder.arr[i])):
                pos = jcast('int', (pos - 1))
            if (pos > 0):
                jset(Code03_TreeOrder.right, Code03_TreeOrder.stack[pos], i)
            if (pos < top):
                Code03_TreeOrder.left[i] = jcast('int', Code03_TreeOrder.stack[jcast('int', jadd(pos, 1))])
            jset(Code03_TreeOrder.stack, (pos := jcast('int', (pos + (1)))), i)
            top = jcast('int', pos)
            i = jcast('int', (i + 1))

    # 防止递归爆栈用迭代的方式实现先序遍历
    @staticmethod
    def pre():
        size = jcast('int', 1)
        i = jcast('int', 0)
        cur = 0
        while (size > 0):
            cur = jcast('int', Code03_TreeOrder.stack[((_java_old_1 := size), (size := jcast('int', (size + (-1)))), _java_old_1)[2]])
            jset(Code03_TreeOrder.arr, (i := jcast('int', (i + (1)))), cur)
            if (Code03_TreeOrder.right[cur] != 0):
                jset(Code03_TreeOrder.stack, (size := jcast('int', (size + (1)))), Code03_TreeOrder.right[cur])
            if (Code03_TreeOrder.left[cur] != 0):
                jset(Code03_TreeOrder.stack, (size := jcast('int', (size + (1)))), Code03_TreeOrder.left[cur])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_TreeOrder.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code03_TreeOrder.n):
            jcall(in_, 'nextToken')
            jset(Code03_TreeOrder.arr, jcast('int', jget(in_, 'nval')), i)
            i = jcast('int', (i + 1))
        Code03_TreeOrder.build()
        Code03_TreeOrder.pre()
        i = jcast('int', 1)
        while (i <= Code03_TreeOrder.n):
            jcall(out, 'print', jadd(Code03_TreeOrder.arr[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_TreeOrder.MAXN = jcast('int', 100001)
Code03_TreeOrder.arr = jarray('int', [Code03_TreeOrder.MAXN])
Code03_TreeOrder.left = jarray('int', [Code03_TreeOrder.MAXN])
Code03_TreeOrder.right = jarray('int', [Code03_TreeOrder.MAXN])
Code03_TreeOrder.stack = jarray('int', [Code03_TreeOrder.MAXN])
Code03_TreeOrder.n = jcast('int', 0)

if __name__ == '__main__':
    Code03_TreeOrder.main([])
