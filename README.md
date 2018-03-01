# CalcualtorISA
Authors: Colby Banbury and Matt Stout	


## Instruction dictionary:

### lw
Semantics: <br />
		00		00		0000  <br />
		op	   dest     int  <br />

Description:  <br />
	Load word takes a 4 bit 2s compliment intermediate value and stores it in the destination register. Registers are 8 bit 2s compliment.

### beq
Semantics:  <br />
		01	0	0	00	00  <br />
		op b/d 	j  reg1	reg2  <br />

Description:  <br />
	Branch Equals compares two register values and if they are equal it jumps either 1 or 2 lines specified by the j field. The b/d field specifies between beq and disp since 5 instructions are required and only a 2 bit op code can be afforded.

### disp
Semantics:  <br />
		01	1	000		00  <br />
		op b/d 	null	reg  <br />

Description:  <br />
	Display simply displays the value stored in the specified register. The b/d field specifies between beq and disp since 5 instructions are required and only a 2 bit op code can be afforded.

### add
Semantics:  <br />
		10	00	00		00  <br />
		op dest reg1	reg2  <br />

Description:  <br />
	Adds the value in one register to the value of a second and stores it in the destination register.

### sub
Semantics:  <br />
		11	00	00		00  <br />
		op dest	reg1	reg2  <br />

Description:  <br />
	subtracts the value of the second register from the value of the first and stores it in the destination register.

## Testing Files:

### lwDispTest:
Loads a positive value into a register and displays it then loads a negative value and displays it.  <br />
Tests lw, disp, and the basic twos compliment formart<br />

### addTest:
Loads in positive values, adds them, and then displays it then does the same with a negative value.  <br />
Tests add for positive and negative numbers.  <br />

### subTest:
Loads in positive values, subtracts them, and then displays it then does the same with a negative value.  <br />
Tests subtract for positive and negative numbers.  <br />

### beqTest:
Compares equal values with 1 and 2 jumps and displays a value to confirm that the jumps have been made. Additionally it compares two unequal values and confirms that no jump is made.  <br />
Tests the beq function in all jump cases and in the not equal case.  <br />

### overflowTest:
Adds 7 (the max positive value for a 4 bit 2s compliment) until it goes above 127 (the max value for an 8 bit 2s compliment) to check that the value raps around but maintains its positive value.   <br />
Tests the overflow of the value for the behavior we decided on.   <br />

### underflowTest:
adds -8 (the minumum value for a 4 bit 2s compliment) until it goes below -128 (the minimum value for an 8 bit 2s compliment) to check that the value raps around but maintains its negative value.   <br />
Tests the underflow of the value for the behavior we decided on.   <br />