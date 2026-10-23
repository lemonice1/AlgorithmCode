# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 约瑟夫环问题加强
# 一共有1~n这些点，组成首尾相接的环，游戏一共有n-1轮，每轮给定一个数字arr[i]
# 第一轮游戏中，1号点从数字1开始报数，哪个节点报到数字arr[1]，就删除该节点
# 然后下一个节点从数字1开始重新报数，游戏进入第二轮
# 第i轮游戏中，哪个节点报到数字arr[i]，就删除该节点
# 然后下一个节点从数字1开始重新报数，游戏进入第i+1轮
# 最终环上会剩下一个节点, 返回该节点的编号
# 1 <= n, arr[i] <= 10^6
# 来自真实大厂笔试，对数器验证
class Code04_JosephFollowUp:
    __java_fields__ = {}
    # 暴力模拟
    # 为了测试
    @staticmethod
    def joseph1(n, arr):
        n = jcast('int', n)
        if (n == 1):
            return jcast('int', 1)
        next = jarray('int', [jcast('int', jadd(n, 1))])
        i = jcast('int', 1)
        while (i < n):
            next[i] = jcast('int', jcast('int', jadd(i, 1)))
            i = jcast('int', (i + 1))
        next[n] = jcast('int', 1)
        pre = jcast('int', n)
        cur = jcast('int', 1)
        i = jcast('int', 1)
        while (i < n):
            cnt = jcast('int', 1)
            while (cnt < arr[i]):
                pre = jcast('int', cur)
                cur = jcast('int', next[cur])
                cnt = jcast('int', (cnt + 1))
            next[pre] = jcast('int', next[cur])
            cur = jcast('int', next[cur])
            i = jcast('int', (i + 1))
        return jcast('int', cur)

    # 正式方法
    # 时间复杂度O(n)
    @staticmethod
    def joseph2(n, arr):
        n = jcast('int', n)
        if (n == 1):
            return jcast('int', 1)
        ans = jcast('int', 1)
        c = jcast('int', 2)
        i = jcast('int', jcast('int', (n - 1)))
        while (c <= n):
            ans = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', (jcast('int', jadd(ans, arr[i])) - 1)), c)), 1)))
            c = jcast('int', (c + 1))
            i = jcast('int', (i - 1))
        return jcast('int', ans)

    # 随机生成每轮报数
    # 为了测试
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        arr = jarray('int', [n])
        i = jcast('int', 1)
        while (i < n):
            jset(arr, i, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            i = jcast('int', (i + 1))
        return arr

    # 对数器
    # 为了测试
    @staticmethod
    def main(args):
        N = jcast('int', 100)
        V = jcast('int', 500)
        test = jcast('int', 10000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= test):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            arr = Code04_JosephFollowUp.randomArray(n, V)
            ans1 = jcast('int', Code04_JosephFollowUp.joseph1(n, arr))
            ans2 = jcast('int', Code04_JosephFollowUp.joseph2(n, arr))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code04_JosephFollowUp.main([])
