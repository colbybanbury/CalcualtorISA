# CalcualtorISA
Authors: colby banbury and matt stout


## Instruction dictionary:  <br />

lw  <br />
Semantics: <br />
		00		00		0000  <br />
		op	   dest     int  <br />

Description:  <br />
	Load word takes a 4 bit 2s compliment intermediate value and stores it in the destination register. Registers are 8 bit 2s compliment.

beq  <br />
Semantics:  <br />
		01	0	0	00	00  <br />
		op b/d 	j  reg1	reg2  <br />

Description:  <br />
	Branch Equals compares two register values and if they are equal it jumps either 1 or 2 lines specified by the j field. The b/d field specifies between beq and disp since 5 instructions are required and only a 2 bit op code can be afforded.

disp  <br />
Semantics:  <br />
		01	1	000		00  <br />
		op b/d 	null	reg  <br />

Description:  <br />
	Display simply displays the value stored in the specified register. The b/d field specifies between beq and disp since 5 instructions are required and only a 2 bit op code can be afforded.

add  <br />
Semantics:  <br />
		10	00	00		00  <br />
		op dest reg1	reg2  <br />

Description:  <br />
	Adds the value in one register to the value of a second and stores it in the destination register.

sub  <br />
Semantics:  <br />
		11	00	00		00  <br />
		op dest	reg1	reg2  <br />

Description:  <br />
	subtracts the value of the second register from the value of the first and stores it in the destination register.