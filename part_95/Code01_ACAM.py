# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# AC自动机模版(优化版)
# 给你若干目标字符串，还有一篇文章
# 返回每个目标字符串在文章中出现了几次
# 测试链接 : https://www.luogu.com.cn/problem/P5357
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_ACAM:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXS': 'MAXS', 'end': 'end', 'tree': 'tree', 'fail': 'fail', 'cnt': 'cnt', 'times': 'times', 'box': 'box', 'head': 'head', 'next': 'next', 'to': 'to', 'edge': 'edge', 'visited': 'visited'}
    # 目标字符串的数量
    MAXN = 0
    # 所有目标字符串的总字符数量
    MAXS = 0
    # 记录每个目标串的结尾节点编号
    end = None
    # AC自动机
    tree = None
    fail = None
    cnt = 0
    # 具体题目相关，本题为收集词频
    # 所以每个节点记录词频
    times = None
    # 可以用作队列或者栈，一个容器而已
    box = None
    # 链式前向星，为了建立fail指针的反图
    head = None
    next = None
    to = None
    edge = 0
    # 遍历fail反图，递归方法会爆栈，所以用非递归替代
    visited = None
    # AC自动机加入目标字符串
    @staticmethod
    def insert(i, str):
        i = jcast('int', i)
        s = jcall(str, 'toCharArray')
        u = jcast('int', 0)
        j = jcast('int', 0)
        c = 0
        while (j < jget(s, 'length')):
            c = jcast('int', jcast('int', (s[j] - jchar('a'))))
            if (Code01_ACAM.tree[u][c] == 0):
                jset(Code01_ACAM.tree[u], c, ((_java_obj_1 := Code01_ACAM), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
            u = jcast('int', Code01_ACAM.tree[u][c])
            j = jcast('int', (j + 1))
        # 每个目标字符串的结尾节点编号
        Code01_ACAM.end[i] = jcast('int', u)

    # 加入所有目标字符串之后
    # 设置fail指针 以及 设置直接直通表
    # 做了AC自动机固定的优化
    @staticmethod
    def setFail():
        # box当做队列来使用
        l = jcast('int', 0)
        r = jcast('int', 0)
        i = jcast('int', 0)
        while (i <= 25):
            if (Code01_ACAM.tree[0][i] > 0):
                jset(Code01_ACAM.box, ((_java_old_4 := r), (r := jcast('int', (r + (1)))), _java_old_4)[2], Code01_ACAM.tree[0][i])
            i = jcast('int', (i + 1))
        while (l < r):
            u = jcast('int', Code01_ACAM.box[((_java_old_5 := l), (l := jcast('int', (l + (1)))), _java_old_5)[2]])
            i = jcast('int', 0)
            while (i <= 25):
                if (Code01_ACAM.tree[u][i] == 0):
                    jset(Code01_ACAM.tree[u], i, Code01_ACAM.tree[Code01_ACAM.fail[u]][i])
                else:
                    jset(Code01_ACAM.fail, Code01_ACAM.tree[u][i], Code01_ACAM.tree[Code01_ACAM.fail[u]][i])
                    jset(Code01_ACAM.box, ((_java_old_6 := r), (r := jcast('int', (r + (1)))), _java_old_6)[2], Code01_ACAM.tree[u][i])
                i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        n = jcast('int', jstatic('Integer', 'valueOf', jcall(in_, 'readLine')))
        # AC自动机建树
        i = jcast('int', 1)
        while (i <= n):
            Code01_ACAM.insert(i, jcall(in_, 'readLine'))
            i = jcast('int', (i + 1))
        Code01_ACAM.setFail()
        # 读入大文章
        s = jcall(jcall(in_, 'readLine'), 'toCharArray')
        u = jcast('int', 0)
        i = jcast('int', 0)
        while (i < jget(s, 'length')):
            u = jcast('int', Code01_ACAM.tree[u][jcast('int', (s[i] - jchar('a')))])
            # 增加匹配次数
            Code01_ACAM.times[u] = jcast('int', (Code01_ACAM.times[u] + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_ACAM.cnt):
            # 根据fail指针建反图
            # 其实是一颗树
            Code01_ACAM.addEdge(Code01_ACAM.fail[i], i)
            i = jcast('int', (i + 1))
        # 遍历fail指针建的树
        # 汇总每个节点的词频
        Code01_ACAM.f2(0)
        i = jcast('int', 1)
        while (i <= n):
            jcall(out, 'println', Code01_ACAM.times[Code01_ACAM.end[i]])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_ACAM.next, ((_java_obj_7 := Code01_ACAM), (_java_key_8 := 'edge'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code01_ACAM.head[u])
        Code01_ACAM.head[u] = jcast('int', Code01_ACAM.edge)
        Code01_ACAM.to[Code01_ACAM.edge] = jcast('int', v)

    # 逻辑是对的
    # 但是递归开太多层了会爆栈
    # 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    # 深层递归仍受调用栈与内存约束
    @staticmethod
    def f1(u):
        u = jcast('int', u)
        i = jcast('int', Code01_ACAM.head[u])
        while (i > 0):
            Code01_ACAM.f1(Code01_ACAM.to[i])
            Code01_ACAM.times[u] = jcast('int', jcast('int', jadd(Code01_ACAM.times[u], Code01_ACAM.times[Code01_ACAM.to[i]])))
            i = jcast('int', Code01_ACAM.next[i])

    # 使用非递归写法可避免深层调用栈开销
    # 因为是用栈来模拟递归
    # 只消耗内存空间(box和visited)
    # 不消耗系统栈的空间
    # 所以很安全
    @staticmethod
    def f2(u):
        u = jcast('int', u)
        # box当做栈来使用
        r = jcast('int', 0)
        jset(Code01_ACAM.box, ((_java_old_10 := r), (r := jcast('int', (r + (1)))), _java_old_10)[2], u)
        cur = 0
        while (r > 0):
            cur = jcast('int', Code01_ACAM.box[jcast('int', (r - 1))])
            if (not Code01_ACAM.visited[cur]):
                Code01_ACAM.visited[cur] = jcast('boolean', True)
                i = jcast('int', Code01_ACAM.head[cur])
                while (i > 0):
                    jset(Code01_ACAM.box, ((_java_old_11 := r), (r := jcast('int', (r + (1)))), _java_old_11)[2], Code01_ACAM.to[i])
                    i = jcast('int', Code01_ACAM.next[i])
            else:
                r = jcast('int', (r - 1))
                i = jcast('int', Code01_ACAM.head[cur])
                while (i > 0):
                    Code01_ACAM.times[cur] = jcast('int', jcast('int', jadd(Code01_ACAM.times[cur], Code01_ACAM.times[Code01_ACAM.to[i]])))
                    i = jcast('int', Code01_ACAM.next[i])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_ACAM.MAXN = jcast('int', 200001)
Code01_ACAM.MAXS = jcast('int', 200001)
Code01_ACAM.end = jarray('int', [Code01_ACAM.MAXN])
Code01_ACAM.tree = jarray('int', [Code01_ACAM.MAXS, 26])
Code01_ACAM.fail = jarray('int', [Code01_ACAM.MAXS])
Code01_ACAM.cnt = jcast('int', 0)
Code01_ACAM.times = jarray('int', [Code01_ACAM.MAXS])
Code01_ACAM.box = jarray('int', [Code01_ACAM.MAXS])
Code01_ACAM.head = jarray('int', [Code01_ACAM.MAXS])
Code01_ACAM.next = jarray('int', [Code01_ACAM.MAXS])
Code01_ACAM.to = jarray('int', [Code01_ACAM.MAXS])
Code01_ACAM.edge = jcast('int', 0)
Code01_ACAM.visited = jarray('boolean', [Code01_ACAM.MAXS])

if __name__ == '__main__':
    Code01_ACAM.main([])
