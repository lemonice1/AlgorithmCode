# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 合唱队
# 具体描述情打开链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P3205
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_HeightAndChoir:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'dp': 'dp', 'n': 'n', 'MOD': 'MOD'}
    MAXN = 0
    nums = None
    dp = None
    n = 0
    MOD = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_HeightAndChoir.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code03_HeightAndChoir.n):
                jcall(in_, 'nextToken')
                Code03_HeightAndChoir.nums[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            if (Code03_HeightAndChoir.n == 1):
                jcall(out, 'println', 1)
            else:
                jcall(out, 'println', Code03_HeightAndChoir.compute2())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 时间复杂度O(n^2)
    # 严格位置依赖的动态规划
    @staticmethod
    def compute1():
        # 人的编号范围 : 1...n
        # dp[l][r][0] : 形成l...r的状况的方法数，同时要求l位置的数字是最后出现的
        # dp[l][r][1] : 形成l...r的状况的方法数，同时要求r位置的数字是最后出现的
        dp = jarray('int', [jcast('int', jadd(Code03_HeightAndChoir.n, 1)), jcast('int', jadd(Code03_HeightAndChoir.n, 1)), 2])
        i = jcast('int', 1)
        while (i < Code03_HeightAndChoir.n):
            if (Code03_HeightAndChoir.nums[i] < Code03_HeightAndChoir.nums[jcast('int', jadd(i, 1))]):
                jset(dp[i][jcast('int', jadd(i, 1))], 0, 1)
                jset(dp[i][jcast('int', jadd(i, 1))], 1, 1)
            i = jcast('int', (i + 1))
        l = jcast('int', jcast('int', (Code03_HeightAndChoir.n - 2)))
        while (l >= 1):
            r = jcast('int', jcast('int', jadd(l, 2)))
            while (r <= Code03_HeightAndChoir.n):
                if (Code03_HeightAndChoir.nums[l] < Code03_HeightAndChoir.nums[jcast('int', jadd(l, 1))]):
                    jset(dp[l][r], 0, jcast('int', jmod(jcast('int', jadd(dp[l][r][0], dp[jcast('int', jadd(l, 1))][r][0])), Code03_HeightAndChoir.MOD)))
                if (Code03_HeightAndChoir.nums[l] < Code03_HeightAndChoir.nums[r]):
                    jset(dp[l][r], 0, jcast('int', jmod(jcast('int', jadd(dp[l][r][0], dp[jcast('int', jadd(l, 1))][r][1])), Code03_HeightAndChoir.MOD)))
                if (Code03_HeightAndChoir.nums[r] > Code03_HeightAndChoir.nums[l]):
                    jset(dp[l][r], 1, jcast('int', jmod(jcast('int', jadd(dp[l][r][1], dp[l][jcast('int', (r - 1))][0])), Code03_HeightAndChoir.MOD)))
                if (Code03_HeightAndChoir.nums[r] > Code03_HeightAndChoir.nums[jcast('int', (r - 1))]):
                    jset(dp[l][r], 1, jcast('int', jmod(jcast('int', jadd(dp[l][r][1], dp[l][jcast('int', (r - 1))][1])), Code03_HeightAndChoir.MOD)))
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', jcast('int', jmod(jcast('int', jadd(dp[1][Code03_HeightAndChoir.n][0], dp[1][Code03_HeightAndChoir.n][1])), Code03_HeightAndChoir.MOD)))

    # 时间复杂度O(n^2)
    # 空间压缩
    @staticmethod
    def compute2():
        if (Code03_HeightAndChoir.nums[jcast('int', (Code03_HeightAndChoir.n - 1))] < Code03_HeightAndChoir.nums[Code03_HeightAndChoir.n]):
            jset(Code03_HeightAndChoir.dp[Code03_HeightAndChoir.n], 0, 1)
            jset(Code03_HeightAndChoir.dp[Code03_HeightAndChoir.n], 1, 1)
        l = jcast('int', jcast('int', (Code03_HeightAndChoir.n - 2)))
        while (l >= 1):
            if (Code03_HeightAndChoir.nums[l] < Code03_HeightAndChoir.nums[jcast('int', jadd(l, 1))]):
                jset(Code03_HeightAndChoir.dp[jcast('int', jadd(l, 1))], 0, 1)
                jset(Code03_HeightAndChoir.dp[jcast('int', jadd(l, 1))], 1, 1)
            else:
                jset(Code03_HeightAndChoir.dp[jcast('int', jadd(l, 1))], 0, 0)
                jset(Code03_HeightAndChoir.dp[jcast('int', jadd(l, 1))], 1, 0)
            r = jcast('int', jcast('int', jadd(l, 2)))
            while (r <= Code03_HeightAndChoir.n):
                a = jcast('int', 0)
                b = jcast('int', 0)
                if (Code03_HeightAndChoir.nums[l] < Code03_HeightAndChoir.nums[jcast('int', jadd(l, 1))]):
                    a = jcast('int', jcast('int', jmod(jcast('int', jadd(a, Code03_HeightAndChoir.dp[r][0])), Code03_HeightAndChoir.MOD)))
                if (Code03_HeightAndChoir.nums[l] < Code03_HeightAndChoir.nums[r]):
                    a = jcast('int', jcast('int', jmod(jcast('int', jadd(a, Code03_HeightAndChoir.dp[r][1])), Code03_HeightAndChoir.MOD)))
                if (Code03_HeightAndChoir.nums[r] > Code03_HeightAndChoir.nums[l]):
                    b = jcast('int', jcast('int', jmod(jcast('int', jadd(b, Code03_HeightAndChoir.dp[jcast('int', (r - 1))][0])), Code03_HeightAndChoir.MOD)))
                if (Code03_HeightAndChoir.nums[r] > Code03_HeightAndChoir.nums[jcast('int', (r - 1))]):
                    b = jcast('int', jcast('int', jmod(jcast('int', jadd(b, Code03_HeightAndChoir.dp[jcast('int', (r - 1))][1])), Code03_HeightAndChoir.MOD)))
                jset(Code03_HeightAndChoir.dp[r], 0, a)
                jset(Code03_HeightAndChoir.dp[r], 1, b)
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', jcast('int', jmod(jcast('int', jadd(Code03_HeightAndChoir.dp[Code03_HeightAndChoir.n][0], Code03_HeightAndChoir.dp[Code03_HeightAndChoir.n][1])), Code03_HeightAndChoir.MOD)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_HeightAndChoir.MAXN = jcast('int', 1001)
Code03_HeightAndChoir.nums = jarray('int', [Code03_HeightAndChoir.MAXN])
Code03_HeightAndChoir.dp = jarray('int', [Code03_HeightAndChoir.MAXN, 2])
Code03_HeightAndChoir.n = jcast('int', 0)
Code03_HeightAndChoir.MOD = jcast('int', 19650827)

if __name__ == '__main__':
    Code03_HeightAndChoir.main([])
