#include "spimcore.h"


/* ALU */
/* 10 Points */
void ALU(unsigned A,unsigned B,char ALUControl,unsigned *ALUresult,char *Zero)
{

    unsigned result = 0;

    switch (ALUControl) {

        case 0:
            // Addition
            result = A + B;
            break;

        case 1:
            // Subtraction
            result = A - B;
            break;

        case 2:
            // Less Than
            if ((int)A < (int)B) result = 1;
            break;

        case 3:
            // Unsigned Less Than
            if (A < B) result = 1;
            break;

        case 4:
            // Bitwise And
            result = A & B;
            break;

        case 5:
            // Bitwise Or
            result = A | B;
            break;

        case 6:
            // Shift B by 16 (??) 
             result = B << 16;
            break;

        case 7:
            // NOT A
            result = ~A;
            break;
    }

    *ALUresult = result;

    if (result == 0) {
        *Zero = 1;
    }  else {
        *Zero = 0;
    }

}

/* instruction fetch */
/* 10 Points */
int instruction_fetch(unsigned PC,unsigned *Mem,unsigned *instruction)
{
    unsigned ins;

    // Halt Cond
    if (PC % 4 != 0) return 1;

    ins = Mem[PC >> 2];
    
    *instruction = ins;
    
    return 0;
}


/* instruction partition */
/* 10 Points */
void instruction_partition(unsigned instruction, unsigned *op, unsigned *r1,unsigned *r2, unsigned *r3, unsigned *funct, unsigned *offset, unsigned *jsec)
{

}



/* instruction decode */
/* 15 Points */
int instruction_decode(unsigned op,struct_controls *controls)
{

}

/* Read Register */
/* 5 Points */
void read_register(unsigned r1,unsigned r2,unsigned *Reg,unsigned *data1,unsigned *data2)
{

}


/* Sign Extend */
/* 10 Points */
void sign_extend(unsigned offset,unsigned *extended_value)
{

}
#include "spimcore.h"

#define MEMSIZE (65536 >> 2)
#define REGSIZE 32
#define BUFSIZE 256

#define PCINIT 0x4000
#define SPINIT 0xFFFC
#define GPINIT 0xC000

static unsigned Mem[MEMSIZE];
static unsigned Reg[REGSIZE + 4];

#define MEM(addr) (Mem[addr >> 2])

#define PC (Reg[REGSIZE + 0])
#define Status (Reg[REGSIZE + 1])
#define LO (Reg[REGSIZE + 2])
#define HI (Reg[REGSIZE + 3])

const char RegName[REGSIZE + 4][6] = {
	"$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3",
	"$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", 
	"$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", 
	"$t8", "$t9", "$k0", "$k1", "$gp", "$sp", "$fp", "$ra",
	"$pc", "$stat", "$lo", "$hi" };

#define NREG(name) (*Nreg(name))

const char RedirNull[] = "";
const char RedirPrefix[] = ">";

static char Buf[BUFSIZE];
static int Halt = 0;
static FILE *FP;
static char *Redir = (char *) RedirNull;

/*** DATAPATH Signals ***/
// names of instruction sections
unsigned instruction;
unsigned op,	// instruction [31-26]
	r1,	// instruction [25-21]
	r2,	// instruction [20-16]
	r3,	// instruction [15-11]
	funct,	// instruction [5-0]
	offset,	// instruction [15-0]
	jsec;	// instruction [25-0]

// control signals
struct_controls controls;

// Register output
unsigned data1,data2;

// sign extend
unsigned extended_value;

// ALU result
unsigned ALUresult;
char Zero;

// data read from Memory
unsigned memdata;

/******/


unsigned *Nreg(char *name)
{
	int i;

	for (i = 0; i < REGSIZE + 4; i++)
	{
		if (strcmp(name, RegName[i]) == 0)
			return &Reg[i];
		if (strcmp(name, RegName[i] + 1) == 0)
			return &Reg[i];
	}
	return NULL;
}

void Init(void)
{
	memset(Reg, 0, (REGSIZE + 4) * sizeof(unsigned));
	NREG("pc") = PCINIT;
	NREG("sp") = SPINIT;
	NREG("gp") = GPINIT;
}


void DisplayControlSignals(void)
{
	fprintf(stdout, "\tControl Signals: %0x%0x%0x%0x%03x%0x%0x%0x%0x\n", 
			controls.RegDst, 
			controls.Jump, 
			controls.Branch, 
			controls.MemRead, 
			controls.MemtoReg, 
			controls.ALUOp, 
			controls.MemWrite, 
			controls.ALUSrc, 
			controls.RegWrite);
}



void Step(void)
{
	/* fetch instruction from memory */
	Halt = instruction_fetch(PC,Mem,&instruction);

	if(!Halt)
	{
		/* partition the instruction */
		instruction_partition(instruction,&op,&r1,&r2,&r3,&funct,&offset,&jsec);

		/* instruction decode */
		Halt = instruction_decode(op,&controls);
	}

	if(!Halt)
	{
		/* read_register */
		read_register(r1,r2,Reg,&data1,&data2);

		/* sign_extend */
		sign_extend(offset,&extended_value);

		/* ALU */
		Halt = ALU_operations(data1,data2,extended_value,funct,controls.ALUOp,controls.ALUSrc,&ALUresult,&Zero);
	}

	if(!Halt)
	{
		/* read/write memory */
		Halt = rw_memory(ALUresult,data2,controls.MemWrite,controls.MemRead,&memdata,Mem);
	}

	if(!Halt)
	{
		/* write to register */
		write_register(r2,r3,memdata,ALUresult,controls.RegWrite,controls.RegDst,controls.MemtoReg,Reg);

		/* PC update */
		PC_update(jsec,extended_value,controls.Branch,controls.Jump,Zero,&PC);
	}
}

void DumpReg(void)
{
	int i;
	char bb[] = "     ";

	for (i = 0; i < REGSIZE + 4; i++)
	{
		fprintf(stdout, "%s %s%s %08x%s",
			(i % 4 == 0) ? Redir : "",
			RegName[i], bb + strlen(RegName[i]) * sizeof(char),
			Reg[i], (i % 4 == 3) ? "\n" : "     ");
	}
}

// Dump Memory Content where the addresses are in decimal format
void DumpMem(int from, int to)
{
	int i, mt, ma;

	(to < from) && (to = from);
	if (from == to)
	{
		fprintf(stdout, "%s %05d        %08x\n", Redir, from, Mem[from]);
	}
	else
	{
		mt = Mem[ma = from];
		for (i = from + 1; i <= to; i++)
		{
			if (i == to || Mem[i] != mt)
			{
				if (i == ma + 1)
					fprintf(stdout, "%s %05d        %08x\n",
						Redir, ma, mt);
				else
					fprintf(stdout, "%s %05d-%05d  %08x\n",
						Redir, ma, i - 1, mt);
				(i != to) && (mt = Mem[ma = i]);
			}
		}
	}
}


// Dump Memory Content in Hex format
void DumpMemHex(int from, int to)
{
	int i, mt, ma;

	(to < from) && (to = from);
	if (from == to)
	{
		fprintf(stdout, "%s %05x        %08x\n", Redir, from*4, Mem[from]);
	}
	else
	{
		mt = Mem[ma = from];
		for (i = from + 1; i <= to; i++)
		{
			if (i == to || Mem[i] != mt)
			{
				if (i == ma + 1)
					fprintf(stdout, "%s %05x        %08x\n",
						Redir, ma*4, mt);
				else
					fprintf(stdout, "%s %05x-%05x  %08x\n",
						Redir, ma*4, (i - 1)*4, mt);
				(i != to) && (mt = Mem[ma = i]);
			}
		}
	}
}



void DumpHex(int from, int to)
{
	int i, j;

	if (to < from)
	{
		for (i = from, j = 0; i >= to; i--, j++)
		{
			if (j % 4 == 0)
				fprintf(stdout, "%s %04x  ", Redir, (i << 2) + 3);
			fprintf(stdout, " %08x%s", Mem[i], (j % 4 == 3) ? "\n" : "");
		}
	}
	else
	{
		for (i = from, j = 0; i <= to; i++, j++)
		{
			if (j % 4 == 0)
				fprintf(stdout, "%s %04x  ", Redir, i << 2);
			fprintf(stdout, " %08x%s", Mem[i], (j % 4 == 3) ? "\n" : "");
		}
	}
	if (j % 4 != 0)
		fputc('\n', stdout);
}

void Loop(void)
{
	char *tp;
	int sc;

	Init();
	for (;;)
	{
		fprintf(stdout, "\n%s cmd: ", Redir);
		Buf[0] = '\0';
		if (fgets(Buf, BUFSIZE, stdin) == NULL)
			continue;
		if ((tp = strtok(Buf, " ,.\t\n\r")) == NULL)
			continue;
		fputc('\n', stdout);
		switch (*tp)
		{
			case 'g': case 'G':
				DisplayControlSignals();
				break;
			case 'r': case 'R':
				DumpReg();
				break;
			case 'm': case 'M':
				if ((tp = strtok(NULL, " ,.\t\n\r")) == NULL)
				{
					DumpMemHex(0, MEMSIZE);
				}
				else
				{
					sc = (int) strtoul(tp, (char **) NULL, 10);
					if ((tp = strtok(NULL, " ,.\t\n\r")) == NULL)
					{
						DumpMemHex(sc, MEMSIZE);
					}
					else
					{
						DumpMemHex(sc, (int) strtoul(tp, (char **) NULL, 10));
					}
				}
				break;
			case 's': case 'S':
				if ((tp = strtok(NULL, " ,.\t\n\r")) == NULL)
					sc = 1;
				else
					sc = (int) strtoul(tp, (char **) NULL, 10);
				while (sc-- > 0 && !Halt)
					Step();
				fprintf(stdout, "%s step\n", Redir);
				break;
			case 'c': case 'C':
				while (!Halt)
					Step();
				fprintf(stdout, "%s cont\n", Redir);
				break;
			case 'h': case 'H':
				fprintf(stdout, "%s %s\n", Redir, Halt ? "true" : "false");
				break;
			case 'p': case 'P':
				rewind(FP);
				sc = 0;
				while (!feof(FP))
				{
					if (fgets(Buf, BUFSIZE, FP))
						fprintf(stdout, "%s % 5d  %s", Redir, sc++, Buf);
				}
				break;
			case 'i': case 'I':
				fprintf(stdout, "%s %d\n", Redir, MEMSIZE);
				break;
			case 'd': case 'D':
				if ((tp = strtok(NULL, " ,.\t\n\r")) == NULL)
				{
					fprintf(stdout, "%s invalid cmd\n", Redir);
					break;
				}
				sc = (int) strtoul(tp, (char **) NULL, 10);
				if ((tp = strtok(NULL, " ,.\t\n\r")) == NULL)
				{
					fprintf(stdout, "%sinvalid cmd\n", Redir);
					break;
				}
				DumpHex(sc, (int) strtoul(tp, (char **) NULL, 10));
				break;
			case 'x': case 'X': case 'q': case 'Q':
				fprintf(stdout, "%s quit\n", Redir);
				if (Redir == (char *) RedirPrefix)
				{
					fprintf(stdout, "%s%s\n", Redir, Redir);
				}
				return;
			default:
				fprintf(stdout, "%s invalid cmd\n", Redir);
				break;
		}
		if (Redir == (char *) RedirPrefix)
		{
			fprintf(stdout, "%s%s\n", Redir, Redir);
		}
	}
}

int main(int argc, char **argv)
{
	int i;
	unsigned long t;

	setvbuf(stdout, (char *) NULL, _IOLBF, 0);
	if (argc != 2 && argc != 3)
	{
		fprintf(stderr, "syntax: %s input_file [-r]\n", argv[0]);
		return 1;
	}
	if (*argv[1] == '-')
	{
		fprintf(stderr, "syntax: %s input_file [-r]\n", argv[0]);
		return 1;
	}
	if ((FP = fopen(argv[1], "r")) == NULL)
	{
		fprintf(stderr, "%s: cannot open input file %s\n", argv[0], argv[1]);
		return 1;
	}
	if (argc == 3)
	{
		if (strcmp(argv[2], "-r") == 0)
		{
			Redir = (char *) RedirPrefix;
			fprintf(stdout, "%s\n", argv[0]);
		}
		else
		{
			fprintf(stderr, "syntax: %s input_file [-r]\n", argv[0]);
			return 1;
		}
	}
	memset(Mem, 0, MEMSIZE * sizeof(unsigned));
	for (i = PCINIT; !feof(FP); i += 4)
	{
		if (fgets(Buf, BUFSIZE, FP) == NULL)
		{
			if (feof(FP))
				break;
			fprintf(stderr, "%s: file %s reading error\n", argv[0], argv[1]);
			return 1;
		}
		if (sscanf(Buf, "%lx", &t) != 1)
		{
			fprintf(stderr, "%s: file %s error in line %d, continue...\n",
				argv[0], argv[1], i - PCINIT + 1);
			MEM(i) = 0;
		}
		else
		{
			MEM(i) = strtoul(Buf, (char **) NULL, 16);
		}
	}
	Loop();
	fclose(FP);
	return 0;
}

/* ALU operations */
/* 10 Points */
int ALU_operations(unsigned data1,unsigned data2,unsigned extended_value,unsigned funct,char ALUOp,char ALUSrc,unsigned *ALUresult,char *Zero)
{
   
    if (ALUOp == 7) {

        switch (funct) {

            case 32:
                // add
                ALU(data1, data2, 0, ALUresult, Zero);
                break;

            case 34:
                // subtract
                ALU(data1, data2, 1, ALUresult, Zero);
                break;

            case 36:
                // and
                ALU(data1, data2, 4, ALUresult, Zero);
                break;

            case 37:
                // or
                ALU(data1, data2, 5, ALUresult, Zero);
                break;

            case 42:
                // set less than
                ALU(data1, data2, 2, ALUresult, Zero);
                break;

            case 43:
                // set less than unsigned
                ALU(data1, data2, 3, ALUresult, Zero);
                break;

            default: 
                return 1;
        }

    } else {

        if (ALUSrc == 1) {
            // Pass ALU the Immediate
            ALU(data1, extended_value, ALUOp, ALUresult, Zero);
        } else {
            ALU(data1, data2, ALUOp, ALUresult, Zero);
        }
    }

    return 0;
}

/* Read / Write Memory */
/* 10 Points */
int rw_memory(unsigned ALUresult,unsigned data2,char MemWrite,char MemRead,unsigned *memdata,unsigned *Mem)
{

}


/* Write Register */
/* 10 Points */
void write_register(unsigned r2,unsigned r3,unsigned memdata,unsigned ALUresult,char RegWrite,char RegDst,char MemtoReg,unsigned *Reg)
{

}

/* PC update */
/* 10 Points */
void PC_update(unsigned jsec,unsigned extended_value,char Branch,char Jump,char Zero,unsigned *PC)
{

}

