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

# 炮兵阵地(空间压缩优化)
# 给定一个n * m的二维数组grid，其中的1代表可以摆放炮兵，0代表不可以摆放
# 任何炮兵攻击范围是一个"十字型"的区域，具体是上下左右两个格子的区域
# 你的目的是在gird里摆尽量多的炮兵，但要保证任何两个炮兵之间无法互相攻击
# 返回最多能摆几个炮兵
# 1 <= n <= 100
# 1 <= m <= 10
# 0 <= grid[i][j] <= 1
# 测试链接 : https://www.luogu.com.cn/problem/P2704
# 测试链接 : http://poj.org/problem?id=1185
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_SoldierPosition2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXS': 'MAXS', 'grid': 'grid', 'memo': 'memo', 'dp': 'dp', 'sta': 'sta', 'n': 'n', 'm': 'm', 'k': 'k'}
    MAXN = 0
    MAXM = 0
    MAXS = 0
    grid = None
    memo = None
    dp = None
    sta = None
    n = 0
    m = 0
    k = 0
    @staticmethod
    def main(args):
        io = Code02_SoldierPosition2.Kattio(_java_ctor=0)
        Code02_SoldierPosition2.n = jcast('int', jcall(io, 'nextInt'))
        Code02_SoldierPosition2.m = jcast('int', jcall(io, 'nextInt'))
        Code02_SoldierPosition2.k = jcast('int', 0)
        line = None
        i = jcast('int', 0)
        while (i < Code02_SoldierPosition2.n):
            line = jcall(jcall(io, 'next'), 'toCharArray')
            j = jcast('int', 0)
            while (j < Code02_SoldierPosition2.m):
                jset(Code02_SoldierPosition2.grid[i], j, (0 if (line[j] == jchar('H')) else 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code02_SoldierPosition2.prepare(0, 0)
        jcall(io, 'println', Code02_SoldierPosition2.compute())
        jcall(io, 'flush')
        jcall(io, 'close')

    @staticmethod
    def prepare(j, s):
        j = jcast('int', j)
        s = jcast('int', s)
        if (j >= Code02_SoldierPosition2.m):
            jset(Code02_SoldierPosition2.sta, ((_java_obj_1 := Code02_SoldierPosition2), (_java_key_2 := 'k'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], s)
        else:
            Code02_SoldierPosition2.prepare(jcast('int', jadd(j, 1)), s)
            Code02_SoldierPosition2.prepare(jcast('int', jadd(j, 3)), jcast('int', (s | jcast('int', (1 << (j & 31))))))

    @staticmethod
    def compute():
        a = jcast('int', 0)
        cnt = 0
        while (a < Code02_SoldierPosition2.k):
            cnt = jcast('int', Code02_SoldierPosition2.cnt(0, Code02_SoldierPosition2.sta[a]))
            jset(Code02_SoldierPosition2.memo[a], 0, cnt)
            a = jcast('int', (a + 1))
        i = jcast('int', 1)
        while (i < Code02_SoldierPosition2.n):
            a = jcast('int', 0)
            cnt = 0
            while (a < Code02_SoldierPosition2.k):
                cnt = jcast('int', Code02_SoldierPosition2.cnt(i, Code02_SoldierPosition2.sta[a]))
                b = jcast('int', 0)
                while (b < Code02_SoldierPosition2.k):
                    jset(Code02_SoldierPosition2.dp[a], b, 0)
                    if (jcast('int', (Code02_SoldierPosition2.sta[a] & Code02_SoldierPosition2.sta[b])) == 0):
                        c = jcast('int', 0)
                        while (c < Code02_SoldierPosition2.k):
                            if ((jcast('int', (Code02_SoldierPosition2.sta[b] & Code02_SoldierPosition2.sta[c])) == 0) and (jcast('int', (Code02_SoldierPosition2.sta[a] & Code02_SoldierPosition2.sta[c])) == 0)):
                                jset(Code02_SoldierPosition2.dp[a], b, jstatic('Math', 'max', Code02_SoldierPosition2.dp[a][b], jcast('int', jadd(Code02_SoldierPosition2.memo[b][c], cnt))))
                            c = jcast('int', (c + 1))
                    b = jcast('int', (b + 1))
                a = jcast('int', (a + 1))
            tmp = Code02_SoldierPosition2.memo
            Code02_SoldierPosition2.memo = Code02_SoldierPosition2.dp
            Code02_SoldierPosition2.dp = tmp
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        a = jcast('int', 0)
        while (a < Code02_SoldierPosition2.k):
            b = jcast('int', 0)
            while (b < Code02_SoldierPosition2.k):
                ans = jcast('int', jstatic('Math', 'max', ans, Code02_SoldierPosition2.memo[a][b]))
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))
        return jcast('int', ans)

    @staticmethod
    def cnt(i, s):
        i = jcast('int', i)
        s = jcast('int', s)
        ans = jcast('int', 0)
        j = jcast('int', 0)
        while (j < Code02_SoldierPosition2.m):
            if ((jcast('int', (jcast('int', (s >> (j & 31))) & 1)) == 1) and (Code02_SoldierPosition2.grid[i][j] == 1)):
                ans = jcast('int', (ans + 1))
            j = jcast('int', (j + 1))
        return jcast('int', ans)

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
            except Exception as _java_exception_4:
                if jinstanceof(_java_exception_4, 'Exception'):
                    e = _java_exception_4
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
            raise TypeError("No matching overload for Code02_SoldierPosition2.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SoldierPosition2.MAXN = jcast('int', 100)
Code02_SoldierPosition2.MAXM = jcast('int', 10)
Code02_SoldierPosition2.MAXS = jcast('int', 60)
Code02_SoldierPosition2.grid = jarray('int', [Code02_SoldierPosition2.MAXN, Code02_SoldierPosition2.MAXM])
Code02_SoldierPosition2.memo = jarray('int', [Code02_SoldierPosition2.MAXS, Code02_SoldierPosition2.MAXS])
Code02_SoldierPosition2.dp = jarray('int', [Code02_SoldierPosition2.MAXS, Code02_SoldierPosition2.MAXS])
Code02_SoldierPosition2.sta = jarray('int', [Code02_SoldierPosition2.MAXS])
Code02_SoldierPosition2.n = jcast('int', 0)
Code02_SoldierPosition2.m = jcast('int', 0)
Code02_SoldierPosition2.k = jcast('int', 0)

if __name__ == '__main__':
    Code02_SoldierPosition2.main([])
