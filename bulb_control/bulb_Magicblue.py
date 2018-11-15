import time
from magicblue import MagicBlue
from random import randint
import binascii

bulb1 = 'F8:1D:78:63:0E:7D'
bulb2 = 'F8:1D:78:63:00:0D'
print("Establishing Connection with MagicBlue...")
bulb_mac_address = bulb1
bulb = MagicBlue(bulb_mac_address, 9) # Replace 9 by whatever your version is (default: 7)
bulb.connect()
print("Connection established successfully...")
# print "succesS"

def getbin(a):
	ret = [0]*8
	idx = 0
	while(a>0):
		if(a%2 == 1):
			ret[idx] = 1
		a = a//2
		idx+=1

	return ret

def convert(st):
	msg = []
	for x in st:
		a = ord(x)
		for y in reversed(getbin(a)):
			msg.append(y)

	return msg


bulb.turn_off()

st = "EmbeddedSystem"
# st = "CSAW"
message = convert(st)
print("Message to be passed : "+ st)
print("Message encoded in binary : " + ''.join([str(x) for x in message]))

bulb.turn_on()
for _ in range(10):
	bulb.set_color([0, 0, 0])
	time.sleep(0.2)

for x in message:
	if(x == 0):
		bulb.set_color([0, 100, 0])
		time.sleep(0.8)
	else:
		bulb.set_color([0, 200, 0])
		time.sleep(0.8)

for _ in range(10):
	bulb.set_color([0,255,0])
	time.sleep(0.2)

bulb.turn_off()




# brightness = 0
# incr = True
# while(True):
# 	if incr:
# 		brightness += 10
# 		if brightness >= 255:
# 			incr = False
# 			continue
# 	else:
# 		brightness -= 10
# 		if brightness <= 0:
# 			incr = True
# 			continue
# 	bulb.set_color([brightness, 0, 0])         # Set red
# 	# time.sleep(0.01)
# 	print brightness


# bulb.set_random_color()             # Set random
# bulb.turn_off()                     # Turn off the light
# bulb.turn_on()                      # Set white light

# s = "Hello"
# s_bin = ''.join(format(ord(x), 'b') for x in s)

# print ("String: %s", s)
# print ("String in binary: %s", s_bin)
# print ("Appending 0101 at the beginning...")

# s_bin = '01010101'+s_bin

# bulb.turn_off()
# time.sleep(5)
# bulb.turn_on()
# time.sleep(5)
# for n in s_bin:
# 	if n == '1':
# 		bulb.set_color([0, 255, 0])
# 		time.sleep(5)
# 	if n == '0':
# 		bulb.set_color([0, 180, 0])
# 		time.sleep(5)
# 	print(n)

# bulb.turn_off