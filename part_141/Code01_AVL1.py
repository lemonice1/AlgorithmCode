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

# AVL树的实现(Python版)
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
class Code01_AVL1:
    __java_fields__ = {'MAXN': 'MAXN', 'cnt': 'cnt', 'head': 'head', 'key': 'key', 'height': 'height', 'left': 'left', 'right': 'right', 'count': 'count', 'size': 'size'}
    MAXN = 0
    # 空间使用计数
    cnt = 0
    # 整棵树的头节点编号
    head = 0
    # 节点的key
    key = None
    # 子树高度
    height = None
    # 左孩子
    left = None
    # 右孩子
    right = None
    # 节点key的计数
    count = None
    # 子树的数字总数
    size = None
    # 修正信息
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code01_AVL1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_AVL1.size[Code01_AVL1.left[i]], Code01_AVL1.size[Code01_AVL1.right[i]])), Code01_AVL1.count[i])))
        jset(Code01_AVL1.height, i, jcast('int', jadd(jstatic('Math', 'max', Code01_AVL1.height[Code01_AVL1.left[i]], Code01_AVL1.height[Code01_AVL1.right[i]]), 1)))

    # i节点为头的树左旋，返回左旋后头节点的空间编号
    @staticmethod
    def leftRotate(i):
        i = jcast('int', i)
        r = jcast('int', Code01_AVL1.right[i])
        Code01_AVL1.right[i] = jcast('int', Code01_AVL1.left[r])
        Code01_AVL1.left[r] = jcast('int', i)
        Code01_AVL1.up(i)
        Code01_AVL1.up(r)
        return jcast('int', r)

    # i节点为头的树右旋，返回右旋后头节点的空间编号
    @staticmethod
    def rightRotate(i):
        i = jcast('int', i)
        l = jcast('int', Code01_AVL1.left[i])
        Code01_AVL1.left[i] = jcast('int', Code01_AVL1.right[l])
        Code01_AVL1.right[l] = jcast('int', i)
        Code01_AVL1.up(i)
        Code01_AVL1.up(l)
        return jcast('int', l)

    # 检查i节点为头的树是否违规
    # 如果命中了某种违规情况，就进行相应调整
    # 返回树的头节点的空间编号
    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        lh = jcast('int', Code01_AVL1.height[Code01_AVL1.left[i]])
        rh = jcast('int', Code01_AVL1.height[Code01_AVL1.right[i]])
        if (jcast('int', (lh - rh)) > 1):
            if (Code01_AVL1.height[Code01_AVL1.left[Code01_AVL1.left[i]]] >= Code01_AVL1.height[Code01_AVL1.right[Code01_AVL1.left[i]]]):
                i = jcast('int', Code01_AVL1.rightRotate(i))
            else:
                jset(Code01_AVL1.left, i, Code01_AVL1.leftRotate(Code01_AVL1.left[i]))
                i = jcast('int', Code01_AVL1.rightRotate(i))
        else:
            if (jcast('int', (rh - lh)) > 1):
                if (Code01_AVL1.height[Code01_AVL1.right[Code01_AVL1.right[i]]] >= Code01_AVL1.height[Code01_AVL1.left[Code01_AVL1.right[i]]]):
                    i = jcast('int', Code01_AVL1.leftRotate(i))
                else:
                    jset(Code01_AVL1.right, i, Code01_AVL1.rightRotate(Code01_AVL1.right[i]))
                    i = jcast('int', Code01_AVL1.leftRotate(i))
        return jcast('int', i)

    # 增加数字num，重复加入算多个词频
    @staticmethod
    def _java_add_0(num):
        num = jcast('int', num)
        Code01_AVL1.head = jcast('int', Code01_AVL1._java_add_1(Code01_AVL1.head, num))

    # 当前来到i号节点，num这个数字一定会加入以i为头的树
    # 树结构有可能变化，返回头节点编号
    @staticmethod
    def _java_add_1(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            jset(Code01_AVL1.key, ((_java_obj_1 := Code01_AVL1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
            jset(Code01_AVL1.count, Code01_AVL1.cnt, jset(Code01_AVL1.size, Code01_AVL1.cnt, jset(Code01_AVL1.height, Code01_AVL1.cnt, 1)))
            return jcast('int', Code01_AVL1.cnt)
        if (Code01_AVL1.key[i] == num):
            Code01_AVL1.count[i] = jcast('int', (Code01_AVL1.count[i] + 1))
        else:
            if (Code01_AVL1.key[i] > num):
                jset(Code01_AVL1.left, i, Code01_AVL1._java_add_1(Code01_AVL1.left[i], num))
            else:
                jset(Code01_AVL1.right, i, Code01_AVL1._java_add_1(Code01_AVL1.right[i], num))
        Code01_AVL1.up(i)
        return jcast('int', Code01_AVL1.maintain(i))

    # 删除数字num，如果有多个，只删掉一个
    @staticmethod
    def _java_remove_0(num):
        num = jcast('int', num)
        if (Code01_AVL1.rank(num) != Code01_AVL1.rank(jcast('int', jadd(num, 1)))):
            Code01_AVL1.head = jcast('int', Code01_AVL1._java_remove_1(Code01_AVL1.head, num))

    # 当前来到i号节点，以i为头的树一定会减少1个num
    # 树结构有可能变化，返回头节点编号
    @staticmethod
    def _java_remove_1(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (Code01_AVL1.key[i] < num):
            jset(Code01_AVL1.right, i, Code01_AVL1._java_remove_1(Code01_AVL1.right[i], num))
        else:
            if (Code01_AVL1.key[i] > num):
                jset(Code01_AVL1.left, i, Code01_AVL1._java_remove_1(Code01_AVL1.left[i], num))
            else:
                if (Code01_AVL1.count[i] > 1):
                    Code01_AVL1.count[i] = jcast('int', (Code01_AVL1.count[i] - 1))
                else:
                    if ((Code01_AVL1.left[i] == 0) and (Code01_AVL1.right[i] == 0)):
                        return jcast('int', 0)
                    else:
                        if ((Code01_AVL1.left[i] != 0) and (Code01_AVL1.right[i] == 0)):
                            i = jcast('int', Code01_AVL1.left[i])
                        else:
                            if ((Code01_AVL1.left[i] == 0) and (Code01_AVL1.right[i] != 0)):
                                i = jcast('int', Code01_AVL1.right[i])
                            else:
                                mostLeft = jcast('int', Code01_AVL1.right[i])
                                while (Code01_AVL1.left[mostLeft] != 0):
                                    mostLeft = jcast('int', Code01_AVL1.left[mostLeft])
                                jset(Code01_AVL1.right, i, Code01_AVL1.removeMostLeft(Code01_AVL1.right[i], mostLeft))
                                Code01_AVL1.left[mostLeft] = jcast('int', Code01_AVL1.left[i])
                                Code01_AVL1.right[mostLeft] = jcast('int', Code01_AVL1.right[i])
                                i = jcast('int', mostLeft)
        Code01_AVL1.up(i)
        return jcast('int', Code01_AVL1.maintain(i))

    # 以i号节点为头的树上，最左节点的编号一定是mostLeft
    # 删掉这个节点，并保证树的平衡性，返回头节点的编号
    @staticmethod
    def removeMostLeft(i, mostLeft):
        i = jcast('int', i)
        mostLeft = jcast('int', mostLeft)
        if (i == mostLeft):
            return jcast('int', Code01_AVL1.right[i])
        else:
            jset(Code01_AVL1.left, i, Code01_AVL1.removeMostLeft(Code01_AVL1.left[i], mostLeft))
            Code01_AVL1.up(i)
            return jcast('int', Code01_AVL1.maintain(i))

    # 查询num的排名，比num小的数字个数+1，就是num的排名
    @staticmethod
    def rank(num):
        num = jcast('int', num)
        return jcast('int', jcast('int', jadd(Code01_AVL1.small(Code01_AVL1.head, num), 1)))

    # 以i为头的树上，比num小的数字有几个
    @staticmethod
    def small(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', 0)
        if (Code01_AVL1.key[i] >= num):
            return jcast('int', Code01_AVL1.small(Code01_AVL1.left[i], num))
        else:
            return jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_AVL1.size[Code01_AVL1.left[i]], Code01_AVL1.count[i])), Code01_AVL1.small(Code01_AVL1.right[i], num))))

    @staticmethod
    def _java_index_0(x):
        x = jcast('int', x)
        return jcast('int', Code01_AVL1._java_index_1(Code01_AVL1.head, x))

    @staticmethod
    def _java_index_1(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (Code01_AVL1.size[Code01_AVL1.left[i]] >= x):
            return jcast('int', Code01_AVL1._java_index_1(Code01_AVL1.left[i], x))
        else:
            if (jcast('int', jadd(Code01_AVL1.size[Code01_AVL1.left[i]], Code01_AVL1.count[i])) < x):
                return jcast('int', Code01_AVL1._java_index_1(Code01_AVL1.right[i], jcast('int', (jcast('int', (x - Code01_AVL1.size[Code01_AVL1.left[i]])) - Code01_AVL1.count[i]))))
        return jcast('int', Code01_AVL1.key[i])

    @staticmethod
    def _java_pre_0(num):
        num = jcast('int', num)
        return jcast('int', Code01_AVL1._java_pre_1(Code01_AVL1.head, num))

    @staticmethod
    def _java_pre_1(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        if (Code01_AVL1.key[i] >= num):
            return jcast('int', Code01_AVL1._java_pre_1(Code01_AVL1.left[i], num))
        else:
            return jcast('int', jstatic('Math', 'max', Code01_AVL1.key[i], Code01_AVL1._java_pre_1(Code01_AVL1.right[i], num)))

    @staticmethod
    def _java_post_0(num):
        num = jcast('int', num)
        return jcast('int', Code01_AVL1._java_post_1(Code01_AVL1.head, num))

    @staticmethod
    def _java_post_1(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        if (Code01_AVL1.key[i] <= num):
            return jcast('int', Code01_AVL1._java_post_1(Code01_AVL1.right[i], num))
        else:
            return jcast('int', jstatic('Math', 'min', Code01_AVL1.key[i], Code01_AVL1._java_post_1(Code01_AVL1.left[i], num)))

    @staticmethod
    def clear():
        jstatic('Arrays', 'fill', Code01_AVL1.key, 1, jcast('int', jadd(Code01_AVL1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_AVL1.height, 1, jcast('int', jadd(Code01_AVL1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_AVL1.left, 1, jcast('int', jadd(Code01_AVL1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_AVL1.right, 1, jcast('int', jadd(Code01_AVL1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_AVL1.count, 1, jcast('int', jadd(Code01_AVL1.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_AVL1.size, 1, jcast('int', jadd(Code01_AVL1.cnt, 1)), 0)
        Code01_AVL1.cnt = jcast('int', 0)
        Code01_AVL1.head = jcast('int', 0)

    @staticmethod
    def main(args):
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
                Code01_AVL1._java_add_0(x)
            else:
                if (op == 2):
                    Code01_AVL1._java_remove_0(x)
                else:
                    if (op == 3):
                        jcall(out, 'println', Code01_AVL1.rank(x))
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code01_AVL1._java_index_0(x))
                        else:
                            if (op == 5):
                                jcall(out, 'println', Code01_AVL1._java_pre_0(x))
                            else:
                                jcall(out, 'println', Code01_AVL1._java_post_0(x))
            i = jcast('int', (i + 1))
        Code01_AVL1.clear()
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code01_AVL1._java_add_0(*args)
        if _java_choice == 1:
            return Code01_AVL1._java_add_1(*args)
        raise TypeError("No matching overload for Code01_AVL1.add")

    @staticmethod
    def remove(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code01_AVL1._java_remove_0(*args)
        if _java_choice == 1:
            return Code01_AVL1._java_remove_1(*args)
        raise TypeError("No matching overload for Code01_AVL1.remove")

    @staticmethod
    def index(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code01_AVL1._java_index_0(*args)
        if _java_choice == 1:
            return Code01_AVL1._java_index_1(*args)
        raise TypeError("No matching overload for Code01_AVL1.index")

    @staticmethod
    def pre(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code01_AVL1._java_pre_0(*args)
        if _java_choice == 1:
            return Code01_AVL1._java_pre_1(*args)
        raise TypeError("No matching overload for Code01_AVL1.pre")

    @staticmethod
    def post(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code01_AVL1._java_post_0(*args)
        if _java_choice == 1:
            return Code01_AVL1._java_post_1(*args)
        raise TypeError("No matching overload for Code01_AVL1.post")


Code01_AVL1.MAXN = jcast('int', 100001)
Code01_AVL1.cnt = jcast('int', 0)
Code01_AVL1.head = jcast('int', 0)
Code01_AVL1.key = jarray('int', [Code01_AVL1.MAXN])
Code01_AVL1.height = jarray('int', [Code01_AVL1.MAXN])
Code01_AVL1.left = jarray('int', [Code01_AVL1.MAXN])
Code01_AVL1.right = jarray('int', [Code01_AVL1.MAXN])
Code01_AVL1.count = jarray('int', [Code01_AVL1.MAXN])
Code01_AVL1.size = jarray('int', [Code01_AVL1.MAXN])

if __name__ == '__main__':
    Code01_AVL1.main([])
