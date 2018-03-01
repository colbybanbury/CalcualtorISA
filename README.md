# CalcualtorISA
Authors: colby banbury and matt stout


## Instruction dictionary:

lw
Semantics:
		00		00		0000
		op	   dest     int

Description:
	Load word takes a 4 bit 2s compliment intermediate value and stores it in the destination register. Registers are 8 bit 2s compliment.

beq
Semantics:
		01	0	0	00	00
		op b/d 	j  reg1	reg2

Description:
	Branch Equals compares two register values and if they are equal it jumps either 1 or 2 lines specified by the j field. The b/d field specifies between beq and disp since 5 instructions are required and only a 2 bit op code can be afforded.

disp
Semantics:
		01	1	000		00
		op b/d 	null	reg

Description:
	Display simply displays the value stored in the specified register. The b/d field specifies between beq and disp since 5 instructions are required and only a 2 bit op code can be afforded.

add
Semantics:
		10	00	00		00
		op dest reg1	reg2

Description:
	Adds the value in one register to the value of a second and stores it in the destination register.

sub
Semantics:
		11	00	00		00
		op dest	reg1	reg2

Description:
	subtracts the value of the second register from the value of the first and stores it in the destination register.