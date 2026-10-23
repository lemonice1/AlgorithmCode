# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

class HashFunction:
    __java_fields__ = {}
    # 哈希函数实例
    class Hash:
        __java_fields__ = {'md': 'md'}
        # md：实例字段，在构造函数中初始化。
        # 打印支持哪些哈希算法
        @staticmethod
        def showAlgorithms():
            for algorithm in jstatic('Security', 'getAlgorithms', 'MessageDigest'):
                jprint(algorithm, newline=True)

        # 用具体算法名字构造实例
        def _java_init_0(self, algorithm):
            try:
                self.md = jstatic('MessageDigest', 'getInstance', algorithm)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_1:
                if jinstanceof(_java_exception_1, 'NoSuchAlgorithmException'):
                    e = _java_exception_1
                    jcall(e, 'printStackTrace')
                else:
                    raise

        # 输入字符串返回哈希值
        def hashValue(self, input):
            hashInBytes = jcall(self.md, 'digest', jcall(input, 'getBytes', jget(StandardCharsets, 'UTF_8')))
            bigInt = jnew('BigInteger', 1, hashInBytes)
            hashText = jcall(bigInt, 'toString', 16)
            return hashText

        def __init__(self, *args, _java_ctor=None):
            self.md = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['String']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for HashFunction.Hash.Hash")


    @staticmethod
    def generateStrings(arr, n):
        n = jcast('int', n)
        path = jarray('char', [n])
        ans = jnew('ArrayList')
        HashFunction.f(arr, 0, n, path, ans)
        return ans

    @staticmethod
    def f(arr, i, n, path, ans):
        i = jcast('int', i)
        n = jcast('int', n)
        if (i == n):
            jcall(ans, 'add', jstatic('String', 'valueOf', path))
        else:
            for cha in arr:
                path[i] = jcast('char', cha)
                HashFunction.f(arr, jcast('int', jadd(i, 1)), n, path, ans)

    @staticmethod
    def main(args):
        jprint('支持的哈希算法 : ', newline=True)
        jcall(HashFunction.Hash, 'showAlgorithms')
        jprint(newline=True)
        algorithm = 'MD5'
        hash = HashFunction.Hash(algorithm, _java_ctor=0)
        str1 = 'zuochengyunzuochengyunzuochengyun1'
        str2 = 'zuochengyunzuochengyunzuochengyun2'
        str3 = 'zuochengyunzuochengyunzuochengyun3'
        str4 = 'zuochengyunzuochengyunZuochengyun1'
        str5 = 'zuochengyunzuoChengyunzuochengyun2'
        str6 = 'zuochengyunzuochengyunzuochengyUn3'
        str7 = 'zuochengyunzuochengyunzuochengyun1'
        jprint('7个字符串得到的哈希值 : ', newline=True)
        jprint(jcall(hash, 'hashValue', str1), newline=True)
        jprint(jcall(hash, 'hashValue', str2), newline=True)
        jprint(jcall(hash, 'hashValue', str3), newline=True)
        jprint(jcall(hash, 'hashValue', str4), newline=True)
        jprint(jcall(hash, 'hashValue', str5), newline=True)
        jprint(jcall(hash, 'hashValue', str6), newline=True)
        jprint(jcall(hash, 'hashValue', str7), newline=True)
        jprint(newline=True)
        arr = jarray('char', [None], [jchar('a'), jchar('b')])
        n = jcast('int', 20)
        jprint('生成长度为n，字符来自arr，所有可能的字符串', newline=True)
        strs = HashFunction.generateStrings(arr, n)
        # for (String str : strs) {
        # print(str)
        # }
        jprint(jadd('不同字符串的数量 : ', jcall(strs, 'size')), newline=True)
        set = jnew('HashSet')
        for str in strs:
            jcall(set, 'add', jcall(hash, 'hashValue', str))
        # for (String str : set) {
        # print(str)
        # }
        jprint(jadd('不同哈希值的数量 : ', jcall(set, 'size')), newline=True)
        jprint(newline=True)
        m = jcast('int', 13)
        cnts = jarray('int', [m])
        jprint(jadd(jadd('现在看看这些哈希值，% ', m), ' 之后的余数分布情况'), newline=True)
        mod = jnew('BigInteger', jstatic('String', 'valueOf', m))
        for hashCode in set:
            bigInt = jnew('BigInteger', hashCode, 16)
            ans = jcast('int', jcall(jcall(bigInt, 'mod', mod), 'intValue'))
            cnts[ans] = jcast('int', (cnts[ans] + 1))
        i = jcast('int', 0)
        while (i < m):
            jprint(jadd(jadd(jadd(jadd('余数 ', i), ' 出现了 '), cnts[i]), ' 次'), newline=True)
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    HashFunction.main([])
