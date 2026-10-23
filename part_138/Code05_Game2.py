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

# 游戏(迭代版)
# 一共有n个节点，n <= 5000，n为偶数，其中有m个点属于小A，有m个点属于小B，m为n的一半
# 给定n-1条边，节点之间组成一颗树，1号节点是根节点
# 给定长度为n的数组arr，arr[i]的值表示i号节点由谁拥有，0为小A拥有，1为小B拥有
# 游戏有m回合，每回合都有胜负，两人需要选择一个自己拥有、但之前没选过的点，作为本回合当前点
# 小A当前点的子树里有小B当前点，则小A胜；小B当前点的子树里有小A当前点，则小B胜；否则平局
# 返回m回合里能出现k次非平局的游戏方法数，打印k=0..m时的所有答案，对 998244353 取模
# 两场游戏视为不同的定义：当且仅当存在小A拥有的点x，小B在小A选择x的那个回合所选择的点不同
# 测试链接 : https://www.luogu.com.cn/problem/P6478
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Game2:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'n': 'n', 'm': 'm', 'arr': 'arr', 'fac': 'fac', 'c': 'c', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'size': 'size', 'belong': 'belong', 'dp': 'dp', 'backup': 'backup', 'g': 'g', 'f': 'f', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'fa': 'fa', 'e': 'e'}
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
        Code05_Game2.cnt = jcast('int', 1)
        Code05_Game2.fac[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= Code05_Game2.n):
            Code05_Game2.head[i] = jcast('int', 0)
            Code05_Game2.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (Code05_Game2.fac[jcast('int', (i - 1))] * i)), Code05_Game2.MOD)))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i <= Code05_Game2.n):
            jset(Code05_Game2.c[i], 0, 1)
            j = jcast('int', 1)
            while (j <= i):
                jset(Code05_Game2.c[i], j, jcast('long', jmod(jcast('long', jadd(Code05_Game2.c[jcast('int', (i - 1))][j], Code05_Game2.c[jcast('int', (i - 1))][jcast('int', (j - 1))])), Code05_Game2.MOD)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code05_Game2.next[Code05_Game2.cnt] = jcast('int', Code05_Game2.head[u])
        Code05_Game2.to[Code05_Game2.cnt] = jcast('int', v)
        jset(Code05_Game2.head, u, ((_java_obj_1 := Code05_Game2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 迭代版
    # ufe是为了实现迭代版而准备的栈
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    ufe = None
    stackSize = 0
    u = 0
    fa = 0
    e = 0
    @staticmethod
    def push(u, fa, e):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', e)
        jset(Code05_Game2.ufe[Code05_Game2.stackSize], 0, u)
        jset(Code05_Game2.ufe[Code05_Game2.stackSize], 1, fa)
        jset(Code05_Game2.ufe[Code05_Game2.stackSize], 2, e)
        Code05_Game2.stackSize = jcast('int', (Code05_Game2.stackSize + 1))

    @staticmethod
    def pop():
        Code05_Game2.stackSize = jcast('int', (Code05_Game2.stackSize - 1))
        Code05_Game2.u = jcast('int', Code05_Game2.ufe[Code05_Game2.stackSize][0])
        Code05_Game2.fa = jcast('int', Code05_Game2.ufe[Code05_Game2.stackSize][1])
        Code05_Game2.e = jcast('int', Code05_Game2.ufe[Code05_Game2.stackSize][2])

    # 迭代版
    @staticmethod
    def dfs(root):
        root = jcast('int', root)
        Code05_Game2.stackSize = jcast('int', 0)
        Code05_Game2.push(root, 0, jcast('int', (-1)))
        v = 0
        num = 0
        while (Code05_Game2.stackSize > 0):
            Code05_Game2.pop()
            # 第一次来到当前节点，设置初始值
            if (Code05_Game2.e == jcast('int', (-1))):
                Code05_Game2.size[Code05_Game2.u] = jcast('int', 1)
                jset(Code05_Game2.belong[Code05_Game2.u], Code05_Game2.arr[Code05_Game2.u], 1)
                jset(Code05_Game2.dp[Code05_Game2.u], 0, 1)
                Code05_Game2.e = jcast('int', Code05_Game2.head[Code05_Game2.u])
                # 不是第一次来到当前节点
            else:
                v = jcast('int', Code05_Game2.to[Code05_Game2.e])
                # 之前的孩子，dfs过程计算完了，所以用之前孩子的信息，更新当前节点的信息
                if (v != Code05_Game2.fa):
                    i = jcast('int', 0)
                    while (i <= jstatic('Math', 'min', jcast('int', jdiv(Code05_Game2.size[Code05_Game2.u], 2)), Code05_Game2.m)):
                        Code05_Game2.backup[i] = jcast('long', Code05_Game2.dp[Code05_Game2.u][i])
                        jset(Code05_Game2.dp[Code05_Game2.u], i, 0)
                        i = jcast('int', (i + 1))
                    l = jcast('int', 0)
                    while (l <= jstatic('Math', 'min', jcast('int', jdiv(Code05_Game2.size[Code05_Game2.u], 2)), Code05_Game2.m)):
                        r = jcast('int', 0)
                        while (r <= jstatic('Math', 'min', jcast('int', jdiv(Code05_Game2.size[v], 2)), jcast('int', (Code05_Game2.m - l)))):
                            jset(Code05_Game2.dp[Code05_Game2.u], jcast('int', jadd(l, r)), jcast('long', jmod(jcast('long', jadd(Code05_Game2.dp[Code05_Game2.u][jcast('int', jadd(l, r))], jcast('long', jmod(jcast('long', (Code05_Game2.backup[l] * Code05_Game2.dp[v][r])), Code05_Game2.MOD)))), Code05_Game2.MOD)))
                            r = jcast('int', (r + 1))
                        l = jcast('int', (l + 1))
                    Code05_Game2.size[Code05_Game2.u] = jcast('int', jcast('int', jadd(Code05_Game2.size[Code05_Game2.u], Code05_Game2.size[v])))
                    ((_java_obj_4 := Code05_Game2.belong[Code05_Game2.u]), (_java_key_5 := 0), jset(_java_obj_4, _java_key_5, jcast('int', jadd(jget(_java_obj_4, _java_key_5), Code05_Game2.belong[v][0]))))[2]
                    ((_java_obj_6 := Code05_Game2.belong[Code05_Game2.u]), (_java_key_7 := 1), jset(_java_obj_6, _java_key_7, jcast('int', jadd(jget(_java_obj_6, _java_key_7), Code05_Game2.belong[v][1]))))[2]
                # 来到去往下一个孩子的边
                Code05_Game2.e = jcast('int', Code05_Game2.next[Code05_Game2.e])
            # 还有后续子树
            if (Code05_Game2.e != 0):
                Code05_Game2.push(Code05_Game2.u, Code05_Game2.fa, Code05_Game2.e)
                if (Code05_Game2.to[Code05_Game2.e] != Code05_Game2.fa):
                    Code05_Game2.push(Code05_Game2.to[Code05_Game2.e], Code05_Game2.u, jcast('int', (-1)))
                # 没有后续子树，最后计算包含头节点的方法数
            else:
                num = jcast('int', Code05_Game2.belong[Code05_Game2.u][jcast('int', (Code05_Game2.arr[Code05_Game2.u] ^ 1))])
                i = jcast('int', 1)
                while (i <= jstatic('Math', 'min', num, Code05_Game2.m)):
                    Code05_Game2.backup[i] = jcast('long', Code05_Game2.dp[Code05_Game2.u][i])
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                while (i <= jstatic('Math', 'min', num, Code05_Game2.m)):
                    jset(Code05_Game2.dp[Code05_Game2.u], i, jcast('long', jmod(jcast('long', jadd(Code05_Game2.dp[Code05_Game2.u][i], jcast('long', jmod(jcast('long', (Code05_Game2.backup[jcast('int', (i - 1))] * jcast('int', jadd(jcast('int', (num - i)), 1)))), Code05_Game2.MOD)))), Code05_Game2.MOD)))
                    i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        # dfs是迭代版
        Code05_Game2.dfs(1)
        i = jcast('int', 0)
        while (i <= Code05_Game2.m):
            Code05_Game2.g[i] = jcast('long', jcast('long', jmod(jcast('long', (Code05_Game2.dp[1][i] * Code05_Game2.fac[jcast('int', (Code05_Game2.m - i))])), Code05_Game2.MOD)))
            i = jcast('int', (i + 1))
        k = jcast('int', 0)
        while (k <= Code05_Game2.m):
            i = jcast('int', k)
            while (i <= Code05_Game2.m):
                if (jcast('int', (jcast('int', (i - k)) & 1)) == 0):
                    Code05_Game2.f[k] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code05_Game2.f[k], jcast('long', jmod(jcast('long', (Code05_Game2.c[i][k] * Code05_Game2.g[i])), Code05_Game2.MOD)))), Code05_Game2.MOD)))
                else:
                    Code05_Game2.f[k] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code05_Game2.f[k], jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code05_Game2.c[i][k] * Code05_Game2.g[i])), Code05_Game2.MOD)) * jcast('int', (Code05_Game2.MOD - 1)))), Code05_Game2.MOD)))), Code05_Game2.MOD)))
                i = jcast('int', (i + 1))
            k = jcast('int', (k + 1))

    @staticmethod
    def main(args):
        io = Code05_Game2.Kattio(_java_ctor=0)
        Code05_Game2.n = jcast('int', jcall(io, 'nextInt'))
        Code05_Game2.m = jcast('int', jcast('int', (Code05_Game2.n >> (1 & 31))))
        Code05_Game2.build()
        str = jcall(io, 'next')
        i = jcast('int', 1)
        while (i <= Code05_Game2.n):
            jset(Code05_Game2.arr, i, jcast('int', (jcall(str, 'charAt', jcast('int', (i - 1))) - jchar('0'))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code05_Game2.n):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            Code05_Game2.addEdge(u, v)
            Code05_Game2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code05_Game2.compute()
        k = jcast('int', 0)
        while (k <= Code05_Game2.m):
            jcall(io, 'println', Code05_Game2.f[k])
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
            raise TypeError("No matching overload for Code05_Game2.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Game2.MAXN = jcast('int', 5001)
Code05_Game2.MOD = jcast('int', 998244353)
Code05_Game2.n = jcast('int', 0)
Code05_Game2.m = jcast('int', 0)
Code05_Game2.arr = jarray('int', [Code05_Game2.MAXN])
Code05_Game2.fac = jarray('long', [Code05_Game2.MAXN])
Code05_Game2.c = jarray('long', [Code05_Game2.MAXN, Code05_Game2.MAXN])
Code05_Game2.head = jarray('int', [Code05_Game2.MAXN])
Code05_Game2.next = jarray('int', [jcast('int', (Code05_Game2.MAXN << (1 & 31)))])
Code05_Game2.to = jarray('int', [jcast('int', (Code05_Game2.MAXN << (1 & 31)))])
Code05_Game2.cnt = jcast('int', 0)
Code05_Game2.size = jarray('int', [Code05_Game2.MAXN])
Code05_Game2.belong = jarray('int', [Code05_Game2.MAXN, 2])
Code05_Game2.dp = jarray('long', [Code05_Game2.MAXN, Code05_Game2.MAXN])
Code05_Game2.backup = jarray('long', [Code05_Game2.MAXN])
Code05_Game2.g = jarray('long', [Code05_Game2.MAXN])
Code05_Game2.f = jarray('long', [Code05_Game2.MAXN])
Code05_Game2.ufe = jarray('int', [Code05_Game2.MAXN, 3])
Code05_Game2.stackSize = jcast('int', 0)
Code05_Game2.u = jcast('int', 0)
Code05_Game2.fa = jcast('int', 0)
Code05_Game2.e = jcast('int', 0)

if __name__ == '__main__':
    Code05_Game2.main([])
