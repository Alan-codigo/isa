`timescale 1ns/1ns

module RAM (
    input wire [31:0] Datoin,       
    input wire [4:0] Dir,       
    input wire WE,               
    
    output reg [31:0] Datoout       
);


    reg [31:0] ram [0:31];

    always @(*) 
    begin
        if (WE) 
        begin
            // Escribir en la RAM cuando we está en alto
            ram[Dir] = Datoin;
        end 
        
        else 
        begin
            // Leer de la RAM cuando we está en bajo
            Datoout = ram[Dir];
        end
    end
endmodule

