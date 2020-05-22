"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.instructions = {
            "00000001": "HLT",
            "10000010": "LDI",
            "01000111": "PRN",
            "10100010": "MUL",
            "10100000": "ADD",
            "01000101": "PUSH",
            "01000110": "POP",
            "01010000": "CALL",
            "00010001": "RET",
            "10100111": "CMP",
            "01010100": "JMP",
            "01010101": "JEQ",
            "01010110": "JNE"

        }
        self.sp = 7
        self.less_than = 249
        self.equal = 250
        self.greater_than = 251

    def load(self):
        """Load a program into memory."""
        self.reg[self.sp] = 244  # 0xF4
        file_to_open = None
        if len(sys.argv) == 2:
            file_to_open = sys.argv[-1]
        else:
            raise Exception("No file specified!!!")

        program = []
        if file_to_open:
            f = open(file_to_open)
            for line in f:
                line = line.strip()
                if line:
                    final = ""
                    for letter in line:
                        if letter == "#":
                            break
                        elif letter == " ":
                            break
                        else:
                            final += letter
                    if len(final) > 2:
                        program.append(final)
            f.close()

        address = 0
        save_value_to_register = 0b10000010  # LDI
        print_value_at_register = 0b01000111  # PRN
        # For now, we've just hardcoded a program:
        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def run(self):
        """Run the CPU."""
        more_commands = True
        while more_commands:
            instruction_register = self.ram_read(self.pc)
            instruction = self.instructions[instruction_register]
            split_instruction = list(instruction_register)
            operand_a = self.ram[self.pc+1]
            operand_b = self.ram[self.pc+2]

            # print(instruction_register, split_instruction)
            # IR
            if split_instruction[0] == "1":  # 2 OPERANDS
                self.pc += 3

            elif split_instruction[1] == "1":  # 1 OPERAND
                self.pc += 2
            else:
                self.pc += 1

            # INSTRUCTIONS
            if instruction == "HLT":
                more_commands = False

            elif instruction == "JEQ":
                if self.ram[self.equal] == 1:
                    self.jump(operand_a)

            elif instruction == "JNE":
                if self.ram[self.equal] == 0:
                    self.jump(operand_a)

            elif instruction == "JMP":
                self.jump(operand_a)

            elif instruction == "CALL":
                self.stack_push(self.pc)
                val = self.reg_read(operand_a)
                self.pc = val

            elif instruction == "RET":
                val = self.stack_pop()
                self.pc = val

            elif split_instruction[2] == "1":
                self.alu(instruction, operand_a, operand_b)

            elif instruction == "LDI":
                self.reg_write(operand_a, operand_b)

            elif instruction == "PRN":
                val = self.reg_read(operand_a)
                print(val)

            elif instruction == "PUSH":
                self.reg[self.sp] -= 1
                val = self.reg_read(operand_a)
                self.stack_push(val)

            elif instruction == "POP":
                val = self.stack_pop()
                self.reg_write(operand_a, val)
                self.reg[self.sp] += 1

            else:
                raise Exception("unknown instruction")

    def reg_read(self, mar):
        mar = int(mar, 2)
        return self.reg[mar]

    def reg_write(self, mar, mdr):
        # MAR is key, MDR is value
        mar = int(mar, 2)
        if type(mdr) != int:
            mdr = int(mdr, 2)
        self.reg[mar] = mdr

    def jump(self, op_a):
        val = self.reg_read(op_a)
        self.pc = val

    def stack_push(self, val):
        self.ram[self.reg[self.sp]] = val

    def stack_pop(self):
        val = self.ram[self.reg[self.sp]]
        return val

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        reg_a = int(reg_a, 10)
        reg_b = int(reg_b, 10)
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
            self.reg[reg_a] = self.reg[reg_a] & 0xFF
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
            self.reg[reg_a] = self.reg[reg_a] & 0xFF

        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == "DIV":
            self.reg[reg_a] /= self.reg[reg_b]
        elif op == "CMP":
            if self.reg[reg_a] == self.reg[reg_b]:
                self.ram[self.equal] = 1
            elif self.reg[reg_a] < self.reg[reg_b]:
                self.ram[self.less_than] = 1
            else:
                self.ram[self.greater_than] = 1
        else:
            raise Exception("Unsupported ALU operation")

    def ram_read(self, pointer):
        return self.ram[pointer]

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
