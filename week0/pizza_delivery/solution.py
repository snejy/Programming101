import sys

DICTIONARY = {}

def take(name, price):
    keys = sorted(DICTIONARY, key = DICTIONARY.get)
    if name in keys:
        DICTIONARY[name] = DICTIONARY[name] + float(price)
    else:
        DICTIONARY[name] = float(price)
    print("Taking order from {} for {}".format(name, price))

def status():
    for i in DICTIONARY:
        print(i + " - " + str(DICTIONARY[i]))

from time import time
from datetime import datetime

def save():
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filename = "orders_" + stamp + ".txt"
    file = open(filename, "w")
    TIMESTAMPS.append(filename)
    file.write(str(DICTIONARY))
    file.close()

TIMESTAMPS = []

def list():
    for i in range(0,len(TIMESTAMPS)):
        print(str([i + 1]) + ' - ' + TIMESTAMPS[i])

import ast

def load(number):
    flag = False
    text = "You have not saved the current order.If you wish to discard it, type load {} again.".format(number)
    if "list" not in COMMANDS:
        print("Use list command before loading.")
        return
    if 'save' not in COMMANDS and COMMANDS[len(COMMANDS) - 1] != 'load':
        print(text)
        flag = False
    if 'save' in COMMANDS:
        COMMANDS.reverse()
        if COMMANDS.index('save') > COMMANDS.index('take') and COMMANDS[0] != 'load':
            print(text)
            flag = False
        COMMANDS.reverse()
    if flag == True or COMMANDS[len(COMMANDS)-1] == "load":
        file = open(TIMESTAMPS[int(number)-1],"r")
        content = file.read()
        global DICTIONARY 
        DICTIONARY = dict(ast.literal_eval(content))

COMMANDS = []

def main():
    while True: 
        command = input("Enter command>")
        command = command.split(" ")
        if command[0] == "take":
            take(command[1], command[2])
            COMMANDS.append(command[0])
        if command[0] == "status":
            status()
            COMMANDS.append(command[0])
        if command[0] == "save":
            save()
            COMMANDS.append(command[0])
        if command[0] == "list":
            list()
            COMMANDS.append(command[0])
        if command[0] == "load":
            load(command[1])
            COMMANDS.append(command[0])
        if command[0] == "finish":
            print("Finishing order. Goodbye!")
            break
        if command[0] not in ['save','take','list','load','status']:
            unknown = ["Unknown command!","Try one of the following:", 
                "take <name> <price>",  "status",   "save", "list",
                "load <number>",    "finish", "Enter command>"]
            for i in range(0,len(unknown)):
                print(unknown[i])

if __name__ == '__main__':
    main()