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

# 大鱼吃小鱼问题
# 给定一个数组arr，每个值代表鱼的体重
# 每一轮每条鱼都会吃掉右边离自己最近比自己体重小的鱼，每条鱼向右找只吃一条
# 但是吃鱼这件事是同时发生的，也就是同一轮在A吃掉B的同时，A也可能被别的鱼吃掉
# 如果有多条鱼在当前轮找到的是同一条小鱼，那么在这一轮，这条小鱼同时被这些大鱼吃
# 请问多少轮后，鱼的数量就固定了
# 比如 : 8 3 1 5 6 7 2 4
# 第一轮 : 8吃3；3吃1；5、6、7吃2；4没有被吃。数组剩下 8 5 6 7 4
# 第二轮 : 8吃5；5、6、7吃4。数组剩下 8 6 7
# 第三轮 : 8吃6。数组剩下 8 7
# 第四轮 : 8吃7。数组剩下 8。
# 过程结束，返回4
# 测试链接 : https://www.nowcoder.com/practice/77199defc4b74b24b8ebf6244e1793de
# 测试链接 : https://leetcode.cn/problems/steps-to-make-array-non-decreasing/
class Code03_BigFishEatSmallFish:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'stack': 'stack', 'r': 'r', 'MAXM': 'MAXM', 's': 's', 'size': 'size'}
    MAXN = 0
    arr = None
    n = 0
    stack = None
    r = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_BigFishEatSmallFish.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code03_BigFishEatSmallFish.n):
                jcall(in_, 'nextToken')
                Code03_BigFishEatSmallFish.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_BigFishEatSmallFish.turns())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # arr[0...n-1]鱼的体重
    # stack[...]随便用
    @staticmethod
    def turns():
        Code03_BigFishEatSmallFish.r = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', jcast('int', (Code03_BigFishEatSmallFish.n - 1)))
        curTurns = 0
        while (i >= 0):
            # i号鱼，arr[i]
            # 0轮是初始
            curTurns = jcast('int', 0)
            while ((Code03_BigFishEatSmallFish.r > 0) and (Code03_BigFishEatSmallFish.stack[jcast('int', (Code03_BigFishEatSmallFish.r - 1))][0] < Code03_BigFishEatSmallFish.arr[i])):
                curTurns = jcast('int', jstatic('Math', 'max', jcast('int', jadd(curTurns, 1)), Code03_BigFishEatSmallFish.stack[((_java_obj_1 := Code03_BigFishEatSmallFish), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3]][1]))
            jset(Code03_BigFishEatSmallFish.stack[Code03_BigFishEatSmallFish.r], 0, Code03_BigFishEatSmallFish.arr[i])
            jset(Code03_BigFishEatSmallFish.stack[((_java_obj_4 := Code03_BigFishEatSmallFish), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]], 1, curTurns)
            ans = jcast('int', jstatic('Math', 'max', ans, curTurns))
            i = jcast('int', (i - 1))
        return jcast('int', ans)

    # 也找到了leetcode测试链接
    # 测试链接 : https://leetcode.cn/problems/steps-to-make-array-non-decreasing/
    # Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
    MAXM = 0
    s = None
    size = 0
    @staticmethod
    def totalSteps(arr):
        Code03_BigFishEatSmallFish.size = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', jcast('int', (jget(arr, 'length') - 1)))
        curTurns = 0
        while (i >= 0):
            curTurns = jcast('int', 0)
            while ((Code03_BigFishEatSmallFish.size > 0) and (Code03_BigFishEatSmallFish.s[jcast('int', (Code03_BigFishEatSmallFish.size - 1))][0] < arr[i])):
                curTurns = jcast('int', jstatic('Math', 'max', jcast('int', jadd(curTurns, 1)), Code03_BigFishEatSmallFish.s[((_java_obj_7 := Code03_BigFishEatSmallFish), (_java_key_8 := 'size'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3]][1]))
            jset(Code03_BigFishEatSmallFish.s[Code03_BigFishEatSmallFish.size], 0, arr[i])
            jset(Code03_BigFishEatSmallFish.s[((_java_obj_10 := Code03_BigFishEatSmallFish), (_java_key_11 := 'size'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]], 1, curTurns)
            ans = jcast('int', jstatic('Math', 'max', ans, curTurns))
            i = jcast('int', (i - 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_BigFishEatSmallFish.MAXN = jcast('int', 100001)
Code03_BigFishEatSmallFish.arr = jarray('int', [Code03_BigFishEatSmallFish.MAXN])
Code03_BigFishEatSmallFish.n = jcast('int', 0)
Code03_BigFishEatSmallFish.stack = jarray('int', [Code03_BigFishEatSmallFish.MAXN, 2])
Code03_BigFishEatSmallFish.r = jcast('int', 0)
Code03_BigFishEatSmallFish.MAXM = jcast('int', 100001)
Code03_BigFishEatSmallFish.s = jarray('int', [Code03_BigFishEatSmallFish.MAXM, 2])
Code03_BigFishEatSmallFish.size = jcast('int', 0)

if __name__ == '__main__':
    Code03_BigFishEatSmallFish.main([])
