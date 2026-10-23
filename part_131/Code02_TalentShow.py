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

# 牛群的才艺展示
# 一共有n只牛，每只牛有重量和才艺两个属性值
# 要求一定要选若干只牛，使得总重量不少于w，并且选出的牛，希望让
# 才艺的和 / 重量的和，这个比值尽量大
# 返回该比值 * 1000的整数结果，小数部分舍弃
# 1 <= n <= 250
# 1 <= w <= 1000
# 1 <= 牛的重量 <= 10^6
# 1 <= 牛的才艺 <= 10^3
# 测试链接 : https://www.luogu.com.cn/problem/P4377
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_TalentShow:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXW': 'MAXW', 'NA': 'NA', 'sml': 'sml', 'weight': 'weight', 'talent': 'talent', 'value': 'value', 'dp': 'dp', 'n': 'n', 'w': 'w'}
    MAXN = 0
    MAXW = 0
    # 足够小代表无效解
    NA = 0.0
    # 最小精度
    sml = 0.0
    # 重量
    weight = None
    # 才艺
    talent = None
    # (才艺 - x * 重量)的结余
    value = None
    # dp[i][j] : 1...i号牛自由选择，重量必须是j的情况下，最大的结余和
    # 特别的，dp[i][w]表示1...i号牛自由选择，重量必须是w、w+1...的所有情况中，最大的结余和
    # 为了节省时间和空间选择这么定义，同时做空间压缩
    dp = None
    n = 0
    w = 0
    @staticmethod
    def check(x):
        x = jcast('double', x)
        i = jcast('int', 1)
        while (i <= Code02_TalentShow.n):
            Code02_TalentShow.value[i] = jcast('double', (jcast('double', Code02_TalentShow.talent[i]) - (x * Code02_TalentShow.weight[i])))
            i = jcast('int', (i + 1))
        Code02_TalentShow.dp[0] = jcast('double', 0)
        jstatic('Arrays', 'fill', Code02_TalentShow.dp, 1, jcast('int', jadd(Code02_TalentShow.w, 1)), Code02_TalentShow.NA)
        i = jcast('int', 1)
        while (i <= Code02_TalentShow.n):
            p = jcast('int', Code02_TalentShow.w)
            j = 0
            while (p >= 0):
                j = jcast('int', jcast('int', jcast('int', jadd(p, Code02_TalentShow.weight[i]))))
                if (j >= Code02_TalentShow.w):
                    jset(Code02_TalentShow.dp, Code02_TalentShow.w, jstatic('Math', 'max', Code02_TalentShow.dp[Code02_TalentShow.w], jadd(Code02_TalentShow.dp[p], Code02_TalentShow.value[i])))
                else:
                    jset(Code02_TalentShow.dp, j, jstatic('Math', 'max', Code02_TalentShow.dp[j], jadd(Code02_TalentShow.dp[p], Code02_TalentShow.value[i])))
                p = jcast('int', (p - 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', (Code02_TalentShow.dp[Code02_TalentShow.w] >= 0))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_TalentShow.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_TalentShow.w = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code02_TalentShow.n):
            jcall(in_, 'nextToken')
            Code02_TalentShow.weight[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_TalentShow.talent[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        l = jcast('double', 0)
        r = jcast('double', 0)
        x = 0.0
        i = jcast('int', 1)
        while (i <= Code02_TalentShow.n):
            r = jcast('double', jadd(r, Code02_TalentShow.talent[i]))
            i = jcast('int', (i + 1))
        ans = jcast('double', 0)
        while ((l < r) and ((r - l) >= Code02_TalentShow.sml)):
            x = jcast('double', jdiv(jadd(l, r), 2))
            if Code02_TalentShow.check(x):
                ans = jcast('double', x)
                l = jcast('double', jadd(x, Code02_TalentShow.sml))
            else:
                r = jcast('double', (x - Code02_TalentShow.sml))
        jcall(out, 'println', jcast('int', (ans * 1000)))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_TalentShow.MAXN = jcast('int', 251)
Code02_TalentShow.MAXW = jcast('int', 1001)
Code02_TalentShow.NA = jcast('double', (-1000000000.0))
Code02_TalentShow.sml = jcast('double', 1e-06)
Code02_TalentShow.weight = jarray('int', [Code02_TalentShow.MAXN])
Code02_TalentShow.talent = jarray('int', [Code02_TalentShow.MAXN])
Code02_TalentShow.value = jarray('double', [Code02_TalentShow.MAXN])
Code02_TalentShow.dp = jarray('double', [Code02_TalentShow.MAXW])
Code02_TalentShow.n = jcast('int', 0)
Code02_TalentShow.w = jcast('int', 0)

if __name__ == '__main__':
    Code02_TalentShow.main([])
