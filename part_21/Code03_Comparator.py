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

class Code03_Comparator:
    __java_fields__ = {}
    class Employee:
        __java_fields__ = {'company': 'company', 'age': 'age'}
        # company：实例字段，在构造函数中初始化。
        # age：实例字段，在构造函数中初始化。
        def _java_init_0(self, c, a):
            c = jcast('int', c)
            a = jcast('int', a)
            self.company = jcast('int', c)
            self.age = jcast('int', a)

        def __init__(self, *args, _java_ctor=None):
            self.company = jcast('int', 0)
            self.age = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_Comparator.Employee.Employee")


    class EmployeeComparator:
        __java_fields__ = {}
        def compare(self, o1, o2):
            # 任何比较器都默认
            # 如果返回负数认为o1的优先级更高
            # 如果返回正数认为o2的优先级更高
            # 任何比较器都是这样，所以利用这个设定，可以定制优先级怎么确定，也就是怎么比较
            # 不再有大小的概念，就是优先级的概念
            return jcast('int', jcast('int', (jget(o1, 'age') - jget(o2, 'age'))))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def main(args):
        s1 = Code03_Comparator.Employee(2, 27, _java_ctor=0)
        s2 = Code03_Comparator.Employee(1, 60, _java_ctor=0)
        s3 = Code03_Comparator.Employee(4, 19, _java_ctor=0)
        s4 = Code03_Comparator.Employee(3, 23, _java_ctor=0)
        s5 = Code03_Comparator.Employee(1, 35, _java_ctor=0)
        s6 = Code03_Comparator.Employee(3, 55, _java_ctor=0)
        arr = jarray('Employee', [None], [s1, s2, s3, s4, s5, s6])
        jstatic('Arrays', 'sort', arr, Code03_Comparator.EmployeeComparator())
        for e in arr:
            jprint(jadd(jadd(jget(e, 'company'), ' , '), jget(e, 'age')), newline=True)
        jprint('=====', newline=True)
        jstatic('Arrays', 'sort', arr, (lambda a, b: (jget(b, 'age') - jget(a, 'age'))))
        for e in arr:
            jprint(jadd(jadd(jget(e, 'company'), ' , '), jget(e, 'age')), newline=True)
        jprint('=====', newline=True)
        # 所有员工，先按照谁的公司编号小，谁在前；如果公司编号一样，谁年龄小谁在前
        jstatic('Arrays', 'sort', arr, (lambda a, b: ((jget(a, 'company') - jget(b, 'company')) if (jget(a, 'company') != jget(b, 'company')) else (jget(a, 'age') - jget(b, 'age')))))
        for e in arr:
            jprint(jadd(jadd(jget(e, 'company'), ' , '), jget(e, 'age')), newline=True)
        treeSet1 = jnew('TreeSet', Code03_Comparator.EmployeeComparator())
        for e in arr:
            jcall(treeSet1, 'add', e)
        jprint(jcall(treeSet1, 'size'), newline=True)
        # 会去重
        jcall(treeSet1, 'add', Code03_Comparator.Employee(2, 27, _java_ctor=0))
        jprint(jcall(treeSet1, 'size'), newline=True)
        jprint('===', newline=True)
        # 如果不想去重，就需要增加更多的比较
        # 比如对象的内存地址、或者如果对象有数组下标之类的独特信息
        treeSet2 = jnew('TreeSet', (lambda a, b: ((jget(a, 'company') - jget(b, 'company')) if (jget(a, 'company') != jget(b, 'company')) else ((jget(a, 'age') - jget(b, 'age')) if (jget(a, 'age') != jget(b, 'age')) else jcall(jcall(a, 'toString'), 'compareTo', jcall(b, 'toString'))))))
        for e in arr:
            jcall(treeSet2, 'add', e)
        jprint(jcall(treeSet2, 'size'), newline=True)
        # 不会去重
        jcall(treeSet2, 'add', Code03_Comparator.Employee(2, 27, _java_ctor=0))
        jprint(jcall(treeSet2, 'size'), newline=True)
        jprint('===', newline=True)
        # PriorityQueue不会去重，不再展示了
        # 字典序
        str1 = 'abcde'
        str2 = 'ks'
        jprint(jcall(str1, 'compareTo', str2), newline=True)
        jprint(jcall(str2, 'compareTo', str1), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_Comparator.main([])
