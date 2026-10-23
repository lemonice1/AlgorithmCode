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

# 贿赂怪兽
# 开始时你的能力是0，你的目标是从0号怪兽开始，通过所有的n只怪兽
# 如果你当前的能力小于i号怪兽的能力，则必须付出b[i]的钱贿赂这个怪兽
# 然后怪兽就会加入你，他的能力a[i]直接累加到你的能力上
# 如果你当前的能力大于等于i号怪兽的能力，你可以选择直接通过，且能力不会下降
# 但你依然可以选择贿赂这个怪兽，然后怪兽的能力直接累加到你的能力上
# 返回通过所有的怪兽，需要花的最小钱数
# 测试链接 : https://www.nowcoder.com/practice/736e12861f9746ab8ae064d4aae2d5a9
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_BuyMonster:
    __java_fields__ = {}
    # 讲解本题的目的不仅仅是为了通过这个题，而是进行如下的思考:
    # 假设a[i]数值的范围很大，但是b[i]数值的范围不大，该怎么做？
    # 假设a[i]数值的范围不大，但是b[i]数值的范围很大，又该怎么做？
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            a = jarray('int', [jcast('int', jadd(n, 1))])
            b = jarray('int', [jcast('int', jadd(n, 1))])
            i = jcast('int', 1)
            while (i <= n):
                jcall(in_, 'nextToken')
                a[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                b[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code01_BuyMonster.compute1(n, a, b))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 假设a[i]数值的范围很大，但是b[i]数值的范围不大
    # 时间复杂度O(n * 所有怪兽的钱数累加和)
    @staticmethod
    def compute1(n, a, b):
        n = jcast('int', n)
        m = jcast('int', 0)
        for money in b:
            m = jcast('int', jcast('int', jadd(m, money)))
        # dp[i][j] : 花的钱不能超过j，通过前i个怪兽，最大能力是多少
        # 如果dp[i][j] == Integer.MIN_VALUE
        # 表示花的钱不能超过j，无论如何都无法通过前i个怪兽
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 0)
            while (j <= m):
                jset(dp[i], j, jget(Integer, 'MIN_VALUE'))
                if (dp[jcast('int', (i - 1))][j] >= a[i]):
                    jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                if ((jcast('int', (j - b[i])) >= 0) and (dp[jcast('int', (i - 1))][jcast('int', (j - b[i]))] != jget(Integer, 'MIN_VALUE'))):
                    jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(dp[jcast('int', (i - 1))][jcast('int', (j - b[i]))], a[i]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', jcast('int', (-1)))
        j = jcast('int', 0)
        while (j <= m):
            try:
                if (dp[n][j] != jget(Integer, 'MIN_VALUE')):
                    ans = jcast('int', j)
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    # 就是方法1的空间压缩版本
    @staticmethod
    def compute2(n, a, b):
        n = jcast('int', n)
        m = jcast('int', 0)
        for money in b:
            m = jcast('int', jcast('int', jadd(m, money)))
        dp = jarray('int', [jcast('int', jadd(m, 1))])
        i = jcast('int', 1)
        cur = 0
        while (i <= n):
            j = jcast('int', m)
            while (j >= 0):
                cur = jcast('int', jget(Integer, 'MIN_VALUE'))
                if (dp[j] >= a[i]):
                    cur = jcast('int', dp[j])
                if ((jcast('int', (j - b[i])) >= 0) and (dp[jcast('int', (j - b[i]))] != jget(Integer, 'MIN_VALUE'))):
                    cur = jcast('int', jstatic('Math', 'max', cur, jcast('int', jadd(dp[jcast('int', (j - b[i]))], a[i]))))
                dp[j] = jcast('int', cur)
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', jcast('int', (-1)))
        j = jcast('int', 0)
        while (j <= m):
            try:
                if (dp[j] != jget(Integer, 'MIN_VALUE')):
                    ans = jcast('int', j)
                    raise JBreak(None)
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    # 假设a[i]数值的范围不大，但是b[i]数值的范围很大
    # 时间复杂度O(n * 所有怪兽的能力累加和)
    @staticmethod
    def compute3(n, a, b):
        n = jcast('int', n)
        m = jcast('int', 0)
        for ability in a:
            m = jcast('int', jcast('int', jadd(m, ability)))
        # dp[i][j] : 能力正好是j，并且确保能通过前i个怪兽，需要至少花多少钱
        # 如果dp[i][j] == Integer.MAX_VALUE
        # 表示能力正好是j，无论如何都无法通过前i个怪兽
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        j = jcast('int', 1)
        while (j <= m):
            jset(dp[0], j, jget(Integer, 'MAX_VALUE'))
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 0)
            while (j <= m):
                jset(dp[i], j, jget(Integer, 'MAX_VALUE'))
                if ((j >= a[i]) and (dp[jcast('int', (i - 1))][j] != jget(Integer, 'MAX_VALUE'))):
                    jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                if ((jcast('int', (j - a[i])) >= 0) and (dp[jcast('int', (i - 1))][jcast('int', (j - a[i]))] != jget(Integer, 'MAX_VALUE'))):
                    jset(dp[i], j, jstatic('Math', 'min', dp[i][j], jcast('int', jadd(dp[jcast('int', (i - 1))][jcast('int', (j - a[i]))], b[i]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        j = jcast('int', 0)
        while (j <= m):
            ans = jcast('int', jstatic('Math', 'min', ans, dp[n][j]))
            j = jcast('int', (j + 1))
        return jcast('int', (jcast('int', (-1)) if (ans == jget(Integer, 'MAX_VALUE')) else ans))

    # 就是方法3的空间压缩版本
    @staticmethod
    def compute4(n, a, b):
        n = jcast('int', n)
        m = jcast('int', 0)
        for ability in a:
            m = jcast('int', jcast('int', jadd(m, ability)))
        dp = jarray('int', [jcast('int', jadd(m, 1))])
        j = jcast('int', 1)
        while (j <= m):
            dp[j] = jcast('int', jget(Integer, 'MAX_VALUE'))
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        cur = 0
        while (i <= n):
            j = jcast('int', m)
            while (j >= 0):
                cur = jcast('int', jget(Integer, 'MAX_VALUE'))
                if ((j >= a[i]) and (dp[j] != jget(Integer, 'MAX_VALUE'))):
                    cur = jcast('int', dp[j])
                if ((jcast('int', (j - a[i])) >= 0) and (dp[jcast('int', (j - a[i]))] != jget(Integer, 'MAX_VALUE'))):
                    cur = jcast('int', jstatic('Math', 'min', cur, jcast('int', jadd(dp[jcast('int', (j - a[i]))], b[i]))))
                dp[j] = jcast('int', cur)
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        j = jcast('int', 0)
        while (j <= m):
            ans = jcast('int', jstatic('Math', 'min', ans, dp[j]))
            j = jcast('int', (j + 1))
        return jcast('int', (jcast('int', (-1)) if (ans == jget(Integer, 'MAX_VALUE')) else ans))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_BuyMonster.main([])
