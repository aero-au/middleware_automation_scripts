# This is a script to install Installation Manager

import os
import subprocess

print("Hi, this is an automated script to install Installation Manager")
os.system("pwd")
path = input("Please enter the location of the zip file: ")

os.system("unzip " + path + "/agent*.zip" + " -d " + path + "/IM")
os.system("cd " + path + "/IM" + " && " + "./installc " + "-acceptLicense")
