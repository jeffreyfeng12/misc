import re,sys


file = open("output.txt", "r")


numCustomers = 400
numCooks = 8
numTables = 12
machineCapacity = 4

simCheck = [0]*2
custCheck = [0]*5
cookCheck = [0]*6
machCheck = [0]*4

tables_occupied = 0
fryer_use = 0
oven_use = 0
grill_use = 0
fountain_use = 0
success = True 

for line in file.readlines():
    if "Starting simulation: " in line:
        simCheck[0] += 1
    elif "Simulation ended." in line:
        simCheck[1] += 1
    elif " going to Ratsies." in line:
        custCheck[0] += 1
    elif "entered Ratsies" in line:
        custCheck[1] += 1
        tables_occupied += 1
    elif " placing order " in line:
        custCheck[2] += 1
    elif " received order " in line:
        custCheck[3] += 1
    elif " leaving Ratsies" in line:
        custCheck[4] += 1
        tables_occupied -= 1
    elif " reporting for work." in line:
        cookCheck[0] += 1
    elif " starting order " in line:
        cookCheck[1] += 1
    elif " preparing " in line:
        cookCheck[2] += 1
    elif " finished " in line:
        cookCheck[3] += 1
    elif " completed order " in line:
        cookCheck[4] += 1
    elif " going home for the night." in line:
        cookCheck[5] += 1
    elif " starting up for making " in line:
        machCheck[0] += 1
    elif " making " in line:
        machCheck[1] += 1
        if "Fryer" in line:
            #print "Wing number: " + str(fryer_use)
            fryer_use += 1
        elif "Oven" in line:
            oven_use += 1
        elif "Grill Press" in line:
            grill_use += 1
        elif "Fountain" in line:
            fountain_use += 1
    elif " completed " in line:
        machCheck[2] += 1
        if "Fryer" in line:
            fryer_use -= 1
        elif "Oven" in line:
            oven_use -= 1
        elif "Grill Press" in line:
            grill_use -= 1
        elif "Fountain" in line:
            fountain_use -= 1 
    elif " shutting down." in line:
        machCheck[3] += 1
    elif "Did it work?" not in line:
        print line
        success = False
    
    if tables_occupied > numTables:
        print "TOO MANY PEOPLE!!!"
        success = False

    if fryer_use > machineCapacity:
        print "TOO MANY WINGS" + str(fryer_use)
        success = False

    if oven_use > machineCapacity:
        print "TOO MANY PIZZAS" + str(oven_use)
        success = False

    if grill_use > machineCapacity:
        print "TOO MANY SUBS" + str(grill_use)
        success = False

    if fountain_use > machineCapacity:
        print "TOO MANY SODAS" + str(fountain_use)
        success = False
        
    #print "Wing number: " + str(fryer_use)
    
for i in simCheck:
    if i != 1:
        print "Simulation starting/ending"
        success = False

if custCheck[0] != numCustomers:
    print "customers created " + str(custCheck[0])
    success = False

if custCheck[1] != numCustomers:
    print "customers arrive " + str(custCheck[1])
    success = False

if custCheck[2] != numCustomers:
    print "customers placed order " + str(custCheck[2])
    success = False

if custCheck[3] != numCustomers:
    print "customers received order " + str(custCheck[3])
    success = False

if custCheck[4] != numCustomers:
    print "customers leave " + str(custCheck[4])
    success = False

if cookCheck[0] != numCooks:
    print "cook starting " + str(cookCheck[0])
    success = False
    
if cookCheck[1] != numCustomers:
    print "cook received order "+ str(cookCheck[1])
    success = False
    
if cookCheck[2] != 4*numCustomers:
    print "cook started food " + str(cookCheck[2])
    success = False
    
if cookCheck[3] != 4*numCustomers:
    print "cook finished food " + str(cookCheck[3])
    success = False
    
if cookCheck[4] != numCustomers:
    print "cook completed orders " + str(cookCheck[4])
    success = False
    
if cookCheck[5] != numCooks:
    print "cook went home "+ str(cookCheck[5])
    success = False

if machCheck[0] != 4:
    print "machines started "+ str(machCheck[0])
    success = False

if machCheck[1] != 4*numCustomers:
    print "machines started making food "+ str(machCheck[1])
    success = False

if machCheck[2] != 4*numCustomers:
    print "machines finished food "+ str(machCheck[2])
    success = False

if machCheck[3] != 4:
    print "machines shutting down "+ str(machCheck[3])
    success = False


#print simCheck
#print custCheck
#print cookCheck
#print machCheck
print "Success? " + str(success)