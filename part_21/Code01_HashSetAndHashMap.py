# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

class Code01_HashSetAndHashMap:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        # Integer、Long、Double、Float
        # Byte、Short、Character、Boolean
        # String等都有这个特征
        str1 = jnew('String', 'Hello')
        str2 = jnew('String', 'Hello')
        # false，因为不同的内存地址
        jprint((str1 == str2), newline=True)
        # true，因为它们的值是相同的
        jprint(jcall(str1, 'equals', str2), newline=True)
        set = jnew('HashSet')
        jcall(set, 'add', str1)
        jprint(jcall(set, 'contains', 'Hello'), newline=True)
        jprint(jcall(set, 'contains', str2), newline=True)
        jcall(set, 'add', str2)
        jprint(jcall(set, 'size'), newline=True)
        jcall(set, 'remove', str1)
        jcall(set, 'clear')
        jprint(jcall(set, 'isEmpty'), newline=True)
        jprint('===========', newline=True)
        map1 = jnew('HashMap')
        jcall(map1, 'put', str1, 'World')
        jprint(jcall(map1, 'containsKey', 'Hello'), newline=True)
        jprint(jcall(map1, 'containsKey', str2), newline=True)
        jprint(jcall(map1, 'get', str2), newline=True)
        jprint((jcall(map1, 'get', '你好') == None), newline=True)
        jcall(map1, 'remove', 'Hello')
        jprint(jcall(map1, 'size'), newline=True)
        jcall(map1, 'clear')
        jprint(jcall(map1, 'isEmpty'), newline=True)
        jprint('===========', newline=True)
        # 一般在笔试中，未必需要申请哈希表
        map2 = jnew('HashMap')
        jcall(map2, 'put', 56, 7285)
        jcall(map2, 'put', 34, 3671263)
        jcall(map2, 'put', 17, 716311)
        jcall(map2, 'put', 24, 1263161)
        # 上面的map2行为，可以被如下数组的行为替代
        arr = jarray('int', [100])
        arr[56] = jcast('int', 7285)
        arr[34] = jcast('int', 3671263)
        arr[17] = jcast('int', 716311)
        arr[24] = jcast('int', 1263161)
        # 哈希表的增、删、改、查，都可以被数组替代，前提是key的范围是固定的、可控的
        jprint('在笔试场合中哈希表往往会被数组替代', newline=True)
        jprint('===========', newline=True)
        s1 = Code01_HashSetAndHashMap.Student(17, '张三', _java_ctor=0)
        s2 = Code01_HashSetAndHashMap.Student(17, '张三', _java_ctor=0)
        map3 = jnew('HashMap')
        jcall(map3, 'put', s1, '这是张三')
        jprint(jcall(map3, 'containsKey', s1), newline=True)
        jprint(jcall(map3, 'containsKey', s2), newline=True)
        jcall(map3, 'put', s2, '这是另一个张三')
        jprint(jcall(map3, 'size'), newline=True)
        jprint(jcall(map3, 'get', s1), newline=True)
        jprint(jcall(map3, 'get', s2), newline=True)

    class Student:
        __java_fields__ = {'age': 'age', 'name': 'name'}
        # age：实例字段，在构造函数中初始化。
        # name：实例字段，在构造函数中初始化。
        def _java_init_0(self, a, b):
            a = jcast('int', a)
            self.age = jcast('int', a)
            self.name = b

        def __init__(self, *args, _java_ctor=None):
            self.age = jcast('int', 0)
            self.name = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'String']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_HashSetAndHashMap.Student.Student")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_HashSetAndHashMap.main([])
