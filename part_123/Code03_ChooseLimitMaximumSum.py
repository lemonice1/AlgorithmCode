# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 不超过连续k个元素的最大累加和
# 给定一个长度为n的数组arr，你可以随意选择数字
# 要求选择的方案中，连续选择的个数不能超过k个
# 返回能得到的最大累加和
# 1 <= n、k <= 10^5
# 0 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P2627
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_ChooseLimitMaximumSum:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sum': 'sum', 'dp': 'dp', 'queue': 'queue', 'l': 'l', 'r': 'r', 'n': 'n', 'k': 'k'}
    MAXN = 0
    arr = None
    sum = None
    dp = None
    queue = None
    l = 0
    r = 0
    n = 0
    k = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_ChooseLimitMaximumSum.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_ChooseLimitMaximumSum.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code03_ChooseLimitMaximumSum.n):
            jcall(in_, 'nextToken')
            Code03_ChooseLimitMaximumSum.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code03_ChooseLimitMaximumSum.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code03_ChooseLimitMaximumSum.n):
            Code03_ChooseLimitMaximumSum.sum[i] = jcast('long', jcast('long', jadd(Code03_ChooseLimitMaximumSum.sum[jcast('int', (i - 1))], Code03_ChooseLimitMaximumSum.arr[i])))
            i = jcast('int', (i + 1))
        Code03_ChooseLimitMaximumSum.l = jcast('int', jset(Code03_ChooseLimitMaximumSum, 'r', 0))
        jset(Code03_ChooseLimitMaximumSum.queue, ((_java_obj_1 := Code03_ChooseLimitMaximumSum), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], 0)
        i = jcast('int', 1)
        while (i <= Code03_ChooseLimitMaximumSum.n):
            while ((Code03_ChooseLimitMaximumSum.l < Code03_ChooseLimitMaximumSum.r) and (Code03_ChooseLimitMaximumSum.value(Code03_ChooseLimitMaximumSum.queue[jcast('int', (Code03_ChooseLimitMaximumSum.r - 1))]) <= Code03_ChooseLimitMaximumSum.value(i))):
                Code03_ChooseLimitMaximumSum.r = jcast('int', (Code03_ChooseLimitMaximumSum.r - 1))
            jset(Code03_ChooseLimitMaximumSum.queue, ((_java_obj_4 := Code03_ChooseLimitMaximumSum), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], i)
            if ((Code03_ChooseLimitMaximumSum.l < Code03_ChooseLimitMaximumSum.r) and (Code03_ChooseLimitMaximumSum.queue[Code03_ChooseLimitMaximumSum.l] == jcast('int', (jcast('int', (i - Code03_ChooseLimitMaximumSum.k)) - 1)))):
                Code03_ChooseLimitMaximumSum.l = jcast('int', (Code03_ChooseLimitMaximumSum.l + 1))
            jset(Code03_ChooseLimitMaximumSum.dp, i, jcast('long', jadd(Code03_ChooseLimitMaximumSum.value(Code03_ChooseLimitMaximumSum.queue[Code03_ChooseLimitMaximumSum.l]), Code03_ChooseLimitMaximumSum.sum[i])))
            i = jcast('int', (i + 1))
        return jcast('long', Code03_ChooseLimitMaximumSum.dp[Code03_ChooseLimitMaximumSum.n])

    # 不要i位置的数字产生的指标
    @staticmethod
    def value(i):
        i = jcast('int', i)
        return jcast('long', (0 if (i == 0) else jcast('long', (Code03_ChooseLimitMaximumSum.dp[jcast('int', (i - 1))] - Code03_ChooseLimitMaximumSum.sum[i]))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_ChooseLimitMaximumSum.MAXN = jcast('int', 100001)
Code03_ChooseLimitMaximumSum.arr = jarray('int', [Code03_ChooseLimitMaximumSum.MAXN])
Code03_ChooseLimitMaximumSum.sum = jarray('long', [Code03_ChooseLimitMaximumSum.MAXN])
Code03_ChooseLimitMaximumSum.dp = jarray('long', [Code03_ChooseLimitMaximumSum.MAXN])
Code03_ChooseLimitMaximumSum.queue = jarray('int', [Code03_ChooseLimitMaximumSum.MAXN])
Code03_ChooseLimitMaximumSum.l = jcast('int', 0)
Code03_ChooseLimitMaximumSum.r = jcast('int', 0)
Code03_ChooseLimitMaximumSum.n = jcast('int', 0)
Code03_ChooseLimitMaximumSum.k = jcast('int', 0)

if __name__ == '__main__':
    Code03_ChooseLimitMaximumSum.main([])
