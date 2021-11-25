import smbus as bus
import time

BH1750 = 0x23 ## pre defined address of Light sensor
reciever = 0x20 ## receiver address of I2C.

bus = smbus.SMBus(1)

def Light(): 
    address = bus.read_i2c_block_data(BH1750,reciever)
    value = (address[1] + (256 * address[0]))
    return value

def main():
    while True:
        light_value =Light()

        if(light_value >= 1000):
            print("TOO BRIGHT")
            print(light_value)
            
        elif(light_value >= 700 and light_value < 1000):
            print("BRIGHT")
            print(light_value) 
            
        elif(light_value > 200 and light_value < 700):
            print("MEDIUM")
            print(light_value)
            
        elif(light_value < 50 and light_value > 200):
            print("DARK")
            print(light_value)
            
        else:
            print("TOO DARK")
            print(light_value)
     
        time.sleep(2)

main()
