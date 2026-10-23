# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 涂色 & 奇怪打印机
# 假设你有一条长度为5的木板，初始时没有涂过任何颜色
# 你希望把它的5个单位长度分别涂上红、绿、蓝、绿、红
# 用一个长度为5的字符串表示这个目标：RGBGR
# 每次你可以把一段连续的木板涂成一个给定的颜色，后涂的颜色覆盖先涂的颜色
# 例如第一次把木板涂成RRRRR
# 第二次涂成RGGGR
# 第三次涂成RGBGR，达到目标
# 返回尽量少的涂色次数
# 测试链接 : https://www.luogu.com.cn/problem/P4170
# 测试链接 : https://leetcode.cn/problems/strange-printer/
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Coloring:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        str = jcall(br, 'readLine')
        jcall(out, 'println', Code02_Coloring.strangePrinter(str))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 时间复杂度O(n^3)
    # 测试链接 : https://leetcode.cn/problems/strange-printer/
    @staticmethod
    def strangePrinter(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('int', [n, n])
        jset(dp[jcast('int', (n - 1))], jcast('int', (n - 1)), 1)
        i = jcast('int', 0)
        while (i < jcast('int', (n - 1))):
            jset(dp[i], i, 1)
            jset(dp[i], jcast('int', jadd(i, 1)), (1 if (s[i] == s[jcast('int', jadd(i, 1))]) else 2))
            i = jcast('int', (i + 1))
        l = jcast('int', jcast('int', (n - 3)))
        ans = 0
        while (l >= 0):
            r = jcast('int', jcast('int', jadd(l, 2)))
            while (r < n):
                # dp[l][r]
                if (s[l] == s[r]):
                    jset(dp[l], r, dp[l][jcast('int', (r - 1))])
                    # dp[l][r] = dp[l + 1][r];
                else:
                    ans = jcast('int', jget(Integer, 'MAX_VALUE'))
                    m = jcast('int', l)
                    while (m < r):
                        ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(dp[l][m], dp[jcast('int', jadd(m, 1))][r]))))
                        m = jcast('int', (m + 1))
                    jset(dp[l], r, ans)
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', dp[0][jcast('int', (n - 1))])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_Coloring.main([])
