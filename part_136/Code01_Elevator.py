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

# 跳楼机
# 一座大楼一共有h层，楼层编号1~h，有如下四种移动方式
# 1, 向上移动x层
# 2, 向上移动y层
# 3, 向上移动z层
# 4, 回到1层
# 假设你正在第1层，请问大楼里有多少楼层你可以到达
# 1 <= h <= 2^63 - 1
# 1 <= x、y、z <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3403
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Elevator:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'h': 'h', 'x': 'x', 'y': 'y', 'z': 'z', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'heap': 'heap', 'distance': 'distance', 'visited': 'visited'}
    MAXN = 0
    MAXM = 0
    h = 0
    x = 0
    y = 0
    z = 0
    # 链式前向星需要
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # dijkstra算法需要
    # 0 : 当前节点
    # 1 : 源点到当前点距离
    heap = None
    distance = None
    visited = None
    @staticmethod
    def prepare():
        Code01_Elevator.cnt = jcast('int', 1)
        jcall(Code01_Elevator.heap, 'clear')
        jstatic('Arrays', 'fill', Code01_Elevator.head, 0, Code01_Elevator.x, 0)
        jstatic('Arrays', 'fill', Code01_Elevator.distance, 0, Code01_Elevator.x, jget(Long, 'MAX_VALUE'))
        jstatic('Arrays', 'fill', Code01_Elevator.visited, 0, Code01_Elevator.x, False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('long', w)
        Code01_Elevator.next[Code01_Elevator.cnt] = jcast('int', Code01_Elevator.head[u])
        Code01_Elevator.to[Code01_Elevator.cnt] = jcast('int', v)
        Code01_Elevator.weight[Code01_Elevator.cnt] = jcast('long', w)
        jset(Code01_Elevator.head, u, ((_java_obj_1 := Code01_Elevator), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 来自讲解064，dijkstra算法
    @staticmethod
    def dijkstra():
        jcall(Code01_Elevator.heap, 'add', jarray('long', [None], [0, 0]))
        Code01_Elevator.distance[0] = jcast('long', 0)
        cur = None
        u = 0
        w = 0
        while (not jcall(Code01_Elevator.heap, 'isEmpty')):
            try:
                cur = jcall(Code01_Elevator.heap, 'poll')
                u = jcast('int', jcast('int', cur[0]))
                w = jcast('long', cur[1])
                if Code01_Elevator.visited[u]:
                    raise JContinue(None)
                Code01_Elevator.visited[u] = jcast('boolean', True)
                ei = jcast('int', Code01_Elevator.head[u])
                v = 0
                while (ei > 0):
                    v = jcast('int', Code01_Elevator.to[ei])
                    if ((not Code01_Elevator.visited[v]) and (Code01_Elevator.distance[v] > jcast('long', jadd(w, Code01_Elevator.weight[ei])))):
                        Code01_Elevator.distance[v] = jcast('long', jcast('long', jadd(w, Code01_Elevator.weight[ei])))
                        jcall(Code01_Elevator.heap, 'add', jarray('long', [None], [v, Code01_Elevator.distance[v]]))
                    ei = jcast('int', Code01_Elevator.next[ei])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break

    @staticmethod
    def compute():
        Code01_Elevator.dijkstra()
        ans = jcast('long', 0)
        i = jcast('int', 0)
        while (i < Code01_Elevator.x):
            if (Code01_Elevator.distance[i] <= Code01_Elevator.h):
                ans = jcast('long', jcast('long', jadd(ans, jcast('long', jadd(jcast('long', jdiv(jcast('long', (Code01_Elevator.h - Code01_Elevator.distance[i])), Code01_Elevator.x)), 1)))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        io = Code01_Elevator.Kattio(_java_ctor=0)
        Code01_Elevator.h = jcast('long', jcast('long', (jcall(io, 'nextLong') - 1)))
        Code01_Elevator.x = jcast('int', jcall(io, 'nextInt'))
        Code01_Elevator.y = jcast('int', jcall(io, 'nextInt'))
        Code01_Elevator.z = jcast('int', jcall(io, 'nextInt'))
        Code01_Elevator.prepare()
        i = jcast('int', 0)
        while (i < Code01_Elevator.x):
            Code01_Elevator.addEdge(i, jcast('int', jmod(jcast('int', jadd(i, Code01_Elevator.y)), Code01_Elevator.x)), Code01_Elevator.y)
            Code01_Elevator.addEdge(i, jcast('int', jmod(jcast('int', jadd(i, Code01_Elevator.z)), Code01_Elevator.x)), Code01_Elevator.z)
            i = jcast('int', (i + 1))
        jcall(io, 'println', Code01_Elevator.compute())
        jcall(io, 'flush')
        jcall(io, 'close')

    # Kattio 与 StreamTokenizer 接口均由 Python 实现，按输入格式选择，不沿用原语言的速度比较
    # 输入包含特殊格式时，可使用本类先读取字符串，再选择 int 或 float 解析
    # Python 输入输出参考：https://docs.python.org/3/library/io.html
    class Kattio(jclass('PrintWriter')):
        __java_fields__ = {'r': 'r', 'st': 'st'}
        # r：实例字段，在构造函数中初始化。
        # st：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self._java_init_1(jget(System, 'in'), jget(System, 'out'))

        def _java_init_1(self, i, o):
            super().__init__(o)
            self.r = jnew('BufferedReader', jnew('InputStreamReader', i))

        def _java_init_2(self, intput, output):
            super().__init__(output)
            self.r = jnew('BufferedReader', jnew('FileReader', intput))

        def next(self):
            try:
                while ((self.st == None) or (not jcall(self.st, 'hasMoreTokens'))):
                    self.st = jnew('StringTokenizer', jcall(self.r, 'readLine'))
                return jcall(self.st, 'nextToken')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_5:
                if jinstanceof(_java_exception_5, 'Exception'):
                    e = _java_exception_5
                    None
                else:
                    raise
            return None

        def nextInt(self):
            return jcast('int', jstatic('Integer', 'parseInt', self.next()))

        def nextDouble(self):
            return jcast('double', jstatic('Double', 'parseDouble', self.next()))

        def nextLong(self):
            return jcast('long', jstatic('Long', 'parseLong', self.next()))

        def __init__(self, *args, _java_ctor=None):
            self.r = None
            self.st = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[], ['InputStream', 'OutputStream'], ['String', 'String']], [False, False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            if _java_choice == 2:
                return self._java_init_2(*args)
            raise TypeError("No matching overload for Code01_Elevator.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Elevator.MAXN = jcast('int', 100001)
Code01_Elevator.MAXM = jcast('int', 200001)
Code01_Elevator.h = jcast('long', 0)
Code01_Elevator.x = jcast('int', 0)
Code01_Elevator.y = jcast('int', 0)
Code01_Elevator.z = jcast('int', 0)
Code01_Elevator.head = jarray('int', [Code01_Elevator.MAXN])
Code01_Elevator.next = jarray('int', [Code01_Elevator.MAXM])
Code01_Elevator.to = jarray('int', [Code01_Elevator.MAXM])
Code01_Elevator.weight = jarray('long', [Code01_Elevator.MAXM])
Code01_Elevator.cnt = jcast('int', 0)
Code01_Elevator.heap = jnew('PriorityQueue', (lambda a, b: (jcast('int', (-1)) if (a[1] <= b[1]) else 1)))
Code01_Elevator.distance = jarray('long', [Code01_Elevator.MAXN])
Code01_Elevator.visited = jarray('boolean', [Code01_Elevator.MAXN])

if __name__ == '__main__':
    Code01_Elevator.main([])
