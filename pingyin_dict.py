#!/usr/bin/python3
#coding=utf-8

class my_pinyin_dict():

   def __init__(self, pinyin_dict_file = r'.\pinyin_dict.txt'):
        self.read_file(pinyin_dict_file)

        self.zi_list = []
        self.py_list = []
        for item in self.pinyin_list:
            self.zi_list.append(item[0])
            self.py_list.append(item[1:])

   def read_file(self, pinyin_dict_file):
       f = open(pinyin_dict_file, "r", encoding='utf-8')
       PINYIN_DICT = f.read()
       f.close()
       self.pinyin_list = PINYIN_DICT.split(",")

   def fun(self, chr):
       try:
           i = self.zi_list.index(chr)
           return (self.zi_list[i],
                    self.py_list[i])
       except ValueError:
           return None


if __name__ == "__main__":
    md = my_pinyin_dict()
    print(md.fun("蜄"))
