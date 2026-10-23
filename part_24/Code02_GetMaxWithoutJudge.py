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

# 不用任何判断语句和比较操作，返回两个数的最大值
# 测试链接 : https://www.nowcoder.com/practice/d2707eaf98124f1e8f1d9c18ad487f76
class Code02_GetMaxWithoutJudge:
    __java_fields__ = {}
    # 必须保证n一定是0或者1
    # 0变1，1变0
    @staticmethod
    def flip(n):
        n = jcast('int', n)
        return jcast('int', jcast('int', (n ^ 1)))

    # 非负数返回1
    # 负数返回0
    @staticmethod
    def sign(n):
        n = jcast('int', n)
        return jcast('int', Code02_GetMaxWithoutJudge.flip(jcast('int', jushr(n, 31, 32))))

    # 有溢出风险的实现
    @staticmethod
    def getMax1(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', jcast('int', (a - b)))
        # c非负，returnA -> 1
        # c非负，returnB -> 0
        # c负数，returnA -> 0
        # c负数，returnB -> 1
        returnA = jcast('int', Code02_GetMaxWithoutJudge.sign(c))
        returnB = jcast('int', Code02_GetMaxWithoutJudge.flip(returnA))
        return jcast('int', jcast('int', jadd(jcast('int', (a * returnA)), jcast('int', (b * returnB)))))

    # 没有任何问题的实现
    @staticmethod
    def getMax2(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        # c可能是溢出的
        c = jcast('int', jcast('int', (a - b)))
        # a的符号
        sa = jcast('int', Code02_GetMaxWithoutJudge.sign(a))
        # b的符号
        sb = jcast('int', Code02_GetMaxWithoutJudge.sign(b))
        # c的符号
        sc = jcast('int', Code02_GetMaxWithoutJudge.sign(c))
        # 判断A和B，符号是不是不一样，如果不一样diffAB=1，如果一样diffAB=0
        diffAB = jcast('int', jcast('int', (sa ^ sb)))
        # 判断A和B，符号是不是一样，如果一样sameAB=1，如果不一样sameAB=0
        sameAB = jcast('int', Code02_GetMaxWithoutJudge.flip(diffAB))
        returnA = jcast('int', jcast('int', jadd(jcast('int', (diffAB * sa)), jcast('int', (sameAB * sc)))))
        returnB = jcast('int', Code02_GetMaxWithoutJudge.flip(returnA))
        return jcast('int', jcast('int', jadd(jcast('int', (a * returnA)), jcast('int', (b * returnB)))))

    @staticmethod
    def main(args):
        a = jcast('int', jget(Integer, 'MIN_VALUE'))
        b = jcast('int', jget(Integer, 'MAX_VALUE'))
        # getMax1方法会错误，因为溢出
        jprint(Code02_GetMaxWithoutJudge.getMax1(a, b), newline=True)
        # getMax2方法永远正确
        jprint(Code02_GetMaxWithoutJudge.getMax2(a, b), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


# 下面为对应算法的 Python 实现，保留原算法逻辑
# 测试链接 : https://www.nowcoder.com/practice/d2707eaf98124f1e8f1d9c18ad487f76
# 原替代实现已转换为对应的 Python 模块
#
# using namespace std;
#
# class Solution {
# public:
# static int flip(int n) {
# return n ^ 1;
# }
#
# static int sign(int n) {
# return flip((uint32_t) n >> 31);
# }
#
# static int getMax(int a, int b) {
# uint32_t c = (uint32_t) a - (uint32_t) b;
# int sa = sign(a);
# int sb = sign(b);
# int sc = flip(c >> 31);
# int diffAB = sa ^ sb;
# int sameAB = flip(diffAB);
# int returnA = diffAB * sa + sameAB * sc;
# int returnB = flip(returnA);
# return a * returnA + b * returnB;
# }
# };

if __name__ == '__main__':
    Code02_GetMaxWithoutJudge.main([])
