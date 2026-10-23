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

# 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
# 给定一个长度为n的数组arr，接下来有m条操作，每条操作格式如下
# 操作 l r : 打印arr[l..r]范围上，众数到底出现了几次
# 1 <= 所有数值 <= 5 * 10^5
# 内存空间只有64MB，题目要求强制在线，具体规则可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P5048
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_ModeCnt2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'sortList': 'sortList', 'listIdx': 'listIdx', 'modeCnt': 'modeCnt', 'numCnt': 'numCnt'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    # (值、下标)，用来收集同一种数的下标列表
    sortList = None
    # listIdx[i] = j，表示arr[i]这个元素在sortList里的j位置
    listIdx = None
    # modeCnt[i][j]表示从i块到j块中众数的出现次数
    modeCnt = None
    # 数字词频统计
    numCnt = None
    @staticmethod
    def prepare():
        Code04_ModeCnt2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code04_ModeCnt2.n)))
        Code04_ModeCnt2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code04_ModeCnt2.n, Code04_ModeCnt2.blen)) - 1)), Code04_ModeCnt2.blen)))
        i = jcast('int', 1)
        while (i <= Code04_ModeCnt2.n):
            Code04_ModeCnt2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code04_ModeCnt2.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_ModeCnt2.bnum):
            Code04_ModeCnt2.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code04_ModeCnt2.blen)), 1)))
            jset(Code04_ModeCnt2.br, i, jstatic('Math', 'min', jcast('int', (i * Code04_ModeCnt2.blen)), Code04_ModeCnt2.n))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_ModeCnt2.n):
            jset(Code04_ModeCnt2.sortList[i], 0, Code04_ModeCnt2.arr[i])
            jset(Code04_ModeCnt2.sortList[i], 1, i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_ModeCnt2.sortList, 1, jcast('int', jadd(Code04_ModeCnt2.n, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        i = jcast('int', 1)
        while (i <= Code04_ModeCnt2.n):
            jset(Code04_ModeCnt2.listIdx, Code04_ModeCnt2.sortList[i][1], i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_ModeCnt2.bnum):
            j = jcast('int', i)
            while (j <= Code04_ModeCnt2.bnum):
                cnt = jcast('int', Code04_ModeCnt2.modeCnt[i][jcast('int', (j - 1))])
                k = jcast('int', Code04_ModeCnt2.bl[j])
                while (k <= Code04_ModeCnt2.br[j]):
                    cnt = jcast('int', jstatic('Math', 'max', cnt, ((_java_obj_1 := Code04_ModeCnt2.numCnt), (_java_key_2 := Code04_ModeCnt2.arr[k]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]))
                    k = jcast('int', (k + 1))
                jset(Code04_ModeCnt2.modeCnt[i], j, cnt)
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            while (j <= Code04_ModeCnt2.n):
                Code04_ModeCnt2.numCnt[j] = jcast('int', 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ans = jcast('int', 0)
        if (Code04_ModeCnt2.bi[l] == Code04_ModeCnt2.bi[r]):
            i = jcast('int', l)
            while (i <= r):
                ans = jcast('int', jstatic('Math', 'max', ans, ((_java_obj_4 := Code04_ModeCnt2.numCnt), (_java_key_5 := Code04_ModeCnt2.arr[i]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
                i = jcast('int', (i + 1))
            i = jcast('int', l)
            while (i <= r):
                jset(Code04_ModeCnt2.numCnt, Code04_ModeCnt2.arr[i], 0)
                i = jcast('int', (i + 1))
        else:
            ans = jcast('int', Code04_ModeCnt2.modeCnt[jcast('int', jadd(Code04_ModeCnt2.bi[l], 1))][jcast('int', (Code04_ModeCnt2.bi[r] - 1))])
            i = jcast('int', l)
            idx = 0
            while (i <= Code04_ModeCnt2.br[Code04_ModeCnt2.bi[l]]):
                idx = jcast('int', Code04_ModeCnt2.listIdx[i])
                while (((jcast('int', jadd(idx, ans)) <= Code04_ModeCnt2.n) and (Code04_ModeCnt2.sortList[jcast('int', jadd(idx, ans))][0] == Code04_ModeCnt2.arr[i])) and (Code04_ModeCnt2.sortList[jcast('int', jadd(idx, ans))][1] <= r)):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', Code04_ModeCnt2.bl[Code04_ModeCnt2.bi[r]])
            idx = 0
            while (i <= r):
                idx = jcast('int', Code04_ModeCnt2.listIdx[i])
                while (((jcast('int', (idx - ans)) >= 1) and (Code04_ModeCnt2.sortList[jcast('int', (idx - ans))][0] == Code04_ModeCnt2.arr[i])) and (Code04_ModeCnt2.sortList[jcast('int', (idx - ans))][1] >= l)):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code04_ModeCnt2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_ModeCnt2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_ModeCnt2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_ModeCnt2.n):
            jset(Code04_ModeCnt2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code04_ModeCnt2.prepare()
        i = jcast('int', 1)
        l = 0
        r = 0
        lastAns = jcast('int', 0)
        while (i <= Code04_ModeCnt2.m):
            l = jcast('int', jcast('int', (jcall(in_, 'nextInt') ^ lastAns)))
            r = jcast('int', jcast('int', (jcall(in_, 'nextInt') ^ lastAns)))
            lastAns = jcast('int', Code04_ModeCnt2.query(l, r))
            jcall(out, 'println', lastAns)
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_ModeCnt2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_ModeCnt2.MAXN = jcast('int', 500001)
Code04_ModeCnt2.MAXB = jcast('int', 801)
Code04_ModeCnt2.n = jcast('int', 0)
Code04_ModeCnt2.m = jcast('int', 0)
Code04_ModeCnt2.arr = jarray('int', [Code04_ModeCnt2.MAXN])
Code04_ModeCnt2.blen = jcast('int', 0)
Code04_ModeCnt2.bnum = jcast('int', 0)
Code04_ModeCnt2.bi = jarray('int', [Code04_ModeCnt2.MAXN])
Code04_ModeCnt2.bl = jarray('int', [Code04_ModeCnt2.MAXB])
Code04_ModeCnt2.br = jarray('int', [Code04_ModeCnt2.MAXB])
Code04_ModeCnt2.sortList = jarray('int', [Code04_ModeCnt2.MAXN, 2])
Code04_ModeCnt2.listIdx = jarray('int', [Code04_ModeCnt2.MAXN])
Code04_ModeCnt2.modeCnt = jarray('int', [Code04_ModeCnt2.MAXB, Code04_ModeCnt2.MAXB])
Code04_ModeCnt2.numCnt = jarray('int', [Code04_ModeCnt2.MAXN])

if __name__ == '__main__':
    Code04_ModeCnt2.main([])
