# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 基数排序，acm练习风格
# 测试链接 : https://www.luogu.com.cn/problem/P1177
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_RadixSort:
    __java_fields__ = {'BASE': 'BASE', 'MAXN': 'MAXN', 'arr': 'arr', 'help': 'help', 'cnts': 'cnts', 'n': 'n'}
    # 可以设置进制，不一定10进制，随你设置
    BASE = 0
    MAXN = 0
    arr = None
    help = None
    cnts = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_RadixSort.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < Code01_RadixSort.n):
            jcall(in_, 'nextToken')
            Code01_RadixSort.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code01_RadixSort.sort()
        i = jcast('int', 0)
        while (i < jcast('int', (Code01_RadixSort.n - 1))):
            jcall(out, 'print', jadd(Code01_RadixSort.arr[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_RadixSort.arr[jcast('int', (Code01_RadixSort.n - 1))])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def sort():
        # 如果会溢出，那么要改用long类型数组来排序
        # 找到数组中的最小值
        min = jcast('int', Code01_RadixSort.arr[0])
        i = jcast('int', 1)
        while (i < Code01_RadixSort.n):
            min = jcast('int', jstatic('Math', 'min', min, Code01_RadixSort.arr[i]))
            i = jcast('int', (i + 1))
        max = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code01_RadixSort.n):
            # 数组中的每个数字，减去数组中的最小值，就把arr转成了非负数组
            Code01_RadixSort.arr[i] = jcast('int', jcast('int', (Code01_RadixSort.arr[i] - min)))
            # 记录数组中的最大值
            max = jcast('int', jstatic('Math', 'max', max, Code01_RadixSort.arr[i]))
            i = jcast('int', (i + 1))
        # 根据最大值在BASE进制下的位数，决定基数排序做多少轮
        Code01_RadixSort.radixSort(Code01_RadixSort.bits(max))
        # 数组中所有数都减去了最小值，所以最后不要忘了还原
        i = jcast('int', 0)
        while (i < Code01_RadixSort.n):
            Code01_RadixSort.arr[i] = jcast('int', jcast('int', jadd(Code01_RadixSort.arr[i], min)))
            i = jcast('int', (i + 1))

    # 返回number在BASE进制下有几位
    @staticmethod
    def bits(number):
        number = jcast('int', number)
        ans = jcast('int', 0)
        while (number > 0):
            ans = jcast('int', (ans + 1))
            number = jcast('int', jcast('int', jdiv(number, Code01_RadixSort.BASE)))
        return jcast('int', ans)

    # 基数排序核心代码
    # arr内要保证没有负数
    # m是arr中最大值在BASE进制下有几位
    @staticmethod
    def radixSort(bits):
        bits = jcast('int', bits)
        # 理解的时候可以假设BASE = 10
        offset = jcast('int', 1)
        while (bits > 0):
            jstatic('Arrays', 'fill', Code01_RadixSort.cnts, 0)
            i = jcast('int', 0)
            while (i < Code01_RadixSort.n):
                # 数字提取某一位的技巧
                ((_java_obj_1 := Code01_RadixSort.cnts), (_java_key_2 := jcast('int', jmod(jcast('int', jdiv(Code01_RadixSort.arr[i], offset)), Code01_RadixSort.BASE))), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i < Code01_RadixSort.BASE):
                Code01_RadixSort.cnts[i] = jcast('int', jcast('int', jadd(Code01_RadixSort.cnts[i], Code01_RadixSort.cnts[jcast('int', (i - 1))])))
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', (Code01_RadixSort.n - 1)))
            while (i >= 0):
                # 前缀数量分区的技巧
                # 数字提取某一位的技巧
                jset(Code01_RadixSort.help, ((_java_obj_4 := Code01_RadixSort.cnts), (_java_key_5 := jcast('int', jmod(jcast('int', jdiv(Code01_RadixSort.arr[i], offset)), Code01_RadixSort.BASE))), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3], Code01_RadixSort.arr[i])
                i = jcast('int', (i - 1))
            i = jcast('int', 0)
            while (i < Code01_RadixSort.n):
                Code01_RadixSort.arr[i] = jcast('int', Code01_RadixSort.help[i])
                i = jcast('int', (i + 1))
            offset = jcast('int', jcast('int', (offset * Code01_RadixSort.BASE)))
            bits = jcast('int', (bits - 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_RadixSort.BASE = jcast('int', 10)
Code01_RadixSort.MAXN = jcast('int', 100001)
Code01_RadixSort.arr = jarray('int', [Code01_RadixSort.MAXN])
Code01_RadixSort.help = jarray('int', [Code01_RadixSort.MAXN])
Code01_RadixSort.cnts = jarray('int', [Code01_RadixSort.BASE])
Code01_RadixSort.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_RadixSort.main([])
