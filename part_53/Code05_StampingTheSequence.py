# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 戳印序列
# 你想最终得到"abcbc"，认为初始序列为"?????"。印章是"abc"
# 那么可以先用印章盖出"??abc"的状态，
# 然后用印章最左字符和序列的0位置对齐，就盖出了"abcbc"
# 这个过程中，"??abc"中的a字符，被印章中的c字符覆盖了
# 每次盖章的时候，印章必须完全盖在序列内
# 给定一个字符串target是最终的目标，长度为n，认为初始序列为n个'?'
# 给定一个印章字符串stamp，目标是最终盖出target
# 但是印章的使用次数必须在10*n次以内
# 返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成
# 上面的例子返回[2,0]，表示印章最左字符依次和序列2位置、序列0位置对齐盖下去，就得到了target
# 如果不能在10*n次内印出序列，就返回一个空数组
# 测试链接 : https://leetcode.cn/problems/stamping-the-sequence/
class Code05_StampingTheSequence:
    __java_fields__ = {}
    @staticmethod
    def movesToStamp(stamp, target):
        s = jcall(stamp, 'toCharArray')
        t = jcall(target, 'toCharArray')
        m = jcast('int', jget(s, 'length'))
        n = jcast('int', jget(t, 'length'))
        indegree = jarray('int', [jcast('int', jadd(jcast('int', (n - m)), 1))])
        jstatic('Arrays', 'fill', indegree, m)
        graph = jnew('ArrayList')
        i = jcast('int', 0)
        while (i < n):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        queue = jarray('int', [jcast('int', jadd(jcast('int', (n - m)), 1))])
        l = jcast('int', 0)
        r = jcast('int', 0)
        # O(n*m)
        i = jcast('int', 0)
        while (i <= jcast('int', (n - m))):
            # i开头....(m个)
            # i+0 i+1 i+m-1
            j = jcast('int', 0)
            while (j < m):
                if (t[jcast('int', jadd(i, j))] == s[j]):
                    if (((_java_obj_1 := indegree), (_java_key_2 := i), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3] == 0):
                        jset(queue, ((_java_old_4 := r), (r := jcast('int', (r + (1)))), _java_old_4)[2], i)
                else:
                    # i + j
                    # from : 错误的位置
                    # to : i开头的下标
                    jcall(jcall(graph, 'get', jcast('int', jadd(i, j))), 'add', i)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        # 同一个位置取消错误不要重复统计
        visited = jarray('boolean', [n])
        path = jarray('int', [jcast('int', jadd(jcast('int', (n - m)), 1))])
        size = jcast('int', 0)
        while (l < r):
            cur = jcast('int', queue[((_java_old_5 := l), (l := jcast('int', (l + (1)))), _java_old_5)[2]])
            jset(path, ((_java_old_6 := size), (size := jcast('int', (size + (1)))), _java_old_6)[2], cur)
            i = jcast('int', 0)
            while (i < m):
                # cur : 开头位置
                # cur + 0 cur + 1 cur + 2 ... cur + m - 1
                if (not visited[jcast('int', jadd(cur, i))]):
                    visited[jcast('int', jadd(cur, i))] = jcast('boolean', True)
                    for next in jcall(graph, 'get', jcast('int', jadd(cur, i))):
                        if (((_java_obj_7 := indegree), (_java_key_8 := next), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3] == 0):
                            jset(queue, ((_java_old_10 := r), (r := jcast('int', (r + (1)))), _java_old_10)[2], next)
                i = jcast('int', (i + 1))
        if (size != jcast('int', jadd(jcast('int', (n - m)), 1))):
            return jarray('int', [0])
        # path逆序调整
        i = jcast('int', 0)
        j = jcast('int', jcast('int', (size - 1)))
        while (i < j):
            tmp = jcast('int', path[i])
            path[i] = jcast('int', path[j])
            path[j] = jcast('int', tmp)
            i = jcast('int', (i + 1))
            j = jcast('int', (j - 1))
        return path

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


