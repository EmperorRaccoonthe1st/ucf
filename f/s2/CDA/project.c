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

    ins = MEM(PC);
    
    *instruction = ins;
    
    return 0;
}


/* instruction partition */
/* 10 Points */
void instruction_partition(unsigned instruction, unsigned *op, unsigned *r1, unsigned *r2, unsigned *r3, unsigned *funct, unsigned *offset, unsigned *jsec)
{
    *op = (instruction & 0b11111100000000000000000000000000) >> 26;

    *r1 = (instruction & 0b00000011111000000000000000000000) >> 21;

    *r2 = (instruction & 0b00000000000111110000000000000000) >> 16;

    *r3 = (instruction & 0b00000000000000001111100000000000) >> 11;

    *funct = (instruction & 0b00000000000000000000000000111111);

    *offset = (instruction & 0b00000000000000001111111111111111);

    *jsec = (instruction & 0b00000011111111111111111111111111);
}


/* instruction decode */
/* 15 Points */
int instruction_decode(unsigned op,struct_controls *controls)
{
    switch (op) {
       case 0:
            // R-Type
            // add, subtract, set-less-than, sltu, and, or
            controls->RegDst = 1;
            controls->Jump = 0;
            controls->Branch = 0;
            controls->MemRead = 0;
            controls->MemtoReg = 0;
            controls->ALUOp = 7;
            controls->MemWrite = 0;
            controls->ALUSrc = 0;
            controls->RegWrite = 1;
            break;

       case 2:
            // jump: j
            controls->RegDst = 2;
            controls->Jump = 1;
            controls->Branch = 0;
            controls->MemRead = 0;
            controls->MemtoReg = 2;
            controls->ALUOp = 0;
            controls->MemWrite = 0;
            controls->ALUSrc = 1; // should be 2
            controls->RegWrite = 0;
            break;

       case 4:
            // branch-on-equal: beq
            controls->RegDst = 2;
            controls->Jump = 0;
            controls->Branch = 1;
            controls->MemRead = 0;
            controls->MemtoReg = 2;
            controls->ALUOp = 1;
            controls->MemWrite = 0;
            controls->ALUSrc = 0;
            controls->RegWrite = 0;
            break;

       case 8:
            // add-immediate: addi
            controls->RegDst = 0;
            controls->Jump = 0;
            controls->Branch = 0;
            controls->MemRead = 0;
            controls->MemtoReg = 0;
            controls->ALUOp = 0;
            controls->MemWrite = 0;
            controls->ALUSrc = 1;
            controls->RegWrite = 1;
            break;

       case 10:
            // set-less-than-immediate: slti
            controls->RegDst = 0;
            controls->Jump = 0;
            controls->Branch = 0;
            controls->MemRead = 0;
            controls->MemtoReg = 0;
            controls->ALUOp = 2;
            controls->MemWrite = 0;
            controls->ALUSrc = 1;
            controls->RegWrite = 1;
            break;

       case 11:
            // set-less-than-immediate-unsigned: sltiu
            controls->RegDst = 0;
            controls->Jump = 0;
            controls->Branch = 0;
            controls->MemRead = 0;
            controls->MemtoReg = 0;
            controls->ALUOp = 3;
            controls->MemWrite = 0;
            controls->ALUSrc = 1;
            controls->RegWrite = 1;
            break;

       case 15:
            // load-upper-immediate: lui
            controls->RegDst = 0;
            controls->Jump = 0;
            controls->Branch = 0;
            controls->MemRead = 0;
            controls->MemtoReg = 0;
            controls->ALUOp = 6;
            controls->MemWrite = 0;
            controls->ALUSrc = 1;
            controls->RegWrite = 1;
            break;

       case 35:
            // load-word: lw
            controls->RegDst = 0;
            controls->Jump = 0;
            controls->Branch = 0;
            controls->MemRead = 1;
            controls->MemtoReg = 1;
            controls->ALUOp = 0;
            controls->MemWrite = 0;
            controls->ALUSrc = 1;
            controls->RegWrite = 1;
            break;

       case 43:
            // store-word: sw
            controls->RegDst = 2; 
            controls->Jump = 0;
            controls->Branch = 0;
            controls->MemRead = 0;
            controls->MemtoReg = 2;
            controls->ALUOp = 0;
            controls->MemWrite = 1;
            controls->ALUSrc = 1;
            controls->RegWrite = 0;
            break;

        default:
            return 1;
   
    }

    return 0;
}


/* Read Register */
/* 5 Points */
void read_register(unsigned r1,unsigned r2,unsigned *Reg,unsigned *data1,unsigned *data2)
{
    *data1 = Reg[r1];
    *data2 = Reg[r2];
}


/* Sign Extend */
/* 10 Points */
void sign_extend(unsigned offset,unsigned *extended_value)
{

    unsigned signBit = offset & 0b00000000000000001000000000000000;

    if (signBit > 0) {
        *extended_value = offset | 0b11111111111111110000000000000000;
    } else {
        *extended_value = offset;
    }
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
    if (MemWrite) {
        if (ALUresult % 4 != 0 || ALUresult > 0xFFFF) return 1; 
        MEM(ALUresult) = data2;
    }

    if (MemRead) {
        if (ALUresult % 4 != 0 || ALUresult > 0xFFFF) return 1; 
        *memdata = MEM(ALUresult);
    }

    return 0;
}


/* Write Register */
/* 10 Points */
void write_register(unsigned r2,unsigned r3,unsigned memdata,unsigned ALUresult,char RegWrite,char RegDst,char MemtoReg,unsigned *Reg)
{
    if (RegWrite && MemtoReg) {
        if (RegDst) {
            Reg[r3] = memdata;
        } else {
            Reg[r2] = memdata;
        }
    } else if (RegWrite) {
        if (RegDst) {
            Reg[r3] = ALUresult;
        } else {
            Reg[r2] = ALUresult;
        } 
    }
}


/* PC update */
/* 10 Points */
void PC_update(unsigned jsec,unsigned extended_value,char Branch,char Jump,char Zero,unsigned *PC)
{
    *PC += 4;

    if (Branch && Zero) {
        *PC += extended_value << 2;
    }

    if (Jump) {
        unsigned upperBits = *PC & 0b11110000000000000000000000000000;

        *PC = jsec << 2 | upperBits;
    }
}

