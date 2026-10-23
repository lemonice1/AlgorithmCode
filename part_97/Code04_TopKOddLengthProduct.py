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

# 长度前k名的奇数长度回文子串长度乘积
# 给定一个字符串s和数值k，只关心所有奇数长度的回文子串
# 返回其中长度前k名的回文子串的长度乘积是多少
# 如果奇数长度的回文子串个数不够k个，返回-1
# 测试链接 : https://www.luogu.com.cn/problem/P1659
# 答案对19930726取模
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_TopKOddLengthProduct:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'mk': 'mk', 'm': 'm', 'n': 'n', 'k': 'k', 'ss': 'ss', 'p': 'p', 'cnt': 'cnt'}
    MOD = 0
    MAXN = 0
    mk = None
    m = 0
    n = 0
    k = 0
    ss = None
    p = None
    cnt = None
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_TopKOddLengthProduct.mk = jcall(jcall(in_, 'readLine'), 'split', ' ')
        Code04_TopKOddLengthProduct.m = jcast('int', jstatic('Integer', 'valueOf', Code04_TopKOddLengthProduct.mk[0]))
        Code04_TopKOddLengthProduct.k = jcast('long', jstatic('Long', 'valueOf', Code04_TopKOddLengthProduct.mk[1]))
        jcall(out, 'println', Code04_TopKOddLengthProduct.compute(jcall(in_, 'readLine')))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    @staticmethod
    def compute(s):
        Code04_TopKOddLengthProduct.manacher(s)
        i = jcast('int', 1)
        while (i < Code04_TopKOddLengthProduct.n):
            ((_java_obj_1 := Code04_TopKOddLengthProduct.cnt), (_java_key_2 := jcast('int', (Code04_TopKOddLengthProduct.p[i] - 1))), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
            i = jcast('int', jcast('int', jadd(i, 2)))
        ans = jcast('long', 1)
        sum = jcast('long', 0)
        len = jcast('int', (Code04_TopKOddLengthProduct.m if (jcast('int', (Code04_TopKOddLengthProduct.m & 1)) == 1) else jcast('int', (Code04_TopKOddLengthProduct.m - 1))))
        while ((len >= 1) and (Code04_TopKOddLengthProduct.k > 0)):
            sum = jcast('long', jcast('long', jadd(sum, Code04_TopKOddLengthProduct.cnt[len])))
            ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code04_TopKOddLengthProduct.power(len, jstatic('Math', 'min', Code04_TopKOddLengthProduct.k, sum)))), Code04_TopKOddLengthProduct.MOD)))
            Code04_TopKOddLengthProduct.k = jcast('long', jcast('long', (Code04_TopKOddLengthProduct.k - sum)))
            len = jcast('int', jcast('int', (len - 2)))
        return jcast('int', (jcast('int', (-1)) if (Code04_TopKOddLengthProduct.k > 0) else jcast('int', ans)))

    @staticmethod
    def manacher(str):
        Code04_TopKOddLengthProduct.manacherss(jcall(str, 'toCharArray'))
        i = jcast('int', 0)
        c = jcast('int', 0)
        r = jcast('int', 0)
        len = 0
        while (i < Code04_TopKOddLengthProduct.n):
            len = jcast('int', (jstatic('Math', 'min', Code04_TopKOddLengthProduct.p[jcast('int', (jcast('int', (2 * c)) - i))], jcast('int', (r - i))) if (r > i) else 1))
            while (((jcast('int', jadd(i, len)) < Code04_TopKOddLengthProduct.n) and (jcast('int', (i - len)) >= 0)) and (Code04_TopKOddLengthProduct.ss[jcast('int', jadd(i, len))] == Code04_TopKOddLengthProduct.ss[jcast('int', (i - len))])):
                len = jcast('int', (len + 1))
            if (jcast('int', jadd(i, len)) > r):
                r = jcast('int', jcast('int', jadd(i, len)))
                c = jcast('int', i)
            Code04_TopKOddLengthProduct.p[i] = jcast('int', len)
            i = jcast('int', (i + 1))

    @staticmethod
    def manacherss(a):
        Code04_TopKOddLengthProduct.n = jcast('int', jcast('int', jadd(jcast('int', (jget(a, 'length') * 2)), 1)))
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < Code04_TopKOddLengthProduct.n):
            jset(Code04_TopKOddLengthProduct.ss, i, (jchar('#') if (jcast('int', (i & 1)) == 0) else a[((_java_old_4 := j), (j := jcast('int', (j + (1)))), _java_old_4)[2]]))
            i = jcast('int', (i + 1))

    @staticmethod
    def power(x, n):
        x = jcast('long', x)
        n = jcast('long', n)
        ans = jcast('long', 1)
        while (n > 0):
            if (jcast('long', (n & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code04_TopKOddLengthProduct.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code04_TopKOddLengthProduct.MOD)))
            n = jcast('long', jcast('long', (n >> (1 & 63))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_TopKOddLengthProduct.MOD = jcast('int', 19930726)
Code04_TopKOddLengthProduct.MAXN = jcast('int', 10000001)
Code04_TopKOddLengthProduct.mk = None
Code04_TopKOddLengthProduct.m = jcast('int', 0)
Code04_TopKOddLengthProduct.n = jcast('int', 0)
Code04_TopKOddLengthProduct.k = jcast('long', 0)
Code04_TopKOddLengthProduct.ss = jarray('char', [jcast('int', (Code04_TopKOddLengthProduct.MAXN << (1 & 31)))])
Code04_TopKOddLengthProduct.p = jarray('int', [jcast('int', (Code04_TopKOddLengthProduct.MAXN << (1 & 31)))])
Code04_TopKOddLengthProduct.cnt = jarray('int', [Code04_TopKOddLengthProduct.MAXN])

if __name__ == '__main__':
    Code04_TopKOddLengthProduct.main([])
