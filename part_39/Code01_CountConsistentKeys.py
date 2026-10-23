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

# 牛牛和他的朋友们约定了一套接头密匙系统，用于确认彼此身份
# 密匙由一组数字序列表示，两个密匙被认为是一致的，如果满足以下条件：
# 密匙 b 的长度不超过密匙 a 的长度。
# 对于任意 0 <= i < length(b)，有b[i+1] - b[i] == a[i+1] - a[i]
# 现在给定了m个密匙 b 的数组，以及n个密匙 a 的数组
# 请你返回一个长度为 m 的结果数组 ans，表示每个密匙b都有多少一致的密匙
# 数组 a 和数组 b 中的元素个数均不超过 10^5
# 1 <= m, n <= 1000
# 测试链接 : https://www.nowcoder.com/practice/c552d3b4dfda49ccb883a6371d9a6932
class Code01_CountConsistentKeys:
    __java_fields__ = {'MAXN': 'MAXN', 'tree': 'tree', 'pass': 'pass_', 'cnt': 'cnt'}
    @staticmethod
    def countConsistentKeys(b, a):
        Code01_CountConsistentKeys.build()
        builder = jnew('StringBuilder')
        # [3,6,50,10] -> "3#44#-40#"
        for nums in a:
            jcall(builder, 'setLength', 0)
            i = jcast('int', 1)
            while (i < jget(nums, 'length')):
                jcall(builder, 'append', jadd(jstatic('String', 'valueOf', jcast('int', (nums[i] - nums[jcast('int', (i - 1))]))), '#'))
                i = jcast('int', (i + 1))
            Code01_CountConsistentKeys.insert(jcall(builder, 'toString'))
        ans = jarray('int', [jget(b, 'length')])
        i = jcast('int', 0)
        while (i < jget(b, 'length')):
            jcall(builder, 'setLength', 0)
            nums = b[i]
            j = jcast('int', 1)
            while (j < jget(nums, 'length')):
                jcall(builder, 'append', jadd(jstatic('String', 'valueOf', jcast('int', (nums[j] - nums[jcast('int', (j - 1))]))), '#'))
                j = jcast('int', (j + 1))
            jset(ans, i, Code01_CountConsistentKeys.count(jcall(builder, 'toString')))
            i = jcast('int', (i + 1))
        Code01_CountConsistentKeys.clear()
        return ans

    # 如果将来增加了数据量，就改大这个值
    MAXN = 0
    tree = None
    pass_ = None
    cnt = 0
    @staticmethod
    def build():
        Code01_CountConsistentKeys.cnt = jcast('int', 1)

    # '0' ~ '9' 10个 0~9
    # '#' 10
    # '-' 11
    @staticmethod
    def path(cha):
        cha = jcast('char', cha)
        if (cha == jchar('#')):
            return jcast('int', 10)
        else:
            if (cha == jchar('-')):
                return jcast('int', 11)
            else:
                return jcast('int', jcast('int', (cha - jchar('0'))))

    @staticmethod
    def insert(word):
        cur = jcast('int', 1)
        Code01_CountConsistentKeys.pass_[cur] = jcast('int', (Code01_CountConsistentKeys.pass_[cur] + 1))
        i = jcast('int', 0)
        path = 0
        while (i < jcall(word, 'length')):
            path = jcast('int', Code01_CountConsistentKeys.path(jcall(word, 'charAt', i)))
            if (Code01_CountConsistentKeys.tree[cur][path] == 0):
                jset(Code01_CountConsistentKeys.tree[cur], path, ((_java_obj_1 := Code01_CountConsistentKeys), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
            cur = jcast('int', Code01_CountConsistentKeys.tree[cur][path])
            Code01_CountConsistentKeys.pass_[cur] = jcast('int', (Code01_CountConsistentKeys.pass_[cur] + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def count(pre):
        cur = jcast('int', 1)
        i = jcast('int', 0)
        path = 0
        while (i < jcall(pre, 'length')):
            path = jcast('int', Code01_CountConsistentKeys.path(jcall(pre, 'charAt', i)))
            if (Code01_CountConsistentKeys.tree[cur][path] == 0):
                return jcast('int', 0)
            cur = jcast('int', Code01_CountConsistentKeys.tree[cur][path])
            i = jcast('int', (i + 1))
        return jcast('int', Code01_CountConsistentKeys.pass_[cur])

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code01_CountConsistentKeys.cnt):
            jstatic('Arrays', 'fill', Code01_CountConsistentKeys.tree[i], 0)
            Code01_CountConsistentKeys.pass_[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CountConsistentKeys.MAXN = jcast('int', 2000001)
Code01_CountConsistentKeys.tree = jarray('int', [Code01_CountConsistentKeys.MAXN, 12])
Code01_CountConsistentKeys.pass_ = jarray('int', [Code01_CountConsistentKeys.MAXN])
Code01_CountConsistentKeys.cnt = jcast('int', 0)
