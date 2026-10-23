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

# 文本编辑器，块状链表实现，Python版
# 一开始文本为空，光标在文本开头，也就是1位置，请实现如下6种操作
# Move k     : 将光标移动到第k个字符之后，操作保证光标不会到非法位置
# Insert n s : 在光标处插入长度为n的字符串s，光标位置不变
# Delete n   : 删除光标后的n个字符，光标位置不变，操作保证有足够字符
# Get n      : 输出光标后的n个字符，光标位置不变，操作保证有足够字符
# Prev       : 光标前移一个字符，操作保证光标不会到非法位置
# Next       : 光标后移一个字符，操作保证光标不会到非法位置
# Insert操作时，字符串s中ASCII码在[32,126]范围上的字符一定有n个，其他字符请过滤掉
# 测试链接 : https://www.luogu.com.cn/problem/P4008
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_TextEditor2:
    __java_fields__ = {'MAXN': 'MAXN', 'BLEN': 'BLEN', 'BNUM': 'BNUM', 'space': 'space', 'pool': 'pool', 'top': 'top', 'nxt': 'nxt', 'siz': 'siz', 'str': 'str', 'bi': 'bi', 'pi': 'pi'}
    # 整个文章能到达的最大长度
    MAXN = 0
    # 块内容量，近似等于 2 * 根号n，每块内容大小不会超过容量
    BLEN = 0
    # 块的数量上限
    BNUM = 0
    # 写入内容的空间，编号为i的块，内容写入到space[i]
    space = None
    # 编号分配池，其实是一个栈，分配编号从栈顶弹出，回收编号从栈顶压入
    pool = None
    # 分配池的栈顶
    top = 0
    # nxt[i]表示编号为i的块，下一块的编号
    nxt = None
    # siz[i]表示编号为i的块，写入了多少长度的内容
    siz = None
    # 插入字符串时，先读入进str，然后写入到块
    # 获取字符串时，先从块里取出内容保留在str，然后打印str
    str = None
    # 准备好分配池，从栈顶到栈底，依次是1、2、... BNUM - 1
    # 准备好头块的配置
    @staticmethod
    def prepare():
        i = jcast('int', 1)
        id = jcast('int', jcast('int', (Code06_TextEditor2.BNUM - 1)))
        while (i < Code06_TextEditor2.BNUM):
            Code06_TextEditor2.pool[i] = jcast('int', id)
            i = jcast('int', (i + 1))
            id = jcast('int', (id - 1))
        Code06_TextEditor2.top = jcast('int', jcast('int', (Code06_TextEditor2.BNUM - 1)))
        Code06_TextEditor2.siz[0] = jcast('int', 0)
        Code06_TextEditor2.nxt[0] = jcast('int', jcast('int', (-1)))

    # 分配编号
    @staticmethod
    def assign():
        return jcast('int', Code06_TextEditor2.pool[((_java_obj_1 := Code06_TextEditor2), (_java_key_2 := 'top'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))), _java_old_3)[4]])

    # 回收编号
    @staticmethod
    def recycle(id):
        id = jcast('int', id)
        jset(Code06_TextEditor2.pool, ((_java_obj_4 := Code06_TextEditor2), (_java_key_5 := 'top'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], id)

    # 寻找整个文章中的pos位置
    # 找到所在块的编号 和 块内位置
    # 块编号设置给bi，块内位置设置给pi
    bi = 0
    pi = 0
    @staticmethod
    def find(pos):
        pos = jcast('int', pos)
        curb = jcast('int', 0)
        while ((curb != jcast('int', (-1))) and (pos > Code06_TextEditor2.siz[curb])):
            pos = jcast('int', jcast('int', (pos - Code06_TextEditor2.siz[curb])))
            curb = jcast('int', Code06_TextEditor2.nxt[curb])
        Code06_TextEditor2.bi = jcast('int', curb)
        Code06_TextEditor2.pi = jcast('int', pos)

    # 链表中让curb块和nextb块，连在一起，然后让nextb块从0位置开始，写入如下的内容
    # 从src[pos]开始，拿取长度为len的字符串
    @staticmethod
    def linkAndWrite(curb, nextb, src, pos, len):
        curb = jcast('int', curb)
        nextb = jcast('int', nextb)
        pos = jcast('int', pos)
        len = jcast('int', len)
        Code06_TextEditor2.nxt[nextb] = jcast('int', Code06_TextEditor2.nxt[curb])
        Code06_TextEditor2.nxt[curb] = jcast('int', nextb)
        jstatic('System', 'arraycopy', src, pos, Code06_TextEditor2.space[nextb], 0, len)
        Code06_TextEditor2.siz[nextb] = jcast('int', len)

    # curb块里，在内容的后面，追加nextb块的内容，然后nextb块从链表中删掉
    @staticmethod
    def merge(curb, nextb):
        curb = jcast('int', curb)
        nextb = jcast('int', nextb)
        jstatic('System', 'arraycopy', Code06_TextEditor2.space[nextb], 0, Code06_TextEditor2.space[curb], Code06_TextEditor2.siz[curb], Code06_TextEditor2.siz[nextb])
        Code06_TextEditor2.siz[curb] = jcast('int', jcast('int', jadd(Code06_TextEditor2.siz[curb], Code06_TextEditor2.siz[nextb])))
        Code06_TextEditor2.nxt[curb] = jcast('int', Code06_TextEditor2.nxt[nextb])
        Code06_TextEditor2.recycle(nextb)

    # curb块的pos位置往后的内容，写入到新分裂出的块里
    @staticmethod
    def split(curb, pos):
        curb = jcast('int', curb)
        pos = jcast('int', pos)
        if ((curb == jcast('int', (-1))) or (pos == Code06_TextEditor2.siz[curb])):
            return
        nextb = jcast('int', Code06_TextEditor2.assign())
        Code06_TextEditor2.linkAndWrite(curb, nextb, Code06_TextEditor2.space[curb], pos, jcast('int', (Code06_TextEditor2.siz[curb] - pos)))
        Code06_TextEditor2.siz[curb] = jcast('int', pos)

    # 从头到尾遍历所有的块，检查任意相邻块，内容大小的累加和 <= 块内容量，就合并
    @staticmethod
    def maintain():
        curb = jcast('int', 0)
        nextb = 0
        while (curb != jcast('int', (-1))):
            nextb = jcast('int', Code06_TextEditor2.nxt[curb])
            while ((nextb != jcast('int', (-1))) and (jcast('int', jadd(Code06_TextEditor2.siz[curb], Code06_TextEditor2.siz[nextb])) <= Code06_TextEditor2.BLEN)):
                Code06_TextEditor2.merge(curb, nextb)
                nextb = jcast('int', Code06_TextEditor2.nxt[curb])
            curb = jcast('int', Code06_TextEditor2.nxt[curb])

    # 插入的字符串在str中，长度为len，从整个文章的pos位置插入
    @staticmethod
    def insert(pos, len):
        pos = jcast('int', pos)
        len = jcast('int', len)
        Code06_TextEditor2.find(pos)
        Code06_TextEditor2.split(Code06_TextEditor2.bi, Code06_TextEditor2.pi)
        curb = jcast('int', Code06_TextEditor2.bi)
        newb = 0
        done = jcast('int', 0)
        while (jcast('int', jadd(done, Code06_TextEditor2.BLEN)) <= len):
            newb = jcast('int', Code06_TextEditor2.assign())
            Code06_TextEditor2.linkAndWrite(curb, newb, Code06_TextEditor2.str, done, Code06_TextEditor2.BLEN)
            done = jcast('int', jcast('int', jadd(done, Code06_TextEditor2.BLEN)))
            curb = jcast('int', newb)
        if (len > done):
            newb = jcast('int', Code06_TextEditor2.assign())
            Code06_TextEditor2.linkAndWrite(curb, newb, Code06_TextEditor2.str, done, jcast('int', (len - done)))
        Code06_TextEditor2.maintain()

    # 从整个文章的pos位置，往后len的长度，这些内容删掉
    @staticmethod
    def erase(pos, len):
        pos = jcast('int', pos)
        len = jcast('int', len)
        Code06_TextEditor2.find(pos)
        Code06_TextEditor2.split(Code06_TextEditor2.bi, Code06_TextEditor2.pi)
        curb = jcast('int', Code06_TextEditor2.bi)
        nextb = jcast('int', Code06_TextEditor2.nxt[curb])
        while ((nextb != jcast('int', (-1))) and (len > Code06_TextEditor2.siz[nextb])):
            len = jcast('int', jcast('int', (len - Code06_TextEditor2.siz[nextb])))
            Code06_TextEditor2.recycle(nextb)
            nextb = jcast('int', Code06_TextEditor2.nxt[nextb])
        if (nextb != jcast('int', (-1))):
            Code06_TextEditor2.split(nextb, len)
            Code06_TextEditor2.recycle(nextb)
            Code06_TextEditor2.nxt[curb] = jcast('int', Code06_TextEditor2.nxt[nextb])
        else:
            Code06_TextEditor2.nxt[curb] = jcast('int', jcast('int', (-1)))
        Code06_TextEditor2.maintain()

    # 从整个文章的pos位置，往后len的长度，这些内容找到，写入进str
    @staticmethod
    def get(pos, len):
        pos = jcast('int', pos)
        len = jcast('int', len)
        Code06_TextEditor2.find(pos)
        curb = jcast('int', Code06_TextEditor2.bi)
        pos = jcast('int', Code06_TextEditor2.pi)
        done = jcast('int', (len if (len < jcast('int', (Code06_TextEditor2.siz[curb] - pos))) else jcast('int', (Code06_TextEditor2.siz[curb] - pos))))
        jstatic('System', 'arraycopy', Code06_TextEditor2.space[curb], pos, Code06_TextEditor2.str, 0, done)
        curb = jcast('int', Code06_TextEditor2.nxt[curb])
        while ((curb != jcast('int', (-1))) and (jcast('int', jadd(done, Code06_TextEditor2.siz[curb])) <= len)):
            jstatic('System', 'arraycopy', Code06_TextEditor2.space[curb], 0, Code06_TextEditor2.str, done, Code06_TextEditor2.siz[curb])
            done = jcast('int', jcast('int', jadd(done, Code06_TextEditor2.siz[curb])))
            curb = jcast('int', Code06_TextEditor2.nxt[curb])
        if ((curb != jcast('int', (-1))) and (done < len)):
            jstatic('System', 'arraycopy', Code06_TextEditor2.space[curb], 0, Code06_TextEditor2.str, done, jcast('int', (len - done)))

    @staticmethod
    def main(args):
        in_ = Code06_TextEditor2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('BufferedOutputStream', jget(System, 'out')))
        n = jcast('int', jcall(in_, 'nextInt'))
        pos = jcast('int', 0)
        len = 0
        op = None
        Code06_TextEditor2.prepare()
        i = jcast('int', 1)
        while (i <= n):
            op = jcall(in_, 'nextString')
            if jcall(op, 'equals', 'Prev'):
                pos = jcast('int', (pos - 1))
            else:
                if jcall(op, 'equals', 'Next'):
                    pos = jcast('int', (pos + 1))
                else:
                    if jcall(op, 'equals', 'Move'):
                        pos = jcast('int', jcall(in_, 'nextInt'))
                    else:
                        if jcall(op, 'equals', 'Insert'):
                            len = jcast('int', jcall(in_, 'nextInt'))
                            j = jcast('int', 0)
                            while (j < len):
                                jset(Code06_TextEditor2.str, j, jcall(in_, 'nextChar'))
                                j = jcast('int', (j + 1))
                            Code06_TextEditor2.insert(pos, len)
                        else:
                            if jcall(op, 'equals', 'Delete'):
                                len = jcast('int', jcall(in_, 'nextInt'))
                                Code06_TextEditor2.erase(pos, len)
                            else:
                                len = jcast('int', jcall(in_, 'nextInt'))
                                Code06_TextEditor2.get(pos, len)
                                jcall(out, 'write', Code06_TextEditor2.str, 0, len)
                                jcall(out, 'write', jchar('\n'))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

        # 读取下一个ASCII码范围在[32,126]的字符
        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not (((c < 32) or (c > 126))):
                    break
            return jcast('char', jcast('char', c))

        def nextString(self):
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            sb = jnew('StringBuilder', 16)
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                jcall(sb, 'append', jcast('char', b))
                b = jcast('byte', self.readByte())
            return jcall(sb, 'toString')

        def nextInt(self):
            num = jcast('int', 0)
            sign = jcast('int', 1)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            if (b == jchar('-')):
                sign = jcast('int', jcast('int', (-1)))
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', jcast('int', (sign * num)))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code06_TextEditor2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_TextEditor2.MAXN = jcast('int', 3000001)
Code06_TextEditor2.BLEN = jcast('int', 3001)
Code06_TextEditor2.BNUM = jcast('int', jcast('int', (jcast('int', jdiv(Code06_TextEditor2.MAXN, Code06_TextEditor2.BLEN)) << (1 & 31))))
Code06_TextEditor2.space = jarray('char', [Code06_TextEditor2.BNUM, Code06_TextEditor2.BLEN])
Code06_TextEditor2.pool = jarray('int', [Code06_TextEditor2.BNUM])
Code06_TextEditor2.top = jcast('int', 0)
Code06_TextEditor2.nxt = jarray('int', [Code06_TextEditor2.BNUM])
Code06_TextEditor2.siz = jarray('int', [Code06_TextEditor2.BNUM])
Code06_TextEditor2.str = jarray('char', [Code06_TextEditor2.MAXN])
Code06_TextEditor2.bi = jcast('int', 0)
Code06_TextEditor2.pi = jcast('int', 0)

if __name__ == '__main__':
    Code06_TextEditor2.main([])
