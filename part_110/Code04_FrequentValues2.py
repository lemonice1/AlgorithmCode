# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 出现次数最多的数有几个
# 给定一个长度为n的数组arr，该数组一定是有序的
# 一共有m次查询，每次查询arr[l~r]上出现次数最多的数有几个
# 题目查看 : https://www.luogu.com.cn/problem/UVA11235
# 题目提交 : https://vjudge.net/problem/UVA-11235
# 洛谷上提交会发生远程连接错误，需要绑定一个UVA账号再提交
# 也可以注册一个vjudge账号来提交，不过如果UVA链接不上就需要等
# 其实用对数器验证即可，我肯定是提交通过测试了的
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_FrequentValues2:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'arr': 'arr', 'log2': 'log2', 'bucket': 'bucket', 'left': 'left', 'right': 'right', 'stmax': 'stmax'}
    MAXN = 0
    LIMIT = 0
    arr = None
    log2 = None
    bucket = None
    left = None
    right = None
    stmax = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        # 题目给定的数值范围-100000 ~ +100000
        # 把arr[0]设置成不会到达的数字即可
        Code04_FrequentValues2.arr[0] = jcast('int', jcast('int', (-23333333)))
        cnt = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= n):
            if (Code04_FrequentValues2.arr[jcast('int', (i - 1))] != Code04_FrequentValues2.arr[i]):
                Code04_FrequentValues2.right[cnt] = jcast('int', jcast('int', (i - 1)))
                jset(Code04_FrequentValues2.left, (cnt := jcast('int', (cnt + (1)))), i)
            Code04_FrequentValues2.bucket[i] = jcast('int', cnt)
            i = jcast('int', (i + 1))
        Code04_FrequentValues2.right[cnt] = jcast('int', n)
        Code04_FrequentValues2.log2[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= cnt):
            Code04_FrequentValues2.log2[i] = jcast('int', jcast('int', jadd(Code04_FrequentValues2.log2[jcast('int', (i >> (1 & 31)))], 1)))
            jset(Code04_FrequentValues2.stmax[i], 0, jcast('int', jadd(jcast('int', (Code04_FrequentValues2.right[i] - Code04_FrequentValues2.left[i])), 1)))
            i = jcast('int', (i + 1))
        p = jcast('int', 1)
        while (p <= Code04_FrequentValues2.log2[cnt]):
            i = jcast('int', 1)
            while (jcast('int', (jcast('int', jadd(i, jcast('int', (1 << (p & 31))))) - 1)) <= cnt):
                jset(Code04_FrequentValues2.stmax[i], p, jstatic('Math', 'max', Code04_FrequentValues2.stmax[i][jcast('int', (p - 1))], Code04_FrequentValues2.stmax[jcast('int', jadd(i, jcast('int', (1 << (jcast('int', (p - 1)) & 31)))))][jcast('int', (p - 1))]))
                i = jcast('int', (i + 1))
            p = jcast('int', (p + 1))

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            tmp = jcast('int', l)
            l = jcast('int', r)
            r = jcast('int', tmp)
        lbucket = jcast('int', Code04_FrequentValues2.bucket[l])
        rbucket = jcast('int', Code04_FrequentValues2.bucket[r])
        if (lbucket == rbucket):
            return jcast('int', jcast('int', jadd(jcast('int', (r - l)), 1)))
        a = jcast('int', jcast('int', jadd(jcast('int', (Code04_FrequentValues2.right[lbucket] - l)), 1)))
        b = jcast('int', jcast('int', jadd(jcast('int', (r - Code04_FrequentValues2.left[rbucket])), 1)))
        c = jcast('int', 0)
        if (jcast('int', jadd(lbucket, 1)) < rbucket):
            from_ = jcast('int', jcast('int', jadd(lbucket, 1)))
            to = jcast('int', jcast('int', (rbucket - 1)))
            p = jcast('int', Code04_FrequentValues2.log2[jcast('int', jadd(jcast('int', (to - from_)), 1))])
            c = jcast('int', jstatic('Math', 'max', Code04_FrequentValues2.stmax[from_][p], Code04_FrequentValues2.stmax[jcast('int', jadd(jcast('int', (to - jcast('int', (1 << (p & 31))))), 1))][p]))
        return jcast('int', jstatic('Math', 'max', jstatic('Math', 'max', a, b), c))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            try:
                n = jcast('int', jcast('int', jget(in_, 'nval')))
                if (n == 0):
                    raise JBreak(None)
                jcall(in_, 'nextToken')
                m = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', 1)
                while (i <= n):
                    jcall(in_, 'nextToken')
                    Code04_FrequentValues2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                    i = jcast('int', (i + 1))
                Code04_FrequentValues2.build(n)
                i = jcast('int', 1)
                l = 0
                r = 0
                while (i <= m):
                    jcall(in_, 'nextToken')
                    l = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    r = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(out, 'println', Code04_FrequentValues2.query(l, r))
                    i = jcast('int', (i + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_FrequentValues2.MAXN = jcast('int', 100001)
Code04_FrequentValues2.LIMIT = jcast('int', 17)
Code04_FrequentValues2.arr = jarray('int', [Code04_FrequentValues2.MAXN])
Code04_FrequentValues2.log2 = jarray('int', [Code04_FrequentValues2.MAXN])
Code04_FrequentValues2.bucket = jarray('int', [Code04_FrequentValues2.MAXN])
Code04_FrequentValues2.left = jarray('int', [Code04_FrequentValues2.MAXN])
Code04_FrequentValues2.right = jarray('int', [Code04_FrequentValues2.MAXN])
Code04_FrequentValues2.stmax = jarray('int', [Code04_FrequentValues2.MAXN, Code04_FrequentValues2.LIMIT])

if __name__ == '__main__':
    Code04_FrequentValues2.main([])
