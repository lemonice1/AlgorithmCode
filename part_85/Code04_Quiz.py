# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 知识竞赛
# 最近部门要选两个员工去参加一个需要合作的知识竞赛，
# 每个员工均有一个推理能力值ai，以及一个阅读能力值bi
# 如果选择第i个人和第j个人去参加竞赛，
# 两人在推理方面的能力为X = (ai + aj)/2
# 两人在阅读方面的能力为Y = (bi + bj)/2
# 现在需要最大化他们表现较差一方面的能力
# 即让min(X,Y) 尽可能大，问这个值最大是多少
# 测试链接 : https://www.nowcoder.com/practice/2a9089ea7e5b474fa8f688eae76bc050
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Quiz:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'n': 'n'}
    MAXN = 0
    nums = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code04_Quiz.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code04_Quiz.n):
                jcall(in_, 'nextToken')
                jset(Code04_Quiz.nums[i], 0, jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jset(Code04_Quiz.nums[i], 1, jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            ans = jcast('int', Code04_Quiz.compute())
            jcall(out, 'println', jdiv(jcast('double', ans), 2))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code04_Quiz.nums, 0, Code04_Quiz.n, (lambda a, b: jcast('int', (jstatic('Math', 'abs', (a[0] - a[1])) - jstatic('Math', 'abs', (b[0] - b[1]))))))
        # 左边最大的推理能力
        maxA = jcast('int', Code04_Quiz.nums[0][0])
        # 左边最大的阅读能力
        maxB = jcast('int', Code04_Quiz.nums[0][1])
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i < Code04_Quiz.n):
            if (Code04_Quiz.nums[i][0] <= Code04_Quiz.nums[i][1]):
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(maxA, Code04_Quiz.nums[i][0]))))
            else:
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(maxB, Code04_Quiz.nums[i][1]))))
            maxA = jcast('int', jstatic('Math', 'max', maxA, Code04_Quiz.nums[i][0]))
            maxB = jcast('int', jstatic('Math', 'max', maxB, Code04_Quiz.nums[i][1]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Quiz.MAXN = jcast('int', 200001)
Code04_Quiz.nums = jarray('int', [Code04_Quiz.MAXN, 2])
Code04_Quiz.n = jcast('int', 0)

if __name__ == '__main__':
    Code04_Quiz.main([])
