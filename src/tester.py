from rewrite import SerialLogger
from csvwriter import csvwriter
from fakedata import testlist

# this is where the json parsing and main program will run

""" logger = SerialLogger()

print(logger.baud)

connection = logger.autoConnect()

data = logger.MultipleReader(connection)

try:
    print(data)
except Exception:
    pass """

test = csvwriter()
test.csvWrite("test1",testlist)