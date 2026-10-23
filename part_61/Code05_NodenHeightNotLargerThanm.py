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

# 节点数为n高度不大于m的二叉树个数
# 现在有n个节点，计算出有多少个不同结构的二叉树
# 满足节点个数为n且树的高度不超过m的方案
# 因为答案很大，所以答案需要模上1000000007后输出
# 测试链接 : https://www.nowcoder.com/practice/aaefe5896cce4204b276e213e725f3ea
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_NodenHeightNotLargerThanm:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'dp1': 'dp1', 'dp2': 'dp2', 'dp3': 'dp3'}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code05_NodenHeightNotLargerThanm.compute3(n, m))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    MAXN = 0
    MOD = 0
    # 记忆化搜索
    dp1 = None
    # 二叉树节点数为n
    # 高度不能超过m
    # 结构数返回
    # 记忆化搜索
    @staticmethod
    def compute1(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        if (n == 0):
            return jcast('int', 1)
        # n > 0
        if (m == 0):
            return jcast('int', 0)
        if (Code05_NodenHeightNotLargerThanm.dp1[n][m] != jcast('int', (-1))):
            return jcast('int', jcast('int', Code05_NodenHeightNotLargerThanm.dp1[n][m]))
        ans = jcast('long', 0)
        # n个点，头占掉1个
        k = jcast('int', 0)
        while (k < n):
            # 一共n个节点，头节点已经占用了1个名额
            # 如果左树占用k个，那么右树就占用i-k-1个
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', jmod(jcast('long', (jcast('long', Code05_NodenHeightNotLargerThanm.compute1(k, jcast('int', (m - 1)))) * Code05_NodenHeightNotLargerThanm.compute1(jcast('int', (jcast('int', (n - k)) - 1)), jcast('int', (m - 1))))), Code05_NodenHeightNotLargerThanm.MOD)))), Code05_NodenHeightNotLargerThanm.MOD)))
            k = jcast('int', (k + 1))
        jset(Code05_NodenHeightNotLargerThanm.dp1[n], m, ans)
        return jcast('int', jcast('int', ans))

    # 严格位置依赖的动态规划
    dp2 = None
    @staticmethod
    def compute2(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        j = jcast('int', 0)
        while (j <= m):
            jset(Code05_NodenHeightNotLargerThanm.dp2[0], j, 1)
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= m):
                jset(Code05_NodenHeightNotLargerThanm.dp2[i], j, 0)
                k = jcast('int', 0)
                while (k < i):
                    # 一共i个节点，头节点已经占用了1个名额
                    # 如果左树占用k个，那么右树就占用i-k-1个
                    jset(Code05_NodenHeightNotLargerThanm.dp2[i], j, jcast('long', jmod(jcast('long', jadd(Code05_NodenHeightNotLargerThanm.dp2[i][j], jcast('long', jmod(jcast('long', (Code05_NodenHeightNotLargerThanm.dp2[k][jcast('int', (j - 1))] * Code05_NodenHeightNotLargerThanm.dp2[jcast('int', (jcast('int', (i - k)) - 1))][jcast('int', (j - 1))])), Code05_NodenHeightNotLargerThanm.MOD)))), Code05_NodenHeightNotLargerThanm.MOD)))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', Code05_NodenHeightNotLargerThanm.dp2[n][m]))

    # 空间压缩
    dp3 = None
    @staticmethod
    def compute3(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        Code05_NodenHeightNotLargerThanm.dp3[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= n):
            Code05_NodenHeightNotLargerThanm.dp3[i] = jcast('long', 0)
            i = jcast('int', (i + 1))
        j = jcast('int', 1)
        while (j <= m):
            # 根据依赖，一定要先枚举列
            i = jcast('int', n)
            while (i >= 1):
                # 再枚举行，而且i不需要到达0，i>=1即可
                Code05_NodenHeightNotLargerThanm.dp3[i] = jcast('long', 0)
                k = jcast('int', 0)
                while (k < i):
                    # 枚举
                    Code05_NodenHeightNotLargerThanm.dp3[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code05_NodenHeightNotLargerThanm.dp3[i], jcast('long', jmod(jcast('long', (Code05_NodenHeightNotLargerThanm.dp3[k] * Code05_NodenHeightNotLargerThanm.dp3[jcast('int', (jcast('int', (i - k)) - 1))])), Code05_NodenHeightNotLargerThanm.MOD)))), Code05_NodenHeightNotLargerThanm.MOD)))
                    k = jcast('int', (k + 1))
                i = jcast('int', (i - 1))
            j = jcast('int', (j + 1))
        return jcast('int', jcast('int', Code05_NodenHeightNotLargerThanm.dp3[n]))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_NodenHeightNotLargerThanm.MAXN = jcast('int', 51)
Code05_NodenHeightNotLargerThanm.MOD = jcast('int', 1000000007)
Code05_NodenHeightNotLargerThanm.dp1 = jarray('long', [Code05_NodenHeightNotLargerThanm.MAXN, Code05_NodenHeightNotLargerThanm.MAXN])
i = jcast('int', 0)
while (i < Code05_NodenHeightNotLargerThanm.MAXN):
    j = jcast('int', 0)
    while (j < Code05_NodenHeightNotLargerThanm.MAXN):
        jset(Code05_NodenHeightNotLargerThanm.dp1[i], j, jcast('int', (-1)))
        j = jcast('int', (j + 1))
    i = jcast('int', (i + 1))
Code05_NodenHeightNotLargerThanm.dp2 = jarray('long', [Code05_NodenHeightNotLargerThanm.MAXN, Code05_NodenHeightNotLargerThanm.MAXN])
Code05_NodenHeightNotLargerThanm.dp3 = jarray('long', [Code05_NodenHeightNotLargerThanm.MAXN])

if __name__ == '__main__':
    Code05_NodenHeightNotLargerThanm.main([])
