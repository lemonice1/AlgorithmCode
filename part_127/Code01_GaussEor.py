# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 高斯消元解决异或方程组模版题
# 有一个长度为n的数组arr，可能有重复值，数字都是long类型的正数
# 每个数拥有的质数因子一定不超过2000，每个数最多挑选一次
# 在至少要选一个数的情况下，你可以随意挑选数字乘起来
# 乘得的结果需要是完全平方数，请问有几种挑选数字的方法
# 方法数可能很大，答案对 1000000007 取模
# 1 <= n <= 300
# 1 <= arr[i] <= 10^18
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=5833
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_GaussEor:
    __java_fields__ = {'MOD': 'MOD', 'MAXV': 'MAXV', 'MAXN': 'MAXN', 'arr': 'arr', 'mat': 'mat', 'prime': 'prime', 'cnt': 'cnt', 'visit': 'visit', 'pow2': 'pow2', 'n': 'n'}
    MOD = 0
    MAXV = 0
    MAXN = 0
    arr = None
    mat = None
    # 收集2000以内的质数，一共就303个，这是大于arr的个数的
    prime = None
    # 2000以内质数的个数，一共就303个，这是大于arr的个数的
    cnt = 0
    # 埃氏筛需要
    visit = None
    # pow2[i] : 2的i次方 % MOD
    pow2 = None
    n = 0
    @staticmethod
    def prepare():
        # 得到2000以内的质数
        # 如果不会就去看，讲解097，埃氏筛
        # 当然也可以用欧拉筛，也在讲解097
        i = jcast('int', 2)
        while (jcast('int', (i * i)) <= Code01_GaussEor.MAXV):
            if (not Code01_GaussEor.visit[i]):
                j = jcast('int', jcast('int', (i * i)))
                while (j <= Code01_GaussEor.MAXV):
                    Code01_GaussEor.visit[j] = jcast('boolean', True)
                    j = jcast('int', jcast('int', jadd(j, i)))
            i = jcast('int', (i + 1))
        Code01_GaussEor.cnt = jcast('int', 0)
        i = jcast('int', 2)
        while (i <= Code01_GaussEor.MAXV):
            if (not Code01_GaussEor.visit[i]):
                jset(Code01_GaussEor.prime, ((_java_obj_1 := Code01_GaussEor), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], i)
            i = jcast('int', (i + 1))
        # 2的i次方%MOD的结果
        Code01_GaussEor.pow2[0] = jcast('int', 1)
        i = jcast('int', 1)
        while (i < Code01_GaussEor.MAXN):
            Code01_GaussEor.pow2[i] = jcast('int', jcast('int', jmod(jcast('int', (Code01_GaussEor.pow2[jcast('int', (i - 1))] * 2)), Code01_GaussEor.MOD)))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        Code01_GaussEor.prepare()
        # 题目会读取10^18范围内的long类型数字
        # StreamTokenizer 兼容层的 nval 使用 float；大整数应读取字符串后用 int 解析，避免浮点舍入
        # 这里使用 Kattio 分词接口，Python 示例见 part_14/Code05_Kattio.py
        # 有详细的说明
        io = Code01_GaussEor.Kattio(_java_ctor=0)
        test = jcast('int', jcall(io, 'nextInt'))
        t = jcast('int', 1)
        while (t <= test):
            Code01_GaussEor.n = jcast('int', jcall(io, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code01_GaussEor.n):
                jset(Code01_GaussEor.arr, i, jcall(io, 'nextLong'))
                i = jcast('int', (i + 1))
            jcall(io, 'println', jadd(jadd('Case #', t), ':'))
            jcall(io, 'println', Code01_GaussEor.compute())
            t = jcast('int', (t + 1))
        jcall(io, 'flush')
        jcall(io, 'close')

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code01_GaussEor.cnt):
            j = jcast('int', 1)
            while (j <= jcast('int', jadd(Code01_GaussEor.cnt, 1))):
                jset(Code01_GaussEor.mat[i], j, 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        cur = 0
        i = jcast('int', 1)
        while (i <= Code01_GaussEor.n):
            cur = jcast('long', Code01_GaussEor.arr[i])
            j = jcast('int', 1)
            while ((j <= Code01_GaussEor.cnt) and (cur != 0)):
                while (jcast('long', jmod(cur, Code01_GaussEor.prime[j])) == 0):
                    ((_java_obj_4 := Code01_GaussEor.mat[j]), (_java_key_5 := i), jset(_java_obj_4, _java_key_5, jcast('int', (jget(_java_obj_4, _java_key_5) ^ 1))))[2]
                    cur = jcast('long', jcast('long', jdiv(cur, Code01_GaussEor.prime[j])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code01_GaussEor.gauss(Code01_GaussEor.cnt)
        # 主元的数量
        main = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_GaussEor.cnt):
            if (Code01_GaussEor.mat[i][i] == 1):
                main = jcast('int', (main + 1))
            i = jcast('int', (i + 1))
        # 影响每个主元的自由元们一旦确定
        # 那么该主元选和不选也就唯一确定了
        # 所以重点是自由元如何决策，n - main就是自由元的数量
        # 自由元之间一定相互独立，每个自由元都可以做出选和不选的决定
        # 所以一共是2的(n - main)次方种决策
        # 但是想象一下，如果所有自由元都不选，
        # mat值的部分(cnt+1列)全是0啊！那么意味着，所有主元也都不选
        # 但是题目要求至少要选一个数，所以不能出现自由元都不选的情况
        # 所以返回方法数-1
        # 能够分析的前提是对主元和自由元之间的关系有清晰的认识
        return jcast('int', jcast('int', (Code01_GaussEor.pow2[jcast('int', (Code01_GaussEor.n - main))] - 1)))

    # 高斯消元解决异或方程组模版
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        if ((j < i) and (Code01_GaussEor.mat[j][j] == 1)):
                            raise JContinue(None)
                        if (Code01_GaussEor.mat[j][i] == 1):
                            Code01_GaussEor.swap(i, j)
                            raise JBreak(None)
                    except JContinue as _java_control_7:
                        if _java_control_7.label not in (None,):
                            raise
                    except JBreak as _java_control_7:
                        if _java_control_7.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if (Code01_GaussEor.mat[i][i] == 1):
                    j = jcast('int', 1)
                    while (j <= n):
                        if ((i != j) and (Code01_GaussEor.mat[j][i] == 1)):
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                ((_java_obj_8 := Code01_GaussEor.mat[j]), (_java_key_9 := k), jset(_java_obj_8, _java_key_9, jcast('int', (jget(_java_obj_8, _java_key_9) ^ Code01_GaussEor.mat[i][k]))))[2]
                                k = jcast('int', (k + 1))
                        j = jcast('int', (j + 1))
            except JContinue as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
            except JBreak as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = Code01_GaussEor.mat[a]
        Code01_GaussEor.mat[a] = Code01_GaussEor.mat[b]
        Code01_GaussEor.mat[b] = tmp

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
            except Exception as _java_exception_10:
                if jinstanceof(_java_exception_10, 'Exception'):
                    e = _java_exception_10
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
            raise TypeError("No matching overload for Code01_GaussEor.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_GaussEor.MOD = jcast('int', 1000000007)
Code01_GaussEor.MAXV = jcast('int', 2000)
Code01_GaussEor.MAXN = jcast('int', 305)
Code01_GaussEor.arr = jarray('long', [Code01_GaussEor.MAXN])
Code01_GaussEor.mat = jarray('int', [Code01_GaussEor.MAXN, Code01_GaussEor.MAXN])
Code01_GaussEor.prime = jarray('int', [jcast('int', jadd(Code01_GaussEor.MAXV, 1))])
Code01_GaussEor.cnt = jcast('int', 0)
Code01_GaussEor.visit = jarray('boolean', [jcast('int', jadd(Code01_GaussEor.MAXV, 1))])
Code01_GaussEor.pow2 = jarray('int', [Code01_GaussEor.MAXN])
Code01_GaussEor.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_GaussEor.main([])
