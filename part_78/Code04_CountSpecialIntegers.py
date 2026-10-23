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

# 完全没有重复的数字个数
# 给定正整数n，返回在[1, n]范围内每一位都互不相同的正整数个数
# 测试链接 : https://leetcode.cn/problems/count-special-integers/
class Code04_CountSpecialIntegers:
    __java_fields__ = {}
    @staticmethod
    def countSpecialNumbers(n):
        n = jcast('int', n)
        len = jcast('int', 1)
        offset = jcast('int', 1)
        tmp = jcast('int', jcast('int', jdiv(n, 10)))
        while (tmp > 0):
            len = jcast('int', (len + 1))
            offset = jcast('int', jcast('int', (offset * 10)))
            tmp = jcast('int', jcast('int', jdiv(tmp, 10)))
        # cnt[i] :
        # 一共长度为len，还剩i位没有确定，确定的前缀为len-i位，且确定的前缀不为空
        # 0~9一共10个数字，没有选择的数字剩下10-(len-i)个
        # 那么在后续的i位上，有多少种排列
        # 比如：len = 4
        # cnt[4]不计算
        # cnt[3] = 9 * 8 * 7
        # cnt[2] = 8 * 7
        # cnt[1] = 7
        # cnt[0] = 1，表示前缀已确定，后续也没有了，那么就是1种排列，就是前缀的状况
        # 再比如：len = 6
        # cnt[6]不计算
        # cnt[5] = 9 * 8 * 7 * 6 * 5
        # cnt[4] = 8 * 7 * 6 * 5
        # cnt[3] = 7 * 6 * 5
        # cnt[2] = 6 * 5
        # cnt[1] = 5
        # cnt[0] = 1，表示前缀已确定，后续也没有了，那么就是1种排列，就是前缀的状况
        # 下面for循环就是求解cnt的代码
        cnt = jarray('int', [len])
        cnt[0] = jcast('int', 1)
        i = jcast('int', 1)
        k = jcast('int', jcast('int', jadd(jcast('int', (10 - len)), 1)))
        while (i < len):
            cnt[i] = jcast('int', jcast('int', (cnt[jcast('int', (i - 1))] * k)))
            i = jcast('int', (i + 1))
            k = jcast('int', (k + 1))
        ans = jcast('int', 0)
        if (len >= 2):
            # 如果n的位数是len位，先计算位数少于len的数中，每一位都互不相同的正整数个数，并累加
            # 所有1位数中，每一位都互不相同的正整数个数 = 9
            # 所有2位数中，每一位都互不相同的正整数个数 = 9 * 9
            # 所有3位数中，每一位都互不相同的正整数个数 = 9 * 9 * 8
            # 所有4位数中，每一位都互不相同的正整数个数 = 9 * 9 * 8 * 7
            # ...比len少的位数都累加...
            ans = jcast('int', 9)
            i = jcast('int', 2)
            a = jcast('int', 9)
            b = jcast('int', 9)
            while (i < len):
                a = jcast('int', jcast('int', (a * b)))
                ans = jcast('int', jcast('int', jadd(ans, a)))
                i = jcast('int', (i + 1))
                b = jcast('int', (b - 1))
        # 如果n的位数是len位，已经计算了位数少于len个的情况
        # 下面计算一定有len位的数字中，<=n且每一位都互不相同的正整数个数
        first = jcast('int', jcast('int', jdiv(n, offset)))
        # 小于num最高位数字的情况
        ans = jcast('int', jcast('int', jadd(ans, jcast('int', (jcast('int', (first - 1)) * cnt[jcast('int', (len - 1))])))))
        # 后续累加上，等于num最高位数字的情况
        ans = jcast('int', jcast('int', jadd(ans, Code04_CountSpecialIntegers.f(cnt, n, jcast('int', (len - 1)), jcast('int', jdiv(offset, 10)), jcast('int', (1 << (first & 31)))))))
        return jcast('int', ans)

    # 之前已经确定了和num一样的前缀，且确定的部分一定不为空
    # 还有len位没有确定
    # 哪些数字已经选了，哪些数字没有选，用status表示
    # 返回<=num且每一位数字都不一样的正整数有多少个
    @staticmethod
    def f(cnt, num, len, offset, status):
        num = jcast('int', num)
        len = jcast('int', len)
        offset = jcast('int', offset)
        status = jcast('int', status)
        if (len == 0):
            # num自己
            return jcast('int', 1)
        ans = jcast('int', 0)
        # first是num当前位的数字
        first = jcast('int', jcast('int', jmod(jcast('int', jdiv(num, offset)), 10)))
        cur = jcast('int', 0)
        while (cur < first):
            if (jcast('int', (status & jcast('int', (1 << (cur & 31))))) == 0):
                ans = jcast('int', jcast('int', jadd(ans, cnt[jcast('int', (len - 1))])))
            cur = jcast('int', (cur + 1))
        if (jcast('int', (status & jcast('int', (1 << (first & 31))))) == 0):
            ans = jcast('int', jcast('int', jadd(ans, Code04_CountSpecialIntegers.f(cnt, num, jcast('int', (len - 1)), jcast('int', jdiv(offset, 10)), jcast('int', (status | jcast('int', (1 << (first & 31)))))))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


