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

# 有一次错误称重求最重物品
# 这道题后来增加了测试数据，其实没意思
# 下面通过调整数据表示与输入输出减少常数开销
# 看看注释的部分，其他代码和课上的一样
# 测试链接 : https://www.luogu.com.cn/problem/P5027
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_FindMaxWeighing2:
    __java_fields__ = {'MAXN': 'MAXN', 'data': 'data', 'mat': 'mat', 'n': 'n'}
    MAXN = 0
    data = None
    # mat改成long[][]，删除sml，整数直接判断是否为0，不使用浮点误差阈值
    mat = None
    n = 0
    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = Code04_FindMaxWeighing2.mat[a]
        Code04_FindMaxWeighing2.mat[a] = Code04_FindMaxWeighing2.mat[b]
        Code04_FindMaxWeighing2.mat[b] = tmp

    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                max = jcast('int', i)
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        # 原来是Math.abs(mat[j][j]) >= sml
                        if ((j < i) and (Code04_FindMaxWeighing2.mat[j][j] != 0)):
                            raise JContinue(None)
                        if (jstatic('Math', 'abs', Code04_FindMaxWeighing2.mat[j][i]) > jstatic('Math', 'abs', Code04_FindMaxWeighing2.mat[max][i])):
                            max = jcast('int', j)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                Code04_FindMaxWeighing2.swap(i, max)
                # 找不到主元直接返回，由check检查零对角元素并判不合法
                if (Code04_FindMaxWeighing2.mat[i][i] == 0):
                    return
                # 原版把主元行除以主元，使主元变为1的操作
                # long除法会截断分数，所以不再进行这种归一化
                # 原版消去当前列其他所有行的元素
                # 现在只消去下方元素，得到上三角矩阵，之后再回代
                j = jcast('int', jcast('int', jadd(i, 1)))
                while (j <= n):
                    # 反复进行整行相减、交换，直到mat[j][i]变为0
                    while (Code04_FindMaxWeighing2.mat[j][i] != 0):
                        # 原来是double rate = mat[j][i] / mat[i][i]
                        # 现在使用反方向的整数商，进行辗转消元
                        rate = jcast('long', jcast('long', jdiv(Code04_FindMaxWeighing2.mat[i][i], Code04_FindMaxWeighing2.mat[j][i])))
                        # 商为0时可以跳过相减，但仍然需要交换两行
                        if (rate != 0):
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                # 原版更新第j行，现在更新第i行
                                # 当前列的元素变成整数除法的余数
                                ((_java_obj_3 := Code04_FindMaxWeighing2.mat[i]), (_java_key_4 := k), jset(_java_obj_3, _java_key_4, jcast('long', (jget(_java_obj_3, _java_key_4) - jcast('long', (Code04_FindMaxWeighing2.mat[j][k] * rate))))))[2]
                                k = jcast('int', (k + 1))
                        # 设当前列两元素为a、b
                        # 相减再交换后，变成b、a%b，与辗转相除相同
                        # 在运算不溢出的前提下，最终下方元素变为0
                        Code04_FindMaxWeighing2.swap(i, j)
                    j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def check():
        Code04_FindMaxWeighing2.gauss(Code04_FindMaxWeighing2.n)
        # 原版消元后直接读取最后一列，现在需要倒序回代
        # 因为只消去了下方元素，第i行仍然可能包含编号大于i的变量
        i = jcast('int', Code04_FindMaxWeighing2.n)
        while (i >= 1):
            if (Code04_FindMaxWeighing2.mat[i][i] == 0):
                return jcast('int', 0)
            # 编号大于i的变量已经求出，保存在对应行的最后一列
            # 从当前方程右侧减去这些变量的贡献
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j <= Code04_FindMaxWeighing2.n):
                ((_java_obj_5 := Code04_FindMaxWeighing2.mat[i]), (_java_key_6 := jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))), jset(_java_obj_5, _java_key_6, jcast('long', (jget(_java_obj_5, _java_key_6) - jcast('long', (Code04_FindMaxWeighing2.mat[i][j] * Code04_FindMaxWeighing2.mat[j][jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))]))))))[2]
                j = jcast('int', (j + 1))
            # 通过余数精确判断重量是否为整数
            if (jcast('long', jmod(Code04_FindMaxWeighing2.mat[i][jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))], Code04_FindMaxWeighing2.mat[i][i])) != 0):
                return jcast('int', 0)
            # 除以当前变量的系数，得到重量，仍保存在最后一列
            ((_java_obj_7 := Code04_FindMaxWeighing2.mat[i]), (_java_key_8 := jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))), jset(_java_obj_7, _java_key_8, jcast('long', jdiv(jget(_java_obj_7, _java_key_8), Code04_FindMaxWeighing2.mat[i][i]))))[2]
            i = jcast('int', (i - 1))
        # 原来是double maxv = Double.MIN_VALUE;
        maxv = jcast('long', 0)
        maxt = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_FindMaxWeighing2.n):
            if (Code04_FindMaxWeighing2.mat[i][i] == 0):
                return jcast('int', 0)
            # 删除原来的浮点判整：
            # mat[i][n + 1] != (int) mat[i][n + 1]
            # 整数条件已在回代时检查，这里只检查正数
            if (Code04_FindMaxWeighing2.mat[i][jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))] <= 0):
                return jcast('int', 0)
            if (maxv < Code04_FindMaxWeighing2.mat[i][jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))]):
                maxv = jcast('long', Code04_FindMaxWeighing2.mat[i][jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))])
                maxt = jcast('int', 1)
                ans = jcast('int', i)
            else:
                if (maxv == Code04_FindMaxWeighing2.mat[i][jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))]):
                    maxt = jcast('int', (maxt + 1))
            i = jcast('int', (i + 1))
        if (maxt > 1):
            return jcast('int', 0)
        return jcast('int', ans)

    @staticmethod
    def swapData(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = Code04_FindMaxWeighing2.data[i]
        Code04_FindMaxWeighing2.data[i] = Code04_FindMaxWeighing2.data[j]
        Code04_FindMaxWeighing2.data[j] = tmp

    @staticmethod
    def main(args):
        in_ = Code04_FindMaxWeighing2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_FindMaxWeighing2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        m = 0
        while (i <= jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))):
            m = jcast('int', jcall(in_, 'nextInt'))
            j = jcast('int', 1)
            cur = 0
            while (j <= m):
                cur = jcast('int', jcall(in_, 'nextInt'))
                jset(Code04_FindMaxWeighing2.data[i], cur, 1)
                j = jcast('int', (j + 1))
            jset(Code04_FindMaxWeighing2.data[i], jcast('int', jadd(Code04_FindMaxWeighing2.n, 1)), jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        times = jcast('int', 0)
        k = jcast('int', 1)
        while (k <= jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))):
            Code04_FindMaxWeighing2.swapData(k, jcast('int', jadd(Code04_FindMaxWeighing2.n, 1)))
            i = jcast('int', 1)
            while (i <= Code04_FindMaxWeighing2.n):
                j = jcast('int', 1)
                while (j <= jcast('int', jadd(Code04_FindMaxWeighing2.n, 1))):
                    jset(Code04_FindMaxWeighing2.mat[i], j, Code04_FindMaxWeighing2.data[i][j])
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            Code04_FindMaxWeighing2.swapData(k, jcast('int', jadd(Code04_FindMaxWeighing2.n, 1)))
            cur = jcast('int', Code04_FindMaxWeighing2.check())
            if (cur != 0):
                times = jcast('int', (times + 1))
                ans = jcast('int', cur)
            k = jcast('int', (k + 1))
        if (times != 1):
            jcall(out, 'println', 'illegal')
        else:
            jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_9 := self), (_java_key_10 := 'ptr'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_FindMaxWeighing2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_FindMaxWeighing2.MAXN = jcast('int', 102)
Code04_FindMaxWeighing2.data = jarray('int', [Code04_FindMaxWeighing2.MAXN, Code04_FindMaxWeighing2.MAXN])
Code04_FindMaxWeighing2.mat = jarray('long', [Code04_FindMaxWeighing2.MAXN, Code04_FindMaxWeighing2.MAXN])
Code04_FindMaxWeighing2.n = jcast('int', 0)

if __name__ == '__main__':
    Code04_FindMaxWeighing2.main([])
