# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 有趣的数列(重要! 因子计数法)
# 求第n项卡特兰数，要求答案对p取模
# 1 <= n <= 10^6
# 1 <= p <= 10^9
# p可能不为质数
# 测试链接 : https://www.luogu.com.cn/problem/P3200
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_FunnySequence:
    __java_fields__ = {'MAXN': 'MAXN', 'minpf': 'minpf', 'prime': 'prime', 'cnt': 'cnt', 'counts': 'counts'}
    MAXN = 0
    # 如果minpf[i] == 0，代表i是质数
    # 如果minpf[i] != 0，代表i是合数，并且最小质因子是minpf[i]
    minpf = None
    # 质数表
    prime = None
    # 质数表大小
    cnt = 0
    # 因子计数
    counts = None
    # 来自讲解097，欧拉筛，时间复杂度O(n)
    @staticmethod
    def euler(n):
        n = jcast('int', n)
        jstatic('Arrays', 'fill', Code05_FunnySequence.minpf, 2, n, 0)
        Code05_FunnySequence.cnt = jcast('int', 0)
        i = jcast('int', 2)
        while (i <= n):
            try:
                # minpf[i] == 0代表i为质数，收集进质数表
                # minpf数组替代了讲解097中visit数组的作用
                if (Code05_FunnySequence.minpf[i] == 0):
                    jset(Code05_FunnySequence.prime, ((_java_obj_2 := Code05_FunnySequence), (_java_key_3 := 'cnt'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4], i)
                j = jcast('int', 0)
                while (j < Code05_FunnySequence.cnt):
                    try:
                        if (jcast('int', (i * Code05_FunnySequence.prime[j])) > n):
                            raise JBreak(None)
                        # 此时收集(i * prime[j])这个数的最小质因子为prime[j]
                        # minpf[i * prime[j]] != 0，也标记了(i * prime[j])是合数
                        # 讲解097欧拉筛的部分，重点解释了这个过程，看完必懂
                        jset(Code05_FunnySequence.minpf, jcast('int', (i * Code05_FunnySequence.prime[j])), Code05_FunnySequence.prime[j])
                        if (jcast('int', jmod(i, Code05_FunnySequence.prime[j])) == 0):
                            raise JBreak(None)
                    except JContinue as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                    except JBreak as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def power(x, p, mod):
        x = jcast('long', x)
        p = jcast('long', p)
        mod = jcast('int', mod)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), mod)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), mod)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    # 使用的是公式2 + 质因子计数法
    @staticmethod
    def compute(n, mod):
        n = jcast('int', n)
        mod = jcast('int', mod)
        # 利用欧拉筛生成[2 ~ 2*n]范围上所有数的最小质因子
        # 如果x为质数，minpf[x] == 0
        # 如果x为合数，x的最小质因子为minpf[x]
        Code05_FunnySequence.euler(jcast('int', (2 * n)))
        # 分母每个因子设置计数
        jstatic('Arrays', 'fill', Code05_FunnySequence.counts, 2, jcast('int', jadd(n, 1)), jcast('int', (-1)))
        # 分子每个因子设置计数
        jstatic('Arrays', 'fill', Code05_FunnySequence.counts, jcast('int', jadd(n, 2)), jcast('int', jadd(jcast('int', (2 * n)), 1)), 1)
        # 从大到小的每个数统计计数
        # 合数根据最小质因子来分解，变成更小数字的计数
        # 质数无法分解，计数确定，最后快速幂计算乘积
        i = jcast('int', jcast('int', (2 * n)))
        while (i >= 2):
            if (Code05_FunnySequence.minpf[i] != 0):
                ((_java_obj_6 := Code05_FunnySequence.counts), (_java_key_7 := Code05_FunnySequence.minpf[i]), jset(_java_obj_6, _java_key_7, jcast('int', jadd(jget(_java_obj_6, _java_key_7), Code05_FunnySequence.counts[i]))))[2]
                ((_java_obj_8 := Code05_FunnySequence.counts), (_java_key_9 := jcast('int', jdiv(i, Code05_FunnySequence.minpf[i]))), jset(_java_obj_8, _java_key_9, jcast('int', jadd(jget(_java_obj_8, _java_key_9), Code05_FunnySequence.counts[i]))))[2]
                Code05_FunnySequence.counts[i] = jcast('int', 0)
            i = jcast('int', (i - 1))
        # 每个质数的幂，都乘起来，就是最后答案
        ans = jcast('long', 1)
        i = jcast('int', 2)
        while (i <= jcast('int', (2 * n))):
            if (Code05_FunnySequence.counts[i] != 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code05_FunnySequence.power(i, Code05_FunnySequence.counts[i], mod))), mod)))
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', ans))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        mod = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code05_FunnySequence.compute(n, mod))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_FunnySequence.MAXN = jcast('int', 2000001)
Code05_FunnySequence.minpf = jarray('int', [Code05_FunnySequence.MAXN])
Code05_FunnySequence.prime = jarray('int', [Code05_FunnySequence.MAXN])
Code05_FunnySequence.cnt = jcast('int', 0)
Code05_FunnySequence.counts = jarray('int', [Code05_FunnySequence.MAXN])

if __name__ == '__main__':
    Code05_FunnySequence.main([])
