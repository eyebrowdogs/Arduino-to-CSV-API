import serial,csv, serial.tools.list_ports
from datetime import datetime
import time
import os

verbose = True
ldebug = True
verbp = print if verbose else lambda x: None
debugp = print if ldebug else lambda *x,**y: None



class csvwriter:
    def __init__(self,prefix=None,sufix=None):
        self.prefix = prefix
        self.sufix = sufix

    def addEnds(self,name):
        if self.prefix is not None:
            name = f"{self.prefix} {name}"
        if self.sufix is not None:
            name = f"{self.sufix} {name}"

    def getTimestamp(self,format):
        now = datetime.now()
        timestamp = str(now.strftime(format))

    def pathFormater(self,name,path):
        if path is None: #writes on current path
            path = os.path.abspath(os.curdir)  
            name = os.path.join(path,"CSVs",name)+".csv"
            #return name
        else: # writes on config key path
            try:
                name = os.path.join(path, name)+".csv"
            except Exception as e:
                print(str(e))
                verbp("❌Could not find path from config key path")
            #return name
        return name
    
    def csvWrite(self,name,data,mode="w"):
        try:
            with open(name, mode,newline="\n",) as f:
                print("Writing csv..")
                writer = csv.writer(f)
                writer.writerows(data)
                verbp('✅ csv written successfully')

        except Exception:
            verbp("❌ Failed to open file, check path:")
            print(str(name))


