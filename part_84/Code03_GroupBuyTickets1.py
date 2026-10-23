# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 组团买票
# 景区里一共有m个项目，景区的第i个项目有如下两个参数：
# game[i] = { Ki, Bi }，Ki、Bi一定是正数
# Ki代表折扣系数，Bi代表票价
# 举个例子 : Ki = 2, Bi = 10
# 如果只有1个人买票，单张门票的价格为 : Bi - Ki * 1 = 8
# 所以这1个人游玩该项目要花8元
# 如果有2个人买票，单张门票的价格为 : Bi - Ki * 2 = 6
# 所以这2个人游玩该项目要花6 * 2 = 12元
# 如果有5个人买票，单张门票的价格为 : Bi - Ki * 5 = 0
# 所以这5个人游玩该项目要花5 * 0 = 0元
# 如果有更多人买票，都认为花0元(因为让项目倒贴钱实在是太操蛋了)
# 于是可以认为，如果有x个人买票，单张门票的价格为 : Bi - Ki * x
# x个人游玩这个项目的总花费是 : max { x * (Bi - Ki * x), 0 }
# 单位一共有n个人，每个人最多可以选1个项目来游玩，也可以不选任何项目
# 所有员工将在明晚提交选择，然后由你去按照上面的规则，统一花钱购票
# 你想知道自己需要准备多少钱，就可以应付所有可能的情况，返回这个最保险的钱数
# 数据量描述 :
# 1 <= M、N、Ki、Bi <= 10^5
# 来自真实大厂笔试，没有在线测试，对数器验证
class Code03_GroupBuyTickets1:
    __java_fields__ = {}
    # 暴力方法
    # 为了验证
    # 每个人做出所有可能的选择
    # 时间复杂度O((m+1)的n次方)
    @staticmethod
    def enough1(n, games):
        n = jcast('int', n)
        m = jcast('int', jget(games, 'length'))
        cnts = jarray('int', [m])
        return jcast('int', Code03_GroupBuyTickets1.f(0, n, m, games, cnts))

    @staticmethod
    def f(i, n, m, games, cnts):
        i = jcast('int', i)
        n = jcast('int', n)
        m = jcast('int', m)
        if (i == n):
            ans = jcast('int', 0)
            j = jcast('int', 0)
            k = 0
            b = 0
            x = 0
            while (j < m):
                k = jcast('int', games[j][0])
                b = jcast('int', games[j][1])
                x = jcast('int', cnts[j])
                ans = jcast('int', jcast('int', jadd(ans, jstatic('Math', 'max', jcast('int', (jcast('int', (b - jcast('int', (k * x)))) * x)), 0))))
                j = jcast('int', (j + 1))
            return jcast('int', ans)
        else:
            ans = jcast('int', Code03_GroupBuyTickets1.f(jcast('int', jadd(i, 1)), n, m, games, cnts))
            j = jcast('int', 0)
            while (j < m):
                cnts[j] = jcast('int', (cnts[j] + 1))
                ans = jcast('int', jstatic('Math', 'max', ans, Code03_GroupBuyTickets1.f(jcast('int', jadd(i, 1)), n, m, games, cnts)))
                cnts[j] = jcast('int', (cnts[j] - 1))
                j = jcast('int', (j + 1))
            return jcast('int', ans)

    # 正式方法
    # 时间复杂度O(n * logm)
    @staticmethod
    def enough2(n, games):
        n = jcast('int', n)
        # 哪个项目，再来一人挣得最多
        # 大根堆
        heap = jnew('PriorityQueue', (lambda a, b: (jcall(b, 'earn') - jcall(a, 'earn'))))
        for g in games:
            jcall(heap, 'add', Code03_GroupBuyTickets1.Game(g[0], g[1], _java_ctor=0))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            try:
                # 一个个的人，依次送到当前最挣钱的项目里去
                if (jcall(jcall(heap, 'peek'), 'earn') <= 0):
                    raise JBreak(None)
                cur = jcall(heap, 'poll')
                ans = jcast('int', jcast('int', jadd(ans, jcall(cur, 'earn'))))
                cur.people = jcast('int', (cur.people + 1))
                jcall(heap, 'add', cur)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    class Game:
        __java_fields__ = {'ki': 'ki', 'bi': 'bi', 'people': 'people'}
        # 折扣系数
        # ki：实例字段，在构造函数中初始化。
        # 门票原价
        # bi：实例字段，在构造函数中初始化。
        # 之前的人数
        # people：实例字段，在构造函数中初始化。
        def _java_init_0(self, k, b):
            k = jcast('int', k)
            b = jcast('int', b)
            self.ki = jcast('int', k)
            self.bi = jcast('int', b)
            self.people = jcast('int', 0)

        # 如果再来一人，这个项目得到多少钱
        def earn(self):
            # bi - (people + 1) * ki : 当前的人，门票原价减少了，当前的门票价格
            # people * ki : 当前人的到来，之前的所有人，门票价格都再减去ki
            return jcast('int', jcast('int', (jcast('int', (self.bi - jcast('int', (jcast('int', jadd(self.people, 1)) * self.ki)))) - jcast('int', (self.people * self.ki)))))

        def __init__(self, *args, _java_ctor=None):
            self.ki = jcast('int', 0)
            self.bi = jcast('int', 0)
            self.people = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_GroupBuyTickets1.Game.Game")


    # 为了验证
    @staticmethod
    def randomGames(m, v):
        m = jcast('int', m)
        v = jcast('int', v)
        ans = jarray('int', [m, 2])
        i = jcast('int', 0)
        while (i < m):
            jset(ans[i], 0, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            jset(ans[i], 1, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            i = jcast('int', (i + 1))
        return ans

    # 为了验证
    @staticmethod
    def main(args):
        N = jcast('int', 8)
        M = jcast('int', 8)
        V = jcast('int', 20)
        testTimes = jcast('int', 2000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= testTimes):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            m = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * M)), 1)))
            games = Code03_GroupBuyTickets1.randomGames(m, V)
            ans1 = jcast('int', Code03_GroupBuyTickets1.enough1(n, games))
            ans2 = jcast('int', Code03_GroupBuyTickets1.enough2(n, games))
            if (ans1 != ans2):
                jprint('出错了！', newline=True)
            if (jcast('int', jmod(i, 100)) == 0):
                jprint(jadd(jadd('测试到第', i), '组'), newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_GroupBuyTickets1.main([])
