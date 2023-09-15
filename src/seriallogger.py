import serial, serial.tools.list_ports
from datetime import datetime
import time
import re
import sys

verbose = True
ldebug = False
verbp = print if verbose else lambda x: None
debugp = print if ldebug else lambda *x,**y: None


class SerialLogger:
    '''Autoconnect utilities'''
    def __init__(self,baud=9600,parity="N",stopbits=1,verbose=True):
        self.baud = baud
        self.parity = parity
        self.stopbits = stopbits
        #defaul values
        
    
    def trigger():
        pass

    def connector(self,port,tries=2):
        '''tries to connect to a port 'tries' times'''
        try:
            connection = serial.Serial(port,baudrate=self.baud,parity=self.parity,stopbits=self.stopbits,write_timeout=1.0,timeout=1.0)
            connection.reset_input_buffer()
            verbp("✅ Succesful connection at port "+port)
            debugp("🐛Is port " + port + " open?: " + str(connection.is_open),"🐛")
            debugp("🐛Waiting for device handshake🐛")
            connection.reset_input_buffer()
            connection.reset_output_buffer()
            for _ in range(tries):
                connection.write('a'.encode('utf-8'))
                time.sleep(1)
                response = connection.readline()
                dresponse = response.decode('utf-8')
                if dresponse == 'a\r\n':
                    verbp("✅ ArduinoDE found")
                    connection.reset_input_buffer()
                    connection.reset_output_buffer()
                    return connection
                connection.reset_output_buffer()
                connection.reset_input_buffer() 
            verbp("❌ This device is not running ArduinoDE, upload .ino file to board an try again")
            return False
        except Exception as ex:
            debugp(str(ex))
            verbp("❌ Failed connection at at port " + port)
        return False
        
    def ender(self,conn,start=None):
        '''looks for the end keyword and ends the reading, retunrs array of data read '''
        data = []
        debugp("🐛Beginning reader function🐛") 
        reading = True
        while reading == True:
            line = conn.readline()
            debugp(line)
            dline = line.decode('utf-8')
            debugp(dline)
            if dline == "end\r\n":
                end = time.monotonic()
                debugp("Ended reader")
                elapsed = end - start
                debugp(f"Elapsed time:  {elapsed:0.8f} ")  
                reading  = False
                return data
            else:
                noends = dline[0:][:-2]
                dupes = noends.split(",")
                data.append(dupes)
                reading = True
        pass


    def autoConnect(self,port_list=serial.tools.list_ports.comports(),word=None,rest=True,ignorelist=None):
        '''Tries to connect to open ports, useful for when port keep changing, takes is a list of ports to scan or ignore'''
        debugp("🐛PortList:",*port_list,"🐛")
        wordlist = []
        restlist = []
        if word is not None:
            wordlist = [name[0] for name in port_list if re.search(word, str(name))]
            debugp("🐛Wordlist:",wordlist,"🐛")
            if rest:
                restlist = [name[0] for name in port_list if (re.search(word, str(name[0]))) is None]
                debugp("🐛Restlist:",restlist,"🐛")
        if word is None:
            restlist = [name[0] for name in port_list ]
        filteredlist = wordlist+restlist
        debugp("🐛Before ignore",filteredlist)
        if ignorelist is not None:
            ignorelist = list(ignorelist)
            debugp("🐛Ignorelist:",ignorelist,"🐛")
            #filteredlist = [name for name in filteredlist != ignorelist[:]]
            #filteredlist = [list(set(filteredlist).intersection(set(ignorelist))) for filteredlist in ignorelist]
            setfil = set(filteredlist)
            setign = set(ignorelist)
            diff = setfil.difference(setign)
            filteredlist = list(diff)
        if len(filteredlist) == 0:
            verbp("❌No ports/devices found, check word, ignored list or enable rest")
            sys.exit(1)
        debugp("🐛Filteredlist",filteredlist,"🐛")

        for port in filteredlist:
            conn = self.connector(port)
            if conn:
                debugp("🐛Good conn in "+port+"🐛")
                return conn
        
        print("❌ No device found running ArduinoDE")
            

    def MultipleReader(self,connection):
        '''Reads multiple values at a time, returns data list'''
        conn = connection
        verbp("Waiting...")
        while True:
            try:
                buff = conn.readline()
                #print(buff)
                dbuff = buff.decode('utf-8')
                if dbuff == "begin\r\n":
                    start = time.monotonic()
                    verbp("✅ Starting reader")
                    return self.ender(conn,start)
                conn.reset_input_buffer()
            except Exception as e:
                print(str(e))
                print("❌ Device disconnected")
                sys.exit()

        
