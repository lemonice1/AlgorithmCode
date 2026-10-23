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

# 拓扑排序模版（牛客）
# 邻接表建图（动态方式）
# 测试链接 : https://www.nowcoder.com/practice/88f7e156ca7d43a1a535f619cd3f495c
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_TopoSortDynamicNowcoder:
    __java_fields__ = {'MAXN': 'MAXN', 'queue': 'queue', 'l': 'l', 'r': 'r', 'indegree': 'indegree', 'ans': 'ans', 'n': 'n', 'm': 'm'}
    MAXN = 0
    # 拓扑排序，用到队列
    queue = None
    l = 0
    r = 0
    # 拓扑排序，入度表
    indegree = None
    # 收集拓扑排序的结果
    ans = None
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_TopoSortDynamicNowcoder.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_TopoSortDynamicNowcoder.m = jcast('int', jcast('int', jget(in_, 'nval')))
            # 动态建图，比赛肯定不行，但是一般大厂笔试、面试允许
            graph = jnew('ArrayList')
            i = jcast('int', 0)
            while (i <= Code02_TopoSortDynamicNowcoder.n):
                jcall(graph, 'add', jnew('ArrayList'))
                i = jcast('int', (i + 1))
            jstatic('Arrays', 'fill', Code02_TopoSortDynamicNowcoder.indegree, 0, jcast('int', jadd(Code02_TopoSortDynamicNowcoder.n, 1)), 0)
            i = jcast('int', 0)
            from_ = 0
            to = 0
            while (i < Code02_TopoSortDynamicNowcoder.m):
                jcall(in_, 'nextToken')
                from_ = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                to = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(jcall(graph, 'get', from_), 'add', to)
                Code02_TopoSortDynamicNowcoder.indegree[to] = jcast('int', (Code02_TopoSortDynamicNowcoder.indegree[to] + 1))
                i = jcast('int', (i + 1))
            if (not Code02_TopoSortDynamicNowcoder.topoSort(graph)):
                jcall(out, 'println', jcast('int', (-1)))
            else:
                i = jcast('int', 0)
                while (i < jcast('int', (Code02_TopoSortDynamicNowcoder.n - 1))):
                    jcall(out, 'print', jadd(Code02_TopoSortDynamicNowcoder.ans[i], ' '))
                    i = jcast('int', (i + 1))
                jcall(out, 'println', Code02_TopoSortDynamicNowcoder.ans[jcast('int', (Code02_TopoSortDynamicNowcoder.n - 1))])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 有拓扑排序返回true
    # 没有拓扑排序返回false
    @staticmethod
    def topoSort(graph):
        Code02_TopoSortDynamicNowcoder.l = jcast('int', jset(Code02_TopoSortDynamicNowcoder, 'r', 0))
        i = jcast('int', 1)
        while (i <= Code02_TopoSortDynamicNowcoder.n):
            if (Code02_TopoSortDynamicNowcoder.indegree[i] == 0):
                jset(Code02_TopoSortDynamicNowcoder.queue, ((_java_obj_1 := Code02_TopoSortDynamicNowcoder), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], i)
            i = jcast('int', (i + 1))
        fill = jcast('int', 0)
        while (Code02_TopoSortDynamicNowcoder.l < Code02_TopoSortDynamicNowcoder.r):
            cur = jcast('int', Code02_TopoSortDynamicNowcoder.queue[((_java_obj_4 := Code02_TopoSortDynamicNowcoder), (_java_key_5 := 'l'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])
            jset(Code02_TopoSortDynamicNowcoder.ans, ((_java_old_7 := fill), (fill := jcast('int', (fill + (1)))), _java_old_7)[2], cur)
            for next in jcall(graph, 'get', cur):
                if (((_java_obj_8 := Code02_TopoSortDynamicNowcoder.indegree), (_java_key_9 := next), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))))[3] == 0):
                    jset(Code02_TopoSortDynamicNowcoder.queue, ((_java_obj_11 := Code02_TopoSortDynamicNowcoder), (_java_key_12 := 'r'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4], next)
        return jcast('boolean', (fill == Code02_TopoSortDynamicNowcoder.n))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_TopoSortDynamicNowcoder.MAXN = jcast('int', 200001)
Code02_TopoSortDynamicNowcoder.queue = jarray('int', [Code02_TopoSortDynamicNowcoder.MAXN])
Code02_TopoSortDynamicNowcoder.l = jcast('int', 0)
Code02_TopoSortDynamicNowcoder.r = jcast('int', 0)
Code02_TopoSortDynamicNowcoder.indegree = jarray('int', [Code02_TopoSortDynamicNowcoder.MAXN])
Code02_TopoSortDynamicNowcoder.ans = jarray('int', [Code02_TopoSortDynamicNowcoder.MAXN])
Code02_TopoSortDynamicNowcoder.n = jcast('int', 0)
Code02_TopoSortDynamicNowcoder.m = jcast('int', 0)

if __name__ == '__main__':
    Code02_TopoSortDynamicNowcoder.main([])
