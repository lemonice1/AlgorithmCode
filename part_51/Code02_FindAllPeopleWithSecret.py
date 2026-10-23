# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 找出知晓秘密的所有专家
# 给你一个整数 n ，表示有 n 个专家从 0 到 n - 1 编号
# 另外给你一个下标从 0 开始的二维整数数组 meetings
# 其中 meetings[i] = [xi, yi, timei] 表示专家 xi 和专家 yi 在时间 timei 要开一场会
# 一个专家可以同时参加 多场会议 。最后，给你一个整数 firstPerson
# 专家 0 有一个 秘密 ，最初，他在时间 0 将这个秘密分享给了专家 firstPerson
# 接着，这个秘密会在每次有知晓这个秘密的专家参加会议时进行传播
# 更正式的表达是，每次会议，如果专家 xi 在时间 timei 时知晓这个秘密
# 那么他将会与专家 yi 分享这个秘密，反之亦然。秘密共享是 瞬时发生 的
# 也就是说，在同一时间，一个专家不光可以接收到秘密，还能在其他会议上与其他专家分享
# 在所有会议都结束之后，返回所有知晓这个秘密的专家列表
# 你可以按 任何顺序 返回答案
# 链接测试 : https://leetcode.cn/problems/find-all-people-with-secret/
class Code02_FindAllPeopleWithSecret:
    __java_fields__ = {'MAXN': 'MAXN', 'father': 'father', 'secret': 'secret'}
    MAXN = 0
    father = None
    # 集合的标签信息 : 设置集合的一些属性
    # 属性在哪？secret[代表元素] 代表集合的属性
    secret = None
    @staticmethod
    def build(n, first):
        n = jcast('int', n)
        first = jcast('int', first)
        i = jcast('int', 0)
        while (i < n):
            Code02_FindAllPeopleWithSecret.father[i] = jcast('int', i)
            Code02_FindAllPeopleWithSecret.secret[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        Code02_FindAllPeopleWithSecret.father[first] = jcast('int', 0)
        Code02_FindAllPeopleWithSecret.secret[0] = jcast('boolean', True)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code02_FindAllPeopleWithSecret.father[i]):
            jset(Code02_FindAllPeopleWithSecret.father, i, Code02_FindAllPeopleWithSecret.find(Code02_FindAllPeopleWithSecret.father[i]))
        return jcast('int', Code02_FindAllPeopleWithSecret.father[i])

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code02_FindAllPeopleWithSecret.find(x))
        fy = jcast('int', Code02_FindAllPeopleWithSecret.find(y))
        if (fx != fy):
            Code02_FindAllPeopleWithSecret.father[fx] = jcast('int', fy)
            Code02_FindAllPeopleWithSecret.secret[fy] = jcast('boolean', (Code02_FindAllPeopleWithSecret.secret[fy] | Code02_FindAllPeopleWithSecret.secret[fx]))

    # 会议排序 : m * log m
    # 处理过程 : O(m)
    # 收集答案 : O(n)
    @staticmethod
    def findAllPeople(n, meetings, first):
        n = jcast('int', n)
        first = jcast('int', first)
        Code02_FindAllPeopleWithSecret.build(n, first)
        # {0 : 专家   1 : 专家编号   2 : 时刻}
        jstatic('Arrays', 'sort', meetings, (lambda a, b: (a[2] - b[2])))
        m = jcast('int', jget(meetings, 'length'))
        l = jcast('int', 0)
        r = 0
        while (l < m):
            r = jcast('int', l)
            while ((jcast('int', jadd(r, 1)) < m) and (meetings[l][2] == meetings[jcast('int', jadd(r, 1))][2])):
                r = jcast('int', (r + 1))
            # l....r这些会议，一定是一个时刻
            i = jcast('int', l)
            while (i <= r):
                Code02_FindAllPeopleWithSecret.union(meetings[i][0], meetings[i][1])
                i = jcast('int', (i + 1))
            # 有小的撤销行为，但这不是可撤销并查集
            # 只是每一批没有知道秘密的专家重新建立集合而已
            i = jcast('int', l)
            a = 0
            b = 0
            while (i <= r):
                a = jcast('int', meetings[i][0])
                b = jcast('int', meetings[i][1])
                if (not Code02_FindAllPeopleWithSecret.secret[Code02_FindAllPeopleWithSecret.find(a)]):
                    Code02_FindAllPeopleWithSecret.father[a] = jcast('int', a)
                if (not Code02_FindAllPeopleWithSecret.secret[Code02_FindAllPeopleWithSecret.find(b)]):
                    Code02_FindAllPeopleWithSecret.father[b] = jcast('int', b)
                i = jcast('int', (i + 1))
            l = jcast('int', jcast('int', jadd(r, 1)))
        ans = jnew('ArrayList')
        i = jcast('int', 0)
        while (i < n):
            if Code02_FindAllPeopleWithSecret.secret[Code02_FindAllPeopleWithSecret.find(i)]:
                jcall(ans, 'add', i)
            i = jcast('int', (i + 1))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_FindAllPeopleWithSecret.MAXN = jcast('int', 100001)
Code02_FindAllPeopleWithSecret.father = jarray('int', [Code02_FindAllPeopleWithSecret.MAXN])
Code02_FindAllPeopleWithSecret.secret = jarray('boolean', [Code02_FindAllPeopleWithSecret.MAXN])
