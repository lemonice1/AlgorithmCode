# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 反尼姆博弈(反常游戏)
# 一共有n堆石头，两人轮流进行游戏
# 在每个玩家的回合中，玩家需要选择任何一个非空的石头堆，并从这堆石头中移除任意正数的石头数量
# 谁先拿走最后的石头就失败，返回最终谁会获胜
# 先手获胜，打印John
# 后手获胜，打印Brother
# 测试链接 : https://www.luogu.com.cn/problem/P4279
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_AntiNimGame:
    __java_fields__ = {'MAXN': 'MAXN', 'stones': 'stones', 't': 't', 'n': 'n'}
    MAXN = 0
    stones = None
    t = 0
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_AntiNimGame.t = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < Code04_AntiNimGame.t):
            jcall(in_, 'nextToken')
            Code04_AntiNimGame.n = jcast('int', jcast('int', jget(in_, 'nval')))
            j = jcast('int', 0)
            while (j < Code04_AntiNimGame.n):
                jcall(in_, 'nextToken')
                Code04_AntiNimGame.stones[j] = jcast('int', jcast('int', jget(in_, 'nval')))
                j = jcast('int', (j + 1))
            jcall(out, 'println', Code04_AntiNimGame.compute())
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        eor = jcast('int', 0)
        sum = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code04_AntiNimGame.n):
            eor = jcast('int', jcast('int', (eor ^ Code04_AntiNimGame.stones[i])))
            sum = jcast('int', jcast('int', jadd(sum, (1 if (Code04_AntiNimGame.stones[i] == 1) else 0))))
            i = jcast('int', (i + 1))
        if (sum == Code04_AntiNimGame.n):
            return ('Brother' if (jcast('int', (Code04_AntiNimGame.n & 1)) == 1) else 'John')
        else:
            return ('John' if (eor != 0) else 'Brother')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_AntiNimGame.MAXN = jcast('int', 51)
Code04_AntiNimGame.stones = jarray('int', [Code04_AntiNimGame.MAXN])
Code04_AntiNimGame.t = jcast('int', 0)
Code04_AntiNimGame.n = jcast('int', 0)

if __name__ == '__main__':
    Code04_AntiNimGame.main([])
