# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大食物链计数
# a -> b，代表a在食物链中被b捕食
# 给定一个有向无环图，返回
# 这个图中从最初级动物到最顶级捕食者的食物链有几条
# 测试链接 : https://www.luogu.com.cn/problem/P4017
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_FoodLines:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MOD': 'MOD', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'queue': 'queue', 'indegree': 'indegree', 'lines': 'lines', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    MOD = 0
    # 链式前向星建图
    head = None
    next = None
    to = None
    cnt = 0
    # 拓扑排序需要的队列
    queue = None
    # 拓扑排序需要的入度表
    indegree = None
    # 拓扑排序需要的推送信息
    lines = None
    n = 0
    m = 0
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code01_FoodLines.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code01_FoodLines.indegree, 0, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code01_FoodLines.lines, 0, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code01_FoodLines.head, 0, jcast('int', jadd(n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code01_FoodLines.next[Code01_FoodLines.cnt] = jcast('int', Code01_FoodLines.head[u])
        Code01_FoodLines.to[Code01_FoodLines.cnt] = jcast('int', v)
        jset(Code01_FoodLines.head, u, ((_java_obj_1 := Code01_FoodLines), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code01_FoodLines.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_FoodLines.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_FoodLines.build(Code01_FoodLines.n)
            i = jcast('int', 0)
            u = 0
            v = 0
            while (i < Code01_FoodLines.m):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                Code01_FoodLines.addEdge(u, v)
                Code01_FoodLines.indegree[v] = jcast('int', (Code01_FoodLines.indegree[v] + 1))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code01_FoodLines.ways())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def ways():
        l = jcast('int', 0)
        r = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_FoodLines.n):
            if (Code01_FoodLines.indegree[i] == 0):
                jset(Code01_FoodLines.queue, ((_java_old_4 := r), (r := jcast('int', (r + (1)))), _java_old_4)[2], i)
                Code01_FoodLines.lines[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        while (l < r):
            u = jcast('int', Code01_FoodLines.queue[((_java_old_5 := l), (l := jcast('int', (l + (1)))), _java_old_5)[2]])
            if (Code01_FoodLines.head[u] == 0):
                # 当前的u节点不再有后续邻居了
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code01_FoodLines.lines[u])), Code01_FoodLines.MOD)))
            else:
                ei = jcast('int', Code01_FoodLines.head[u])
                v = 0
                while (ei > 0):
                    # u -> v
                    v = jcast('int', Code01_FoodLines.to[ei])
                    Code01_FoodLines.lines[v] = jcast('int', jcast('int', jmod(jcast('int', jadd(Code01_FoodLines.lines[v], Code01_FoodLines.lines[u])), Code01_FoodLines.MOD)))
                    if (((_java_obj_6 := Code01_FoodLines.indegree), (_java_key_7 := v), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (-1)))))[3] == 0):
                        jset(Code01_FoodLines.queue, ((_java_old_9 := r), (r := jcast('int', (r + (1)))), _java_old_9)[2], v)
                    ei = jcast('int', Code01_FoodLines.next[ei])
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_FoodLines.MAXN = jcast('int', 5001)
Code01_FoodLines.MAXM = jcast('int', 500001)
Code01_FoodLines.MOD = jcast('int', 80112002)
Code01_FoodLines.head = jarray('int', [Code01_FoodLines.MAXN])
Code01_FoodLines.next = jarray('int', [Code01_FoodLines.MAXM])
Code01_FoodLines.to = jarray('int', [Code01_FoodLines.MAXM])
Code01_FoodLines.cnt = jcast('int', 0)
Code01_FoodLines.queue = jarray('int', [Code01_FoodLines.MAXN])
Code01_FoodLines.indegree = jarray('int', [Code01_FoodLines.MAXN])
Code01_FoodLines.lines = jarray('int', [Code01_FoodLines.MAXN])
Code01_FoodLines.n = jcast('int', 0)
Code01_FoodLines.m = jcast('int', 0)

if __name__ == '__main__':
    Code01_FoodLines.main([])
