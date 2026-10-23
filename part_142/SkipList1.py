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

# 跳表的实现(Python版)
# 实现一种结构，支持如下操作，要求单次调用的时间复杂度O(log n)
# 1，增加x，重复加入算多个词频
# 2，删除x，如果有多个，只删掉一个
# 3，查询x的排名，x的排名为，比x小的数的个数+1
# 4，查询数据中排名为x的数
# 5，查询x的前驱，x的前驱为，小于x的数中最大的数，不存在返回整数最小值
# 6，查询x的后继，x的后继为，大于x的数中最小的数，不存在返回整数最大值
# 所有操作的次数 <= 10^5
# -10^7 <= x <= +10^7
# 测试链接 : https://www.luogu.com.cn/problem/P3369
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class SkipList1:
    __java_fields__ = {'MAXL': 'MAXL', 'MAXN': 'MAXN', 'cnt': 'cnt', 'key': 'key', 'count': 'count', 'level': 'level', 'next': 'next', 'len': 'len'}
    # 跳表最大层的限制
    MAXL = 0
    MAXN = 0
    # 空间使用计数
    cnt = 0
    # 节点的key
    key = None
    # 节点key的计数
    count = None
    # 节点拥有多少层指针
    level = None
    # 节点每一层指针指向哪个节点
    next = None
    # 节点每一层指针的长度(底层跨过多少数，左开右闭)
    len = None
    # 建立跳表
    @staticmethod
    def build():
        SkipList1.cnt = jcast('int', 1)
        SkipList1.key[SkipList1.cnt] = jcast('int', jget(Integer, 'MIN_VALUE'))
        SkipList1.level[SkipList1.cnt] = jcast('int', SkipList1.MAXL)

    # 使用多少空间一律清空
    @staticmethod
    def clear():
        jstatic('Arrays', 'fill', SkipList1.key, 1, jcast('int', jadd(SkipList1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', SkipList1.count, 1, jcast('int', jadd(SkipList1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', SkipList1.level, 1, jcast('int', jadd(SkipList1.cnt, 1)), 0)
        i = jcast('int', 1)
        while (i <= SkipList1.cnt):
            jstatic('Arrays', 'fill', SkipList1.next[i], 0)
            jstatic('Arrays', 'fill', SkipList1.len[i], 0)
            i = jcast('int', (i + 1))
        SkipList1.cnt = jcast('int', 0)

    # 扔骰子决定节点的层数
    @staticmethod
    def random():
        ans = jcast('int', 1)
        while (jstatic('Math', 'random') < 0.5):
            ans = jcast('int', (ans + 1))
        return jcast('int', jstatic('Math', 'min', ans, SkipList1.MAXL))

    # 当前在i号节点的h层，返回key为num的节点，空间编号是多少
    @staticmethod
    def find(i, h, num):
        i = jcast('int', i)
        h = jcast('int', h)
        num = jcast('int', num)
        while ((SkipList1.next[i][h] != 0) and (SkipList1.key[SkipList1.next[i][h]] < num)):
            i = jcast('int', SkipList1.next[i][h])
        if (h == 1):
            if ((SkipList1.next[i][h] != 0) and (SkipList1.key[SkipList1.next[i][h]] == num)):
                return jcast('int', SkipList1.next[i][h])
            else:
                return jcast('int', 0)
        return jcast('int', SkipList1.find(i, jcast('int', (h - 1)), num))

    # 增加num，重复加入算多个词频
    @staticmethod
    def add(num):
        num = jcast('int', num)
        if (SkipList1.find(1, SkipList1.MAXL, num) != 0):
            SkipList1.addCount(1, SkipList1.MAXL, num)
        else:
            jset(SkipList1.key, ((_java_obj_1 := SkipList1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
            SkipList1.count[SkipList1.cnt] = jcast('int', 1)
            jset(SkipList1.level, SkipList1.cnt, SkipList1.random())
            SkipList1.addNode(1, SkipList1.MAXL, SkipList1.cnt)

    # 当前在i号节点的h层，num增加一个词频
    @staticmethod
    def addCount(i, h, num):
        i = jcast('int', i)
        h = jcast('int', h)
        num = jcast('int', num)
        while ((SkipList1.next[i][h] != 0) and (SkipList1.key[SkipList1.next[i][h]] < num)):
            i = jcast('int', SkipList1.next[i][h])
        if (h == 1):
            ((_java_obj_4 := SkipList1.count), (_java_key_5 := SkipList1.next[i][h]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
        else:
            SkipList1.addCount(i, jcast('int', (h - 1)), num)
        ((_java_obj_7 := SkipList1.len[i]), (_java_key_8 := h), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]

    # 当前在i号节点的h层，插入空间编号为j的节点
    # 返回值：从i号节点出发，直到把空间编号为j的节点插入，底层总共有多少数字比key[j]小
    # 返回值很重要，因为上游需要这个信息来改动指针的长度信息
    @staticmethod
    def addNode(i, h, j):
        i = jcast('int', i)
        h = jcast('int', h)
        j = jcast('int', j)
        rightCnt = jcast('int', 0)
        while ((SkipList1.next[i][h] != 0) and (SkipList1.key[SkipList1.next[i][h]] < SkipList1.key[j])):
            rightCnt = jcast('int', jcast('int', jadd(rightCnt, SkipList1.len[i][h])))
            i = jcast('int', SkipList1.next[i][h])
        if (h == 1):
            jset(SkipList1.next[j], h, SkipList1.next[i][h])
            jset(SkipList1.next[i], h, j)
            jset(SkipList1.len[j], h, SkipList1.count[SkipList1.next[j][h]])
            jset(SkipList1.len[i], h, SkipList1.count[SkipList1.next[i][h]])
            return jcast('int', rightCnt)
        else:
            downCnt = jcast('int', SkipList1.addNode(i, jcast('int', (h - 1)), j))
            if (h > SkipList1.level[j]):
                ((_java_obj_10 := SkipList1.len[i]), (_java_key_11 := h), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]
            else:
                jset(SkipList1.next[j], h, SkipList1.next[i][h])
                jset(SkipList1.next[i], h, j)
                jset(SkipList1.len[j], h, jcast('int', (jcast('int', (jcast('int', jadd(SkipList1.len[i][h], 1)) - downCnt)) - SkipList1.count[j])))
                jset(SkipList1.len[i], h, jcast('int', jadd(downCnt, SkipList1.count[j])))
            return jcast('int', jcast('int', jadd(rightCnt, downCnt)))

    # 删除x，如果有多个，只删掉一个
    @staticmethod
    def remove(num):
        num = jcast('int', num)
        j = jcast('int', SkipList1.find(1, SkipList1.MAXL, num))
        if (j != 0):
            if (SkipList1.count[j] > 1):
                SkipList1.removeCount(1, SkipList1.MAXL, num)
            else:
                SkipList1.removeNode(1, SkipList1.MAXL, j)

    # 当前在i号节点的h层，num减少一个词频
    @staticmethod
    def removeCount(i, h, num):
        i = jcast('int', i)
        h = jcast('int', h)
        num = jcast('int', num)
        while ((SkipList1.next[i][h] != 0) and (SkipList1.key[SkipList1.next[i][h]] < num)):
            i = jcast('int', SkipList1.next[i][h])
        if (h == 1):
            ((_java_obj_13 := SkipList1.count), (_java_key_14 := SkipList1.next[i][h]), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]
        else:
            SkipList1.removeCount(i, jcast('int', (h - 1)), num)
        ((_java_obj_16 := SkipList1.len[i]), (_java_key_17 := h), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (-1)))), _java_old_18)[4]

    # 当前在i号节点的h层，删除空间编号为j的节点
    @staticmethod
    def removeNode(i, h, j):
        i = jcast('int', i)
        h = jcast('int', h)
        j = jcast('int', j)
        if (h < 1):
            return
        while ((SkipList1.next[i][h] != 0) and (SkipList1.key[SkipList1.next[i][h]] < SkipList1.key[j])):
            i = jcast('int', SkipList1.next[i][h])
        if (h > SkipList1.level[j]):
            ((_java_obj_19 := SkipList1.len[i]), (_java_key_20 := h), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]
        else:
            jset(SkipList1.next[i], h, SkipList1.next[j][h])
            ((_java_obj_22 := SkipList1.len[i]), (_java_key_23 := h), jset(_java_obj_22, _java_key_23, jcast('int', jadd(jget(_java_obj_22, _java_key_23), jcast('int', (SkipList1.len[j][h] - 1))))))[2]
        SkipList1.removeNode(i, jcast('int', (h - 1)), j)

    # 查询num的排名
    @staticmethod
    def rank(num):
        num = jcast('int', num)
        return jcast('int', jcast('int', jadd(SkipList1.small(1, SkipList1.MAXL, num), 1)))

    # 当前在i号节点的h层，查询有多少个数字比num小
    @staticmethod
    def small(i, h, num):
        i = jcast('int', i)
        h = jcast('int', h)
        num = jcast('int', num)
        rightCnt = jcast('int', 0)
        while ((SkipList1.next[i][h] != 0) and (SkipList1.key[SkipList1.next[i][h]] < num)):
            rightCnt = jcast('int', jcast('int', jadd(rightCnt, SkipList1.len[i][h])))
            i = jcast('int', SkipList1.next[i][h])
        if (h == 1):
            return jcast('int', rightCnt)
        else:
            return jcast('int', jcast('int', jadd(rightCnt, SkipList1.small(i, jcast('int', (h - 1)), num))))

    # 查询排名第x的key是什么
    @staticmethod
    def _java_index_0(x):
        x = jcast('int', x)
        return jcast('int', SkipList1._java_index_1(1, SkipList1.MAXL, x))

    # 当前在i号节点的h层，查询排名第x的key是什么
    @staticmethod
    def _java_index_1(i, h, x):
        i = jcast('int', i)
        h = jcast('int', h)
        x = jcast('int', x)
        c = jcast('int', 0)
        while ((SkipList1.next[i][h] != 0) and (jcast('int', jadd(c, SkipList1.len[i][h])) < x)):
            c = jcast('int', jcast('int', jadd(c, SkipList1.len[i][h])))
            i = jcast('int', SkipList1.next[i][h])
        if (h == 1):
            return jcast('int', SkipList1.key[SkipList1.next[i][h]])
        else:
            return jcast('int', SkipList1._java_index_1(i, jcast('int', (h - 1)), jcast('int', (x - c))))

    # 查询num的前驱
    @staticmethod
    def _java_pre_0(num):
        num = jcast('int', num)
        return jcast('int', SkipList1._java_pre_1(1, SkipList1.MAXL, num))

    @staticmethod
    def _java_pre_1(i, h, num):
        i = jcast('int', i)
        h = jcast('int', h)
        num = jcast('int', num)
        while ((SkipList1.next[i][h] != 0) and (SkipList1.key[SkipList1.next[i][h]] < num)):
            i = jcast('int', SkipList1.next[i][h])
        if (h == 1):
            return jcast('int', (jget(Integer, 'MIN_VALUE') if (i == 1) else SkipList1.key[i]))
        else:
            return jcast('int', SkipList1._java_pre_1(i, jcast('int', (h - 1)), num))

    # 查询num的后继
    @staticmethod
    def _java_post_0(num):
        num = jcast('int', num)
        return jcast('int', SkipList1._java_post_1(1, SkipList1.MAXL, num))

    @staticmethod
    def _java_post_1(i, h, num):
        i = jcast('int', i)
        h = jcast('int', h)
        num = jcast('int', num)
        while ((SkipList1.next[i][h] != 0) and (SkipList1.key[SkipList1.next[i][h]] < num)):
            i = jcast('int', SkipList1.next[i][h])
        if (h == 1):
            if (SkipList1.next[i][h] == 0):
                return jcast('int', jget(Integer, 'MAX_VALUE'))
            if (SkipList1.key[SkipList1.next[i][h]] > num):
                return jcast('int', SkipList1.key[SkipList1.next[i][h]])
            i = jcast('int', SkipList1.next[i][h])
            if (SkipList1.next[i][h] == 0):
                return jcast('int', jget(Integer, 'MAX_VALUE'))
            else:
                return jcast('int', SkipList1.key[SkipList1.next[i][h]])
        else:
            return jcast('int', SkipList1._java_post_1(i, jcast('int', (h - 1)), num))

    @staticmethod
    def main(args):
        SkipList1.build()
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        op = 0
        x = 0
        while (i <= n):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                SkipList1.add(x)
            else:
                if (op == 2):
                    SkipList1.remove(x)
                else:
                    if (op == 3):
                        jcall(out, 'println', SkipList1.rank(x))
                    else:
                        if (op == 4):
                            jcall(out, 'println', SkipList1._java_index_0(x))
                        else:
                            if (op == 5):
                                jcall(out, 'println', SkipList1._java_pre_0(x))
                            else:
                                jcall(out, 'println', SkipList1._java_post_0(x))
            i = jcast('int', (i + 1))
        SkipList1.clear()
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def index(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return SkipList1._java_index_0(*args)
        if _java_choice == 1:
            return SkipList1._java_index_1(*args)
        raise TypeError("No matching overload for SkipList1.index")

    @staticmethod
    def pre(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return SkipList1._java_pre_0(*args)
        if _java_choice == 1:
            return SkipList1._java_pre_1(*args)
        raise TypeError("No matching overload for SkipList1.pre")

    @staticmethod
    def post(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return SkipList1._java_post_0(*args)
        if _java_choice == 1:
            return SkipList1._java_post_1(*args)
        raise TypeError("No matching overload for SkipList1.post")


SkipList1.MAXL = jcast('int', 20)
SkipList1.MAXN = jcast('int', 100001)
SkipList1.cnt = jcast('int', 0)
SkipList1.key = jarray('int', [SkipList1.MAXN])
SkipList1.count = jarray('int', [SkipList1.MAXN])
SkipList1.level = jarray('int', [SkipList1.MAXN])
SkipList1.next = jarray('int', [SkipList1.MAXN, jcast('int', jadd(SkipList1.MAXL, 1))])
SkipList1.len = jarray('int', [SkipList1.MAXN, jcast('int', jadd(SkipList1.MAXL, 1))])

if __name__ == '__main__':
    SkipList1.main([])
