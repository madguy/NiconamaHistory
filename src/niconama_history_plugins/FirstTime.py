#-*- coding:utf-8
'''
Created on 2011/03/20

@author: madguy
'''
from niconama_history.PluginBase import PluginBase

class commentFilter(PluginBase):

    def __init__(self, db):
        PluginBase.__init__(self)
        self.__flag = True

    @property
    def name(self):
        return 'FirstTimer'

    def analyzeDay(self, rows):
        if self.__flag:
            self.__flag = False
            return '放送を開始しました！'

if __name__ == '__main__':
    pass