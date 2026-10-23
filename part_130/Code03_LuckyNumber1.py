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

# 幸运数字(递归版)
# 一共有n个点，编号1~n，由n-1条边连成一棵树，每个点上有数字
# 一共有q条查询，每次返回a到b的路径上，可以随意选择数字，能得到的最大异或和
# 1 <= n <= 2 * 10^4
# 1 <= q <= 2 * 10^5
# 0 <= 点上的数字 <= 2^60
# 测试链接 : https://www.luogu.com.cn/problem/P3292
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code03_LuckyNumber2.py
class Code03_LuckyNumber1:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'BIT': 'BIT', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'deep': 'deep', 'stjump': 'stjump', 'power': 'power', 'bases': 'bases', 'levels': 'levels', 'basis': 'basis'}
    # 节点个数上限
    MAXN = 0
    # 树上倍增的次方上限
    LIMIT = 0
    # 节点值最大的位数
    BIT = 0
    # 每个节点值的数组
    arr = None
    # 链式前向星
    head = None
    next = None
    to = None
    cnt = 0
    # 树上倍增需要的深度表
    deep = None
    # 树上倍增需要的倍增表
    stjump = None
    # 树上倍增根据实际节点个数确定的次方
    power = 0
    # bases[i][j]表示：
    # 头节点到i节点路径上的数字，建立异或空间线性基，其中j位的线性基是哪个数字
    bases = None
    # levels[i][j]表示：
    # 头节点到i节点路径上的数字，建立异或空间线性基，其中j位的线性基来自哪一层
    levels = None
    @staticmethod
    def prepare(n):
        n = jcast('int', n)
        Code03_LuckyNumber1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code03_LuckyNumber1.head, 1, jcast('int', jadd(n, 1)), 0)
        Code03_LuckyNumber1.power = jcast('int', Code03_LuckyNumber1.log2(n))

    @staticmethod
    def log2(n):
        n = jcast('int', n)
        ans = jcast('int', 0)
        while (jcast('int', (1 << (ans & 31))) <= jcast('int', (n >> (1 & 31)))):
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code03_LuckyNumber1.next[Code03_LuckyNumber1.cnt] = jcast('int', Code03_LuckyNumber1.head[u])
        Code03_LuckyNumber1.to[Code03_LuckyNumber1.cnt] = jcast('int', v)
        jset(Code03_LuckyNumber1.head, u, ((_java_obj_1 := Code03_LuckyNumber1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_LuckyNumber1.deep[u] = jcast('int', jcast('int', jadd(Code03_LuckyNumber1.deep[f], 1)))
        jset(Code03_LuckyNumber1.stjump[u], 0, f)
        p = jcast('int', 1)
        while (p <= Code03_LuckyNumber1.power):
            jset(Code03_LuckyNumber1.stjump[u], p, Code03_LuckyNumber1.stjump[Code03_LuckyNumber1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        i = jcast('int', 0)
        while (i <= Code03_LuckyNumber1.BIT):
            jset(Code03_LuckyNumber1.bases[u], i, Code03_LuckyNumber1.bases[f][i])
            jset(Code03_LuckyNumber1.levels[u], i, Code03_LuckyNumber1.levels[f][i])
            i = jcast('int', (i + 1))
        Code03_LuckyNumber1.insertReplace(Code03_LuckyNumber1.arr[u], Code03_LuckyNumber1.deep[u], Code03_LuckyNumber1.bases[u], Code03_LuckyNumber1.levels[u])
        e = jcast('int', Code03_LuckyNumber1.head[u])
        while (e != 0):
            if (Code03_LuckyNumber1.to[e] != f):
                Code03_LuckyNumber1.dfs(Code03_LuckyNumber1.to[e], u)
            e = jcast('int', Code03_LuckyNumber1.next[e])

    # 插入和替换线性基，本题最重要的函数
    @staticmethod
    def insertReplace(curv, curl, basis, level):
        curv = jcast('long', curv)
        curl = jcast('int', curl)
        i = jcast('int', Code03_LuckyNumber1.BIT)
        while (i >= 0):
            if (jcast('long', (curv >> (i & 63))) == 1):
                if (basis[i] == 0):
                    basis[i] = jcast('long', curv)
                    level[i] = jcast('int', curl)
                    return jcast('boolean', True)
                if (curl > level[i]):
                    tmp1 = jcast('long', curv)
                    curv = jcast('long', basis[i])
                    basis[i] = jcast('long', tmp1)
                    tmp2 = jcast('int', level[i])
                    level[i] = jcast('int', curl)
                    curl = jcast('int', tmp2)
                curv = jcast('long', jcast('long', (curv ^ basis[i])))
            i = jcast('int', (i - 1))
        return jcast('boolean', False)

    @staticmethod
    def lca(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (Code03_LuckyNumber1.deep[x] < Code03_LuckyNumber1.deep[y]):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        p = jcast('int', Code03_LuckyNumber1.power)
        while (p >= 0):
            if (Code03_LuckyNumber1.deep[Code03_LuckyNumber1.stjump[x][p]] >= Code03_LuckyNumber1.deep[y]):
                x = jcast('int', Code03_LuckyNumber1.stjump[x][p])
            p = jcast('int', (p - 1))
        if (x == y):
            return jcast('int', x)
        p = jcast('int', Code03_LuckyNumber1.power)
        while (p >= 0):
            if (Code03_LuckyNumber1.stjump[x][p] != Code03_LuckyNumber1.stjump[y][p]):
                x = jcast('int', Code03_LuckyNumber1.stjump[x][p])
                y = jcast('int', Code03_LuckyNumber1.stjump[y][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code03_LuckyNumber1.stjump[x][0])

    basis = None
    @staticmethod
    def query(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        lca = jcast('int', Code03_LuckyNumber1.lca(x, y))
        basisx = Code03_LuckyNumber1.bases[x]
        levelx = Code03_LuckyNumber1.levels[x]
        basisy = Code03_LuckyNumber1.bases[y]
        levely = Code03_LuckyNumber1.levels[y]
        jstatic('Arrays', 'fill', Code03_LuckyNumber1.basis, 0)
        i = jcast('int', Code03_LuckyNumber1.BIT)
        while (i >= 0):
            num = jcast('long', basisx[i])
            if ((levelx[i] >= Code03_LuckyNumber1.deep[lca]) and (num != 0)):
                Code03_LuckyNumber1.basis[i] = jcast('long', num)
            i = jcast('int', (i - 1))
        i = jcast('int', Code03_LuckyNumber1.BIT)
        while (i >= 0):
            try:
                num = jcast('long', basisy[i])
                if ((levely[i] >= Code03_LuckyNumber1.deep[lca]) and (num != 0)):
                    j = jcast('int', i)
                    while (j >= 0):
                        try:
                            if (jcast('long', (num >> (j & 63))) == 1):
                                if (Code03_LuckyNumber1.basis[j] == 0):
                                    Code03_LuckyNumber1.basis[j] = jcast('long', num)
                                    raise JBreak(None)
                                num = jcast('long', jcast('long', (num ^ Code03_LuckyNumber1.basis[j])))
                        except JContinue as _java_control_5:
                            if _java_control_5.label not in (None,):
                                raise
                        except JBreak as _java_control_5:
                            if _java_control_5.label not in (None,):
                                raise
                            break
                        j = jcast('int', (j - 1))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
            i = jcast('int', (i - 1))
        ans = jcast('long', 0)
        i = jcast('int', Code03_LuckyNumber1.BIT)
        while (i >= 0):
            ans = jcast('long', jstatic('Math', 'max', ans, jcast('long', (ans ^ Code03_LuckyNumber1.basis[i]))))
            i = jcast('int', (i - 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        io = Code03_LuckyNumber1.Kattio(_java_ctor=0)
        n = jcast('int', jcall(io, 'nextInt'))
        q = jcast('int', jcall(io, 'nextInt'))
        Code03_LuckyNumber1.prepare(n)
        i = jcast('int', 1)
        while (i <= n):
            jset(Code03_LuckyNumber1.arr, i, jcall(io, 'nextLong'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            Code03_LuckyNumber1.addEdge(u, v)
            Code03_LuckyNumber1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code03_LuckyNumber1.dfs(1, 0)
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= q):
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            jcall(io, 'println', Code03_LuckyNumber1.query(x, y))
            i = jcast('int', (i + 1))
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
            except Exception as _java_exception_6:
                if jinstanceof(_java_exception_6, 'Exception'):
                    e = _java_exception_6
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
            raise TypeError("No matching overload for Code03_LuckyNumber1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_LuckyNumber1.MAXN = jcast('int', 20002)
Code03_LuckyNumber1.LIMIT = jcast('int', 16)
Code03_LuckyNumber1.BIT = jcast('int', 60)
Code03_LuckyNumber1.arr = jarray('long', [Code03_LuckyNumber1.MAXN])
Code03_LuckyNumber1.head = jarray('int', [Code03_LuckyNumber1.MAXN])
Code03_LuckyNumber1.next = jarray('int', [jcast('int', (Code03_LuckyNumber1.MAXN << (1 & 31)))])
Code03_LuckyNumber1.to = jarray('int', [jcast('int', (Code03_LuckyNumber1.MAXN << (1 & 31)))])
Code03_LuckyNumber1.cnt = jcast('int', 0)
Code03_LuckyNumber1.deep = jarray('int', [Code03_LuckyNumber1.MAXN])
Code03_LuckyNumber1.stjump = jarray('int', [Code03_LuckyNumber1.MAXN, Code03_LuckyNumber1.LIMIT])
Code03_LuckyNumber1.power = jcast('int', 0)
Code03_LuckyNumber1.bases = jarray('long', [Code03_LuckyNumber1.MAXN, jcast('int', jadd(Code03_LuckyNumber1.BIT, 1))])
Code03_LuckyNumber1.levels = jarray('int', [Code03_LuckyNumber1.MAXN, jcast('int', jadd(Code03_LuckyNumber1.BIT, 1))])
Code03_LuckyNumber1.basis = jarray('long', [jcast('int', jadd(Code03_LuckyNumber1.BIT, 1))])

if __name__ == '__main__':
    Code03_LuckyNumber1.main([])
