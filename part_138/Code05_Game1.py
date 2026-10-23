# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 游戏(递归版)
# 一共有n个节点，n <= 5000，n为偶数，其中有m个点属于小A，有m个点属于小B，m为n的一半
# 给定n-1条边，节点之间组成一颗树，1号节点是根节点
# 给定长度为n的数组arr，arr[i]的值表示i号节点由谁拥有，0为小A拥有，1为小B拥有
# 游戏有m回合，每回合都有胜负，两人需要选择一个自己拥有、但之前没选过的点，作为本回合当前点
# 小A当前点的子树里有小B当前点，则小A胜；小B当前点的子树里有小A当前点，则小B胜；否则平局
# 返回m回合里能出现k次非平局的游戏方法数，打印k=0..m时的所有答案，对 998244353 取模
# 两场游戏视为不同的定义：当且仅当存在小A拥有的点x，小B在小A选择x的那个回合所选择的点不同
# 测试链接 : https://www.luogu.com.cn/problem/P6478
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块；深层递归需考虑调用栈与内存开销
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# dfs从递归版改迭代版的实现，请看Code05_Game2文件
class Code05_Game1:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'n': 'n', 'm': 'm', 'arr': 'arr', 'fac': 'fac', 'c': 'c', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'size': 'size', 'belong': 'belong', 'dp': 'dp', 'backup': 'backup', 'g': 'g', 'f': 'f'}
    MAXN = 0
    MOD = 0
    n = 0
    m = 0
    arr = None
    fac = None
    c = None
    # 链式前向星需要
    head = None
    next = None
    to = None
    cnt = 0
    # dfs需要
    size = None
    belong = None
    dp = None
    backup = None
    # 反演需要
    g = None
    # 最后答案
    f = None
    @staticmethod
    def build():
        Code05_Game1.cnt = jcast('int', 1)
        Code05_Game1.fac[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= Code05_Game1.n):
            Code05_Game1.head[i] = jcast('int', 0)
            Code05_Game1.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (Code05_Game1.fac[jcast('int', (i - 1))] * i)), Code05_Game1.MOD)))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i <= Code05_Game1.n):
            jset(Code05_Game1.c[i], 0, 1)
            j = jcast('int', 1)
            while (j <= i):
                jset(Code05_Game1.c[i], j, jcast('long', jmod(jcast('long', jadd(Code05_Game1.c[jcast('int', (i - 1))][j], Code05_Game1.c[jcast('int', (i - 1))][jcast('int', (j - 1))])), Code05_Game1.MOD)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code05_Game1.next[Code05_Game1.cnt] = jcast('int', Code05_Game1.head[u])
        Code05_Game1.to[Code05_Game1.cnt] = jcast('int', v)
        jset(Code05_Game1.head, u, ((_java_obj_1 := Code05_Game1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 递归版
    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_Game1.size[u] = jcast('int', 1)
        jset(Code05_Game1.belong[u], Code05_Game1.arr[u], 1)
        jset(Code05_Game1.dp[u], 0, 1)
        # 首先计算不包含头节点的方法数
        e = jcast('int', Code05_Game1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_Game1.to[e])
            if (v != fa):
                Code05_Game1.dfs(v, u)
                # 之前所有子树结合的计算结果，拷贝进backup
                i = jcast('int', 0)
                while (i <= jstatic('Math', 'min', jcast('int', jdiv(Code05_Game1.size[u], 2)), Code05_Game1.m)):
                    Code05_Game1.backup[i] = jcast('long', Code05_Game1.dp[u][i])
                    jset(Code05_Game1.dp[u], i, 0)
                    i = jcast('int', (i + 1))
                # 树型dp的枚举行为利用子树的节点数做上限进行复杂度优化
                l = jcast('int', 0)
                while (l <= jstatic('Math', 'min', jcast('int', jdiv(Code05_Game1.size[u], 2)), Code05_Game1.m)):
                    r = jcast('int', 0)
                    while (r <= jstatic('Math', 'min', jcast('int', jdiv(Code05_Game1.size[v], 2)), jcast('int', (Code05_Game1.m - l)))):
                        jset(Code05_Game1.dp[u], jcast('int', jadd(l, r)), jcast('long', jmod(jcast('long', jadd(Code05_Game1.dp[u][jcast('int', jadd(l, r))], jcast('long', jmod(jcast('long', (Code05_Game1.backup[l] * Code05_Game1.dp[v][r])), Code05_Game1.MOD)))), Code05_Game1.MOD)))
                        r = jcast('int', (r + 1))
                    l = jcast('int', (l + 1))
                Code05_Game1.size[u] = jcast('int', jcast('int', jadd(Code05_Game1.size[u], Code05_Game1.size[v])))
                ((_java_obj_4 := Code05_Game1.belong[u]), (_java_key_5 := 0), jset(_java_obj_4, _java_key_5, jcast('int', jadd(jget(_java_obj_4, _java_key_5), Code05_Game1.belong[v][0]))))[2]
                ((_java_obj_6 := Code05_Game1.belong[u]), (_java_key_7 := 1), jset(_java_obj_6, _java_key_7, jcast('int', jadd(jget(_java_obj_6, _java_key_7), Code05_Game1.belong[v][1]))))[2]
            e = jcast('int', Code05_Game1.next[e])
        # 最后计算包含头节点的方法数
        # 更新dp[u][i]，i可以把上限定为min(对手拥有的节点数，m)
        # u为头的子树中，对手有几个节点
        num = jcast('int', Code05_Game1.belong[u][jcast('int', (Code05_Game1.arr[u] ^ 1))])
        # 不包含头节点的方法数，拷贝到backup
        i = jcast('int', 1)
        while (i <= jstatic('Math', 'min', num, Code05_Game1.m)):
            Code05_Game1.backup[i] = jcast('long', Code05_Game1.dp[u][i])
            i = jcast('int', (i + 1))
        # 计算包含头节点的方法数，累加上
        i = jcast('int', 1)
        while (i <= jstatic('Math', 'min', num, Code05_Game1.m)):
            jset(Code05_Game1.dp[u], i, jcast('long', jmod(jcast('long', jadd(Code05_Game1.dp[u][i], jcast('long', jmod(jcast('long', (Code05_Game1.backup[jcast('int', (i - 1))] * jcast('int', jadd(jcast('int', (num - i)), 1)))), Code05_Game1.MOD)))), Code05_Game1.MOD)))
            i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        # dfs是递归版
        Code05_Game1.dfs(1, 0)
        i = jcast('int', 0)
        while (i <= Code05_Game1.m):
            Code05_Game1.g[i] = jcast('long', jcast('long', jmod(jcast('long', (Code05_Game1.dp[1][i] * Code05_Game1.fac[jcast('int', (Code05_Game1.m - i))])), Code05_Game1.MOD)))
            i = jcast('int', (i + 1))
        k = jcast('int', 0)
        while (k <= Code05_Game1.m):
            i = jcast('int', k)
            while (i <= Code05_Game1.m):
                if (jcast('int', (jcast('int', (i - k)) & 1)) == 0):
                    Code05_Game1.f[k] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code05_Game1.f[k], jcast('long', jmod(jcast('long', (Code05_Game1.c[i][k] * Code05_Game1.g[i])), Code05_Game1.MOD)))), Code05_Game1.MOD)))
                else:
                    # -1 和 (MOD-1) 同余
                    Code05_Game1.f[k] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code05_Game1.f[k], jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code05_Game1.c[i][k] * Code05_Game1.g[i])), Code05_Game1.MOD)) * jcast('int', (Code05_Game1.MOD - 1)))), Code05_Game1.MOD)))), Code05_Game1.MOD)))
                i = jcast('int', (i + 1))
            k = jcast('int', (k + 1))

    @staticmethod
    def main(args):
        io = Code05_Game1.Kattio(_java_ctor=0)
        Code05_Game1.n = jcast('int', jcall(io, 'nextInt'))
        Code05_Game1.m = jcast('int', jcast('int', (Code05_Game1.n >> (1 & 31))))
        Code05_Game1.build()
        str = jcall(io, 'next')
        i = jcast('int', 1)
        while (i <= Code05_Game1.n):
            jset(Code05_Game1.arr, i, jcast('int', (jcall(str, 'charAt', jcast('int', (i - 1))) - jchar('0'))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code05_Game1.n):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            Code05_Game1.addEdge(u, v)
            Code05_Game1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code05_Game1.compute()
        k = jcast('int', 0)
        while (k <= Code05_Game1.m):
            jcall(io, 'println', Code05_Game1.f[k])
            k = jcast('int', (k + 1))
        jcall(io, 'flush')
        jcall(io, 'close')

    # Kattio 与 StreamTokenizer 接口均由 Python 实现，按输入格式选择，不沿用原语言的速度比较
    # 输入包含特殊格式时，可使用本类先读取字符串，再选择 int 或 float 解析
    # Python 输入输出参考：https://docs.python.org/3/library/io.html
    class Kattio(jclass('PrintWriter')):
        __java_fields__ = {'r': 'r', 'st': 'st'}
        # r：实例字段，在构造函数中初始化。
        # st：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self._java_init_1(jget(System, 'in'), jget(System, 'out'))

        def _java_init_1(self, i, o):
            super().__init__(o)
            self.r = jnew('BufferedReader', jnew('InputStreamReader', i))

        def _java_init_2(self, intput, output):
            super().__init__(output)
            self.r = jnew('BufferedReader', jnew('FileReader', intput))

        def next(self):
            try:
                while ((self.st == None) or (not jcall(self.st, 'hasMoreTokens'))):
                    self.st = jnew('StringTokenizer', jcall(self.r, 'readLine'))
                return jcall(self.st, 'nextToken')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_8:
                if jinstanceof(_java_exception_8, 'Exception'):
                    e = _java_exception_8
                    None
                else:
                    raise
            return None

        def nextInt(self):
            return jcast('int', jstatic('Integer', 'parseInt', self.next()))

        def nextDouble(self):
            return jcast('double', jstatic('Double', 'parseDouble', self.next()))

        def nextLong(self):
            return jcast('long', jstatic('Long', 'parseLong', self.next()))

        def __init__(self, *args, _java_ctor=None):
            self.r = None
            self.st = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[], ['InputStream', 'OutputStream'], ['String', 'String']], [False, False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            if _java_choice == 2:
                return self._java_init_2(*args)
            raise TypeError("No matching overload for Code05_Game1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Game1.MAXN = jcast('int', 5001)
Code05_Game1.MOD = jcast('int', 998244353)
Code05_Game1.n = jcast('int', 0)
Code05_Game1.m = jcast('int', 0)
Code05_Game1.arr = jarray('int', [Code05_Game1.MAXN])
Code05_Game1.fac = jarray('long', [Code05_Game1.MAXN])
Code05_Game1.c = jarray('long', [Code05_Game1.MAXN, Code05_Game1.MAXN])
Code05_Game1.head = jarray('int', [Code05_Game1.MAXN])
Code05_Game1.next = jarray('int', [jcast('int', (Code05_Game1.MAXN << (1 & 31)))])
Code05_Game1.to = jarray('int', [jcast('int', (Code05_Game1.MAXN << (1 & 31)))])
Code05_Game1.cnt = jcast('int', 0)
Code05_Game1.size = jarray('int', [Code05_Game1.MAXN])
Code05_Game1.belong = jarray('int', [Code05_Game1.MAXN, 2])
Code05_Game1.dp = jarray('long', [Code05_Game1.MAXN, Code05_Game1.MAXN])
Code05_Game1.backup = jarray('long', [Code05_Game1.MAXN])
Code05_Game1.g = jarray('long', [Code05_Game1.MAXN])
Code05_Game1.f = jarray('long', [Code05_Game1.MAXN])

if __name__ == '__main__':
    Code05_Game1.main([])
