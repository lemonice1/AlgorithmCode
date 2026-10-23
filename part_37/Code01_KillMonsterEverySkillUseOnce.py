# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 现在有一个打怪类型的游戏，这个游戏是这样的，你有n个技能
# 每一个技能会有一个伤害，
# 同时若怪物小于等于一定的血量，则该技能可能造成双倍伤害
# 每一个技能最多只能释放一次，已知怪物有m点血量
# 现在想问你最少用几个技能能消灭掉他(血量小于等于0)
# 技能的数量是n，怪物的血量是m
# i号技能的伤害是x[i]，i号技能触发双倍伤害的血量最小值是y[i]
# 1 <= n <= 10
# 1 <= m、x[i]、y[i] <= 10^6
# 测试链接 : https://www.nowcoder.com/practice/d88ef50f8dab4850be8cd4b95514bbbd
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
#
class Code01_KillMonsterEverySkillUseOnce:
    __java_fields__ = {'MAXN': 'MAXN', 'kill': 'kill', 'blood': 'blood'}
    MAXN = 0
    kill = None
    blood = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            t = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < t):
                jcall(in_, 'nextToken')
                n = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                m = jcast('int', jcast('int', jget(in_, 'nval')))
                j = jcast('int', 0)
                while (j < n):
                    jcall(in_, 'nextToken')
                    Code01_KillMonsterEverySkillUseOnce.kill[j] = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    Code01_KillMonsterEverySkillUseOnce.blood[j] = jcast('int', jcast('int', jget(in_, 'nval')))
                    j = jcast('int', (j + 1))
                ans = jcast('int', Code01_KillMonsterEverySkillUseOnce.f(n, 0, m))
                jcall(out, 'println', (jcast('int', (-1)) if (ans == jget(Integer, 'MAX_VALUE')) else ans))
                i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(br, 'close')
        jcall(out, 'close')

    # kill[i]、blood[i]
    # n : 一共几个技能
    # i : 当前来到了第几号技能
    # r : 怪兽目前的剩余血量
    @staticmethod
    def f(n, i, r):
        n = jcast('int', n)
        i = jcast('int', i)
        r = jcast('int', r)
        if (r <= 0):
            # 之前的决策已经让怪兽挂了！返回使用了多少个节能
            return jcast('int', i)
        # r > 0
        if (i == n):
            # 无效，之前的决策无效
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        # 返回至少需要几个技能可以将怪兽杀死
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        j = jcast('int', i)
        while (j < n):
            Code01_KillMonsterEverySkillUseOnce.swap(i, j)
            ans = jcast('int', jstatic('Math', 'min', ans, Code01_KillMonsterEverySkillUseOnce.f(n, jcast('int', jadd(i, 1)), jcast('int', (r - (Code01_KillMonsterEverySkillUseOnce.kill[i] if (r > Code01_KillMonsterEverySkillUseOnce.blood[i]) else jcast('int', (Code01_KillMonsterEverySkillUseOnce.kill[i] * 2))))))))
            Code01_KillMonsterEverySkillUseOnce.swap(i, j)
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    # i号技能和j号技能，参数交换
    # j号技能要来到i位置，试一下
    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code01_KillMonsterEverySkillUseOnce.kill[i])
        Code01_KillMonsterEverySkillUseOnce.kill[i] = jcast('int', Code01_KillMonsterEverySkillUseOnce.kill[j])
        Code01_KillMonsterEverySkillUseOnce.kill[j] = jcast('int', tmp)
        tmp = jcast('int', Code01_KillMonsterEverySkillUseOnce.blood[i])
        Code01_KillMonsterEverySkillUseOnce.blood[i] = jcast('int', Code01_KillMonsterEverySkillUseOnce.blood[j])
        Code01_KillMonsterEverySkillUseOnce.blood[j] = jcast('int', tmp)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_KillMonsterEverySkillUseOnce.MAXN = jcast('int', 11)
Code01_KillMonsterEverySkillUseOnce.kill = jarray('int', [Code01_KillMonsterEverySkillUseOnce.MAXN])
Code01_KillMonsterEverySkillUseOnce.blood = jarray('int', [Code01_KillMonsterEverySkillUseOnce.MAXN])

if __name__ == '__main__':
    Code01_KillMonsterEverySkillUseOnce.main([])
