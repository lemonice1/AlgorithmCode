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

# 刀砍毒杀怪兽问题
# 怪兽的初始血量是一个整数hp，给出每一回合刀砍和毒杀的数值cuts和poisons
# 第i回合如果用刀砍，怪兽在这回合会直接损失cuts[i]的血，不再有后续效果
# 第i回合如果用毒杀，怪兽在这回合不会损失血量，但是之后每回合都损失poisons[i]的血量
# 并且你选择的所有毒杀效果，在之后的回合都会叠加
# 两个数组cuts、poisons，长度都是n，代表你一共可以进行n回合
# 每一回合你只能选择刀砍或者毒杀中的一个动作
# 如果你在n个回合内没有直接杀死怪兽，意味着你已经无法有新的行动了
# 但是怪兽如果有中毒效果的话，那么怪兽依然会在血量耗尽的那回合死掉
# 返回至少多少回合，怪兽会死掉
# 数据范围 :
# 1 <= n <= 10^5
# 1 <= hp <= 10^9
# 1 <= cuts[i]、poisons[i] <= 10^9
# 本题来自真实大厂笔试，找不到测试链接，所以用对数器验证
class Code07_CutOrPoison:
    __java_fields__ = {}
    # 动态规划方法(只是为了验证)
    # 目前没有讲动态规划，所以不需要理解这个函数
    # 这个函数只是为了验证二分答案的方法是否正确的
    # 纯粹为了写对数器验证才设计的方法，血量比较大的时候会超时
    # 这个方法不做要求，此时并不需要理解，可以在学习完动态规划章节之后来看看这个函数
    @staticmethod
    def fast1(cuts, poisons, hp):
        hp = jcast('int', hp)
        sum = jcast('int', 0)
        for num in poisons:
            sum = jcast('int', jcast('int', jadd(sum, num)))
        dp = jarray('int', [jget(cuts, 'length'), jcast('int', jadd(hp, 1)), jcast('int', jadd(sum, 1))])
        return jcast('int', Code07_CutOrPoison.f1(cuts, poisons, 0, hp, 0, dp))

    # 不做要求
    @staticmethod
    def f1(cuts, poisons, i, r, p, dp):
        i = jcast('int', i)
        r = jcast('int', r)
        p = jcast('int', p)
        r = jcast('int', jcast('int', (r - p)))
        if (r <= 0):
            return jcast('int', jcast('int', jadd(i, 1)))
        if (i == jget(cuts, 'length')):
            if (p == 0):
                return jcast('int', jget(Integer, 'MAX_VALUE'))
            else:
                return jcast('int', jcast('int', jadd(jcast('int', jadd(jget(cuts, 'length'), 1)), jcast('int', jdiv(jcast('int', (jcast('int', jadd(r, p)) - 1)), p)))))
        if (dp[i][r][p] != 0):
            return jcast('int', dp[i][r][p])
        p1 = jcast('int', (jcast('int', jadd(i, 1)) if (r <= cuts[i]) else Code07_CutOrPoison.f1(cuts, poisons, jcast('int', jadd(i, 1)), jcast('int', (r - cuts[i])), p, dp)))
        p2 = jcast('int', Code07_CutOrPoison.f1(cuts, poisons, jcast('int', jadd(i, 1)), r, jcast('int', jadd(p, poisons[i])), dp))
        ans = jcast('int', jstatic('Math', 'min', p1, p2))
        jset(dp[i][r], p, ans)
        return jcast('int', ans)

    # 二分答案法
    # 最优解
    # 时间复杂度O(n * log(hp))，额外空间复杂度O(1)
    @staticmethod
    def fast2(cuts, poisons, hp):
        hp = jcast('int', hp)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        l = jcast('int', 1)
        r = jcast('int', jcast('int', jadd(hp, 1)))
        m = 0
        while (l <= r):
            # m中点，一定要让怪兽在m回合内死掉，更多回合无意义
            m = jcast('int', jcast('int', jadd(l, jcast('int', (jcast('int', (r - l)) >> (1 & 31))))))
            if Code07_CutOrPoison.f(cuts, poisons, hp, m):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # cuts、posions，每一回合刀砍、毒杀的效果
    # hp：怪兽血量
    # limit：回合的限制
    @staticmethod
    def f(cuts, posions, hp, limit):
        hp = jcast('long', hp)
        limit = jcast('int', limit)
        n = jcast('int', jstatic('Math', 'min', jget(cuts, 'length'), limit))
        i = jcast('int', 0)
        j = jcast('int', 1)
        while (i < n):
            hp = jcast('long', jcast('long', (hp - jstatic('Math', 'max', jcast('long', cuts[i]), jcast('long', (jcast('long', jcast('int', (limit - j))) * jcast('long', posions[i])))))))
            if (hp <= 0):
                return jcast('boolean', True)
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        return jcast('boolean', False)

    # 对数器测试
    @staticmethod
    def main(args):
        # 随机测试的数据量不大
        # 因为数据量大了，fast1方法会超时
        # 所以在数据量不大的情况下，验证fast2方法功能正确即可
        # fast2 方法用于优化大规模输入的求解
        # 因为时间复杂度就是最优的
        jprint('测试开始', newline=True)
        N = jcast('int', 30)
        V = jcast('int', 20)
        H = jcast('int', 300)
        testTimes = jcast('int', 10000)
        i = jcast('int', 0)
        while (i < testTimes):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            cuts = Code07_CutOrPoison.randomArray(n, V)
            posions = Code07_CutOrPoison.randomArray(n, V)
            hp = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * H)), 1)))
            ans1 = jcast('int', Code07_CutOrPoison.fast1(cuts, posions, hp))
            ans2 = jcast('int', Code07_CutOrPoison.fast2(cuts, posions, hp))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    # 对数器测试
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            i = jcast('int', (i + 1))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code07_CutOrPoison.main([])
