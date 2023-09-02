# ArduinoToCSV
### **Save csv files with sensor data on you computer, no shields or additional devices needed**

- Serial comm-based python script and Arduino code. 
- Button controlled data collection triggering. Press once to start, green LED will light up and data will be sent. Press again to stop, red LED will light up signaling no data is being sent.
- Python script saves a csv file after data RX is complete. Look in the script's "CSVs" directory for timestamped files.
- Docs folder contains a SolidWorks assembly of the pictured enclosure, STLs and .sldprt files.
- Change timestamp format, prefix, sufix, timed or enumerated output in the config.json file. Alternatively provide your own JSON file as:

```bash
$ python3 serial_com.py yourfile.json
```
Your file must follow this format:

```json
{
    "filesPath": null,
    "prefix": "Example",
    "sufix": "Example",
    "timestampF": "%B %d %H:%M:%S",
    "baudRate": null,
    "port": null,
    "CA": false,
    "livePlots": true,
    "timer": true
}

```
- **filespath**: Absolute path to save output csvs, leave at null for local repo saving on /CSVs/
- **prefix**: string prefix on filename
- **sufix**: string sufix on filename
- **timestampF**: format string for the timestamp on the filename
see  [datetime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) documentation or https://strftime.org
- **baudRate**: bR of connection, default is 9600
- **CA**: Continuously append. Append on each reading, good for long sessions
- **timer**: replace counter with milliseconds from the start

Pyserial is need to run, install as follows
```bash
$ pip install pyserial
```

## Setup:
1. Upload  `src/ArduinoDE/ArduinoDE.ino` to your board
2. Keep your board connected to your computer
3. Run `serial_com.py` wait for the scrip to detect the arduino and connect to it.
4. Click the button to collect data and click again to stop. A csv file will be saved with you data. See previous to change save path and filenames.


PASCO capstone-like DIY spring plotter made for **PhD. Pablo Enrique Moreira** 
by **Paul Navarro Amezcua**
at *Universidad Ánahuac Querétaro.* 
    Métodos Cuantitativos Dept.

<img src="https://raw.githubusercontent.com/eyebrowdogs/ArduinoDE/main/docs/ensamble%203.PNG" width="350">



(Enclosure, status LEDs etc are optional, a sensor of any type can be used paired to the Arduino board in any wiring configuration. Modify the Arduino code accordingly)

| Components  | Notes |
| ------------- | ------------- |
| Arduino UNO  | (AVR board) |
| Red 5mm LED  | 220 Ohm resitor in series  |
| Green 5mm LED | 220 Ohm resitor in series  |
| 2/4 pin 6mm Push Button | 10k Ohm pull-down resitor in series  |
| Mini 170 Breadboard | (Or solder averything together)  |
| 7 M3x10mm Screws  | (I used wood screws) |

