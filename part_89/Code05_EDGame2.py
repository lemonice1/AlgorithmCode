# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# E&D游戏
# 桌子上有2n堆石子，编号为1、2、3...2n
# 其中1、2为一组；3、4为一组；5、6为一组...2n-1、2n为一组
# 每组可以进行分割操作：
# 任取一堆石子，将其移走，然后分割同一组的另一堆石子
# 从中取出若干个石子放在被移走的位置，组成新的一堆
# 操作完成后，组内每堆的石子数必须保证大于0
# 显然，被分割的一堆的石子数至少要为2
# 两个人轮流进行分割操作，如果轮到某人进行操作时，所有堆的石子数均为1，判此人输掉比赛
# 返回先手能不能获胜
# 测试链接 : https://www.luogu.com.cn/problem/P2148
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_EDGame2:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        t = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < t):
            jcall(in_, 'nextToken')
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            sg = jcast('int', 0)
            j = jcast('int', 1)
            a = 0
            b = 0
            while (j <= n):
                jcall(in_, 'nextToken')
                a = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                b = jcast('int', jcast('int', jget(in_, 'nval')))
                sg = jcast('int', jcast('int', (sg ^ Code05_EDGame2.lowZero(jcast('int', (jcast('int', (a - 1)) | jcast('int', (b - 1))))))))
                j = jcast('int', jcast('int', jadd(j, 2)))
            if (sg != 0):
                jcall(out, 'println', 'YES')
            else:
                jcall(out, 'println', 'NO')
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def lowZero(status):
        status = jcast('int', status)
        ans = jcast('int', 0)
        while (status > 0):
            try:
                if (jcast('int', (status & 1)) == 0):
                    raise JBreak(None)
                status = jcast('int', jcast('int', (status >> (1 & 31))))
                ans = jcast('int', (ans + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code05_EDGame2.main([])
