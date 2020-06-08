#!/usr/bin/python

import smbus
import time

address = 0x62
bus = smbus.SMBus(1)

bus.write_i2c_block_data(address, 0x06, [0x28, 0x6e]) # 1kHz reference
bus.write_byte(address, 0x10)                         # AM
bus.write_i2c_block_data(address, 0x2c, [0xb8])       # 10.35MHz + 450kHz + 648kHz

time.sleep(10)

bus.write_i2c_block_data(address, 0x04, [0x00, 0xcf]) # 50kHz reference
bus.write_byte(address, 0x11)                         # FM
bus.write_i2c_block_data(address, 0x07, [0xf6])       # 10.7MHz + 91.2MHz


