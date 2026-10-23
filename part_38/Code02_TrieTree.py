# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 用固定数组实现前缀树，空间使用是静态的。推荐！
# 测试链接 : https://www.nowcoder.com/practice/7f8a8553ddbf4eaab749ec988726702b
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_TrieTree:
    __java_fields__ = {'MAXN': 'MAXN', 'tree': 'tree', 'end': 'end', 'pass': 'pass_', 'cnt': 'cnt', 'm': 'm', 'op': 'op', 'splits': 'splits'}
    # 如果将来增加了数据量，就改大这个值
    MAXN = 0
    tree = None
    end = None
    pass_ = None
    cnt = 0
    @staticmethod
    def build():
        Code02_TrieTree.cnt = jcast('int', 1)

    @staticmethod
    def insert(word):
        cur = jcast('int', 1)
        Code02_TrieTree.pass_[cur] = jcast('int', (Code02_TrieTree.pass_[cur] + 1))
        i = jcast('int', 0)
        path = 0
        while (i < jcall(word, 'length')):
            path = jcast('int', jcast('int', (jcall(word, 'charAt', i) - jchar('a'))))
            if (Code02_TrieTree.tree[cur][path] == 0):
                jset(Code02_TrieTree.tree[cur], path, ((_java_obj_1 := Code02_TrieTree), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
            cur = jcast('int', Code02_TrieTree.tree[cur][path])
            Code02_TrieTree.pass_[cur] = jcast('int', (Code02_TrieTree.pass_[cur] + 1))
            i = jcast('int', (i + 1))
        Code02_TrieTree.end[cur] = jcast('int', (Code02_TrieTree.end[cur] + 1))

    @staticmethod
    def search(word):
        cur = jcast('int', 1)
        i = jcast('int', 0)
        path = 0
        while (i < jcall(word, 'length')):
            path = jcast('int', jcast('int', (jcall(word, 'charAt', i) - jchar('a'))))
            if (Code02_TrieTree.tree[cur][path] == 0):
                return jcast('int', 0)
            cur = jcast('int', Code02_TrieTree.tree[cur][path])
            i = jcast('int', (i + 1))
        return jcast('int', Code02_TrieTree.end[cur])

    @staticmethod
    def prefixNumber(pre):
        cur = jcast('int', 1)
        i = jcast('int', 0)
        path = 0
        while (i < jcall(pre, 'length')):
            path = jcast('int', jcast('int', (jcall(pre, 'charAt', i) - jchar('a'))))
            if (Code02_TrieTree.tree[cur][path] == 0):
                return jcast('int', 0)
            cur = jcast('int', Code02_TrieTree.tree[cur][path])
            i = jcast('int', (i + 1))
        return jcast('int', Code02_TrieTree.pass_[cur])

    @staticmethod
    def delete(word):
        if (Code02_TrieTree.search(word) > 0):
            cur = jcast('int', 1)
            # 下面这一行代码，讲课的时候没加
            # 本题不会用到pass[1]的信息，所以加不加都可以，不过正确的写法是加上
            Code02_TrieTree.pass_[cur] = jcast('int', (Code02_TrieTree.pass_[cur] - 1))
            i = jcast('int', 0)
            path = 0
            while (i < jcall(word, 'length')):
                path = jcast('int', jcast('int', (jcall(word, 'charAt', i) - jchar('a'))))
                if (((_java_obj_4 := Code02_TrieTree.pass_), (_java_key_5 := Code02_TrieTree.tree[cur][path]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3] == 0):
                    jset(Code02_TrieTree.tree[cur], path, 0)
                    return
                cur = jcast('int', Code02_TrieTree.tree[cur][path])
                i = jcast('int', (i + 1))
            Code02_TrieTree.end[cur] = jcast('int', (Code02_TrieTree.end[cur] - 1))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code02_TrieTree.cnt):
            jstatic('Arrays', 'fill', Code02_TrieTree.tree[i], 0)
            Code02_TrieTree.end[i] = jcast('int', 0)
            Code02_TrieTree.pass_[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    m = 0
    op = 0
    splits = None
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        line = None
        while ((line := jcall(in_, 'readLine')) != None):
            Code02_TrieTree.build()
            Code02_TrieTree.m = jcast('int', jstatic('Integer', 'valueOf', line))
            i = jcast('int', 1)
            while (i <= Code02_TrieTree.m):
                Code02_TrieTree.splits = jcall(jcall(in_, 'readLine'), 'split', ' ')
                Code02_TrieTree.op = jcast('int', jstatic('Integer', 'valueOf', Code02_TrieTree.splits[0]))
                if (Code02_TrieTree.op == 1):
                    Code02_TrieTree.insert(Code02_TrieTree.splits[1])
                else:
                    if (Code02_TrieTree.op == 2):
                        Code02_TrieTree.delete(Code02_TrieTree.splits[1])
                    else:
                        if (Code02_TrieTree.op == 3):
                            jcall(out, 'println', ('YES' if (Code02_TrieTree.search(Code02_TrieTree.splits[1]) > 0) else 'NO'))
                        else:
                            if (Code02_TrieTree.op == 4):
                                jcall(out, 'println', Code02_TrieTree.prefixNumber(Code02_TrieTree.splits[1]))
                i = jcast('int', (i + 1))
            Code02_TrieTree.clear()
        jcall(out, 'flush')
        jcall(in_, 'close')
        jcall(out, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_TrieTree.MAXN = jcast('int', 150001)
Code02_TrieTree.tree = jarray('int', [Code02_TrieTree.MAXN, 26])
Code02_TrieTree.end = jarray('int', [Code02_TrieTree.MAXN])
Code02_TrieTree.pass_ = jarray('int', [Code02_TrieTree.MAXN])
Code02_TrieTree.cnt = jcast('int', 0)
Code02_TrieTree.m = jcast('int', 0)
Code02_TrieTree.op = jcast('int', 0)
Code02_TrieTree.splits = None

if __name__ == '__main__':
    Code02_TrieTree.main([])
