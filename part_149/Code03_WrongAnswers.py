# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 错误答案数量，带权并查集模版题3
# 有n个数字，下标1 ~ n，但是并不知道每个数字是多少
# 操作 l r v，代表l~r范围上累加和为v
# 一共m个操作，如果某个操作和之前的操作信息自相矛盾，认为当前操作是错误的，不进行这个操作
# 最后打印错误操作的数量
# 1 <= n <= 200000    1 <= m <= 40000
# 累加和不会超过int类型范围
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=3038
# 测试链接 : https://vjudge.net/problem/HDU-3038
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_WrongAnswers:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'ans': 'ans', 'father': 'father', 'dist': 'dist'}
    MAXN = 0
    n = 0
    m = 0
    ans = 0
    father = None
    dist = None
    @staticmethod
    def prepare():
        Code03_WrongAnswers.ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i <= Code03_WrongAnswers.n):
            Code03_WrongAnswers.father[i] = jcast('int', i)
            Code03_WrongAnswers.dist[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_WrongAnswers.father[i]):
            tmp = jcast('int', Code03_WrongAnswers.father[i])
            jset(Code03_WrongAnswers.father, i, Code03_WrongAnswers.find(tmp))
            Code03_WrongAnswers.dist[i] = jcast('int', jcast('int', jadd(Code03_WrongAnswers.dist[i], Code03_WrongAnswers.dist[tmp])))
        return jcast('int', Code03_WrongAnswers.father[i])

    @staticmethod
    def union(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        lf = jcast('int', Code03_WrongAnswers.find(l))
        rf = jcast('int', Code03_WrongAnswers.find(r))
        if (lf != rf):
            Code03_WrongAnswers.father[lf] = jcast('int', rf)
            Code03_WrongAnswers.dist[lf] = jcast('int', jcast('int', (jcast('int', jadd(v, Code03_WrongAnswers.dist[r])) - Code03_WrongAnswers.dist[l])))

    @staticmethod
    def check(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        if (Code03_WrongAnswers.find(l) == Code03_WrongAnswers.find(r)):
            if (jcast('int', (Code03_WrongAnswers.dist[l] - Code03_WrongAnswers.dist[r])) != v):
                return jcast('boolean', False)
        return jcast('boolean', True)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_WrongAnswers.n = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
            jcall(in_, 'nextToken')
            Code03_WrongAnswers.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_WrongAnswers.prepare()
            i = jcast('int', 1)
            l = 0
            r = 0
            v = 0
            while (i <= Code03_WrongAnswers.m):
                jcall(in_, 'nextToken')
                l = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                r = jcast('int', jcast('int', jadd(jcast('int', jget(in_, 'nval')), 1)))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                if (not Code03_WrongAnswers.check(l, r, v)):
                    Code03_WrongAnswers.ans = jcast('int', (Code03_WrongAnswers.ans + 1))
                else:
                    Code03_WrongAnswers.union(l, r, v)
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_WrongAnswers.ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_WrongAnswers.MAXN = jcast('int', 200002)
Code03_WrongAnswers.n = jcast('int', 0)
Code03_WrongAnswers.m = jcast('int', 0)
Code03_WrongAnswers.ans = jcast('int', 0)
Code03_WrongAnswers.father = jarray('int', [Code03_WrongAnswers.MAXN])
Code03_WrongAnswers.dist = jarray('int', [Code03_WrongAnswers.MAXN])

if __name__ == '__main__':
    Code03_WrongAnswers.main([])
