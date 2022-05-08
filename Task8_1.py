import smbus
import time

BH1750 = 0x23 # default device I2C address
ONE_TIME_HIGH_RES_MODE = 0x20
 
bus = smbus.SMBus(1) 

# function to converet 2 bytes of data into a decimal number
def convert_to_int(data):
  return ((data[1] + (256 * data[0])) / 1.2)
 
def read_light_sensor(addr=BH1750):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
  return convert_to_int(data)
 
def I2CLightSensor():

      rl = read_light_sensor()
      if rl > 200:
          print("too bright")
      elif rl <= 200 and rl > 25:
          print("bright")
      elif rl <= 25 and rl > 20:
          print("medium")
      elif rl <= 20 and rl > 10:
          print("dark")
      else:
          print("too dark")
      time.sleep(0.5)

while True:
    I2CLightSensor()

