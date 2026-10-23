# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 返回无序数组中累加和为给定值的最长子数组长度
# 给定一个无序数组arr, 其中元素可正、可负、可0
# 给定一个整数aim
# 求arr所有子数组中累加和为aim的最长子数组长度
# 测试链接 : https://www.nowcoder.com/practice/36fb0fd3c656480c92b569258a1223d5
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_LongestSubarraySumEqualsAim:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'aim': 'aim', 'map': 'map'}
    MAXN = 0
    arr = None
    n = 0
    aim = 0
    # key : 某个前缀和
    # value : 这个前缀和最早出现的位置
    map = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_LongestSubarraySumEqualsAim.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_LongestSubarraySumEqualsAim.aim = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code02_LongestSubarraySumEqualsAim.n):
                jcall(in_, 'nextToken')
                Code02_LongestSubarraySumEqualsAim.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code02_LongestSubarraySumEqualsAim.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        jcall(Code02_LongestSubarraySumEqualsAim.map, 'clear')
        # 重要 : 0这个前缀和，一个数字也没有的时候，就存在了
        jcall(Code02_LongestSubarraySumEqualsAim.map, 'put', 0, jcast('int', (-1)))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        sum = jcast('int', 0)
        while (i < Code02_LongestSubarraySumEqualsAim.n):
            sum = jcast('int', jcast('int', jadd(sum, Code02_LongestSubarraySumEqualsAim.arr[i])))
            if jcall(Code02_LongestSubarraySumEqualsAim.map, 'containsKey', jcast('int', (sum - Code02_LongestSubarraySumEqualsAim.aim))):
                ans = jcast('int', jstatic('Math', 'max', ans, (i - jcall(Code02_LongestSubarraySumEqualsAim.map, 'get', jcast('int', (sum - Code02_LongestSubarraySumEqualsAim.aim))))))
            if (not jcall(Code02_LongestSubarraySumEqualsAim.map, 'containsKey', sum)):
                jcall(Code02_LongestSubarraySumEqualsAim.map, 'put', sum, i)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_LongestSubarraySumEqualsAim.MAXN = jcast('int', 100001)
Code02_LongestSubarraySumEqualsAim.arr = jarray('int', [Code02_LongestSubarraySumEqualsAim.MAXN])
Code02_LongestSubarraySumEqualsAim.n = jcast('int', 0)
Code02_LongestSubarraySumEqualsAim.aim = jcast('int', 0)
Code02_LongestSubarraySumEqualsAim.map = jnew('HashMap')

if __name__ == '__main__':
    Code02_LongestSubarraySumEqualsAim.main([])
