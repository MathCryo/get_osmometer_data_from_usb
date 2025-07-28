# import serial
# s="empty"
# with serial.Serial('/dev/ttyUSB0', 9600, timeout=10) as ser:
#     # w = ser.write(b'')
#     s = ser.readlines() 
#     print(s)# read up to ten bytes (timeout)
#     # line = ser.readline()   # read a '\n' terminated line
# print(s)
# def collect_data(exeriment_duration):
#
import asyncio
import serial_asyncio
import time
import logging
from datetime import date # python package for working with date/time
""" SET THE PORT FOR THE WHOLE FILE HERE"""
PORT ="/dev/ttyUSB0"
# Create and configure a logger
todays_date = date.today()
date_based_logfile = f"Osmometry_data-on-{todays_date}.log"

logging.basicConfig(
    filename=date_based_logfile,
    filemode='a',
    format='%(levelname)s - %(asctime)s - %(message)s',
    level=logging.INFO
)
async def read_serial_data(reader):
    while True:
        data = await reader.readline() # or reader.read(num_bytes)
        if not data:
            break # Connection closed
        print("Received:", data.decode().strip())
        logging.info(data.decode().strip())
async def main():
    reader, writer = await serial_asyncio.open_serial_connection(
        url=PORT, baudrate=9600) # Replace with your port

    try:
        await read_serial_data(reader)
    except asyncio.CancelledError:
        pass # Task cancelled, e.g., on program exit
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
