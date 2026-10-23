# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 统计全1子矩形的数量
# 给你一个 m * n 的矩阵 mat，其中只有0和1两种值
# 请你返回有多少个 子矩形 的元素全部都是1
# 测试链接 : https://leetcode.cn/problems/count-submatrices-with-all-ones/
class Code04_CountSubmatricesWithAllOnes:
    __java_fields__ = {'MAXM': 'MAXM', 'height': 'height', 'stack': 'stack', 'r': 'r'}
    MAXM = 0
    height = None
    stack = None
    r = 0
    @staticmethod
    def numSubmat(mat):
        n = jcast('int', jget(mat, 'length'))
        m = jcast('int', jget(mat[0], 'length'))
        ans = jcast('int', 0)
        jstatic('Arrays', 'fill', Code04_CountSubmatricesWithAllOnes.height, 0, m, 0)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                Code04_CountSubmatricesWithAllOnes.height[j] = jcast('int', (0 if (mat[i][j] == 0) else jcast('int', jadd(Code04_CountSubmatricesWithAllOnes.height[j], 1))))
                j = jcast('int', (j + 1))
            ans = jcast('int', jcast('int', jadd(ans, Code04_CountSubmatricesWithAllOnes.countFromBottom(m))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 比如
    # 1
    # 1
    # 1         1
    # 1         1         1
    # 1         1         1
    # 1         1         1
    #
    # 3  ....   6   ....  8
    # left      cur        i
    # 如上图，假设6位置从栈中弹出，6位置的高度为6(上面6个1)
    # 6位置的左边、离6位置最近、且小于高度6的是3位置(left)，3位置的高度是3
    # 6位置的右边、离6位置最近、且小于高度6的是8位置(i)，8位置的高度是4
    # 此时我们求什么？
    # 1) 求在4~7范围上必须以高度6作为高的矩形有几个？
    # 2) 求在4~7范围上必须以高度5作为高的矩形有几个？
    # 也就是说，<=4的高度一律不求，>6的高度一律不求！
    # 其他位置也会从栈里弹出，等其他位置弹出的时候去求！
    # 那么在4~7范围上必须以高度6作为高的矩形有几个？如下：
    # 4..4  4..5  4..6  4..7
    # 5..5  5..6  5..7
    # 6..6  6..7
    # 7..7
    # 10个！什么公式？
    # 4...7范围的长度为4，那么数量就是 : 4*5/2
    # 同理在4~7范围上，必须以高度5作为高的矩形也是这么多
    # 所以cur从栈里弹出时产生的数量 :
    # (cur位置的高度-Max{left位置的高度,i位置的高度}) * ((i-left-1)*(i-left)/2)
    @staticmethod
    def countFromBottom(m):
        m = jcast('int', m)
        # height[0...m-1]
        Code04_CountSubmatricesWithAllOnes.r = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        left = 0
        len = 0
        bottom = 0
        while (i < m):
            while ((Code04_CountSubmatricesWithAllOnes.r > 0) and (Code04_CountSubmatricesWithAllOnes.height[Code04_CountSubmatricesWithAllOnes.stack[jcast('int', (Code04_CountSubmatricesWithAllOnes.r - 1))]] >= Code04_CountSubmatricesWithAllOnes.height[i])):
                cur = jcast('int', Code04_CountSubmatricesWithAllOnes.stack[((_java_obj_1 := Code04_CountSubmatricesWithAllOnes), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3]])
                if (Code04_CountSubmatricesWithAllOnes.height[cur] > Code04_CountSubmatricesWithAllOnes.height[i]):
                    # 只有height[cur] > height[i]才结算
                    # 如果是因为height[cur]==height[i]导致cur位置从栈中弹出
                    # 那么不结算！等i位置弹出的时候再说！
                    # 上一节课讲了很多这种相等时候的处理，比如"柱状图中最大的矩形"问题
                    left = jcast('int', (jcast('int', (-1)) if (Code04_CountSubmatricesWithAllOnes.r == 0) else Code04_CountSubmatricesWithAllOnes.stack[jcast('int', (Code04_CountSubmatricesWithAllOnes.r - 1))]))
                    len = jcast('int', jcast('int', (jcast('int', (i - left)) - 1)))
                    bottom = jcast('int', jstatic('Math', 'max', (0 if (left == jcast('int', (-1))) else Code04_CountSubmatricesWithAllOnes.height[left]), Code04_CountSubmatricesWithAllOnes.height[i]))
                    ans = jcast('int', jcast('int', jadd(ans, jcast('int', jdiv(jcast('int', (jcast('int', (jcast('int', (Code04_CountSubmatricesWithAllOnes.height[cur] - bottom)) * len)) * jcast('int', jadd(len, 1)))), 2)))))
            jset(Code04_CountSubmatricesWithAllOnes.stack, ((_java_obj_4 := Code04_CountSubmatricesWithAllOnes), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], i)
            i = jcast('int', (i + 1))
        while (Code04_CountSubmatricesWithAllOnes.r > 0):
            cur = jcast('int', Code04_CountSubmatricesWithAllOnes.stack[((_java_obj_7 := Code04_CountSubmatricesWithAllOnes), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3]])
            left = jcast('int', (jcast('int', (-1)) if (Code04_CountSubmatricesWithAllOnes.r == 0) else Code04_CountSubmatricesWithAllOnes.stack[jcast('int', (Code04_CountSubmatricesWithAllOnes.r - 1))]))
            len = jcast('int', jcast('int', (jcast('int', (m - left)) - 1)))
            down = jcast('int', (0 if (left == jcast('int', (-1))) else Code04_CountSubmatricesWithAllOnes.height[left]))
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', jdiv(jcast('int', (jcast('int', (jcast('int', (Code04_CountSubmatricesWithAllOnes.height[cur] - down)) * len)) * jcast('int', jadd(len, 1)))), 2)))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_CountSubmatricesWithAllOnes.MAXM = jcast('int', 151)
Code04_CountSubmatricesWithAllOnes.height = jarray('int', [Code04_CountSubmatricesWithAllOnes.MAXM])
Code04_CountSubmatricesWithAllOnes.stack = jarray('int', [Code04_CountSubmatricesWithAllOnes.MAXM])
Code04_CountSubmatricesWithAllOnes.r = jcast('int', 0)
