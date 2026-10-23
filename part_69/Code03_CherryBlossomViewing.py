# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 观赏樱花
# 给定一个背包的容量t，一共有n种货物，并且给定每种货物的信息
# 花费(cost)、价值(val)、数量(cnt)
# 如果cnt == 0，代表这种货物可以无限选择
# 如果cnt > 0，那么cnt代表这种货物的数量
# 挑选货物的总容量在不超过t的情况下，返回能得到的最大价值
# 背包容量不超过1000，每一种货物的花费都>0
# 测试链接 : https://www.luogu.com.cn/problem/P1833
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 完全背包转化为多重背包
# 再把多重背包通过二进制分组转化为01背包
class Code03_CherryBlossomViewing:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXW': 'MAXW', 'ENOUGH': 'ENOUGH', 'v': 'v', 'w': 'w', 'dp': 'dp', 'hour1': 'hour1', 'minute1': 'minute1', 'hour2': 'hour2', 'minute2': 'minute2', 't': 't', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXW = 0
    ENOUGH = 0
    v = None
    w = None
    dp = None
    hour1 = 0
    minute1 = 0
    hour2 = 0
    minute2 = 0
    t = 0
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        jcall(in_, 'parseNumbers')
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_CherryBlossomViewing.hour1 = jcast('int', jcast('int', jget(in_, 'nval')))
            # 跳过冒号
            jcall(in_, 'nextToken')
            jcall(in_, 'nextToken')
            Code03_CherryBlossomViewing.minute1 = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_CherryBlossomViewing.hour2 = jcast('int', jcast('int', jget(in_, 'nval')))
            # 跳过冒号
            jcall(in_, 'nextToken')
            jcall(in_, 'nextToken')
            Code03_CherryBlossomViewing.minute2 = jcast('int', jcast('int', jget(in_, 'nval')))
            if (Code03_CherryBlossomViewing.minute1 > Code03_CherryBlossomViewing.minute2):
                Code03_CherryBlossomViewing.hour2 = jcast('int', (Code03_CherryBlossomViewing.hour2 - 1))
                Code03_CherryBlossomViewing.minute2 = jcast('int', jcast('int', jadd(Code03_CherryBlossomViewing.minute2, 60)))
            # 计算背包容量
            Code03_CherryBlossomViewing.t = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (jcast('int', (Code03_CherryBlossomViewing.hour2 - Code03_CherryBlossomViewing.hour1)) * 60)), Code03_CherryBlossomViewing.minute2)) - Code03_CherryBlossomViewing.minute1)))
            jcall(in_, 'nextToken')
            Code03_CherryBlossomViewing.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_CherryBlossomViewing.m = jcast('int', 0)
            i = jcast('int', 0)
            cost = 0
            val = 0
            cnt = 0
            while (i < Code03_CherryBlossomViewing.n):
                jcall(in_, 'nextToken')
                cost = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                val = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                cnt = jcast('int', jcast('int', jget(in_, 'nval')))
                if (cnt == 0):
                    cnt = jcast('int', Code03_CherryBlossomViewing.ENOUGH)
                # 二进制分组
                k = jcast('int', 1)
                while (k <= cnt):
                    jset(Code03_CherryBlossomViewing.v, ((_java_obj_1 := Code03_CherryBlossomViewing), (_java_key_2 := 'm'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], jcast('int', (k * val)))
                    Code03_CherryBlossomViewing.w[Code03_CherryBlossomViewing.m] = jcast('int', jcast('int', (k * cost)))
                    cnt = jcast('int', jcast('int', (cnt - k)))
                    k = jcast('int', jcast('int', (k << (1 & 31))))
                if (cnt > 0):
                    jset(Code03_CherryBlossomViewing.v, ((_java_obj_4 := Code03_CherryBlossomViewing), (_java_key_5 := 'm'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], jcast('int', (cnt * val)))
                    Code03_CherryBlossomViewing.w[Code03_CherryBlossomViewing.m] = jcast('int', jcast('int', (cnt * cost)))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_CherryBlossomViewing.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 01背包的空间压缩代码(模版)
    @staticmethod
    def compute():
        jstatic('Arrays', 'fill', Code03_CherryBlossomViewing.dp, 0, jcast('int', jadd(Code03_CherryBlossomViewing.t, 1)), 0)
        i = jcast('int', 1)
        while (i <= Code03_CherryBlossomViewing.m):
            j = jcast('int', Code03_CherryBlossomViewing.t)
            while (j >= Code03_CherryBlossomViewing.w[i]):
                jset(Code03_CherryBlossomViewing.dp, j, jstatic('Math', 'max', Code03_CherryBlossomViewing.dp[j], jcast('int', jadd(Code03_CherryBlossomViewing.dp[jcast('int', (j - Code03_CherryBlossomViewing.w[i]))], Code03_CherryBlossomViewing.v[i]))))
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code03_CherryBlossomViewing.dp[Code03_CherryBlossomViewing.t])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_CherryBlossomViewing.MAXN = jcast('int', 100001)
Code03_CherryBlossomViewing.MAXW = jcast('int', 1001)
Code03_CherryBlossomViewing.ENOUGH = jcast('int', 1001)
Code03_CherryBlossomViewing.v = jarray('int', [Code03_CherryBlossomViewing.MAXN])
Code03_CherryBlossomViewing.w = jarray('int', [Code03_CherryBlossomViewing.MAXN])
Code03_CherryBlossomViewing.dp = jarray('int', [Code03_CherryBlossomViewing.MAXW])
Code03_CherryBlossomViewing.hour1 = jcast('int', 0)
Code03_CherryBlossomViewing.minute1 = jcast('int', 0)
Code03_CherryBlossomViewing.hour2 = jcast('int', 0)
Code03_CherryBlossomViewing.minute2 = jcast('int', 0)
Code03_CherryBlossomViewing.t = jcast('int', 0)
Code03_CherryBlossomViewing.n = jcast('int', 0)
Code03_CherryBlossomViewing.m = jcast('int', 0)

if __name__ == '__main__':
    Code03_CherryBlossomViewing.main([])
