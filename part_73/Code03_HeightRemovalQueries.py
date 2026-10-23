# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 移除子树后的二叉树高度
# 给你一棵 二叉树 的根节点 root ，树中有 n 个节点
# 每个节点都可以被分配一个从 1 到 n 且互不相同的值
# 另给你一个长度为 m 的数组 queries
# 你必须在树上执行 m 个 独立 的查询，其中第 i 个查询你需要执行以下操作：
# 从树中 移除 以 queries[i] 的值作为根节点的子树
# 题目所用测试用例保证 queries[i] 不等于根节点的值
# 返回一个长度为 m 的数组 answer
# 其中 answer[i] 是执行第 i 个查询后树的高度
# 注意：
# 查询之间是独立的，所以在每个查询执行后，树会回到其初始状态
# 树的高度是从根到树中某个节点的 最长简单路径中的边数
# 测试链接 : https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/
class Code03_HeightRemovalQueries:
    __java_fields__ = {'MAXN': 'MAXN', 'dfn': 'dfn', 'deep': 'deep', 'size': 'size', 'maxl': 'maxl', 'maxr': 'maxr', 'dfnCnt': 'dfnCnt'}
    # 不要提交这个类
    class TreeNode:
        __java_fields__ = {'val': 'val', 'left': 'left', 'right': 'right'}
        # val：实例字段，在构造函数中初始化。
        # left：实例字段，在构造函数中初始化。
        # right：实例字段，在构造函数中初始化。
        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.left = None
            self.right = None
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 提交如下的方法
    MAXN = 0
    # 下标为节点的值
    dfn = None
    # 下标为dfn序号
    deep = None
    # 下标为dfn序号
    size = None
    maxl = None
    maxr = None
    dfnCnt = 0
    @staticmethod
    def treeQueries(root, queries):
        Code03_HeightRemovalQueries.dfnCnt = jcast('int', 0)
        Code03_HeightRemovalQueries.f(root, 0)
        i = jcast('int', 1)
        while (i <= Code03_HeightRemovalQueries.dfnCnt):
            jset(Code03_HeightRemovalQueries.maxl, i, jstatic('Math', 'max', Code03_HeightRemovalQueries.maxl[jcast('int', (i - 1))], Code03_HeightRemovalQueries.deep[i]))
            i = jcast('int', (i + 1))
        Code03_HeightRemovalQueries.maxr[jcast('int', jadd(Code03_HeightRemovalQueries.dfnCnt, 1))] = jcast('int', 0)
        i = jcast('int', Code03_HeightRemovalQueries.dfnCnt)
        while (i >= 1):
            jset(Code03_HeightRemovalQueries.maxr, i, jstatic('Math', 'max', Code03_HeightRemovalQueries.maxr[jcast('int', jadd(i, 1))], Code03_HeightRemovalQueries.deep[i]))
            i = jcast('int', (i - 1))
        m = jcast('int', jget(queries, 'length'))
        ans = jarray('int', [m])
        i = jcast('int', 0)
        while (i < m):
            leftMax = jcast('int', Code03_HeightRemovalQueries.maxl[jcast('int', (Code03_HeightRemovalQueries.dfn[queries[i]] - 1))])
            rightMax = jcast('int', Code03_HeightRemovalQueries.maxr[jcast('int', jadd(Code03_HeightRemovalQueries.dfn[queries[i]], Code03_HeightRemovalQueries.size[Code03_HeightRemovalQueries.dfn[queries[i]]]))])
            jset(ans, i, jstatic('Math', 'max', leftMax, rightMax))
            i = jcast('int', (i + 1))
        return ans

    # 来到x节点，从头节点到x节点经过了k条边
    @staticmethod
    def f(x, k):
        k = jcast('int', k)
        i = jcast('int', ((_java_obj_1 := Code03_HeightRemovalQueries), (_java_key_2 := 'dfnCnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        jset(Code03_HeightRemovalQueries.dfn, jget(x, 'val'), i)
        Code03_HeightRemovalQueries.deep[i] = jcast('int', k)
        Code03_HeightRemovalQueries.size[i] = jcast('int', 1)
        if (jget(x, 'left') != None):
            Code03_HeightRemovalQueries.f(jget(x, 'left'), jcast('int', jadd(k, 1)))
            Code03_HeightRemovalQueries.size[i] = jcast('int', jcast('int', jadd(Code03_HeightRemovalQueries.size[i], Code03_HeightRemovalQueries.size[Code03_HeightRemovalQueries.dfn[jget(jget(x, 'left'), 'val')]])))
        if (jget(x, 'right') != None):
            Code03_HeightRemovalQueries.f(jget(x, 'right'), jcast('int', jadd(k, 1)))
            Code03_HeightRemovalQueries.size[i] = jcast('int', jcast('int', jadd(Code03_HeightRemovalQueries.size[i], Code03_HeightRemovalQueries.size[Code03_HeightRemovalQueries.dfn[jget(jget(x, 'right'), 'val')]])))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_HeightRemovalQueries.MAXN = jcast('int', 100010)
Code03_HeightRemovalQueries.dfn = jarray('int', [Code03_HeightRemovalQueries.MAXN])
Code03_HeightRemovalQueries.deep = jarray('int', [Code03_HeightRemovalQueries.MAXN])
Code03_HeightRemovalQueries.size = jarray('int', [Code03_HeightRemovalQueries.MAXN])
Code03_HeightRemovalQueries.maxl = jarray('int', [Code03_HeightRemovalQueries.MAXN])
Code03_HeightRemovalQueries.maxr = jarray('int', [Code03_HeightRemovalQueries.MAXN])
Code03_HeightRemovalQueries.dfnCnt = jcast('int', 0)
