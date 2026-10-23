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

# 格子全变成0的操作方案
# 有一个n*m的二维网格，给定每个网格的初始值，一定是0、1、2中的一个
# 如果某个网格获得了一些数值加成，也会用%3的方式变成0、1、2中的一个
# 比如有个网格一开始值是1，获得4的加成之后，值为(1+4)%3 = 2
# 有一个神奇的刷子，一旦在某个网格处刷一下，该网格会获得2的加成
# 并且该网格上、下、左、右的格子，都会获得1的加成
# 最终目标是所有网格都变成0，题目保证一定有解，但不保证唯一解
# 得到哪一种方案都可以，打印一共需要刷几下，并且把操作方案打印出来
# 1 <= n、m <= 30
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=5755
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_GamblerBo:
    __java_fields__ = {'MOD': 'MOD', 'MAXS': 'MAXS', 'mat': 'mat', 'dir': 'dir', 'n': 'n', 'm': 'm', 's': 's', 'inv': 'inv_data'}
    MOD = 0
    MAXS = 0
    mat = None
    dir = None
    n = 0
    m = 0
    s = 0
    inv_data = None
    @staticmethod
    def inv():
        Code01_GamblerBo.inv_data[1] = jcast('int', 1)
        i = jcast('int', 2)
        while (i < Code01_GamblerBo.MOD):
            Code01_GamblerBo.inv_data[i] = jcast('int', jcast('int', jcast('long', (Code01_GamblerBo.MOD - jcast('long', jmod(jcast('long', (jcast('long', Code01_GamblerBo.inv_data[jcast('int', jmod(Code01_GamblerBo.MOD, i))]) * jcast('int', jdiv(Code01_GamblerBo.MOD, i)))), Code01_GamblerBo.MOD))))))
            i = jcast('int', (i + 1))

    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code01_GamblerBo.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code01_GamblerBo.s):
            j = jcast('int', 1)
            while (j <= jcast('int', jadd(Code01_GamblerBo.s, 1))):
                jset(Code01_GamblerBo.mat[i], j, 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        cur = 0
        row = 0
        col = 0
        i = jcast('int', 0)
        while (i < Code01_GamblerBo.n):
            j = jcast('int', 0)
            while (j < Code01_GamblerBo.m):
                cur = jcast('int', jcast('int', jadd(jcast('int', jadd(jcast('int', (i * Code01_GamblerBo.m)), j)), 1)))
                jset(Code01_GamblerBo.mat[cur], cur, 2)
                d = jcast('int', 0)
                while (d <= 3):
                    row = jcast('int', jcast('int', jadd(i, Code01_GamblerBo.dir[d])))
                    col = jcast('int', jcast('int', jadd(j, Code01_GamblerBo.dir[jcast('int', jadd(d, 1))])))
                    if ((((row >= 0) and (row < Code01_GamblerBo.n)) and (col >= 0)) and (col < Code01_GamblerBo.m)):
                        jset(Code01_GamblerBo.mat[cur], jcast('int', jadd(jcast('int', jadd(jcast('int', (row * Code01_GamblerBo.m)), col)), 1)), 1)
                    d = jcast('int', (d + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    # 这道题目比较特殊，打印任何一种方案都可以
    # 于是认为所有自由元的操作次数为0
    # 也就是认为消元之后，主元不被任何自由元影响
    # 所以代码可以简化
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        if ((j < i) and (Code01_GamblerBo.mat[j][j] != 0)):
                            raise JContinue(None)
                        if (Code01_GamblerBo.mat[j][i] != 0):
                            Code01_GamblerBo.swap(i, j)
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if (Code01_GamblerBo.mat[i][i] != 0):
                    j = jcast('int', 1)
                    while (j <= n):
                        if ((i != j) and (Code01_GamblerBo.mat[j][i] != 0)):
                            gcd = jcast('int', Code01_GamblerBo.gcd(Code01_GamblerBo.mat[j][i], Code01_GamblerBo.mat[i][i]))
                            a = jcast('int', jcast('int', jdiv(Code01_GamblerBo.mat[i][i], gcd)))
                            b = jcast('int', jcast('int', jdiv(Code01_GamblerBo.mat[j][i], gcd)))
                            if ((j < i) and (Code01_GamblerBo.mat[j][j] != 0)):
                                # 只需要调整，j行主元的系数，也就是j行j列的值
                                # 不需要调整，j行，j+1列 ~ i-1列的值，所对应自由元的系数
                                # 因为最终方案默认所有自由元都不操作
                                jset(Code01_GamblerBo.mat[j], j, jcast('int', jmod(jcast('int', (Code01_GamblerBo.mat[j][j] * a)), Code01_GamblerBo.MOD)))
                            # 正常消元
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                jset(Code01_GamblerBo.mat[j], k, jcast('int', jmod(jcast('int', jadd(jcast('int', jmod(jcast('int', (jcast('int', (Code01_GamblerBo.mat[j][k] * a)) - jcast('int', (Code01_GamblerBo.mat[i][k] * b)))), Code01_GamblerBo.MOD)), Code01_GamblerBo.MOD)), Code01_GamblerBo.MOD)))
                                k = jcast('int', (k + 1))
                        j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        # 由于本题的特殊性，不需要去管任何自由元的影响
        # 就当自由元不操作，直接求主元的操作次数即可
        i = jcast('int', 1)
        while (i <= n):
            if (Code01_GamblerBo.mat[i][i] != 0):
                jset(Code01_GamblerBo.mat[i], jcast('int', jadd(n, 1)), jcast('int', jmod(jcast('int', (Code01_GamblerBo.mat[i][jcast('int', jadd(n, 1))] * Code01_GamblerBo.inv_data[Code01_GamblerBo.mat[i][i]])), Code01_GamblerBo.MOD)))
            i = jcast('int', (i + 1))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = Code01_GamblerBo.mat[a]
        Code01_GamblerBo.mat[a] = Code01_GamblerBo.mat[b]
        Code01_GamblerBo.mat[b] = tmp

    @staticmethod
    def main(args):
        Code01_GamblerBo.inv()
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        test = jcast('int', jcast('int', jget(in_, 'nval')))
        t = jcast('int', 1)
        while (t <= test):
            jcall(in_, 'nextToken')
            Code01_GamblerBo.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_GamblerBo.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_GamblerBo.s = jcast('int', jcast('int', (Code01_GamblerBo.n * Code01_GamblerBo.m)))
            Code01_GamblerBo.prepare()
            i = jcast('int', 1)
            while (i <= Code01_GamblerBo.s):
                jcall(in_, 'nextToken')
                jset(Code01_GamblerBo.mat[i], jcast('int', jadd(Code01_GamblerBo.s, 1)), jcast('int', jmod(jcast('int', (3 - jcast('int', jget(in_, 'nval')))), Code01_GamblerBo.MOD)))
                i = jcast('int', (i + 1))
            Code01_GamblerBo.gauss(Code01_GamblerBo.s)
            ans = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= Code01_GamblerBo.s):
                ans = jcast('int', jcast('int', jadd(ans, Code01_GamblerBo.mat[i][jcast('int', jadd(Code01_GamblerBo.s, 1))])))
                i = jcast('int', (i + 1))
            jcall(out, 'println', ans)
            i = jcast('int', 1)
            id = jcast('int', 1)
            while (i <= Code01_GamblerBo.n):
                j = jcast('int', 1)
                while (j <= Code01_GamblerBo.m):
                    while (((_java_obj_3 := Code01_GamblerBo.mat[id]), (_java_key_4 := jcast('int', jadd(Code01_GamblerBo.s, 1))), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (-1)))), _java_old_5)[4] > 0):
                        jcall(out, 'println', jadd(jadd(i, ' '), j))
                    j = jcast('int', (j + 1))
                    id = jcast('int', (id + 1))
                i = jcast('int', (i + 1))
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_GamblerBo.MOD = jcast('int', 3)
Code01_GamblerBo.MAXS = jcast('int', 1001)
Code01_GamblerBo.mat = jarray('int', [Code01_GamblerBo.MAXS, Code01_GamblerBo.MAXS])
Code01_GamblerBo.dir = jarray('int', [None], [0, jcast('int', (-1)), 0, 1, 0])
Code01_GamblerBo.n = jcast('int', 0)
Code01_GamblerBo.m = jcast('int', 0)
Code01_GamblerBo.s = jcast('int', 0)
Code01_GamblerBo.inv_data = jarray('int', [Code01_GamblerBo.MOD])

if __name__ == '__main__':
    Code01_GamblerBo.main([])
