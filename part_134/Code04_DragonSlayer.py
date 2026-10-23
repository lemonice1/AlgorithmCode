# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 屠龙勇士
# 一共n只巨龙，每只巨龙都有初始血量hp[i]，每只巨龙都有恢复能力recovery[i]
# 每只巨龙都会在攻击结束后开始恢复，初始一共m把剑，每把剑攻击力init[i]
# 每只巨龙只有当血量恰好为0时，才能被杀死。面对某只具体的龙，只能用固定的剑来攻击，规定如下：
# 攻击力不高于当前巨龙的血量，并且攻击力最大的一把剑，如果没有这样的剑，就选择攻击力最低的一把剑
# 需要按1~n的顺序依次讨伐巨龙，i号巨龙被杀后，那把攻击的剑会消失，同时奖励攻击力reward[i]的剑
# 勇士制定的策略如下，不管面对什么巨龙，攻击过程只打击ans下，让当前巨龙的血量<=0
# 然后在当前巨龙恢复的过程中，如果血量恰好为0，那么当前巨龙被杀死，勇士继续讨伐下一只
# 你的任务是算出最小的ans，让勇士可以在该策略下杀死所有巨龙
# 如果在固定打击次数的策略下，就是无法杀死所有巨龙，返回-1
# 查看数据范围可以打开测试链接 : https://www.luogu.com.cn/problem/P4774
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_DragonSlayer:
    __java_fields__ = {'MAXN': 'MAXN', 'hp': 'hp', 'recovery': 'recovery', 'reward': 'reward', 'init': 'init', 'attack': 'attack', 'sorted': 'sorted', 'd': 'd', 'x': 'x', 'y': 'y', 'px': 'px', 'py': 'py'}
    MAXN = 0
    hp = None
    recovery = None
    reward = None
    init = None
    attack = None
    sorted = None
    # 讲解139 - 扩展欧几里得算法
    d = 0
    x = 0
    y = 0
    px = 0
    py = 0
    @staticmethod
    def exgcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        if (b == 0):
            Code04_DragonSlayer.d = jcast('long', a)
            Code04_DragonSlayer.x = jcast('long', 1)
            Code04_DragonSlayer.y = jcast('long', 0)
        else:
            Code04_DragonSlayer.exgcd(b, jcast('long', jmod(a, b)))
            Code04_DragonSlayer.px = jcast('long', Code04_DragonSlayer.x)
            Code04_DragonSlayer.py = jcast('long', Code04_DragonSlayer.y)
            Code04_DragonSlayer.x = jcast('long', Code04_DragonSlayer.py)
            Code04_DragonSlayer.y = jcast('long', jcast('long', (Code04_DragonSlayer.px - jcast('long', (Code04_DragonSlayer.py * jcast('long', jdiv(a, b)))))))

    # 讲解033 - 位运算实现乘法
    # a*b过程每一步都%mod，这么写是防止溢出，也叫龟速乘
    @staticmethod
    def multiply(a, b, mod):
        a = jcast('long', a)
        b = jcast('long', b)
        mod = jcast('long', mod)
        a = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(a, mod)), mod)), mod)))
        b = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(b, mod)), mod)), mod)))
        ans = jcast('long', 0)
        while (b != 0):
            if (jcast('long', (b & 1)) != 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, a)), mod)))
            a = jcast('long', jcast('long', jmod(jcast('long', jadd(a, a)), mod)))
            b = jcast('long', jcast('long', (b >> (1 & 63))))
        return jcast('long', ans)

    # 每只怪物根据血量找到攻击的剑
    # 哪只龙需要砍最多次，才能让其血量<=0，返回最多的次数
    @staticmethod
    def allocate(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        jcall(Code04_DragonSlayer.sorted, 'clear')
        i = jcast('int', 1)
        while (i <= m):
            jcall(Code04_DragonSlayer.sorted, 'put', Code04_DragonSlayer.init[i], jadd(jcall(Code04_DragonSlayer.sorted, 'getOrDefault', Code04_DragonSlayer.init[i], 0), 1))
            i = jcast('int', (i + 1))
        max = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= n):
            sword = jcall(Code04_DragonSlayer.sorted, 'floorKey', Code04_DragonSlayer.hp[i])
            if (sword == None):
                sword = jcall(Code04_DragonSlayer.sorted, 'firstKey')
            Code04_DragonSlayer.attack[i] = jcast('long', sword)
            jcall(Code04_DragonSlayer.sorted, 'put', sword, (jcall(Code04_DragonSlayer.sorted, 'get', sword) - 1))
            if (jcall(Code04_DragonSlayer.sorted, 'get', sword) == 0):
                jcall(Code04_DragonSlayer.sorted, 'remove', sword)
            jcall(Code04_DragonSlayer.sorted, 'put', Code04_DragonSlayer.reward[i], jadd(jcall(Code04_DragonSlayer.sorted, 'getOrDefault', Code04_DragonSlayer.reward[i], 0), 1))
            max = jcast('long', jstatic('Math', 'max', max, jcast('long', jdiv(jcast('long', (jcast('long', jadd(Code04_DragonSlayer.hp[i], Code04_DragonSlayer.attack[i])) - 1)), Code04_DragonSlayer.attack[i]))))
            # 血量 = 血量 % 恢复力，变成余数形式
            Code04_DragonSlayer.hp[i] = jcast('long', jcast('long', jmod(Code04_DragonSlayer.hp[i], Code04_DragonSlayer.recovery[i])))
            i = jcast('int', (i + 1))
        return jcast('long', max)

    # bi * ans ≡ ri(% mi)方程组求解 + 本题对解的特殊处理
    @staticmethod
    def compute(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        # max变量很关键，最后的逻辑需要用到
        # 哪只龙需要砍最多次，才能让其血量<=0，这个最多的次数就是max
        max = jcast('long', Code04_DragonSlayer.allocate(n, m))
        tail = jcast('long', 0)
        lcm = jcast('long', 1)
        tmp = 0
        a = 0
        b = 0
        c = 0
        x0 = 0
        # ans = lcm * x + tail
        i = jcast('int', 1)
        while (i <= n):
            # ai * ans = ai * lcm * x + tail * ai  1号方程
            # ai * ans = ri * y + hi               2号方程
            # ai * lcm * x + ri * y = hi - tail * ai
            a = jcast('long', Code04_DragonSlayer.multiply(Code04_DragonSlayer.attack[i], lcm, Code04_DragonSlayer.recovery[i]))
            b = jcast('long', Code04_DragonSlayer.recovery[i])
            c = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(jcast('long', (Code04_DragonSlayer.hp[i] - jcast('long', (Code04_DragonSlayer.attack[i] * tail)))), b)), b)), b)))
            Code04_DragonSlayer.exgcd(a, b)
            if (jcast('long', jmod(c, Code04_DragonSlayer.d)) != 0):
                return jcast('long', jcast('int', (-1)))
            x0 = jcast('long', Code04_DragonSlayer.multiply(Code04_DragonSlayer.x, jcast('long', jdiv(c, Code04_DragonSlayer.d)), jcast('long', jdiv(b, Code04_DragonSlayer.d))))
            tmp = jcast('long', jcast('long', (lcm * jcast('long', jdiv(b, Code04_DragonSlayer.d)))))
            tail = jcast('long', jcast('long', jmod(jcast('long', jadd(tail, Code04_DragonSlayer.multiply(x0, lcm, tmp))), tmp)))
            lcm = jcast('long', tmp)
            i = jcast('int', (i + 1))
        # 通解 ans = ? * lcm + tail
        # 下面属于本题的特殊处理，注意max变量的含义
        # 上面的大思路是，对每只怪兽，根据如下的公式，整理出同余式
        # ans * a[i] = h[i] + 每只怪兽若干恢复次数 * r[i]
        # 同余式为，ans * a[i] ≡ h[i] (% r[i])
        # 注意！能建立起的同余式，需要默认"每只怪兽若干恢复次数"的范围是整数
        # 最终解出，ans = k * lcm + tail，tail是最小正数解
        # 但实际情况是，"每只怪兽若干恢复次数"毫无疑问是非负的，并不是整个整数域
        # 也就是说，需要确保把每只怪兽的血量砍到<=0，然后才能保证，每只怪兽若干恢复次数>=0
        # 也就是说，ans = k * lcm + tail，需要确保，ans >= max，注意max变量的含义！
        # 如果tail >= max，那么答案就是tail，此时k==0
        # 如果tail < max，想保证ans >= max，其实就是tail + k * lcm >= max
        # k = (max - tail) / lcm，向上取整，也就是k = (max - tail + lcm - 1) / lcm
        # 所以，ans = (max - tail + lcm - 1) / lcm * lcm + tail
        ans = 0
        if (tail >= max):
            ans = jcast('long', tail)
        else:
            ans = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jdiv(jcast('long', (jcast('long', jadd(jcast('long', (max - tail)), lcm)) - 1)), lcm)) * lcm)), tail)))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        cases = jcast('int', jcast('int', jget(in_, 'nval')))
        t = jcast('int', 1)
        while (t <= cases):
            jcall(in_, 'nextToken')
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= n):
                jcall(in_, 'nextToken')
                Code04_DragonSlayer.hp[i] = jcast('long', jcast('long', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= n):
                jcall(in_, 'nextToken')
                Code04_DragonSlayer.recovery[i] = jcast('long', jcast('long', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= n):
                jcall(in_, 'nextToken')
                Code04_DragonSlayer.reward[i] = jcast('long', jcast('long', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= m):
                jcall(in_, 'nextToken')
                Code04_DragonSlayer.init[i] = jcast('long', jcast('long', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_DragonSlayer.compute(n, m))
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_DragonSlayer.MAXN = jcast('int', 100001)
Code04_DragonSlayer.hp = jarray('long', [Code04_DragonSlayer.MAXN])
Code04_DragonSlayer.recovery = jarray('long', [Code04_DragonSlayer.MAXN])
Code04_DragonSlayer.reward = jarray('long', [Code04_DragonSlayer.MAXN])
Code04_DragonSlayer.init = jarray('long', [Code04_DragonSlayer.MAXN])
Code04_DragonSlayer.attack = jarray('long', [Code04_DragonSlayer.MAXN])
Code04_DragonSlayer.sorted = jnew('TreeMap')
Code04_DragonSlayer.d = jcast('long', 0)
Code04_DragonSlayer.x = jcast('long', 0)
Code04_DragonSlayer.y = jcast('long', 0)
Code04_DragonSlayer.px = jcast('long', 0)
Code04_DragonSlayer.py = jcast('long', 0)

if __name__ == '__main__':
    Code04_DragonSlayer.main([])
