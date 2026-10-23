# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 火星词典
# 现有一种使用英语字母的火星语言
# 这门语言的字母顺序对你来说是未知的。
# 给你一个来自这种外星语言字典的字符串列表 words
# words 中的字符串已经 按这门新语言的字母顺序进行了排序 。
# 如果这种说法是错误的，并且给出的 words 不能对应任何字母的顺序，则返回 ""
# 否则，返回一个按新语言规则的 字典递增顺序 排序的独特字符串
# 如果有多个解决方案，则返回其中任意一个
# words中的单词一定都是小写英文字母组成的
# 测试链接 : https://leetcode.cn/problems/alien-dictionary/
# 测试链接(不需要会员) : https://leetcode.cn/problems/Jf1JuT/
class Code04_AlienDictionary:
    __java_fields__ = {}
    @staticmethod
    def alienOrder(words):
        # 入度表，26种字符
        indegree = jarray('int', [26])
        jstatic('Arrays', 'fill', indegree, jcast('int', (-1)))
        for w in words:
            i = jcast('int', 0)
            while (i < jcall(w, 'length')):
                jset(indegree, jcast('int', (jcall(w, 'charAt', i) - jchar('a'))), 0)
                i = jcast('int', (i + 1))
        # 'a' -> 0
        # 'b' -> 1
        # 'z' -> 25
        # x -> x - 'a'
        graph = jnew('ArrayList')
        i = jcast('int', 0)
        while (i < 26):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        j = 0
        len = 0
        while (i < jcast('int', (jget(words, 'length') - 1))):
            try:
                cur = words[i]
                next = words[jcast('int', jadd(i, 1))]
                j = jcast('int', 0)
                len = jcast('int', jstatic('Math', 'min', jcall(cur, 'length'), jcall(next, 'length')))
                while (j < len):
                    try:
                        if (jcall(cur, 'charAt', j) != jcall(next, 'charAt', j)):
                            jcall(jcall(graph, 'get', jcast('int', (jcall(cur, 'charAt', j) - jchar('a')))), 'add', jcast('int', (jcall(next, 'charAt', j) - jchar('a'))))
                            ((_java_obj_3 := indegree), (_java_key_4 := jcast('int', (jcall(next, 'charAt', j) - jchar('a')))), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))), _java_old_5)[4]
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if ((j < jcall(cur, 'length')) and (j == jcall(next, 'length'))):
                    return ''
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        queue = jarray('int', [26])
        l = jcast('int', 0)
        r = jcast('int', 0)
        kinds = jcast('int', 0)
        i = jcast('int', 0)
        while (i < 26):
            if (indegree[i] != jcast('int', (-1))):
                kinds = jcast('int', (kinds + 1))
            if (indegree[i] == 0):
                jset(queue, ((_java_old_6 := r), (r := jcast('int', (r + (1)))), _java_old_6)[2], i)
            i = jcast('int', (i + 1))
        ans = jnew('StringBuilder')
        while (l < r):
            cur = jcast('int', queue[((_java_old_7 := l), (l := jcast('int', (l + (1)))), _java_old_7)[2]])
            jcall(ans, 'append', jcast('char', jcast('int', jadd(cur, jchar('a')))))
            for next in jcall(graph, 'get', cur):
                if (((_java_obj_8 := indegree), (_java_key_9 := next), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))))[3] == 0):
                    jset(queue, ((_java_old_11 := r), (r := jcast('int', (r + (1)))), _java_old_11)[2], next)
        return (jcall(ans, 'toString') if (jcall(ans, 'length') == kinds) else '')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


