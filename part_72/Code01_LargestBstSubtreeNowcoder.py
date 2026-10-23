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

# 最大BST子树，牛客测试
# 因为题目1是leetcode收费题，所以补充一个牛客的测试链接
# 题意完全一样，但是需要根据牛客给的数据格式，建立二叉树
# 测试链接 : https://www.nowcoder.com/practice/380d49d7f99242709ab4b91c36bf2acc
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_LargestBstSubtreeNowcoder:
    __java_fields__ = {}
    class TreeNode:
        __java_fields__ = {'val': 'val', 'left': 'left', 'right': 'right'}
        # val：实例字段，在构造函数中初始化。
        # left：实例字段，在构造函数中初始化。
        # right：实例字段，在构造函数中初始化。
        def _java_init_0(self, v):
            v = jcast('int', v)
            self.val = jcast('int', v)

        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.left = None
            self.right = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_LargestBstSubtreeNowcoder.TreeNode.TreeNode")


    @staticmethod
    def largestBSTSubtree(root):
        return jcast('int', jget(Code01_LargestBstSubtreeNowcoder.f(root), 'maxBstSize'))

    class Info:
        __java_fields__ = {'max': 'max', 'min': 'min', 'isBst': 'isBst', 'maxBstSize': 'maxBstSize'}
        # max：实例字段，在构造函数中初始化。
        # min：实例字段，在构造函数中初始化。
        # isBst：实例字段，在构造函数中初始化。
        # maxBstSize：实例字段，在构造函数中初始化。
        def _java_init_0(self, a, b, c, d):
            a = jcast('long', a)
            b = jcast('long', b)
            c = jcast('boolean', c)
            d = jcast('int', d)
            self.max = jcast('long', a)
            self.min = jcast('long', b)
            self.isBst = jcast('boolean', c)
            self.maxBstSize = jcast('int', d)

        def __init__(self, *args, _java_ctor=None):
            self.max = jcast('long', 0)
            self.min = jcast('long', 0)
            self.isBst = jcast('boolean', False)
            self.maxBstSize = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['long', 'long', 'boolean', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_LargestBstSubtreeNowcoder.Info.Info")


    @staticmethod
    def f(x):
        if (x == None):
            return Code01_LargestBstSubtreeNowcoder.Info(jget(Long, 'MIN_VALUE'), jget(Long, 'MAX_VALUE'), True, 0, _java_ctor=0)
        infol = Code01_LargestBstSubtreeNowcoder.f(jget(x, 'left'))
        infor = Code01_LargestBstSubtreeNowcoder.f(jget(x, 'right'))
        max = jcast('long', jstatic('Math', 'max', jget(x, 'val'), jstatic('Math', 'max', jget(infol, 'max'), jget(infor, 'max'))))
        min = jcast('long', jstatic('Math', 'min', jget(x, 'val'), jstatic('Math', 'min', jget(infol, 'min'), jget(infor, 'min'))))
        isBst = jcast('boolean', (((jget(infol, 'isBst') and jget(infor, 'isBst')) and (jget(infol, 'max') < jget(x, 'val'))) and (jget(x, 'val') < jget(infor, 'min'))))
        maxBSTSize = 0
        if isBst:
            maxBSTSize = jcast('int', jcast('int', jadd(jcast('int', jadd(jget(infol, 'maxBstSize'), jget(infor, 'maxBstSize'))), 1)))
        else:
            maxBSTSize = jcast('int', jstatic('Math', 'max', jget(infol, 'maxBstSize'), jget(infor, 'maxBstSize')))
        return Code01_LargestBstSubtreeNowcoder.Info(max, min, isBst, maxBSTSize, _java_ctor=0)

    # 根据牛客的题目描述，读入数据、建二叉树、调用方法、打印答案
    @staticmethod
    def main(args):
        in_ = Code01_LargestBstSubtreeNowcoder.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        n = jcast('int', jcall(in_, 'nextInt'))
        root = jcast('int', jcall(in_, 'nextInt'))
        arr = jarray('TreeNode', [jcast('int', jadd(n, 1))])
        i = jcast('int', 1)
        while (i <= n):
            jset(arr, i, Code01_LargestBstSubtreeNowcoder.TreeNode(i, _java_ctor=0))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        fa = 0
        l = 0
        r = 0
        while (i <= n):
            fa = jcast('int', jcall(in_, 'nextInt'))
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            if (l != 0):
                jset(arr[fa], 'left', arr[l])
            if (r != 0):
                jset(arr[fa], 'right', arr[r])
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_LargestBstSubtreeNowcoder.largestBSTSubtree(arr[root]))
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
            return jcast('int', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

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
            raise TypeError("No matching overload for Code01_LargestBstSubtreeNowcoder.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_LargestBstSubtreeNowcoder.main([])
