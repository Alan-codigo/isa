`timescale 1ns/1ns

module ISA(

    input [19:0]Instruction,
    output [31:0]Salida

);

wire [31:0] d1BR_op1Alu;
wire [31:0] d2BR_op2Alu;

wire [31:0] AluOut_RamIn;

BR instanciaBanco(
    //entradas
    .DL1(Instruction[19:15]),
    .DL2(Instruction[14:10]),
    .DE(0),
    .DATO(0),
    .WE(Instruction[9]),

    //salidas
    .op1(d1BR_op1Alu),
    .op2(d2BR_op2Alu)
);

ALU instanciaAlu(
    .Op1(d1BR_op1Alu),
    .Op2(d2BR_op2Alu),
    .AluOp(Instruction[8:6]),
    .Resultado(AluOut_RamIn)
);

RAM instanciaRam(
    .Datoin(AluOut_RamIn),
    .Dir(Instruction[19:5]),
    .WE(Instruction[0]),
    .Datoout(Salida)
);

endmodule
