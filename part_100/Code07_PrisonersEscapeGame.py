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

# 囚徒生存问题
# 有100个犯人被关在监狱，犯人编号0~99，监狱长准备了100个盒子，盒子编号0~99
# 这100个盒子排成一排，放在一个房间里面，盒子编号从左往右有序排列
# 最开始时，每个犯人的编号放在每个盒子里，两种编号一一对应，监狱长构思了一个处决犯人的计划
# 监狱长打开了很多盒子，并交换了盒子里犯人的编号
# 交换行为完全随机，但依然保持每个盒子都有一个犯人编号
# 监狱长规定，每个犯人单独进入房间，可以打开50个盒子，寻找自己的编号
# 该犯人全程无法和其他犯人进行任何交流，并且不能交换盒子中的编号，只能打开查看
# 寻找过程结束后把所有盒子关上，走出房间，然后下一个犯人再进入房间，重复上述过程
# 监狱长规定，每个犯人在尝试50次的过程中，都需要找到自己的编号
# 如果有任何一个犯人没有做到这一点，100个犯人全部处决
# 所有犯人在一起交谈的时机只能发生在游戏开始之前，游戏一旦开始直到最后一个人结束都无法交流
# 请尽量制定一个让所有犯人存活概率最大的策略
# 来自论文<The Cell Probe Complexity of Succinct Data Structures>
# 作者Anna Gal和Peter Bro Miltersen写于2007年
# 如今该题变成了流行题，还有大量科普视频
class Code07_PrisonersEscapeGame:
    __java_fields__ = {}
    # 通过多次模拟实验得到的概率
    @staticmethod
    def escape1(people, tryTimes, testTimes):
        people = jcast('int', people)
        tryTimes = jcast('int', tryTimes)
        testTimes = jcast('int', testTimes)
        escape = jcast('int', 0)
        i = jcast('int', 0)
        while (i < testTimes):
            arr = Code07_PrisonersEscapeGame.generateRandomArray(people)
            if (Code07_PrisonersEscapeGame.maxCircle(arr) <= tryTimes):
                escape = jcast('int', (escape + 1))
            i = jcast('int', (i + 1))
        return jcast('double', jdiv(jcast('double', escape), jcast('double', testTimes)))

    # 求arr中最大环的长度
    @staticmethod
    def maxCircle(arr):
        maxCircle = jcast('int', 1)
        i = jcast('int', 0)
        while (i < jget(arr, 'length')):
            curCircle = jcast('int', 1)
            while (i != arr[i]):
                Code07_PrisonersEscapeGame.swap(arr, i, arr[i])
                curCircle = jcast('int', (curCircle + 1))
            maxCircle = jcast('int', jstatic('Math', 'max', maxCircle, curCircle))
            i = jcast('int', (i + 1))
        return jcast('int', maxCircle)

    # 生成随机arr
    # 原本每个位置的数都等概率出现在自己或者其他位置
    @staticmethod
    def generateRandomArray(len):
        len = jcast('int', len)
        arr = jarray('int', [len])
        i = jcast('int', 0)
        while (i < len):
            arr[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', (len - 1)))
        while (i > 0):
            Code07_PrisonersEscapeGame.swap(arr, i, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(i, 1)))))
            i = jcast('int', (i - 1))
        return arr

    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', arr[i])
        arr[i] = jcast('int', arr[j])
        arr[j] = jcast('int', tmp)

    # 公式版
    # 一定要保证tryTimes大于等于people的一半，否则该函数失效
    # 导致死亡的情况数 : C(r,100) * (r-1)! * (100-r)!，r从51~100，累加起来
    # 死亡概率 : C(r,100) * (r-1)! * (100-r)! / 100!，r从51~100，累加起来
    # 化简后的死亡概率 : 1/r，r从51~100，累加起来
    @staticmethod
    def escape2(people, tryTimes):
        people = jcast('int', people)
        tryTimes = jcast('int', tryTimes)
        a = jcast('double', 0)
        r = jcast('int', jcast('int', jadd(tryTimes, 1)))
        while (r <= people):
            a = jcast('double', jadd(a, jdiv(jcast('double', 1), jcast('double', r))))
            r = jcast('int', (r + 1))
        return jcast('double', (jcast('double', 1) - a))

    @staticmethod
    def main(args):
        people = jcast('int', 100)
        # 一定要保证tryTimes大于等于people的一半
        tryTimes = jcast('int', 50)
        testTimes = jcast('int', 100000)
        jprint(jadd('参与游戏的人数 : ', people), newline=True)
        jprint(jadd('每人的尝试次数 : ', tryTimes), newline=True)
        jprint(jadd('模拟实验的次数 : ', testTimes), newline=True)
        jprint(jadd('通过模拟实验得到的概率为 : ', Code07_PrisonersEscapeGame.escape1(people, tryTimes, testTimes)), newline=True)
        jprint(jadd('通过公式计算得到的概率为 : ', Code07_PrisonersEscapeGame.escape2(people, tryTimes)), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code07_PrisonersEscapeGame.main([])
