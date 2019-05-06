# Garrett Morris
# Advanced Operating Systems
# 05/06/2019
# Objectives: The objective of this project was to run a 
# simulation of virtual memory paging schemes. Four different
# paging schemes were implemented: First-In-First-Out, Random,
# Least Recently Used, and Least Frequently Used.

import random
import matplotlib.pyplot as plt
import os

# user input for which file simulation to run
data_file = input("Please choose a file 1-10 to run simulation ")

# data files are stored in a directory of this project called 'snapshots'
if data_file == str(1):
    f = open('snapshots/sim_0_3_512_256.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 256
    title = 'sim_0_3_512_256'
elif data_file == str(2):
    f = open('snapshots/sim_1_5_1024_256.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 256
    title = 'sim_1_5_1024_256'
elif data_file == str(3):
    f = open('snapshots/sim_2_5_1024_512.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 512
    title = 'sim_2_5_1024_512'
elif data_file == str(4):
    f = open('snapshots/sim_3_5_1024_768.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 768
    title = 'sim_3_5_1024_768'
elif data_file == str(5):
    f = open('snapshots/sim_4_10_1024_256.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 256
    title = 'sim_4_10_1024_256'
elif data_file == str(6):
    f = open('snapshots/sim_5_10_1024_512.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 512
    title = 'sim_5_10_1024_512'
elif data_file == str(7):
    f = open('snapshots/sim_6_10_1024_768.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 768
    title = 'sim_6_10_1024_768'
elif data_file == str(8):
    f = open('snapshots/sim_7_25_1024_256.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 256
    title = 'sim_7_25_1024_256'
elif data_file == str(9):
    f = open('snapshots/sim_8_25_1024_512.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 512
    title = 'sim_8_25_1024_512'
elif data_file == str(10):
    f = open('snapshots/sim_9_25_1024_768.txt')
    r = f.read()
    data = r.split(' ')
    data.pop(len(data) -1)
    pm = 768
    title = 'sim_9_25_1024_768'

phys_mem = {} # dictionary to store hex addresses
page_fault = 0 # number of page faults
page_fault_final = []

# initialize dictionary along with variables for replacement algorithms
for x in range(pm):
    phys_mem[x] = ['', 0, 1]

#------------------------------------------------------------
# FIFO
page_fault = 0 # track page faults
fill = 0 # track which slot in physical memory needs to be replaced
for item in data: # traverse list with all addresses
    trash, hex_address = item.split(",0x") # split the address into process and hex address
    dec_address = int(hex_address, 16) # convert hex address into decimal

    present = False # boolean to track if address is in physical memory

    for slot in phys_mem: # traverse dictionary containing physical memory slots
        if phys_mem[slot][0] == dec_address: # if the hex address is in physical memory
            present = True
    if not present:
        phys_mem[fill][0] = dec_address 
        print(item + " = Process " + trash + " access line " + str(dec_address))
        page_fault += 1
        if fill < (pm - 1): # check to see if physical memory is full
            fill += 1 
        else:
            fill = 0 # reset physical memory tracker to 0 so the oldest entry will be replaced
page_fault_final.append(page_fault)
#------------------------------------------------------------
# Random Replacement
for x in range(pm):
    phys_mem[x] = ['', 0, 1]
page_fault = 0   
fill = 0
for item in data:
    trash, hex_address = item.split(",0x")
    dec_address = int(hex_address, 16)
    # fill up physical memory 
    if fill < pm: 
        phys_mem[fill][0] = dec_address
        print(item + " = Process " + trash + " access line " +str(dec_address))
        fill += 1
        page_fault += 1
    else:
        present = False
        for pm_slot in phys_mem:
            if phys_mem[pm_slot][0] == dec_address:
                present = True
        if not present:
            mem_slot = random.randint(0, (pm -1))
            print(item + " = Process " + trash + " access line " +str(dec_address))
            page_fault += 1
            phys_mem[mem_slot][0] = dec_address
page_fault_final.append(page_fault)
#------------------------------------------------------------
# LRU
for x in range(pm):
    phys_mem[x] = ['', 0, 1]
page_fault = 0   
fill = 0
access_time = 0
for item in data:
    trash, hex_address = item.split(",0x")
    dec_address = int(hex_address, 16)

    present = False # boolean to track if address is in physical memory
    if fill < pm: # fill physical memory first
        phys_mem[fill][0] = dec_address
        print(item + " = Process " + trash + " access line " +str(dec_address))
        fill += 1
        page_fault += 1
    else:
        for slot in phys_mem: # traverse dictionary containing physical memory slots
            if phys_mem[slot][0] == dec_address: # if the hex address is in physical memory
                present = True
        if not present:
            for slot in phys_mem: # find lowest access time
                if slot == 0:
                    replace = slot
                    low = phys_mem[slot][1]
                else:
                    if phys_mem[slot][1] < low:
                        replace = slot
                        low = phys_mem[slot][1]
            phys_mem[replace][0] = dec_address
            phys_mem[replace][1] = access_time
            print(item + " = Process " + trash + " access line " +str(dec_address))
            page_fault += 1
    access_time += 1
            
page_fault_final.append(page_fault)           
#------------------------------------------------------------
# LFU
for x in range(pm):
    phys_mem[x] = ['', 1, 0]
page_fault = 0   
fill = 0
access_time = 0
for item in data:
    trash, hex_address = item.split(",0x")
    dec_address = int(hex_address, 16)

    present = False # boolean to track if address is in physical memory
    if fill < pm: # fill physical memory first
        phys_mem[fill][0] = dec_address
        print(item + " = Process " + trash + " access line " +str(dec_address))
        fill += 1
        page_fault += 1
    else:
        for slot in phys_mem: # traverse dictionary containing physical memory slots
            if phys_mem[slot][0] == dec_address: # if the hex address is in physical memory
                present = True
        if not present:
            for slot in phys_mem: # find frequency for all pages
                phys_mem[slot][2] = phys_mem[slot][1] / access_time
            for slot in phys_mem: # find lowest frequency
                if slot == 0:
                    replace = slot
                    low = phys_mem[slot][2]
                else:
                    if phys_mem[slot][2] < low:
                        low = phys_mem[slot][2]
            phys_mem[replace][0] = dec_address
            phys_mem[replace][1] += 1
            print(item + " = Process " + trash + " access line " +str(dec_address))
            page_fault += 1
    access_time += 1
page_fault_final.append(page_fault)
# Display
plt.style.use('ggplot')
#x = ['FIFO', 'LRU', 'LFU', 'Random']
x = ['FIFO', 'Random', 'LRU', 'LFU']
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, page_fault_final, color='green')
plt.xlabel("Algorithms")
plt.ylabel("Page Faults")
plt.title(title)
plt.xticks(x_pos, x)
plt.show()
