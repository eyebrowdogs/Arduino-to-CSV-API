#!/usr/bin/env python
from seriallogger import SerialLogger
from csvwriter import csvwriter
import sys
import os
import json


if len(sys.argv)>=2:
    configPath = str(sys.argv[1])
else:   configPath = "src/config.json"

subpath = os.path.abspath(os.curdir)
print(subpath)
subpath = os.path.join(subpath,configPath)
print(subpath)

try:
    
    with open (subpath, 'r') as f:
        configData = json.load(f)
except Exception:
    print("❌ Failed to read configuration file, check for config.json or provide a valid configuration file")
    print("Eg:$ main.py myconfig.json")

    filesPath = None
    prefix = None
    sufix = None
    timestampF = "%d-%m-%Y-%H:%M:%S"
    baudrate = None
    port = None
    ignorePorts = None

try:
    filesPath = configData['filesPath']
    prefix = configData['prefix']
    sufix = configData['sufix']
    timestampF = configData['timestampF']
    baudrate = configData['baudRate']
    port = configData['port']
    ignorePorts = configData['ignorePorts']


except Exception as e:
    print(str(e))
    print('❌Missing keys for config JSON')


logger = SerialLogger()
connection = logger.autoConnect(ignorelist=ignorePorts)

while True:
    data = logger.MultipleReader(connection)
    writer = csvwriter(prefix=prefix,sufix=sufix,here=False,timeStamp=True,format=timestampF,path=filesPath)
    name = writer.makeName()
    writer.csvWrite(name,data)

