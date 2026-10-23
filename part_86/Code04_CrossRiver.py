# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 过河问题
# 一共n人出游，他们走到一条河的西岸，想要过河到东岸
# 每个人都有一个渡河时间ti，西岸有一条船，一次最多乘坐两人
# 如果船上有一个人，划到对岸的时间，等于这个人的渡河时间
# 如果船上有两个人，划到对岸的时间，等于两个人的渡河时间的最大值
# 返回最少要花费多少时间，才能使所有人都过河
# 测试链接 : https://www.luogu.com.cn/problem/P1809
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_CrossRiver:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'dp': 'dp', 'n': 'n'}
    MAXN = 0
    nums = None
    dp = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code04_CrossRiver.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code04_CrossRiver.n):
                jcall(in_, 'nextToken')
                Code04_CrossRiver.nums[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_CrossRiver.minCost())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def minCost():
        jstatic('Arrays', 'sort', Code04_CrossRiver.nums, 0, Code04_CrossRiver.n)
        if (Code04_CrossRiver.n >= 1):
            Code04_CrossRiver.dp[0] = jcast('int', Code04_CrossRiver.nums[0])
        if (Code04_CrossRiver.n >= 2):
            Code04_CrossRiver.dp[1] = jcast('int', Code04_CrossRiver.nums[1])
        if (Code04_CrossRiver.n >= 3):
            Code04_CrossRiver.dp[2] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code04_CrossRiver.nums[0], Code04_CrossRiver.nums[1])), Code04_CrossRiver.nums[2])))
        i = jcast('int', 3)
        while (i < Code04_CrossRiver.n):
            jset(Code04_CrossRiver.dp, i, jstatic('Math', 'min', jcast('int', jadd(jcast('int', jadd(Code04_CrossRiver.dp[jcast('int', (i - 1))], Code04_CrossRiver.nums[i])), Code04_CrossRiver.nums[0])), jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(Code04_CrossRiver.dp[jcast('int', (i - 2))], Code04_CrossRiver.nums[1])), Code04_CrossRiver.nums[1])), Code04_CrossRiver.nums[i])), Code04_CrossRiver.nums[0]))))
            i = jcast('int', (i + 1))
        return jcast('int', Code04_CrossRiver.dp[jcast('int', (Code04_CrossRiver.n - 1))])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_CrossRiver.MAXN = jcast('int', 100001)
Code04_CrossRiver.nums = jarray('int', [Code04_CrossRiver.MAXN])
Code04_CrossRiver.dp = jarray('int', [Code04_CrossRiver.MAXN])
Code04_CrossRiver.n = jcast('int', 0)

if __name__ == '__main__':
    Code04_CrossRiver.main([])
