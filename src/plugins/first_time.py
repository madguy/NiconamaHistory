#-*- coding:utf-8
'''
Created on 2011/03/20

@author: madguy
'''
from niconama_history.plugin_base import PluginBase

class CommentFilter(PluginBase):
    """
    放送開始日を抽出するプラグインです。
    """
    def __init__(self):
        self.__flag = True

    def analyzeDay(self, date, rows):
        if self.__flag:
            self.__flag = False
            return u'放送を開始しました！'

if __name__ == '__main__':
    pass