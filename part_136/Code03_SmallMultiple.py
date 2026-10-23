# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 正整数倍的最小数位和
# 给定一个整数k，求一个k的正整数倍s，使得在十进制下，s的数位累加和最小
# 2 <= k <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/AT_arc084_b
# 测试链接 : https://atcoder.jp/contests/abc077/tasks/arc084_b
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_SmallMultiple:
    __java_fields__ = {'MAXK': 'MAXK', 'k': 'k', 'deque': 'deque', 'visit': 'visit'}
    MAXK = 0
    k = 0
    # 01bfs需要
    deque = None
    visit = None
    # 来自讲解062，01bfs
    @staticmethod
    def bfs():
        jcall(Code03_SmallMultiple.deque, 'clear')
        jcall(Code03_SmallMultiple.deque, 'add', jarray('int', [None], [1, 1]))
        cur = None
        mod = 0
        cost = 0
        while (not jcall(Code03_SmallMultiple.deque, 'isEmpty')):
            cur = jcall(Code03_SmallMultiple.deque, 'pollFirst')
            mod = jcast('int', cur[0])
            cost = jcast('int', cur[1])
            if (not Code03_SmallMultiple.visit[mod]):
                Code03_SmallMultiple.visit[mod] = jcast('boolean', True)
                if (mod == 0):
                    return jcast('int', cost)
                jcall(Code03_SmallMultiple.deque, 'addFirst', jarray('int', [None], [jcast('int', jmod(jcast('int', (mod * 10)), Code03_SmallMultiple.k)), cost]))
                jcall(Code03_SmallMultiple.deque, 'addLast', jarray('int', [None], [jcast('int', jmod(jcast('int', jadd(mod, 1)), Code03_SmallMultiple.k)), jcast('int', jadd(cost, 1))]))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_SmallMultiple.k = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code03_SmallMultiple.bfs())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SmallMultiple.MAXK = jcast('int', 100001)
Code03_SmallMultiple.k = jcast('int', 0)
Code03_SmallMultiple.deque = jnew('ArrayDeque')
Code03_SmallMultiple.visit = jarray('boolean', [Code03_SmallMultiple.MAXK])

if __name__ == '__main__':
    Code03_SmallMultiple.main([])
