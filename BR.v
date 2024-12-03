`timescale 1ns/1ns

module BR(
    // Entradas
    input [4:0] DL1,
    input [4:0] DL2,
    input [4:0] DE,
    input [31:0] DATO,
    input WE,

    // Salidas
    output reg [31:0] op1,
    output reg [31:0] op2
);

    reg [31:0] BR [0:31];


    initial begin
        $readmemb("banco.txt", BR);  // Cargar datos desde el archivo
    end

    always @* begin
        if (WE) begin 
            BR[DE] = DATO; 
        end

        // Leer valores de los registros
        op1 = BR[DL1];
        op2 = BR[DL2];
    end

endmodule
