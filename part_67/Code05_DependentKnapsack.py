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

# 有依赖的背包(模版)
# 物品分为两大类：主件和附件
# 主件的购买没有限制，钱够就可以；附件的购买有限制，该附件所归属的主件先购买，才能购买这个附件
# 例如，若想买打印机或扫描仪这样的附件，必须先购买电脑这个主件
# 以下是一些主件及其附件的展示：
# 电脑：打印机，扫描仪 | 书柜：图书 | 书桌：台灯，文具 | 工作椅：无附件
# 每个主件最多有2个附件，并且附件不会再有附件，主件购买后，怎么去选择归属附件完全随意，钱够就可以
# 所有的物品编号都在1~m之间，每个物品有三个信息：价格v、重要度p、归属q
# 价格就是花费，价格 * 重要度 就是收益，归属就是该商品是依附于哪个编号的主件
# 比如一件商品信息为[300,2,6]，花费300，收益600，该商品是6号主件商品的附件
# 再比如一件商品信息[100,4,0]，花费100，收益400，该商品自身是主件(q==0)
# 给定m件商品的信息，给定总钱数n，返回在不违反购买规则的情况下最大的收益
# 测试链接 : https://www.luogu.com.cn/problem/P1064
# 测试链接 : https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_DependentKnapsack:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'cost': 'cost', 'val': 'val', 'king': 'king', 'fans': 'fans', 'follows': 'follows', 'dp': 'dp', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    cost = None
    val = None
    king = None
    fans = None
    follows = None
    dp = None
    n = 0
    m = 0
    @staticmethod
    def clean():
        i = jcast('int', 1)
        while (i <= Code05_DependentKnapsack.m):
            Code05_DependentKnapsack.fans[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code05_DependentKnapsack.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_DependentKnapsack.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_DependentKnapsack.clean()
            i = jcast('int', 1)
            v = 0
            p = 0
            q = 0
            while (i <= Code05_DependentKnapsack.m):
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                p = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                q = jcast('int', jcast('int', jget(in_, 'nval')))
                Code05_DependentKnapsack.cost[i] = jcast('int', v)
                Code05_DependentKnapsack.val[i] = jcast('int', jcast('int', (v * p)))
                Code05_DependentKnapsack.king[i] = jcast('boolean', (q == 0))
                if (q != 0):
                    jset(Code05_DependentKnapsack.follows[q], ((_java_obj_1 := Code05_DependentKnapsack.fans), (_java_key_2 := q), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], i)
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code05_DependentKnapsack.compute2())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 严格位置依赖的动态规划
    @staticmethod
    def compute1():
        # dp[0][....] = 0 : 无商品的时候
        dp = jarray('int', [jcast('int', jadd(Code05_DependentKnapsack.m, 1)), jcast('int', jadd(Code05_DependentKnapsack.n, 1))])
        # p : 上次展开的主商品编号
        p = jcast('int', 0)
        i = jcast('int', 1)
        fan1 = 0
        fan2 = 0
        while (i <= Code05_DependentKnapsack.m):
            if Code05_DependentKnapsack.king[i]:
                j = jcast('int', 0)
                while (j <= Code05_DependentKnapsack.n):
                    # dp[i][j] : 0...i范围上，只关心主商品，并且进行展开
                    # 花费不超过j的情况下，获得的最大收益
                    # 可能性1 : 不考虑当前主商品
                    jset(dp[i], j, dp[p][j])
                    if (jcast('int', (j - Code05_DependentKnapsack.cost[i])) >= 0):
                        # 可能性2 : 考虑当前主商品，只要主
                        jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(dp[p][jcast('int', (j - Code05_DependentKnapsack.cost[i]))], Code05_DependentKnapsack.val[i]))))
                    # fan1 : 如果有附1商品，编号给fan1，如果没有，fan1 == -1
                    # fan2 : 如果有附2商品，编号给fan2，如果没有，fan2 == -1
                    fan1 = jcast('int', (Code05_DependentKnapsack.follows[i][0] if (Code05_DependentKnapsack.fans[i] >= 1) else jcast('int', (-1))))
                    fan2 = jcast('int', (Code05_DependentKnapsack.follows[i][1] if (Code05_DependentKnapsack.fans[i] >= 2) else jcast('int', (-1))))
                    if ((fan1 != jcast('int', (-1))) and (jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan1])) >= 0)):
                        # 可能性3 : 主 + 附1
                        jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(jcast('int', jadd(dp[p][jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan1]))], Code05_DependentKnapsack.val[i])), Code05_DependentKnapsack.val[fan1]))))
                    if ((fan2 != jcast('int', (-1))) and (jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan2])) >= 0)):
                        # 可能性4 : 主 + 附2
                        jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(jcast('int', jadd(dp[p][jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan2]))], Code05_DependentKnapsack.val[i])), Code05_DependentKnapsack.val[fan2]))))
                    if (((fan1 != jcast('int', (-1))) and (fan2 != jcast('int', (-1)))) and (jcast('int', (jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan1])) - Code05_DependentKnapsack.cost[fan2])) >= 0)):
                        # 可能性5 : 主 + 附1 + 附2
                        jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(dp[p][jcast('int', (jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan1])) - Code05_DependentKnapsack.cost[fan2]))], Code05_DependentKnapsack.val[i])), Code05_DependentKnapsack.val[fan1])), Code05_DependentKnapsack.val[fan2]))))
                    j = jcast('int', (j + 1))
                p = jcast('int', i)
            i = jcast('int', (i + 1))
        return jcast('int', dp[p][Code05_DependentKnapsack.n])

    # 空间压缩
    @staticmethod
    def compute2():
        jstatic('Arrays', 'fill', Code05_DependentKnapsack.dp, 0, jcast('int', jadd(Code05_DependentKnapsack.n, 1)), 0)
        i = jcast('int', 1)
        fan1 = 0
        fan2 = 0
        while (i <= Code05_DependentKnapsack.m):
            if Code05_DependentKnapsack.king[i]:
                j = jcast('int', Code05_DependentKnapsack.n)
                while (j >= Code05_DependentKnapsack.cost[i]):
                    jset(Code05_DependentKnapsack.dp, j, jstatic('Math', 'max', Code05_DependentKnapsack.dp[j], jcast('int', jadd(Code05_DependentKnapsack.dp[jcast('int', (j - Code05_DependentKnapsack.cost[i]))], Code05_DependentKnapsack.val[i]))))
                    fan1 = jcast('int', (Code05_DependentKnapsack.follows[i][0] if (Code05_DependentKnapsack.fans[i] >= 1) else jcast('int', (-1))))
                    fan2 = jcast('int', (Code05_DependentKnapsack.follows[i][1] if (Code05_DependentKnapsack.fans[i] >= 2) else jcast('int', (-1))))
                    if ((fan1 != jcast('int', (-1))) and (jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan1])) >= 0)):
                        jset(Code05_DependentKnapsack.dp, j, jstatic('Math', 'max', Code05_DependentKnapsack.dp[j], jcast('int', jadd(jcast('int', jadd(Code05_DependentKnapsack.dp[jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan1]))], Code05_DependentKnapsack.val[i])), Code05_DependentKnapsack.val[fan1]))))
                    if ((fan2 != jcast('int', (-1))) and (jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan2])) >= 0)):
                        jset(Code05_DependentKnapsack.dp, j, jstatic('Math', 'max', Code05_DependentKnapsack.dp[j], jcast('int', jadd(jcast('int', jadd(Code05_DependentKnapsack.dp[jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan2]))], Code05_DependentKnapsack.val[i])), Code05_DependentKnapsack.val[fan2]))))
                    if (((fan1 != jcast('int', (-1))) and (fan2 != jcast('int', (-1)))) and (jcast('int', (jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan1])) - Code05_DependentKnapsack.cost[fan2])) >= 0)):
                        jset(Code05_DependentKnapsack.dp, j, jstatic('Math', 'max', Code05_DependentKnapsack.dp[j], jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(Code05_DependentKnapsack.dp[jcast('int', (jcast('int', (jcast('int', (j - Code05_DependentKnapsack.cost[i])) - Code05_DependentKnapsack.cost[fan1])) - Code05_DependentKnapsack.cost[fan2]))], Code05_DependentKnapsack.val[i])), Code05_DependentKnapsack.val[fan1])), Code05_DependentKnapsack.val[fan2]))))
                    j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code05_DependentKnapsack.dp[Code05_DependentKnapsack.n])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_DependentKnapsack.MAXN = jcast('int', 33001)
Code05_DependentKnapsack.MAXM = jcast('int', 61)
Code05_DependentKnapsack.cost = jarray('int', [Code05_DependentKnapsack.MAXM])
Code05_DependentKnapsack.val = jarray('int', [Code05_DependentKnapsack.MAXM])
Code05_DependentKnapsack.king = jarray('boolean', [Code05_DependentKnapsack.MAXM])
Code05_DependentKnapsack.fans = jarray('int', [Code05_DependentKnapsack.MAXM])
Code05_DependentKnapsack.follows = jarray('int', [Code05_DependentKnapsack.MAXM, 2])
Code05_DependentKnapsack.dp = jarray('int', [Code05_DependentKnapsack.MAXN])
Code05_DependentKnapsack.n = jcast('int', 0)
Code05_DependentKnapsack.m = jcast('int', 0)

if __name__ == '__main__':
    Code05_DependentKnapsack.main([])
