# reads an instruction from file, converts it to machine code, and outputs it
def process_instruction(line, output_file):

    # look for "//"" for a comment (returns -1 if not there)
    comment = ""
    slash_pos = line.find("//")

    # if found, take the "//"" and everything after and store it as a comment
    if slash_pos >= 0:
        comment = line[slash_pos:].replace("\n", "")
        # then get rid of it
        line = line[:slash_pos]
    
    # split what remains into a list of words making up the assembly instruction
    assembly_instruction = line.split()

    #if there is an assembly instruction
    if assembly_instruction:

        # remove and save the line number ("0.")
        line_number = assembly_instruction.pop(0)
        # send the rest to be converted into machine code
        instruction = convert_instruction(assembly_instruction)
        # write the converted instruction to the output file
        output_file.write(line_number + " " + instruction + " ")

    # write comments if they exist and go to the next line
    output_file.write(comment + "\n")

# converts an instruction from assembly into machine code
def convert_instruction(assembly_instruction):

    machine_instruction = 0

    # convert an operation into its opcode
    operation = assembly_instruction.pop(0)
    operations = ["MOV", "NOT", "OR", "AND", "XOR", "SHR", "ADD", "SUB", \
                  "INC", "DEC", "LDI", "LDM", "JMP", "JIZ", "JIN", "STM"]
    if operation in operations:
        opcode = operations.index(operation)
    else:
        return "Error: invalid operation"
    
    # put the opcode in bits 14 downto 11
    machine_instruction = machine_instruction | (opcode << 11)

    # FIRST ARGUMENT
    arg1 = int(assembly_instruction.pop(0))
    # opcodes 0 through 11 have the first argument end at bit 8
    if opcode >= 0 and opcode <= 11:
        machine_instruction = machine_instruction | (arg1 << 8)
    # opcodes 12 through 15 have the first argument end at bit 5
    else:
        machine_instruction = machine_instruction | (arg1 << 5)

    # SECOND ARGUMENT
    if assembly_instruction:
        arg2 = int(assembly_instruction.pop(0))
        # opcodes 0 through 9 have the second argument end at bit 5
        if opcode >= 0 and opcode <= 9:
            machine_instruction = machine_instruction | (arg2 << 5)
        # opcodes 10, 11, and 15 have the second argument end at bit 0
        elif opcode in [10, 11, 15]:
            machine_instruction = machine_instruction | arg2
        # opcodes 12 through 14 don't have a second argument

    # THIRD ARGUMENT
    if assembly_instruction:
        arg3 = int(assembly_instruction.pop(0))
    # opcodes 2, 3, 4, 6, and 7 have the third argument end at bit 2
        if opcode in [2, 3, 4, 6, 7]:
            machine_instruction = machine_instruction | (arg3 << 2)
        # other opcodes don't have a third argument
    
    # convert machine instruction to a binary string 15 bits long
    machine_inst_binary = "{0:015b}".format(machine_instruction)
    # insert spaces for readability
    machine_inst_binary = machine_inst_binary[0:3] + " " + machine_inst_binary[3:7] + " " \
                          + machine_inst_binary[7:11] + " " + machine_inst_binary[11:]

    return machine_inst_binary

def main():
    # prompt the user for the file name of the assembly program
    input_filename = input("Enter file name of assembly program: ")

    # add "assembled" to the output file name before the .txt
    output_filename = input_filename[:len(input_filename) - 4] + "_assembled" \
                    + input_filename[len(input_filename) - 4:]

    try:
        input_file = open(input_filename, 'r')
    except:
        print("Couldn't find input file")
        input("Press enter to exit")
        exit(0)

    output_file = open(output_filename, 'w')

    # convert the lines of the assembly program until reaching the end of the input file
    for line in input_file:
        process_instruction(line, output_file)
    
    input_file.close()
    output_file.close()
    print("Converted program to machine code in", output_filename)
    input("Press enter to exit")

if __name__ == '__main__':
    main()