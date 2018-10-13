#author : ben
import sys, os
from datetime import datetime

import binascii

def replace_hex(original_path,new_bin_path,start_region=0x0):
    orig_f = read_file(original_path) #read full file
    new_bin_f = read_file(new_bin_path) #read binary to replace
    
    orig = bytearray.fromhex(orig_f)
    new_bin = bytearray.fromhex(new_bin_f)    
    
    for i in range(len(new_bin)):
        orig[start_region + i] = new_bin[i]
    
    save_file(orig)

def read_file(path):
    # Open in binary mode (so you don't read two byte line endings on Windows as one byte)
    with open(path, 'rb') as f:
        hexdata = binascii.hexlify(f.read())
    return hexdata

def save_file(bin_file):
    new_byte_array = bytearray(bin_file)
    outputName = "HEX_Replace-%s.bin" % (datetime.now().strftime("%Y-%d-%m--%H-%M-%S"))
    with open(outputName, 'wb') as file:
        file.write(new_byte_array)
    print "File saved to %s." % (os.getcwd() + "\\" + outputName)
    
def hexa(val): 
    #format
    return hex(val)[2:].zfill(2)