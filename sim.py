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

reg0, reg1, reg2, reg3 = 0

regs = [reg0, reg1, reg2, reg3]

fileName = raw_input("Enter the name of the file you would like to simulate: ")

file = open(fileName)
instructions = file.readlines()						#list of each line in the txt
instructions = [x.strip("\n") for x in instructions] #therefore a list of the instructions

count = 0

while count < len(instructions)
	instruction = instructions[count]
	opCode = instruction[:2]
	if(opCode = "00"):	#lw
		regs[instruction[2:4]] = intRead(instructions[4:7], instructions[4:7]) #stores int
	elif(opCode = "01"): #beq/disp
		if(instruction[2:3] = "0"):#beq
			jump = int(instruction[3:4], base=2) +1 #0+1 = jump 1
			if(regs[instruction[4:6]]==regs[instruction[6:]]):#compare
				count+=j
		else:#disp
			print(regs[instruction[6:]])
	elif(opCode = "10"): #add
		regs[instruction[2:4]] = regs[instruction[4:6]] + regs[instruction[6:]]
	elif(opCode = "11"):#sub
		regs[instruction[2:4]] = regs[instruction[4:6]] - regs[instruction[6:]]
	else:
		print("opCode failure")
	count+=1


def getReg(regCode):					#converts a binary string to an int 
	return regs[int(regCode, base=2)]	#and uses it to get the reg encoded

def intRead(intCode, neg): #intCode is the 3 bits that aren't the pos/flag, neg is pos/neg, both strings
	val = int(intCode, base=2)
	if(int(neg, base=2)):
		val = val *-1
	return val	#returns int
