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

# 机器人跳跃问题
# 机器人正在玩一个古老的基于DOS的游戏
# 游戏中有N+1座建筑，从0到N编号，从左到右排列
# 编号为0的建筑高度为0个单位，编号为i的建筑的高度为H(i)个单位
# 起初机器人在编号为0的建筑处
# 每一步，它跳到下一个（右边）建筑。假设机器人在第k个建筑，且它现在的能量值是E
# 下一步它将跳到第个k+1建筑
# 它将会得到或者失去正比于与H(k+1)与E之差的能量
# 如果 H(k+1) > E 那么机器人就失去H(k+1)-E的能量值，否则它将得到E-H(k+1)的能量值
# 游戏目标是到达第个N建筑，在这个过程中，能量值不能为负数个单位
# 现在的问题是机器人以多少能量值开始游戏，才可以保证成功完成游戏
# 测试链接 : https://www.nowcoder.com/practice/7037a3d57bbd4336856b8e16a9cafd71
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_RobotPassThroughBuilding:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n'}
    MAXN = 0
    arr = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_RobotPassThroughBuilding.n = jcast('int', jcast('int', jget(in_, 'nval')))
            l = jcast('int', 0)
            r = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= Code03_RobotPassThroughBuilding.n):
                jcall(in_, 'nextToken')
                Code03_RobotPassThroughBuilding.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                r = jcast('int', jstatic('Math', 'max', r, Code03_RobotPassThroughBuilding.arr[i]))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_RobotPassThroughBuilding.compute(l, r, r))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # [l,r]通关所需最小能量的范围，不停二分
    # max是所有建筑的最大高度
    # 时间复杂度O(n * log(max))，额外空间复杂度O(1)
    @staticmethod
    def compute(l, r, max):
        l = jcast('int', l)
        r = jcast('int', r)
        max = jcast('int', max)
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            # m中点，此时通关所需规定的初始能量
            m = jcast('int', jcast('int', jadd(l, jcast('int', (jcast('int', (r - l)) >> (1 & 31))))))
            if Code03_RobotPassThroughBuilding.f(m, max):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # 初始能量为energy，max是建筑的最大高度，返回能不能通关
    # 为什么要给定建筑的最大高度？
    @staticmethod
    def f(energy, max):
        energy = jcast('int', energy)
        max = jcast('int', max)
        # 注意！
        # 如果给的能量值很大，那么后续能量增长将非常恐怖
        # 完全有可能超出long的范围
        # 所以要在遍历时，一定要加入energy >= max的判断
        # 一旦能量超过高度最大值，后面肯定通关了，可以提前返回了
        # 这里很阴
        i = jcast('int', 1)
        while (i <= Code03_RobotPassThroughBuilding.n):
            if (energy <= Code03_RobotPassThroughBuilding.arr[i]):
                energy = jcast('int', jcast('int', (energy - jcast('int', (Code03_RobotPassThroughBuilding.arr[i] - energy)))))
            else:
                energy = jcast('int', jcast('int', jadd(energy, jcast('int', (energy - Code03_RobotPassThroughBuilding.arr[i])))))
            if (energy >= max):
                return jcast('boolean', True)
            if (energy < 0):
                return jcast('boolean', False)
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_RobotPassThroughBuilding.MAXN = jcast('int', 100001)
Code03_RobotPassThroughBuilding.arr = jarray('int', [Code03_RobotPassThroughBuilding.MAXN])
Code03_RobotPassThroughBuilding.n = jcast('int', 0)

if __name__ == '__main__':
    Code03_RobotPassThroughBuilding.main([])
