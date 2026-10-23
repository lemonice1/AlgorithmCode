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

# 最长递增子序列字典序最小的结果
# 给定数组arr，设长度为n
# 输出arr的最长递增子序列
# 如果有多个答案，请输出其中字典序最小的
# 注意这道题的字典序设定（根据提交的结果推论的）：
# 每个数字看作是单独的字符，比如120认为比36的字典序大
# 保证从左到右每个数字尽量小
# 测试链接 : https://www.nowcoder.com/practice/30fb9b3cab9742ecae9acda1c75bf927
# 测试链接 : https://www.luogu.com.cn/problem/T386911
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 讲解072 - 最长递增子序列及其扩展
class Code03_LIS:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'dp': 'dp_data', 'ends': 'ends', 'ans': 'ans', 'n': 'n', 'k': 'k'}
    MAXN = 0
    nums = None
    dp_data = None
    ends = None
    ans = None
    n = 0
    k = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_LIS.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code03_LIS.n):
                jcall(in_, 'nextToken')
                Code03_LIS.nums[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            Code03_LIS.lis()
            i = jcast('int', 0)
            while (i < jcast('int', (Code03_LIS.k - 1))):
                jcall(out, 'print', jadd(Code03_LIS.ans[i], ' '))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_LIS.ans[jcast('int', (Code03_LIS.k - 1))])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # nums[...]
    @staticmethod
    def lis():
        Code03_LIS.k = jcast('int', Code03_LIS.dp())
        jstatic('Arrays', 'fill', Code03_LIS.ans, 0, Code03_LIS.k, jget(Integer, 'MAX_VALUE'))
        i = jcast('int', 0)
        while (i < Code03_LIS.n):
            if (Code03_LIS.dp_data[i] == Code03_LIS.k):
                # 注意这里
                # 为什么不用判断直接设置
                # 有讲究，课上重点讲了
                Code03_LIS.ans[0] = jcast('int', Code03_LIS.nums[i])
            else:
                if (Code03_LIS.ans[jcast('int', (jcast('int', (Code03_LIS.k - Code03_LIS.dp_data[i])) - 1))] < Code03_LIS.nums[i]):
                    # 注意这里
                    # 为什么只需要判断比前一位(ans[k-dp[i]-1])大即可
                    # 有讲究，课上重点讲了
                    jset(Code03_LIS.ans, jcast('int', (Code03_LIS.k - Code03_LIS.dp_data[i])), Code03_LIS.nums[i])
            i = jcast('int', (i + 1))

    # dp[i] : 必须以i位置的数字开头的情况下，最长递增子序列长度
    # 填好dp表 + 返回最长递增子序列长度
    @staticmethod
    def dp():
        len = jcast('int', 0)
        i = jcast('int', jcast('int', (Code03_LIS.n - 1)))
        find = 0
        while (i >= 0):
            find = jcast('int', Code03_LIS.bs(len, Code03_LIS.nums[i]))
            if (find == jcast('int', (-1))):
                jset(Code03_LIS.ends, ((_java_old_1 := len), (len := jcast('int', (len + (1)))), _java_old_1)[2], Code03_LIS.nums[i])
                Code03_LIS.dp_data[i] = jcast('int', len)
            else:
                Code03_LIS.ends[find] = jcast('int', Code03_LIS.nums[i])
                Code03_LIS.dp_data[i] = jcast('int', jcast('int', jadd(find, 1)))
            i = jcast('int', (i - 1))
        return jcast('int', len)

    # ends[有效区]从大到小的
    # 二分的方式找<=num的最左位置
    @staticmethod
    def bs(len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (len - 1)))
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code03_LIS.ends[m] <= num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_LIS.MAXN = jcast('int', 100001)
Code03_LIS.nums = jarray('int', [Code03_LIS.MAXN])
Code03_LIS.dp_data = jarray('int', [Code03_LIS.MAXN])
Code03_LIS.ends = jarray('int', [Code03_LIS.MAXN])
Code03_LIS.ans = jarray('int', [Code03_LIS.MAXN])
Code03_LIS.n = jcast('int', 0)
Code03_LIS.k = jcast('int', 0)

if __name__ == '__main__':
    Code03_LIS.main([])
