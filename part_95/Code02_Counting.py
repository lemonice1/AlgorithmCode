# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 数数(利用AC自动机检查命中)
# 我们称一个正整数x为幸运数字的条件为
# x的十进制中不包含数字串集合s中任意一个元素作为子串
# 例如s = { 22, 333, 0233 }
# 233是幸运数字，2333、20233、3223不是幸运数字
# 给定n和s，计算不大于n的幸运数字的个数
# 答案对1000000007取模
# 测试链接 : https://www.luogu.com.cn/problem/P3311
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Counting:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'MAXS': 'MAXS', 'num': 'num', 'n': 'n', 'tree': 'tree', 'fail': 'fail', 'cnt': 'cnt', 'alert': 'alert', 'queue': 'queue', 'dp': 'dp'}
    MOD = 0
    # 目标字符串的数量
    MAXN = 0
    # 所有目标字符串的总字符数量
    MAXS = 0
    # 读入的数字
    num = None
    # 读入数字的长度
    n = 0
    # AC自动机
    tree = None
    fail = None
    cnt = 0
    # 具体题目相关，本题为命中任何目标串就直接报警
    # 所以每个节点记录是否触发警报
    alert = None
    queue = None
    # 动态规划表
    dp = None
    @staticmethod
    def clear():
        i = jcast('int', 0)
        while (i <= Code02_Counting.n):
            j = jcast('int', 0)
            while (j <= Code02_Counting.cnt):
                jset(Code02_Counting.dp[i][j][0], 0, jcast('int', (-1)))
                jset(Code02_Counting.dp[i][j][0], 1, jcast('int', (-1)))
                jset(Code02_Counting.dp[i][j][1], 0, jcast('int', (-1)))
                jset(Code02_Counting.dp[i][j][1], 1, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    # AC自动机加入目标字符串
    @staticmethod
    def insert(word):
        w = jcall(word, 'toCharArray')
        u = jcast('int', 0)
        j = jcast('int', 0)
        c = 0
        while (j < jget(w, 'length')):
            c = jcast('int', jcast('int', (w[j] - jchar('0'))))
            if (Code02_Counting.tree[u][c] == 0):
                jset(Code02_Counting.tree[u], c, ((_java_obj_1 := Code02_Counting), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
            u = jcast('int', Code02_Counting.tree[u][c])
            j = jcast('int', (j + 1))
        Code02_Counting.alert[u] = jcast('boolean', True)

    # 加入所有目标字符串之后
    # 设置fail指针 以及 设置直接跳转支路
    # 做了AC自动机固定的优化
    # 做了命中标记前移防止绕圈的优化
    @staticmethod
    def setFail():
        l = jcast('int', 0)
        r = jcast('int', 0)
        i = jcast('int', 0)
        while (i <= 9):
            if (Code02_Counting.tree[0][i] > 0):
                jset(Code02_Counting.queue, ((_java_old_4 := r), (r := jcast('int', (r + (1)))), _java_old_4)[2], Code02_Counting.tree[0][i])
            i = jcast('int', (i + 1))
        while (l < r):
            u = jcast('int', Code02_Counting.queue[((_java_old_5 := l), (l := jcast('int', (l + (1)))), _java_old_5)[2]])
            i = jcast('int', 0)
            while (i <= 9):
                if (Code02_Counting.tree[u][i] == 0):
                    jset(Code02_Counting.tree[u], i, Code02_Counting.tree[Code02_Counting.fail[u]][i])
                else:
                    jset(Code02_Counting.fail, Code02_Counting.tree[u][i], Code02_Counting.tree[Code02_Counting.fail[u]][i])
                    jset(Code02_Counting.queue, ((_java_old_6 := r), (r := jcast('int', (r + (1)))), _java_old_6)[2], Code02_Counting.tree[u][i])
                i = jcast('int', (i + 1))
            # 命中标记前移
            Code02_Counting.alert[u] = jcast('boolean', (Code02_Counting.alert[u] | Code02_Counting.alert[Code02_Counting.fail[u]]))

    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Counting.num = jcall(jcall(in_, 'readLine'), 'toCharArray')
        Code02_Counting.n = jcast('int', jget(Code02_Counting.num, 'length'))
        # AC自动机建树
        m = jcast('int', jstatic('Integer', 'valueOf', jcall(in_, 'readLine')))
        i = jcast('int', 1)
        while (i <= m):
            Code02_Counting.insert(jcall(in_, 'readLine'))
            i = jcast('int', (i + 1))
        Code02_Counting.setFail()
        # 清空动态规划表
        Code02_Counting.clear()
        # 执行记忆化搜索
        jcall(out, 'println', Code02_Counting.f1(0, 0, 0, 0))
        # out.println(f2(0, 0, 0, 0));
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    # 逻辑分支都详细列出来的版本
    # i来到的位置
    # j : AC自动机里来到的节点编号
    # free : 是不是可以随意选择了
    # free = 0，不能随意选择数字，要考虑当前数字的大小
    # free = 1，能随意选择数字
    # has : 之前有没有选择过数字
    # has = 0，之前没选择过数字
    # has = 1，之前选择过数字
    # 返回i....幸运数字的个数
    @staticmethod
    def f1(i, j, free, has):
        i = jcast('int', i)
        j = jcast('int', j)
        free = jcast('int', free)
        has = jcast('int', has)
        if Code02_Counting.alert[j]:
            return jcast('int', 0)
        if (i == Code02_Counting.n):
            return jcast('int', has)
        if (Code02_Counting.dp[i][j][free][has] != jcast('int', (-1))):
            return jcast('int', Code02_Counting.dp[i][j][free][has])
        ans = jcast('int', 0)
        cur = jcast('int', jcast('int', (Code02_Counting.num[i] - jchar('0'))))
        if (has == 0):
            if (free == 0):
                # 分支1 : 之前没有选择过数字 且 之前的决策等于num的前缀
                # 能来到这里说明i一定是0位置, 那么cur必然不是0
                # 当前选择不要数字
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_Counting.f1(jcast('int', jadd(i, 1)), 0, 1, 0))), Code02_Counting.MOD)))
                # 当前选择的数字比cur小
                pick = jcast('int', 1)
                while (pick < cur):
                    ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_Counting.f1(jcast('int', jadd(i, 1)), Code02_Counting.tree[j][pick], 1, 1))), Code02_Counting.MOD)))
                    pick = jcast('int', (pick + 1))
                # 当前选择的数字为cur
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_Counting.f1(jcast('int', jadd(i, 1)), Code02_Counting.tree[j][cur], 0, 1))), Code02_Counting.MOD)))
            else:
                # 分支2 : 之前没有选择过数字 且 之前的决策小于num的前缀
                # 当前选择不要数字
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_Counting.f1(jcast('int', jadd(i, 1)), 0, 1, 0))), Code02_Counting.MOD)))
                # 当前可以选择1~9
                pick = jcast('int', 1)
                while (pick <= 9):
                    ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_Counting.f1(jcast('int', jadd(i, 1)), Code02_Counting.tree[j][pick], 1, 1))), Code02_Counting.MOD)))
                    pick = jcast('int', (pick + 1))
        else:
            if (free == 0):
                # 分支3 : 之前已经选择过数字 且 之前的决策等于num的前缀
                # 当前选择的数字比cur小
                pick = jcast('int', 0)
                while (pick < cur):
                    ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_Counting.f1(jcast('int', jadd(i, 1)), Code02_Counting.tree[j][pick], 1, 1))), Code02_Counting.MOD)))
                    pick = jcast('int', (pick + 1))
                # 当前选择的数字为cur
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_Counting.f1(jcast('int', jadd(i, 1)), Code02_Counting.tree[j][cur], 0, 1))), Code02_Counting.MOD)))
            else:
                # 分支4 : 之前已经选择过数字 且 之前的决策小于num的前缀
                # 当前可以选择0~9
                pick = jcast('int', 0)
                while (pick <= 9):
                    ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_Counting.f1(jcast('int', jadd(i, 1)), Code02_Counting.tree[j][pick], 1, 1))), Code02_Counting.MOD)))
                    pick = jcast('int', (pick + 1))
        jset(Code02_Counting.dp[i][j][free], has, ans)
        return jcast('int', ans)

    # 逻辑合并版
    # 其实和f1方法完全一个意思
    @staticmethod
    def f2(i, u, free, has):
        i = jcast('int', i)
        u = jcast('int', u)
        free = jcast('int', free)
        has = jcast('int', has)
        if Code02_Counting.alert[u]:
            return jcast('int', 0)
        if (i == Code02_Counting.n):
            return jcast('int', has)
        if (Code02_Counting.dp[i][u][free][has] != jcast('int', (-1))):
            return jcast('int', Code02_Counting.dp[i][u][free][has])
        limit = jcast('int', (jcast('int', (Code02_Counting.num[i] - jchar('0'))) if (free == 0) else 9))
        ans = jcast('int', 0)
        pick = jcast('int', 0)
        while (pick <= limit):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_Counting.f2(jcast('int', jadd(i, 1)), (0 if ((has == 0) and (pick == 0)) else Code02_Counting.tree[u][pick]), (0 if ((free == 0) and (pick == limit)) else 1), (0 if ((has == 0) and (pick == 0)) else 1)))), Code02_Counting.MOD)))
            pick = jcast('int', (pick + 1))
        jset(Code02_Counting.dp[i][u][free], has, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Counting.MOD = jcast('int', 1000000007)
Code02_Counting.MAXN = jcast('int', 1301)
Code02_Counting.MAXS = jcast('int', 2001)
Code02_Counting.num = None
Code02_Counting.n = jcast('int', 0)
Code02_Counting.tree = jarray('int', [Code02_Counting.MAXS, 10])
Code02_Counting.fail = jarray('int', [Code02_Counting.MAXS])
Code02_Counting.cnt = jcast('int', 0)
Code02_Counting.alert = jarray('boolean', [Code02_Counting.MAXS])
Code02_Counting.queue = jarray('int', [Code02_Counting.MAXS])
Code02_Counting.dp = jarray('int', [Code02_Counting.MAXN, Code02_Counting.MAXS, 2, 2])

if __name__ == '__main__':
    Code02_Counting.main([])
