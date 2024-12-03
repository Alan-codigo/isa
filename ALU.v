`timescale 1ms/1ns
module ALU(
    
    //entradas
    input [31:0] Op1,
    input [31:0] Op2,
    input [2:0] AluOp,
    //salidas
    output reg[31:0] Resultado

);

always @*
begin
    case (AluOp)

        //AMD
        3'b000:
        begin
            Resultado = Op1 & Op2;
        end

        //OR
        3'b001:
        begin
            Resultado = Op1 | Op2;
        end
        
        3'b010:
        begin
            Resultado = Op1 + Op2;
        end  
        
        3'b110:
        begin
            Resultado = Op1 - Op2;
        end
        
        3'b111:
        begin
            Resultado = Op1 > Op2 ? 1 : 0;
        end
    endcase 
end

endmodule