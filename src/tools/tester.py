from seriallogger import SerialLogger
from csvwriter import csvwriter
from tools.fakedata import testlist

# this is where the json parsing and main program will run

logger = SerialLogger(verbose=False)

""" connection = logger.autoConnect()
data = logger.MultipleReader(connection)
test = csvwriter("test1","test1",False,True,"%B %d %H:%M:%S","/Users/paulnavarro/Code/repos/NewArduinoLogger/src/csvpathtest")
name = test.makeName()
test.csvWrite(name,data) """

""" test = csvwriter("test2","test2",True,True,"%B %d %H:%M:%S","/Users/paulnavarro/Code/repos/NewArduinoLogger/src/csvpathtest")
name = test.makeName()
test.csvWrite(name,testlist) """


connection = logger.autoConnect()

while True:
    data = logger.MultipleReader(connection)
    writer = csvwriter("test1","test1",False,True,"%B %d %H:%M:%S","/Users/paulnavarro/Code/repos/NewArduinoLogger/src/csvpathtest")
    name = writer.makeName()
    writer.csvWrite(name,data)