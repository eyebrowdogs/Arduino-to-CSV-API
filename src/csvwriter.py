import serial,csv, serial.tools.list_ports
from datetime import datetime
import time
import os

verbose = True
ldebug = False
verbp = print if verbose else lambda x: None
debugp = print if ldebug else lambda *x,**y: None



class csvwriter:
    def __init__(self,prefix=None,sufix=None,here=False,timeStamp=True,format=None,path=None):
        self.prefix = prefix
        self.sufix = sufix
        self.here = here
        self.ts = timeStamp
        self.format = format
        self.path = path



    def addEnds(self,name,prefix,sufix): #remove ifs just do
        """ if self.prefix is not None:
            name = f"{self.prefix} {name}"
        if self.sufix is not None:
            name = f"{self.sufix} {name}" """
        if prefix is not None:
            name = f"{prefix} {name}"
        if sufix is not None:
            name = f"{name} {sufix} "
        return name
        


    def getTimestamp(self,format):
        now = datetime.now()
        timestamp = str(now.strftime(format))
        return timestamp

    def pathFormater(self,name,path):
        if path is None: #writes on current path
            path = os.path.abspath(os.curdir)  
            name = os.path.join(path,"CSVs",name)+".csv"
            return name
        else:
            try:
                name = os.path.join(path, name)+".csv"
            except Exception as e:
                print(str(e))
                verbp("❌Could not find path from config key path")
            #return name
        return name
    
    def makeName(self):
        if self.ts and self.format:
            try:
                name = self.getTimestamp(self.format)
            except Exception:
                pass
        else:
            name = "data"
        
        if self.prefix or self.sufix is not None:
            name = self.addEnds(name,self.prefix,self.sufix)
        
        if self.here is False and self.path is not None:
            name = self.pathFormater(name,self.path)
        debugp(name)
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


