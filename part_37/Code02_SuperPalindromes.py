# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 超级回文数(Python版)
# 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
# 现在，给定两个正整数 L 和 R （以字符串形式表示），
# 返回包含在范围 [L, R] 中的超级回文数的数目。
# 1 <= len(L) <= 18
# 1 <= len(R) <= 18
# L 和 R 是表示 [1, 10^18) 范围的整数的字符串
# 测试链接 : https://leetcode.cn/problems/super-palindromes/
class Code02_SuperPalindromes:
    __java_fields__ = {'record': 'record'}
    # [left, right]有多少超级回文数
    # 返回数量
    @staticmethod
    def superpalindromesInRange1(left, right):
        l = jcast('long', jstatic('Long', 'valueOf', left))
        r = jcast('long', jstatic('Long', 'valueOf', right))
        # l....r  long
        # x根号，范围limit
        limit = jcast('long', jcast('long', jstatic('Math', 'sqrt', jcast('double', r))))
        # seed : 枚举量很小，10^18 -> 10^9 -> 10^5
        # seed : 奇数长度回文、偶数长度回文
        seed = jcast('long', 1)
        # num : 根号x，num^2 -> x
        num = jcast('long', 0)
        ans = jcast('int', 0)
        while True:
            # seed生成偶数长度回文数字
            # 123 -> 123321
            num = jcast('long', Code02_SuperPalindromes.evenEnlarge(seed))
            if Code02_SuperPalindromes.check(jcast('long', (num * num)), l, r):
                ans = jcast('int', (ans + 1))
            # seed生成奇数长度回文数字
            # 123 -> 12321
            num = jcast('long', Code02_SuperPalindromes.oddEnlarge(seed))
            if Code02_SuperPalindromes.check(jcast('long', (num * num)), l, r):
                ans = jcast('int', (ans + 1))
            # 123 -> 124 -> 125
            seed = jcast('long', (seed + 1))
            if not ((num < limit)):
                break
        return jcast('int', ans)

    # 根据种子扩充到偶数长度的回文数字并返回
    @staticmethod
    def evenEnlarge(seed):
        seed = jcast('long', seed)
        ans = jcast('long', seed)
        while (seed != 0):
            ans = jcast('long', jcast('long', jadd(jcast('long', (ans * 10)), jcast('long', jmod(seed, 10)))))
            seed = jcast('long', jcast('long', jdiv(seed, 10)))
        return jcast('long', ans)

    # 根据种子扩充到奇数长度的回文数字并返回
    @staticmethod
    def oddEnlarge(seed):
        seed = jcast('long', seed)
        ans = jcast('long', seed)
        seed = jcast('long', jcast('long', jdiv(seed, 10)))
        while (seed != 0):
            ans = jcast('long', jcast('long', jadd(jcast('long', (ans * 10)), jcast('long', jmod(seed, 10)))))
            seed = jcast('long', jcast('long', jdiv(seed, 10)))
        return jcast('long', ans)

    # 判断ans是不是属于[l,r]范围的回文数
    @staticmethod
    def check(ans, l, r):
        ans = jcast('long', ans)
        l = jcast('long', l)
        r = jcast('long', r)
        return jcast('boolean', (((ans >= l) and (ans <= r)) and Code02_SuperPalindromes.isPalindrome(ans)))

    # 验证long类型的数字num，是不是回文数字
    @staticmethod
    def isPalindrome(num):
        num = jcast('long', num)
        offset = jcast('long', 1)
        # 注意这么写是为了防止溢出
        while (jcast('long', jdiv(num, offset)) >= 10):
            offset = jcast('long', jcast('long', (offset * 10)))
        # num    : 52725
        # offset : 10000
        # 首尾判断
        while (num != 0):
            if (jcast('long', jdiv(num, offset)) != jcast('long', jmod(num, 10))):
                return jcast('boolean', False)
            num = jcast('long', jcast('long', jdiv(jcast('long', jmod(num, offset)), 10)))
            offset = jcast('long', jcast('long', jdiv(offset, 100)))
        return jcast('boolean', True)

    # 打表的方法
    # 必然最优解
    # 连二分都懒得用
    @staticmethod
    def superpalindromesInRange2(left, right):
        l = jcast('long', jstatic('Long', 'parseLong', left))
        r = jcast('long', jstatic('Long', 'parseLong', right))
        i = jcast('int', 0)
        while (i < jget(Code02_SuperPalindromes.record, 'length')):
            try:
                if (Code02_SuperPalindromes.record[i] >= l):
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        j = jcast('int', jcast('int', (jget(Code02_SuperPalindromes.record, 'length') - 1)))
        while (j >= 0):
            try:
                if (Code02_SuperPalindromes.record[j] <= r):
                    raise JBreak(None)
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
            j = jcast('int', (j - 1))
        return jcast('int', jcast('int', jadd(jcast('int', (j - i)), 1)))

    record = None
    @staticmethod
    def collect():
        l = jcast('long', 1)
        r = jcast('long', jget(Long, 'MAX_VALUE'))
        limit = jcast('long', jcast('long', jstatic('Math', 'sqrt', jcast('double', r))))
        seed = jcast('long', 1)
        enlarge = jcast('long', 0)
        ans = jnew('ArrayList')
        while True:
            enlarge = jcast('long', Code02_SuperPalindromes.evenEnlarge(seed))
            if Code02_SuperPalindromes.check(jcast('long', (enlarge * enlarge)), l, r):
                jcall(ans, 'add', jcast('long', (enlarge * enlarge)))
            enlarge = jcast('long', Code02_SuperPalindromes.oddEnlarge(seed))
            if Code02_SuperPalindromes.check(jcast('long', (enlarge * enlarge)), l, r):
                jcall(ans, 'add', jcast('long', (enlarge * enlarge)))
            seed = jcast('long', (seed + 1))
            if not ((enlarge < limit)):
                break
        jcall(ans, 'sort', (lambda a, b: jcall(a, 'compareTo', b)))
        return ans

    @staticmethod
    def main(args):
        ans = Code02_SuperPalindromes.collect()
        for p in ans:
            jprint(jadd(p, 'L,'), newline=True)
        jprint(jadd('size : ', jcall(ans, 'size')), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SuperPalindromes.record = jarray('long', [None], [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 400000080000004, 10000000200000001, 10002000300020001, 10004000600040001, 10020210401202001, 10022212521222001, 10024214841242001, 10201020402010201, 10203040504030201, 10205060806050201, 10221432623412201, 10223454745432201, 12100002420000121, 12102202520220121, 12104402820440121, 12122232623222121, 12124434743442121, 12321024642012321, 12323244744232321, 12343456865434321, 12345678987654321, 40000000800000004, 40004000900040004, 1000000002000000001, 1000220014100220001, 1002003004003002001, 1002223236323222001, 1020100204020010201, 1020322416142230201, 1022123226223212201, 1022345658565432201, 1210000024200000121, 1210242036302420121, 1212203226223022121, 1212445458545442121, 1232100246420012321, 1232344458544432321, 1234323468643234321, 4000000008000000004])

if __name__ == '__main__':
    Code02_SuperPalindromes.main([])
