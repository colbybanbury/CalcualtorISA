#Calculator ISA simulator
#autors: Colby Banbury and Matt Stout

#this file simulates an ISA designed to function as a calculator.
#Instruction dictionary
#colby banbury and matt stout

#lw		00	00		0000
#		op  dest     int
#beq	01	0	0		00
#		op b/d 	j		reg
#disp	01	1	000		00
#		op b/d 	null	reg
#add	10	00	00		00
#		op dest reg1	reg2
#sub	11	00	00		00
#		op dest	reg1	reg2

regs = [0, 0, 0, 0]

fileName = input("Enter the name of the file you would like to simulate: ")

file = open(fileName)
instructions = file.readlines()						#list of each line in the txt
instructions = [x.strip("\n") for x in instructions] #therefore a list of the instructions


def getReg(regCode):					#converts a binary string to an int 
	return regs[int(regCode, base=2)]	#and uses it to get the reg encoded

def intRead(intCode, neg): #intCode is the 3 bits that aren't the pos/flag, neg is pos/neg, both strings
	
	val = int(str(intCode), base=2)
	if(int(neg, base=2)):
		val = val *-1
	return val	#returns int


count = 0

while count < len(instructions):
	instruction = instructions[count]
	print("current instruction is " + instruction)
	opCode = instruction[:2]
	if(opCode == "00"):	#lw
		regs[int(instruction[2:4], base=2)] = intRead(instruction[5:], instruction[4:5]) #stores int
	elif(opCode == "01"): #beq/disp
		if(instruction[2:3] == "0"):#beq
			jump = int(instruction[3:4], base=2) +1 #0+1 = jump 1
			if(getReg(instruction[4:6])==getReg(instruction[6:])):#compare
				count+=j
		else:#disp
			print(getReg(instruction[6:]))
	elif(opCode == "10"): #add
		regs[int(instruction[2:4], base =2)] = getReg(instruction[4:6]) + getReg(instruction[6:])
	elif(opCode == "11"):#sub
		regs[int(instruction[2:4], base =2)] = getReg(instruction[4:6]) - getReg(instruction[6:])
	else:
		print("opCode failure")
	count+=1

