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

# 分裂游戏
# 一共有n个瓶子，编号为0 ~ n-1，第i瓶里装有nums[i]个糖豆，每个糖豆认为无差别
# 有两个玩家轮流取糖豆，每一轮的玩家必须选i、j、k三个编号，并且满足i < j <= k
# 当前玩家从i号瓶中拿出一颗糖豆，分裂成两颗糖豆，并且往j、k瓶子中各放入一颗，分裂的糖豆继续无差别
# 要求i号瓶一定要有糖豆，如果j == k，那么相当于从i号瓶中拿出一颗，向另一个瓶子放入了两颗
# 如果轮到某个玩家发现所有糖豆都在n-1号瓶里，导致无法行动，那么该玩家输掉比赛
# 先手希望知道，第一步如何行动可以保证自己获胜，要求返回字典序最小的行动
# 第一步从0号瓶拿出一颗糖豆，并且往2、3号瓶中各放入一颗，可以确保最终自己获胜
# 第一步从0号瓶拿出一颗糖豆，并且往11、13号瓶中各放入一颗，也可以确保自己获胜
# 本题要求每个瓶子的编号看做是一个字符的情况下，最小的字典序，所以返回"0 2 3"
# 如果先手怎么行动都无法获胜，返回"-1 -1 -1"
# 先手还希望知道自己有多少种第一步取糖的行动，可以确保自己获胜，返回方法数
# 测试链接 : https://www.luogu.com.cn/problem/P3185
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_SplitGame:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'sg': 'sg', 'MAXV': 'MAXV', 'appear': 'appear', 't': 't', 'n': 'n'}
    # 20 -> 0
    # 左    右
    MAXN = 0
    nums = None
    sg = None
    MAXV = 0
    appear = None
    t = 0
    n = 0
    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i < Code06_SplitGame.MAXN):
            try:
                jstatic('Arrays', 'fill', Code06_SplitGame.appear, False)
                j = jcast('int', jcast('int', (i - 1)))
                while (j >= 0):
                    k = jcast('int', j)
                    while (k >= 0):
                        jset(Code06_SplitGame.appear, jcast('int', (Code06_SplitGame.sg[j] ^ Code06_SplitGame.sg[k])), True)
                        k = jcast('int', (k - 1))
                    j = jcast('int', (j - 1))
                s = jcast('int', 0)
                while (s < Code06_SplitGame.MAXV):
                    try:
                        if (not Code06_SplitGame.appear[s]):
                            Code06_SplitGame.sg[i] = jcast('int', s)
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    s = jcast('int', (s + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        Code06_SplitGame.build()
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_SplitGame.t = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < Code06_SplitGame.t):
            jcall(in_, 'nextToken')
            Code06_SplitGame.n = jcast('int', jcast('int', jget(in_, 'nval')))
            j = jcast('int', jcast('int', (Code06_SplitGame.n - 1)))
            while (j >= 0):
                jcall(in_, 'nextToken')
                Code06_SplitGame.nums[j] = jcast('int', jcast('int', jget(in_, 'nval')))
                j = jcast('int', (j - 1))
            jcall(out, 'println', Code06_SplitGame.compute())
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        # 每个糖果都是独立游戏，所以把所有糖果的sg值异或
        eor = jcast('int', 0)
        i = jcast('int', jcast('int', (Code06_SplitGame.n - 1)))
        while (i >= 0):
            if (jcast('int', jmod(Code06_SplitGame.nums[i], 2)) == 1):
                eor = jcast('int', jcast('int', (eor ^ Code06_SplitGame.sg[i])))
            i = jcast('int', (i - 1))
        if (eor == 0):
            return jadd('-1 -1 -1\n', '0')
        cnt = jcast('int', 0)
        a = jcast('int', jcast('int', (-1)))
        b = jcast('int', jcast('int', (-1)))
        c = jcast('int', jcast('int', (-1)))
        pos = 0
        i = jcast('int', jcast('int', (Code06_SplitGame.n - 1)))
        while (i >= 1):
            if (Code06_SplitGame.nums[i] > 0):
                j = jcast('int', jcast('int', (i - 1)))
                while (j >= 0):
                    k = jcast('int', j)
                    while (k >= 0):
                        # i j k
                        pos = jcast('int', jcast('int', (jcast('int', (jcast('int', (eor ^ Code06_SplitGame.sg[i])) ^ Code06_SplitGame.sg[j])) ^ Code06_SplitGame.sg[k])))
                        if (pos == 0):
                            cnt = jcast('int', (cnt + 1))
                            if (a == jcast('int', (-1))):
                                a = jcast('int', i)
                                b = jcast('int', j)
                                c = jcast('int', k)
                        k = jcast('int', (k - 1))
                    j = jcast('int', (j - 1))
            i = jcast('int', (i - 1))
        return jstatic('String', 'valueOf', jadd(jadd(jadd(jadd(jadd(jadd(jcast('int', (jcast('int', (Code06_SplitGame.n - 1)) - a)), ' '), jcast('int', (jcast('int', (Code06_SplitGame.n - 1)) - b))), ' '), jcast('int', (jcast('int', (Code06_SplitGame.n - 1)) - c))), '\n'), cnt))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_SplitGame.MAXN = jcast('int', 21)
Code06_SplitGame.nums = jarray('int', [Code06_SplitGame.MAXN])
Code06_SplitGame.sg = jarray('int', [Code06_SplitGame.MAXN])
Code06_SplitGame.MAXV = jcast('int', 101)
Code06_SplitGame.appear = jarray('boolean', [Code06_SplitGame.MAXV])
Code06_SplitGame.t = jcast('int', 0)
Code06_SplitGame.n = jcast('int', 0)

if __name__ == '__main__':
    Code06_SplitGame.main([])
