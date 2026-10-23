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

# 同学找到了洛谷的在线测试，看似是题目3，其实不是
# 区别在于数据量，如下测试链接中的题目
# 会议的数量10^6，会议的开始、结束时间也是10^6
# 排序步骤的实际开销取决于数据规模与 Python 实现，应结合算法复杂度评估
# 而且根据这个数据量，最优解一定不是排序！
# 会议开始、结束时间也是10^6规模，所以不排序也可以做，具体看如下代码和注释
# 并不是课上讲错了，而是这个数据状况太特殊
# 测试链接 : https://www.luogu.com.cn/problem/P1803
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_MeetingMonopoly2:
    __java_fields__ = {'MAXN': 'MAXN', 'latest': 'latest', 'n': 'n'}
    # 既是会议的规模，也是开始、结束时间的规模
    MAXN = 0
    # latest[60] == 40
    # 表示 : 结束时间是60的所有会议中，最晚开始的会议是40的时候开始
    # 比如会议[1, 60]、[30, 60]、[40, 60]
    # 这些会议都在60结束，但是最晚开始的会议是40开始
    # 如果latest[60] == -1
    # 表示没有任何会议在60结束
    latest = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_MeetingMonopoly2.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code03_MeetingMonopoly2.MAXN):
                Code03_MeetingMonopoly2.latest[i] = jcast('int', jcast('int', (-1)))
                i = jcast('int', (i + 1))
            i = jcast('int', 0)
            start = 0
            end = 0
            while (i < Code03_MeetingMonopoly2.n):
                jcall(in_, 'nextToken')
                start = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                end = jcast('int', jcast('int', jget(in_, 'nval')))
                if (Code03_MeetingMonopoly2.latest[end] == jcast('int', (-1))):
                    # 如果结束时间在end的会议之前没发现过
                    # 现在发现了
                    Code03_MeetingMonopoly2.latest[end] = jcast('int', start)
                else:
                    # 如果结束时间在end的会议之前发现过
                    # 记录最晚的开始时间
                    jset(Code03_MeetingMonopoly2.latest, end, jstatic('Math', 'max', Code03_MeetingMonopoly2.latest[end], start))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_MeetingMonopoly2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        ans = jcast('int', 0)
        # 不排序
        # 根据时间遍历
        cur = jcast('int', 0)
        end = jcast('int', 0)
        while (end < Code03_MeetingMonopoly2.MAXN):
            # cur : cur之前不能再安排会议，因为安排会议的人来到了cur时刻
            # end是当前的结束时间
            # 所有以end结束的会议，最晚的开始时间是latest[end]
            # 如果cur <= latest[end]，那么说明可以安排当前以end结束的会议
            if (cur <= Code03_MeetingMonopoly2.latest[end]):
                ans = jcast('int', (ans + 1))
                # 安排之后，目前安排会议的人来到end时刻
                cur = jcast('int', end)
            end = jcast('int', (end + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MeetingMonopoly2.MAXN = jcast('int', 1000001)
Code03_MeetingMonopoly2.latest = jarray('int', [Code03_MeetingMonopoly2.MAXN])
Code03_MeetingMonopoly2.n = jcast('int', 0)

if __name__ == '__main__':
    Code03_MeetingMonopoly2.main([])
