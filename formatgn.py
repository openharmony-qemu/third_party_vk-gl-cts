#!/usr/bin/python3
import os
import sys
import json
import time
import datetime
import subprocess
import shutil
import openpyxl as op
import threading
import requests
import json

def formate_gn():
    top_info = subprocess.Popen(["find", ".", "-name", "*.gn"], stdout=subprocess.PIPE)
    out, err = top_info.communicate()
    strout = out.decode('utf-8')
    gnlist = strout.split('\n') 
    # print("find gn out------:", )

    for ign in gnlist:
        formatcmd = "cat " + ign + " | ../../src/prebuilts/build-tools/linux-x86/bin/gn format --stdin > FORMAT_RESULT.gn;cp -f FORMAT_RESULT.gn " + ign + ";rm FORMAT_RESULT.gn"
        print("format: ", formatcmd)
        os.system(formatcmd)
    # f = open(dirname+"/"+logname, 'w+')
    # f.write(str(curr_time)+"\n")
    # f.write(str(out))
    # f.close()

if __name__ == '__main__':
    formate_gn()