#!/usr/bin/env python3
import serial,time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        for i in range(10):
            ser.write(bytes(f"{i}", "utf-8"))
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(2)
