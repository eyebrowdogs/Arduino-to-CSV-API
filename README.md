# Arduino To CSV API 
### **Save csv files with sensor data on you computer, no shields or additional devices needed**

- Serial comm-based Python script and Arduino code. 
- Automate data collection over Serial Ports, provide your own config and timing
- Change timestamp format, prefix, sufix, timed or enumerated output in the config.json file. Alternatively provide your own JSON file as:

```bash
$ python3 main.py yourfile.json
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
    "ignorePorts":null
}

```
- **filespath**: Absolute path to save output csvs, leave at null for local repo saving on /CSVs/
- **prefix**: string prefix on filename
- **sufix**: string sufix on filename
- **timestampF**: format string for the timestamp on the filename
see  [datetime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) documentation or https://strftime.org
- **baudRate**: bR of connection, default is 9600
- **port**: String of known port, if null autoconnect is enabled
- **ignorePorts**: Array of ports to be ignored at autoConnect

Pyserial is need to run, install as follows
```bash
$ pip install pyserial
```

## Setup:
1. Upload  `yoursketch.ino` to your board
2. Keep your board connected to your computer
3. Run `main.py` wait for the scrip to detect the arduino and connect to it.
4. Trigger data transmission. A csv file will be saved with you data. See previous to change save path and filenames.

## API Objects
### Serial logger
#### New logger
```python
yourlogger = SerialLogger(baud=9600,parity="N",stopbits=1,verbose=True)
```

#### Autoconnect
```python
yourlogger.autoConnect(port_list=serial.tools.list_ports.comports(),word=None,rest=True,ignorelist=None)
```
- **port_list**: List of ports to be scanned, default is pyserial comports()
- **word**: Word to be looked for in port name
- **rest**: If "word" is not found try rest of ports
- **ignorelist**: List of ports to be ignored

#### Manual connect
```python
yourlogger.connector(port,tries=2)
```

- **tries**: Connection tries

Both connectors return a pyserial serial connection object

```python
yourconnector.MultipleReader(connection)
```
- **connection**: Serial connection object

**Returns** data array. Serial line in each item

### CSV writer

```python
yourWriter = csvwriter(prefix=None,sufix=None,here=False,timeStamp=True,format=None,path=None)
```
- **prefix**: Prefix for files
- **sufix**: Sufix for files
- **here**: Write files in current directory
- **timeStamp**: Write timestamp condition
- **format**: Timestamp format, see https://strftime.org
- **path**:Path for file writing
#### Make name

```python
name = yourWriter.makeName()
```
**Returns** generated name string

#### Write to file

```python
yourWriter.csvWrite(name,data,mode="w"):
```
- **name**: Name to save file as, (eg =.makeName() )
- **data**: Data array to be written (eg =SerialLogger.MultipleReader() )
- **mode**: 'w': Write, 'a': Append

**Outputs** a .csv file

## Example

#### Run main.py 
```bash
$ python3 main.py your-own-config.json
```
Script will connect to configured ports, read values and write the in a loop

```python
    ...

logger = SerialLogger()
connection = logger.autoConnect(ignorelist=ignorePorts)

while True:
    data = logger.MultipleReader(connection)
    writer = csvwriter(prefix=prefix,sufix=sufix,here=False,timeStamp=True,format=timestampF,path=filesPath)
    name = writer.makeName()
    writer.csvWrite(name,data)

...   
```








