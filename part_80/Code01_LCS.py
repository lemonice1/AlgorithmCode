# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最长公共子序列其中一个结果
# 给定两个字符串str1和str2
# 输出两个字符串的最长公共子序列
# 如果最长公共子序列为空，则输出-1
# 测试链接 : https://www.nowcoder.com/practice/4727c06b9ee9446cab2e859b4bb86bb8
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 讲解067 - 题目3，最长公共子序列长度
class Code01_LCS:
    __java_fields__ = {'MAXN': 'MAXN', 'dp': 'dp_data', 'ans': 'ans', 's1': 's1', 's2': 's2', 'n': 'n', 'm': 'm', 'k': 'k'}
    MAXN = 0
    dp_data = None
    ans = None
    s1 = None
    s2 = None
    n = 0
    m = 0
    k = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_LCS.s1 = jcall(jcall(br, 'readLine'), 'toCharArray')
        Code01_LCS.s2 = jcall(jcall(br, 'readLine'), 'toCharArray')
        Code01_LCS.n = jcast('int', jget(Code01_LCS.s1, 'length'))
        Code01_LCS.m = jcast('int', jget(Code01_LCS.s2, 'length'))
        Code01_LCS.lcs()
        if (Code01_LCS.k == 0):
            jcall(out, 'println', jcast('int', (-1)))
        else:
            i = jcast('int', 0)
            while (i < Code01_LCS.k):
                jcall(out, 'print', Code01_LCS.ans[i])
                i = jcast('int', (i + 1))
            jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def lcs():
        Code01_LCS.dp()
        Code01_LCS.k = jcast('int', Code01_LCS.dp_data[Code01_LCS.n][Code01_LCS.m])
        if (Code01_LCS.k > 0):
            len = jcast('int', Code01_LCS.k)
            i = jcast('int', Code01_LCS.n)
            j = jcast('int', Code01_LCS.m)
            while (len > 0):
                if (Code01_LCS.s1[jcast('int', (i - 1))] == Code01_LCS.s2[jcast('int', (j - 1))]):
                    jset(Code01_LCS.ans, (len := jcast('int', (len + (-1)))), Code01_LCS.s1[jcast('int', (i - 1))])
                    i = jcast('int', (i - 1))
                    j = jcast('int', (j - 1))
                else:
                    if (Code01_LCS.dp_data[jcast('int', (i - 1))][j] >= Code01_LCS.dp_data[i][jcast('int', (j - 1))]):
                        i = jcast('int', (i - 1))
                    else:
                        j = jcast('int', (j - 1))

    # 填好dp表
    @staticmethod
    def dp():
        i = jcast('int', 1)
        while (i <= Code01_LCS.n):
            j = jcast('int', 1)
            while (j <= Code01_LCS.m):
                if (Code01_LCS.s1[jcast('int', (i - 1))] == Code01_LCS.s2[jcast('int', (j - 1))]):
                    jset(Code01_LCS.dp_data[i], j, jcast('int', jadd(1, Code01_LCS.dp_data[jcast('int', (i - 1))][jcast('int', (j - 1))])))
                else:
                    jset(Code01_LCS.dp_data[i], j, jstatic('Math', 'max', Code01_LCS.dp_data[jcast('int', (i - 1))][j], Code01_LCS.dp_data[i][jcast('int', (j - 1))]))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_LCS.MAXN = jcast('int', 5001)
Code01_LCS.dp_data = jarray('int', [Code01_LCS.MAXN, Code01_LCS.MAXN])
Code01_LCS.ans = jarray('char', [Code01_LCS.MAXN])
Code01_LCS.s1 = None
Code01_LCS.s2 = None
Code01_LCS.n = jcast('int', 0)
Code01_LCS.m = jcast('int', 0)
Code01_LCS.k = jcast('int', 0)

if __name__ == '__main__':
    Code01_LCS.main([])
