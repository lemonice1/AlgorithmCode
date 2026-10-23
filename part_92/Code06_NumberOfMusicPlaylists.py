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

# 播放列表的数量
# 给定三个参数，n、l、k
# 你的音乐播放器里有n首不同的歌
# 在旅途中你的旅伴想要听l首歌
# 听得歌曲不一定不同，即允许歌曲重复
# 请你为她按如下两条规则创建一个播放列表
# 1) 每首歌至少播放一次
# 2) 一首歌只有在其他k首歌播放完之后才能再次播放
# 返回可以满足要求的播放列表的数量
# 结果可能很大对1000000007取模
# 测试链接 : https://leetcode.cn/problems/number-of-music-playlists/
class Code06_NumberOfMusicPlaylists:
    __java_fields__ = {'MOD': 'MOD', 'LIMIT': 'LIMIT', 'fac': 'fac', 'inv': 'inv'}
    MOD = 0
    LIMIT = 0
    fac = None
    inv = None
    @staticmethod
    def power(x, n):
        x = jcast('long', x)
        n = jcast('int', n)
        ans = jcast('long', 1)
        while (n > 0):
            if (jcast('int', (n & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code06_NumberOfMusicPlaylists.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code06_NumberOfMusicPlaylists.MOD)))
            n = jcast('int', jcast('int', (n >> (1 & 31))))
        return jcast('long', ans)

    @staticmethod
    def numMusicPlaylists(n, l, k):
        n = jcast('int', n)
        l = jcast('int', l)
        k = jcast('int', k)
        cur = 0
        ans = jcast('long', 0)
        sign = jcast('long', 1)
        i = jcast('int', 0)
        while (i < jcast('int', (n - k))):
            cur = jcast('long', jcast('long', jmod(jcast('long', (sign * Code06_NumberOfMusicPlaylists.power(jcast('int', (jcast('int', (n - i)) - k)), jcast('int', (l - k))))), Code06_NumberOfMusicPlaylists.MOD)))
            cur = jcast('long', jcast('long', jmod(jcast('long', (cur * Code06_NumberOfMusicPlaylists.fac[n])), Code06_NumberOfMusicPlaylists.MOD)))
            cur = jcast('long', jcast('long', jmod(jcast('long', (cur * Code06_NumberOfMusicPlaylists.inv[i])), Code06_NumberOfMusicPlaylists.MOD)))
            cur = jcast('long', jcast('long', jmod(jcast('long', (cur * Code06_NumberOfMusicPlaylists.inv[jcast('int', (jcast('int', (n - i)) - k))])), Code06_NumberOfMusicPlaylists.MOD)))
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, cur)), Code06_NumberOfMusicPlaylists.MOD)))
            i = jcast('int', (i + 1))
            sign = jcast('long', (jcast('int', (Code06_NumberOfMusicPlaylists.MOD - 1)) if (sign == 1) else 1))
        return jcast('int', jcast('int', ans))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_NumberOfMusicPlaylists.MOD = jcast('int', 1000000007)
Code06_NumberOfMusicPlaylists.LIMIT = jcast('int', 100)
Code06_NumberOfMusicPlaylists.fac = jarray('long', [jcast('int', jadd(Code06_NumberOfMusicPlaylists.LIMIT, 1))])
Code06_NumberOfMusicPlaylists.inv = jarray('long', [jcast('int', jadd(Code06_NumberOfMusicPlaylists.LIMIT, 1))])
Code06_NumberOfMusicPlaylists.fac[0] = jcast('long', 1)
i = jcast('int', 1)
while (i <= Code06_NumberOfMusicPlaylists.LIMIT):
    Code06_NumberOfMusicPlaylists.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', i) * Code06_NumberOfMusicPlaylists.fac[jcast('int', (i - 1))])), Code06_NumberOfMusicPlaylists.MOD)))
    i = jcast('int', (i + 1))
jset(Code06_NumberOfMusicPlaylists.inv, Code06_NumberOfMusicPlaylists.LIMIT, Code06_NumberOfMusicPlaylists.power(Code06_NumberOfMusicPlaylists.fac[Code06_NumberOfMusicPlaylists.LIMIT], jcast('int', (Code06_NumberOfMusicPlaylists.MOD - 2))))
i = jcast('int', jcast('int', (Code06_NumberOfMusicPlaylists.LIMIT - 1)))
while (i >= 0):
    Code06_NumberOfMusicPlaylists.inv[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jcast('int', jadd(i, 1))) * Code06_NumberOfMusicPlaylists.inv[jcast('int', jadd(i, 1))])), Code06_NumberOfMusicPlaylists.MOD)))
    i = jcast('int', (i - 1))
