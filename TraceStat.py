#!/usr/bin/python
import sys,string
class TraceStat:
    def __init__(self,f):
        self.instcnt={}
        self.infile=f
    def run(self):
        while 1:
            line=self.infile.readline()
            if not line:
                break
            a=line.split(':')[1]
            b=a.split(' ')[0].replace('\t','')
            b=b.replace(' ','')
            try:
                self.instcnt[b]=self.instcnt[b]+1
            except KeyError:
                self.instcnt[b]=1
    def dumpres(self):
        for k,v in self.instcnt.items():
            print(str(v)+"\t"+str(k))
t=TraceStat(sys.stdin)
t.run()
t.dumpres()

