import subprocess
import os

def upload_arduino_code(port):
    path = os.path.abspath(os.curdir)
    sketch_file = os.path.join(path,"src/ArduinoDE.ino.hex")
    avrdude_cmd = f'avrdude -v -patmega328p -carduino -P{port} -b115200 -D -Uflash:w:{sketch_file}:i'
    subprocess.call(avrdude_cmd, shell=True)


#board_type = 'arduino:avr:uno'  
#port = '/dev/tty.usbmodem1101'  

#upload_arduino_code(port)
