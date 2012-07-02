# use gdb: gdb -x gdbtrace.py dhrystone > /dev/null
class GdbTracer:
    def __init__(self):
        self.outfile=open("trace.txt",'w')
        gdb.execute("set interactive-mode off")
    def fire(self):
        gdb.Breakpoint("main")
        gdb.execute("run")
        i=gdb.inferiors()[0]
        while(i.is_valid()):
            s=gdb.execute("disas $pc,+1",to_string=True)
            s=s.split('\n')[1]
            #print(s,file=self.outfile) # this is for python3
            print  >>self.outfile, s     # this is for python2
            gdb.execute("stepi")
        self.outfile.close
        gdb.execute("quit")
t=GdbTracer()
t.fire()
