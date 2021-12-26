import smbus2 as smbus
import time

addr = 0x8 # bus address
bus = smbus.SMBus(1) # indicates /dev/ic2-1
recu = 0
numb = 1

print ("Enter 1 for ON or 0 for OFF")
while numb == 1:

	ledstate = input(">>>>   ")
	bus.write_byte(addr, int(ledstate))
	time.sleep(0.5)
	recu = bus.read_byte(addr)
	print (recu)
	time.sleep(0.5)
