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

# 夏季特惠
# 某公司游戏平台的夏季特惠开始了，你决定入手一些游戏
# 现在你一共有X元的预算，平台上所有的 n 个游戏均有折扣
# 标号为 i 的游戏的原价a_i元，现价只要b_i元
# 也就是说该游戏可以优惠 a_i - b_i，并且你购买该游戏能获得快乐值为w_i
# 由于优惠的存在，你可能做出一些冲动消费导致最终买游戏的总费用超过预算
# 只要满足 : 获得的总优惠金额不低于超过预算的总金额
# 那在心理上就不会觉得吃亏。
# 现在你希望在心理上不觉得吃亏的前提下，获得尽可能多的快乐值。
# 测试链接 : https://leetcode.cn/problems/tJau2o/
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_BuyGoodsHaveDiscount:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXX': 'MAXX', 'cost': 'cost', 'val': 'val', 'dp': 'dp', 'n': 'n', 'm': 'm', 'x': 'x'}
    MAXN = 0
    MAXX = 0
    # 对于"一定要买的商品"，直接买！
    # 只把"需要考虑的商品"放入cost、val数组
    cost = None
    val = None
    dp = None
    n = 0
    m = 0
    x = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_BuyGoodsHaveDiscount.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_BuyGoodsHaveDiscount.m = jcast('int', 1)
            jcall(in_, 'nextToken')
            Code02_BuyGoodsHaveDiscount.x = jcast('int', jcast('int', jget(in_, 'nval')))
            ans = jcast('long', 0)
            happy = jcast('long', 0)
            i = jcast('int', 1)
            pre = 0
            cur = 0
            well = 0
            while (i <= Code02_BuyGoodsHaveDiscount.n):
                # 原价
                jcall(in_, 'nextToken')
                pre = jcast('int', jcast('int', jget(in_, 'nval')))
                # 现价
                jcall(in_, 'nextToken')
                cur = jcast('int', jcast('int', jget(in_, 'nval')))
                # 快乐值
                jcall(in_, 'nextToken')
                happy = jcast('long', jcast('long', jget(in_, 'nval')))
                well = jcast('int', jcast('int', (jcast('int', (pre - cur)) - cur)))
                # 如下是一件"一定要买的商品"
                # 预算 = 100，商品原价 = 10，打折后 = 3
                # 那么好处(well) = (10 - 3) - 3 = 4
                # 所以，可以认为这件商品把预算增加到了104！一定要买！
                # 如下是一件"需要考虑的商品"
                # 预算 = 104，商品原价 = 10，打折后 = 8
                # 那么好处(well) = (10 - 8) - 8 = -6
                # 所以，可以认为这件商品就花掉6元！
                # 也就是说以后花的不是打折后的值，是"坏处"
                if (well >= 0):
                    Code02_BuyGoodsHaveDiscount.x = jcast('int', jcast('int', jadd(Code02_BuyGoodsHaveDiscount.x, well)))
                    ans = jcast('long', jcast('long', jadd(ans, happy)))
                else:
                    Code02_BuyGoodsHaveDiscount.cost[Code02_BuyGoodsHaveDiscount.m] = jcast('int', jcast('int', (-well)))
                    jset(Code02_BuyGoodsHaveDiscount.val, ((_java_obj_1 := Code02_BuyGoodsHaveDiscount), (_java_key_2 := 'm'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], happy)
                i = jcast('int', (i + 1))
            ans = jcast('long', jcast('long', jadd(ans, Code02_BuyGoodsHaveDiscount.compute())))
            jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        jstatic('Arrays', 'fill', Code02_BuyGoodsHaveDiscount.dp, 0, jcast('int', jadd(Code02_BuyGoodsHaveDiscount.x, 1)), 0)
        i = jcast('int', 1)
        while (i <= Code02_BuyGoodsHaveDiscount.m):
            j = jcast('int', Code02_BuyGoodsHaveDiscount.x)
            while (j >= Code02_BuyGoodsHaveDiscount.cost[i]):
                jset(Code02_BuyGoodsHaveDiscount.dp, j, jstatic('Math', 'max', Code02_BuyGoodsHaveDiscount.dp[j], jcast('long', jadd(Code02_BuyGoodsHaveDiscount.dp[jcast('int', (j - Code02_BuyGoodsHaveDiscount.cost[i]))], Code02_BuyGoodsHaveDiscount.val[i]))))
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        return jcast('long', Code02_BuyGoodsHaveDiscount.dp[Code02_BuyGoodsHaveDiscount.x])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_BuyGoodsHaveDiscount.MAXN = jcast('int', 501)
Code02_BuyGoodsHaveDiscount.MAXX = jcast('int', 100001)
Code02_BuyGoodsHaveDiscount.cost = jarray('int', [Code02_BuyGoodsHaveDiscount.MAXN])
Code02_BuyGoodsHaveDiscount.val = jarray('long', [Code02_BuyGoodsHaveDiscount.MAXN])
Code02_BuyGoodsHaveDiscount.dp = jarray('long', [Code02_BuyGoodsHaveDiscount.MAXX])
Code02_BuyGoodsHaveDiscount.n = jcast('int', 0)
Code02_BuyGoodsHaveDiscount.m = jcast('int', 0)
Code02_BuyGoodsHaveDiscount.x = jcast('int', 0)

if __name__ == '__main__':
    Code02_BuyGoodsHaveDiscount.main([])
