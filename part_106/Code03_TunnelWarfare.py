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

# 地道相连的房子
# 有n个房子排成一排，编号1~n，一开始每相邻的两个房子之间都有地道
# 实现如下三个操作
# 操作 D x : 把x号房子摧毁，该房子附近的地道也一并摧毁
# 操作 R   : 恢复上次摧毁的房子，该房子附近的地道一并恢复
# 操作 Q x : 查询x号房子能到达的房子数量，包括x号房子自身
# 测试链接 : https://www.luogu.com.cn/problem/P1503
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_TunnelWarfare:
    __java_fields__ = {'MAXN': 'MAXN', 'pre': 'pre', 'suf': 'suf', 'stack': 'stack'}
    MAXN = 0
    # 连续1的最长前缀长度
    pre = None
    # 连续1的最长后缀长度
    suf = None
    # 摧毁的房屋编号入栈，以便执行恢复操作
    stack = None
    @staticmethod
    def up(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        Code03_TunnelWarfare.pre[i] = jcast('int', Code03_TunnelWarfare.pre[jcast('int', (i << (1 & 31)))])
        Code03_TunnelWarfare.suf[i] = jcast('int', Code03_TunnelWarfare.suf[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (Code03_TunnelWarfare.pre[jcast('int', (i << (1 & 31)))] == jcast('int', jadd(jcast('int', (mid - l)), 1))):
            Code03_TunnelWarfare.pre[i] = jcast('int', jcast('int', jadd(Code03_TunnelWarfare.pre[i], Code03_TunnelWarfare.pre[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        if (Code03_TunnelWarfare.suf[jcast('int', (jcast('int', (i << (1 & 31))) | 1))] == jcast('int', (r - mid))):
            Code03_TunnelWarfare.suf[i] = jcast('int', jcast('int', jadd(Code03_TunnelWarfare.suf[i], Code03_TunnelWarfare.suf[jcast('int', (i << (1 & 31)))])))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code03_TunnelWarfare.pre, i, jset(Code03_TunnelWarfare.suf, i, 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_TunnelWarfare.build(l, mid, jcast('int', (i << (1 & 31))))
            Code03_TunnelWarfare.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_TunnelWarfare.up(l, r, i)

    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code03_TunnelWarfare.pre, i, jset(Code03_TunnelWarfare.suf, i, jobv))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code03_TunnelWarfare.update(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code03_TunnelWarfare.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_TunnelWarfare.up(l, r, i)

    # 已知jobi在l...r范围上
    # 返回jobi往两侧扩展出的最大长度
    # 递归需要遵循的潜台词 : 从jobi往两侧扩展，一定无法扩展到l...r范围之外！
    @staticmethod
    def query(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', Code03_TunnelWarfare.pre[i])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                if (jobi > jcast('int', (mid - Code03_TunnelWarfare.suf[jcast('int', (i << (1 & 31)))]))):
                    return jcast('int', jcast('int', jadd(Code03_TunnelWarfare.suf[jcast('int', (i << (1 & 31)))], Code03_TunnelWarfare.pre[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
                else:
                    return jcast('int', Code03_TunnelWarfare.query(jobi, l, mid, jcast('int', (i << (1 & 31)))))
            else:
                if (jcast('int', jadd(mid, Code03_TunnelWarfare.pre[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])) >= jobi):
                    return jcast('int', jcast('int', jadd(Code03_TunnelWarfare.suf[jcast('int', (i << (1 & 31)))], Code03_TunnelWarfare.pre[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
                else:
                    return jcast('int', Code03_TunnelWarfare.query(jobi, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_TunnelWarfare.build(1, n, 1)
            op = None
            stackSize = jcast('int', 0)
            i = jcast('int', 1)
            x = 0
            while (i <= m):
                jcall(in_, 'nextToken')
                op = jget(in_, 'sval')
                if jcall(op, 'equals', 'D'):
                    jcall(in_, 'nextToken')
                    x = jcast('int', jcast('int', jget(in_, 'nval')))
                    Code03_TunnelWarfare.update(x, 0, 1, n, 1)
                    jset(Code03_TunnelWarfare.stack, ((_java_old_1 := stackSize), (stackSize := jcast('int', (stackSize + (1)))), _java_old_1)[2], x)
                else:
                    if jcall(op, 'equals', 'R'):
                        Code03_TunnelWarfare.update(Code03_TunnelWarfare.stack[(stackSize := jcast('int', (stackSize + (-1))))], 1, 1, n, 1)
                    else:
                        jcall(in_, 'nextToken')
                        x = jcast('int', jcast('int', jget(in_, 'nval')))
                        jcall(out, 'println', Code03_TunnelWarfare.query(x, 1, n, 1))
                i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_TunnelWarfare.MAXN = jcast('int', 50001)
Code03_TunnelWarfare.pre = jarray('int', [jcast('int', (Code03_TunnelWarfare.MAXN << (2 & 31)))])
Code03_TunnelWarfare.suf = jarray('int', [jcast('int', (Code03_TunnelWarfare.MAXN << (2 & 31)))])
Code03_TunnelWarfare.stack = jarray('int', [Code03_TunnelWarfare.MAXN])

if __name__ == '__main__':
    Code03_TunnelWarfare.main([])
