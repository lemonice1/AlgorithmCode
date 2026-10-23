# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 威佐夫博弈(Wythoff Game)
# 有两堆石子，数量任意，可以不同，游戏开始由两个人轮流取石子
# 游戏规定，每次有两种不同的取法
# 1) 在任意的一堆中取走任意多的石子
# 2) 可以在两堆中同时取走相同数量的石子
# 最后把石子全部取完者为胜者
# 现在给出初始的两堆石子的数目，返回先手能不能获胜
# 测试链接 : https://www.luogu.com.cn/problem/P2252
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_WythoffGame:
    __java_fields__ = {'split': 'split', 'a': 'a', 'b': 'b'}
    # 黄金分割比例
    # 洛谷在2024年5月增加了测试数据
    # 需要更高精度的黄金比例 + 更高精度的乘法，才能全部通过
    # 增加的测试用例有刻意为难的嫌疑，其实没啥意思
    # 高精度十进制运算使用 decimal.Decimal，BigDecimal 接口由兼容层提供
    split = None
    a = 0
    b = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code06_WythoffGame.a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_WythoffGame.b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code06_WythoffGame.compute())
            jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        min = jcast('int', jstatic('Math', 'min', Code06_WythoffGame.a, Code06_WythoffGame.b))
        max = jcast('int', jstatic('Math', 'max', Code06_WythoffGame.a, Code06_WythoffGame.b))
        # 威佐夫博弈
        # 小 != (大 - 小) * 黄金分割比例，先手赢
        # 小 == (大 - 小) * 黄金分割比例，后手赢
        # 要向下取整
        # 这里用BigDecimal类型的multiply方法，乘完后再转成整型，可以支持高精度的乘
        if (min != jcall(jcall(Code06_WythoffGame.split, 'multiply', jnew('BigDecimal', jcast('int', (max - min)))), 'intValue')):
            return jcast('int', 1)
        else:
            return jcast('int', 0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_WythoffGame.split = jnew('BigDecimal', '1.61803398874989484')
Code06_WythoffGame.a = jcast('int', 0)
Code06_WythoffGame.b = jcast('int', 0)

if __name__ == '__main__':
    Code06_WythoffGame.main([])
