`timescale 1ns/1ns
module tb_ISA;

    reg [19:0] Instruction;  // Registro para la instrucción
    wire [31:0] Salida;      // Salida del módulo ISA

    // Instancia del módulo ISA
    ISA uut (
        .Instruction(Instruction),
        .Salida(Salida)
    );

    // Contador para manejar las direcciones de las instrucciones
    integer i;               // Variable para iterar
    reg [19:0] mem [0:255]; // Memoria para almacenar las instrucciones

    initial begin
        // Leer las instrucciones desde el archivo
        $readmemb("datos_convertidos.txt", mem);
        
        // Aplicar las instrucciones de la memoria
        for (i = 0; i < 30; i = i + 1) begin
            Instruction = mem[i];
            #10; // Espera entre cada instrucción
            $display("Instruction: %b | Salida: %h", Instruction, Salida);
        end

        // Terminar la simulación
        $finish;
    end

endmodule
