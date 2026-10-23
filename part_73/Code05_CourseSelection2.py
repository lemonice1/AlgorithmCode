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

# 选课，树上01背包的最优解
# 在大学里每个学生，为了达到一定的学分，必须从很多课程里选择一些课程来学习
# 在课程里有些课程必须在某些课程之前学习，如高等数学总是在其它课程之前学习
# 现在有 N 门功课，每门课有个学分，每门课有一门或没有直接先修课
# 若课程 a 是课程 b 的先修课即只有学完了课程 a，才能学习课程 b
# 一个学生要从这些课程里选择 M 门课程学习
# 问他能获得的最大学分是多少
# 测试链接 : https://www.luogu.com.cn/problem/P2014
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 最优解，链式前向星建图 + dfn序的利用 + 巧妙定义下的尝试
# 时间复杂度O(n * m)，推荐掌握，尤其是理解有效结构
class Code05_CourseSelection2:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'edgeCnt': 'edgeCnt', 'head': 'head', 'next': 'next', 'to': 'to', 'dfnCnt': 'dfnCnt', 'val': 'val', 'size': 'size', 'dp': 'dp', 'n': 'n', 'm': 'm'}
    MAXN = 0
    nums = None
    # 链式前向星建图
    edgeCnt = 0
    head = None
    next = None
    to = None
    # dfn的计数
    dfnCnt = 0
    # 下标为dfn序号
    val = None
    # 下标为dfn序号
    size = None
    # 动态规划表
    dp = None
    n = 0
    m = 0
    @staticmethod
    def build(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        Code05_CourseSelection2.edgeCnt = jcast('int', 1)
        Code05_CourseSelection2.dfnCnt = jcast('int', 0)
        jstatic('Arrays', 'fill', Code05_CourseSelection2.head, 0, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code05_CourseSelection2.dp[jcast('int', jadd(n, 2))], 0, jcast('int', jadd(m, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code05_CourseSelection2.next[Code05_CourseSelection2.edgeCnt] = jcast('int', Code05_CourseSelection2.head[u])
        Code05_CourseSelection2.to[Code05_CourseSelection2.edgeCnt] = jcast('int', v)
        jset(Code05_CourseSelection2.head, u, ((_java_obj_1 := Code05_CourseSelection2), (_java_key_2 := 'edgeCnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code05_CourseSelection2.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_CourseSelection2.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_CourseSelection2.build(Code05_CourseSelection2.n, Code05_CourseSelection2.m)
            i = jcast('int', 1)
            while (i <= Code05_CourseSelection2.n):
                jcall(in_, 'nextToken')
                Code05_CourseSelection2.addEdge(jcast('int', jget(in_, 'nval')), i)
                jcall(in_, 'nextToken')
                Code05_CourseSelection2.nums[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code05_CourseSelection2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        Code05_CourseSelection2.f(0)
        # 节点编号0 ~ n，dfn序号范围1 ~ n+1
        # 接下来的逻辑其实就是01背包！不过经历了很多转化
        # 整体的顺序是根据dfn序来进行的，从大的dfn序，遍历到小的dfn序
        # dp[i][j] : i ~ n+1 范围的节点，选择j个节点一定要形成有效结构的情况下，最大的累加和
        # 怎么定义有效结构？重点！重点！重点！
        # 假设i ~ n+1范围上，目前所有头节点的上方，有一个总的头节点
        # i ~ n+1范围所有节点，选出来j个节点的结构，
        # 挂在这个假想的总头节点之下，是一个连续的结构，没有断开的情况
        # 那么就说，i ~ n+1范围所有节点，选出来j个节点的结构是一个有效结构
        i = jcast('int', jcast('int', jadd(Code05_CourseSelection2.n, 1)))
        while (i >= 2):
            j = jcast('int', 1)
            while (j <= Code05_CourseSelection2.m):
                jset(Code05_CourseSelection2.dp[i], j, jstatic('Math', 'max', Code05_CourseSelection2.dp[jcast('int', jadd(i, Code05_CourseSelection2.size[i]))][j], jcast('int', jadd(Code05_CourseSelection2.val[i], Code05_CourseSelection2.dp[jcast('int', jadd(i, 1))][jcast('int', (j - 1))]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i - 1))
        # dp[2][m] : 2 ~ n范围上，选择m个节点一定要形成有效结构的情况下，最大的累加和
        # 最后来到dfn序为1的节点，一定是原始的0号节点
        # 原始0号节点下方一定挂着有效结构
        # 并且和补充的0号节点一定能整体连在一起，没有任何跳跃连接
        # 于是整个问题解决
        return jcast('int', jcast('int', jadd(Code05_CourseSelection2.nums[0], Code05_CourseSelection2.dp[2][Code05_CourseSelection2.m])))

    # u这棵子树的节点数返回
    @staticmethod
    def f(u):
        u = jcast('int', u)
        i = jcast('int', ((_java_obj_4 := Code05_CourseSelection2), (_java_key_5 := 'dfnCnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code05_CourseSelection2.val[i] = jcast('int', Code05_CourseSelection2.nums[u])
        Code05_CourseSelection2.size[i] = jcast('int', 1)
        ei = jcast('int', Code05_CourseSelection2.head[u])
        v = 0
        while (ei > 0):
            v = jcast('int', Code05_CourseSelection2.to[ei])
            ((_java_obj_7 := Code05_CourseSelection2.size), (_java_key_8 := i), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), Code05_CourseSelection2.f(v)))))[2]
            ei = jcast('int', Code05_CourseSelection2.next[ei])
        return jcast('int', Code05_CourseSelection2.size[i])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_CourseSelection2.MAXN = jcast('int', 301)
Code05_CourseSelection2.nums = jarray('int', [Code05_CourseSelection2.MAXN])
Code05_CourseSelection2.edgeCnt = jcast('int', 0)
Code05_CourseSelection2.head = jarray('int', [Code05_CourseSelection2.MAXN])
Code05_CourseSelection2.next = jarray('int', [Code05_CourseSelection2.MAXN])
Code05_CourseSelection2.to = jarray('int', [Code05_CourseSelection2.MAXN])
Code05_CourseSelection2.dfnCnt = jcast('int', 0)
Code05_CourseSelection2.val = jarray('int', [jcast('int', jadd(Code05_CourseSelection2.MAXN, 1))])
Code05_CourseSelection2.size = jarray('int', [jcast('int', jadd(Code05_CourseSelection2.MAXN, 1))])
Code05_CourseSelection2.dp = jarray('int', [jcast('int', jadd(Code05_CourseSelection2.MAXN, 2)), Code05_CourseSelection2.MAXN])
Code05_CourseSelection2.n = jcast('int', 0)
Code05_CourseSelection2.m = jcast('int', 0)

if __name__ == '__main__':
    Code05_CourseSelection2.main([])
