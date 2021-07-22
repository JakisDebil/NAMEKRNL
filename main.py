#boot
print("Type help for help")
#import
import platform
import os
import time
from time import sleep
#get OS
_os = platform.system()
#def functions
def clear():
  if _os == "Linux":
    os.system("clear")
  if _os == "Windows":
    os.system("cls")
#mine loop
while True:
  cmd = input("root@main:˜# ")
  
  #check commands
  if cmd == "help":
    print("----------\n - help: show commands\n - clear: clear screen\n----------")
  if cmd == "clear":
    clear()
  if cmd == "dist":
    print("System: [NAME]KRNL\nRelase: 0\nVersion: v0.1alpha\nKrnl: [NAME]\nKrnl Version: v0.2beta\n")
  if cmd == "test":
    print("Testing...")
    sleep(2)
    print("Your Computer [OK]")
  if cmd == "load":
    print("Loading...")
    sleep(5)
    print("Loaded.")