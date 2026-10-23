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

# 单调栈求每个位置左右两侧，离当前位置最近、且值严格小于的位置
# 给定一个可能含有重复值的数组 arr
# 找到每一个 i 位置左边和右边离 i 位置最近且值比 arr[i] 小的位置
# 返回所有位置相应的信息。
# 输入描述：
# 第一行输入一个数字 n，表示数组 arr 的长度。
# 以下一行输入 n 个数字，表示数组的值
# 输出描述：
# 输出n行，每行两个数字 L 和 R，如果不存在，则值为 -1，下标从 0 开始。
# 测试链接 : https://www.nowcoder.com/practice/2a2c00e7a88a498693568cef63a4b7bb
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_LeftRightLess:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'stack': 'stack', 'ans': 'ans', 'n': 'n', 'r': 'r'}
    MAXN = 0
    arr = None
    stack = None
    ans = None
    n = 0
    r = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code01_LeftRightLess.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code01_LeftRightLess.n):
                jcall(in_, 'nextToken')
                Code01_LeftRightLess.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            Code01_LeftRightLess.compute()
            i = jcast('int', 0)
            while (i < Code01_LeftRightLess.n):
                jcall(out, 'println', jadd(jadd(Code01_LeftRightLess.ans[i][0], ' '), Code01_LeftRightLess.ans[i][1]))
                i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # arr[0...n-1]
    @staticmethod
    def compute():
        Code01_LeftRightLess.r = jcast('int', 0)
        cur = 0
        # 遍历阶段
        i = jcast('int', 0)
        while (i < Code01_LeftRightLess.n):
            # i -> arr[i]
            while ((Code01_LeftRightLess.r > 0) and (Code01_LeftRightLess.arr[Code01_LeftRightLess.stack[jcast('int', (Code01_LeftRightLess.r - 1))]] >= Code01_LeftRightLess.arr[i])):
                cur = jcast('int', Code01_LeftRightLess.stack[((_java_obj_1 := Code01_LeftRightLess), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3]])
                # cur当前弹出的位置，左边最近且小
                jset(Code01_LeftRightLess.ans[cur], 0, (Code01_LeftRightLess.stack[jcast('int', (Code01_LeftRightLess.r - 1))] if (Code01_LeftRightLess.r > 0) else jcast('int', (-1))))
                jset(Code01_LeftRightLess.ans[cur], 1, i)
            jset(Code01_LeftRightLess.stack, ((_java_obj_4 := Code01_LeftRightLess), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], i)
            i = jcast('int', (i + 1))
        # 清算阶段
        while (Code01_LeftRightLess.r > 0):
            cur = jcast('int', Code01_LeftRightLess.stack[((_java_obj_7 := Code01_LeftRightLess), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3]])
            jset(Code01_LeftRightLess.ans[cur], 0, (Code01_LeftRightLess.stack[jcast('int', (Code01_LeftRightLess.r - 1))] if (Code01_LeftRightLess.r > 0) else jcast('int', (-1))))
            jset(Code01_LeftRightLess.ans[cur], 1, jcast('int', (-1)))
        # 修正阶段
        # 左侧的答案不需要修正一定是正确的，只有右侧答案需要修正
        # 从右往左修正，n-1位置的右侧答案一定是-1，不需要修正
        i = jcast('int', jcast('int', (Code01_LeftRightLess.n - 2)))
        while (i >= 0):
            if ((Code01_LeftRightLess.ans[i][1] != jcast('int', (-1))) and (Code01_LeftRightLess.arr[Code01_LeftRightLess.ans[i][1]] == Code01_LeftRightLess.arr[i])):
                jset(Code01_LeftRightLess.ans[i], 1, Code01_LeftRightLess.ans[Code01_LeftRightLess.ans[i][1]][1])
            i = jcast('int', (i - 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_LeftRightLess.MAXN = jcast('int', 1000001)
Code01_LeftRightLess.arr = jarray('int', [Code01_LeftRightLess.MAXN])
Code01_LeftRightLess.stack = jarray('int', [Code01_LeftRightLess.MAXN])
Code01_LeftRightLess.ans = jarray('int', [Code01_LeftRightLess.MAXN, 2])
Code01_LeftRightLess.n = jcast('int', 0)
Code01_LeftRightLess.r = jcast('int', 0)

if __name__ == '__main__':
    Code01_LeftRightLess.main([])
