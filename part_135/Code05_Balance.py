# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 天平
# 一共有n个砝码，编号1~n，每个砝码的重量均为1克，或者2克，或者3克
# 砝码与砝码之间的关系是一个n * n的二维数组s
# s[i][j] == '+'，砝码i比砝码j重        s[i][j] == '-'，砝码i比砝码j轻
# s[i][j] == '='，砝码i和砝码j重量一样   s[i][j] == '?'，砝码i和砝码j关系未知
# 数据保证至少存在一种情况符合该矩阵
# 给定编号为a和b的砝码，这两个砝码一定会放在天平的左边，你要另选两个砝码放在天平右边
# 返回有多少种方法，一定让天平左边重(ans1)，一定让天平一样重(ans2)，一定让天平右边重(ans3)
# 1 <= n <= 50
# 测试链接 : https://www.luogu.com.cn/problem/P2474
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Balance:
    __java_fields__ = {'MAXN': 'MAXN', 'dmin': 'dmin', 'dmax': 'dmax', 's': 's', 'n': 'n', 'a': 'a', 'b': 'b', 'ans1': 'ans1', 'ans2': 'ans2', 'ans3': 'ans3'}
    MAXN = 0
    dmin = None
    dmax = None
    s = None
    n = 0
    a = 0
    b = 0
    ans1 = 0
    ans2 = 0
    ans3 = 0
    @staticmethod
    def compute():
        # 设置初始关系
        i = jcast('int', 1)
        while (i <= Code05_Balance.n):
            j = jcast('int', 1)
            while (j <= Code05_Balance.n):
                if (Code05_Balance.s[i][j] == jchar('=')):
                    jset(Code05_Balance.dmin[i], j, 0)
                    jset(Code05_Balance.dmax[i], j, 0)
                else:
                    if (Code05_Balance.s[i][j] == jchar('+')):
                        jset(Code05_Balance.dmin[i], j, 1)
                        jset(Code05_Balance.dmax[i], j, 2)
                    else:
                        if (Code05_Balance.s[i][j] == jchar('-')):
                            jset(Code05_Balance.dmin[i], j, jcast('int', (-2)))
                            jset(Code05_Balance.dmax[i], j, jcast('int', (-1)))
                        else:
                            jset(Code05_Balance.dmin[i], j, jcast('int', (-2)))
                            jset(Code05_Balance.dmax[i], j, 2)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Balance.n):
            jset(Code05_Balance.dmin[i], i, 0)
            jset(Code05_Balance.dmax[i], i, 0)
            i = jcast('int', (i + 1))
        # 来自讲解065，Floyd算法
        bridge = jcast('int', 1)
        while (bridge <= Code05_Balance.n):
            i = jcast('int', 1)
            while (i <= Code05_Balance.n):
                j = jcast('int', 1)
                while (j <= Code05_Balance.n):
                    jset(Code05_Balance.dmin[i], j, jstatic('Math', 'max', Code05_Balance.dmin[i][j], jcast('int', jadd(Code05_Balance.dmin[i][bridge], Code05_Balance.dmin[bridge][j]))))
                    jset(Code05_Balance.dmax[i], j, jstatic('Math', 'min', Code05_Balance.dmax[i][j], jcast('int', jadd(Code05_Balance.dmax[i][bridge], Code05_Balance.dmax[bridge][j]))))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            bridge = jcast('int', (bridge + 1))
        # 统计答案
        Code05_Balance.ans1 = jcast('int', jset(Code05_Balance, 'ans2', jset(Code05_Balance, 'ans3', 0)))
        i = jcast('int', 1)
        while (i <= Code05_Balance.n):
            j = jcast('int', 1)
            while (j < i):
                if ((((i != Code05_Balance.a) and (i != Code05_Balance.b)) and (j != Code05_Balance.a)) and (j != Code05_Balance.b)):
                    if ((Code05_Balance.dmin[Code05_Balance.a][i] > Code05_Balance.dmax[j][Code05_Balance.b]) or (Code05_Balance.dmin[Code05_Balance.a][j] > Code05_Balance.dmax[i][Code05_Balance.b])):
                        Code05_Balance.ans1 = jcast('int', (Code05_Balance.ans1 + 1))
                    if ((Code05_Balance.dmax[Code05_Balance.a][i] < Code05_Balance.dmin[j][Code05_Balance.b]) or (Code05_Balance.dmax[Code05_Balance.a][j] < Code05_Balance.dmin[i][Code05_Balance.b])):
                        Code05_Balance.ans3 = jcast('int', (Code05_Balance.ans3 + 1))
                    if (((Code05_Balance.dmin[Code05_Balance.a][i] == Code05_Balance.dmax[Code05_Balance.a][i]) and (Code05_Balance.dmin[j][Code05_Balance.b] == Code05_Balance.dmax[j][Code05_Balance.b])) and (Code05_Balance.dmin[Code05_Balance.a][i] == Code05_Balance.dmin[j][Code05_Balance.b])):
                        Code05_Balance.ans2 = jcast('int', (Code05_Balance.ans2 + 1))
                    else:
                        if (((Code05_Balance.dmin[Code05_Balance.b][i] == Code05_Balance.dmax[Code05_Balance.b][i]) and (Code05_Balance.dmin[j][Code05_Balance.a] == Code05_Balance.dmax[j][Code05_Balance.a])) and (Code05_Balance.dmin[Code05_Balance.b][i] == Code05_Balance.dmin[j][Code05_Balance.a])):
                            Code05_Balance.ans2 = jcast('int', (Code05_Balance.ans2 + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        numbers = jcall(jcall(br, 'readLine'), 'split', ' ')
        Code05_Balance.n = jcast('int', jstatic('Integer', 'valueOf', numbers[0]))
        Code05_Balance.a = jcast('int', jstatic('Integer', 'valueOf', numbers[1]))
        Code05_Balance.b = jcast('int', jstatic('Integer', 'valueOf', numbers[2]))
        line = None
        i = jcast('int', 1)
        while (i <= Code05_Balance.n):
            line = jcall(jcall(br, 'readLine'), 'toCharArray')
            j = jcast('int', 1)
            while (j <= Code05_Balance.n):
                jset(Code05_Balance.s[i], j, line[jcast('int', (j - 1))])
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code05_Balance.compute()
        jcall(out, 'println', jadd(jadd(jadd(jadd(Code05_Balance.ans1, ' '), Code05_Balance.ans2), ' '), Code05_Balance.ans3))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Balance.MAXN = jcast('int', 51)
Code05_Balance.dmin = jarray('int', [Code05_Balance.MAXN, Code05_Balance.MAXN])
Code05_Balance.dmax = jarray('int', [Code05_Balance.MAXN, Code05_Balance.MAXN])
Code05_Balance.s = jarray('char', [Code05_Balance.MAXN, Code05_Balance.MAXN])
Code05_Balance.n = jcast('int', 0)
Code05_Balance.a = jcast('int', 0)
Code05_Balance.b = jcast('int', 0)
Code05_Balance.ans1 = jcast('int', 0)
Code05_Balance.ans2 = jcast('int', 0)
Code05_Balance.ans3 = jcast('int', 0)

if __name__ == '__main__':
    Code05_Balance.main([])
