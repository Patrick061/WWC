input1 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,
23,9,27,1,5,27,31,1,9,31,35,1,35,10,39,2,13,39,43,1,43,9,47,1,47,9,51,
1,6,51,55,1,13,55,59,1,59,13,63,1,13,63,67,1,6,67,71,1,71,13,75,2,10,75,
79,1,13,79,83,1,83,10,87,2,9,87,91,1,6,91,95,1,9,95,99,2,99,10,103,1,103,
5,107,2,6,107,111,1,111,6,115,1,9,115,119,1,9,119,123,2,10,123,127,1,127,
5,131,2,6,131,135,1,135,5,139,1,9,139,143,2,143,13,147,1,9,147,151,1,151,
2,155,1,9,155,0,99,2,0,14,0]

def WWC(arr,a,b):
    input_code = input1[:]
    input_code[1] = a
    input_code[2] = b

    pointer = 0

    while True:
        code = input_code[pointer]
        #print(f"pointer={pointer}")
        if code == 99:
            break
        elif code == 1:
            pos1 = input_code[pointer+1]
            pos2 = input_code[pointer+2]
            pos3 = input_code[pointer+3]
            input_code[pos3] = input_code[pos1]+input_code[pos2]
            # print(arr[0])
        elif code == 2:
            pos1 = input_code[pointer+1]
            pos2 = input_code[pointer+2]
            pos3 = input_code[pointer+3]
            input_code[pos3] = input_code[pos1]*input_code[pos2]
            #print(arr[0])
        else:
            print("error")
            break 
        pointer+=4

    return input_code[0]



     
a = WWC(input1,12,2)
print(a)



def tester(y,z):
    while y<99:
        copy_array = input1[:]
        #print(copy_array[:5])
        z=0
        while z<99:
            #print(y,z)
            if WWC(copy_array,y,z) == 19690720:
                
                return (y,z) 
                
            z+=1
        y+=1    

a,b = tester(0,0)
print(a,b)




print("")
print("")
print("")
print("NEW 2a")


code2 = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,72,20,224,1001,224,-1440,224,4,224,102,8,223,223,1001,224,5,
224,1,224,223,223,1002,147,33,224,101,-3036,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1102,32,90,
225,101,65,87,224,101,-85,224,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,1102,33,92,225,1102,20,52,225,
1101,76,89,225,1,117,122,224,101,-78,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,54,22,225,1102,5,
24,225,102,50,84,224,101,-4600,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,1102,92,64,225,1101,42,83,224,
101,-125,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,58,195,224,1001,224,-6840,224,4,224,102,8,223,223,101,1,
224,224,1,223,224,223,1101,76,48,225,1001,92,65,224,1001,224,-154,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,4,223,
99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,
99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,
0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,226,224,1002,223,2,223,1005,224,329,
101,1,223,223,7,677,226,224,102,2,223,223,1005,224,344,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,8,226,
226,224,1002,223,2,223,1006,224,374,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,389,1001,223,1,223,1008,226,226,224,1002,223,2,223,
1005,224,404,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,419,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,434,101,1,223,223,
108,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,107,677,677,224,102,2,223,223,1005,
224,479,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,509,101,1,223,223,107,226,677,224,1002,
223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,539,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,554,101,1,223,223,1007,
677,677,224,102,2,223,223,1006,224,569,101,1,223,223,8,677,226,224,102,2,223,223,1006,224,584,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,
1,223,1007,677,226,224,1002,223,2,223,1005,224,614,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,
644,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,659,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]


def WWC2(arr):
    input_code = arr[:]
    pointer = 0

    # Function to determine parameter values based on mode
    def get_param_value(param, mode):
        return param if mode == 1 else input_code[param]

    while True:
        instruction = input_code[pointer]
        opcode = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10

        if opcode == 99:  # Halt
            break

        elif opcode == 1:  # Addition
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            input_code[pos3] = get_param_value(pos1, mode1) + get_param_value(pos2, mode2)
            pointer += 4

        elif opcode == 2:  # Multiplication
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            input_code[pos3] = get_param_value(pos1, mode1) * get_param_value(pos2, mode2)
            pointer += 4

        elif opcode == 3:  # Input
            pos1 = input_code[pointer + 1]
            user_input = int(input("Provide input: "))  # Input ID as per instructions
            input_code[pos1] = user_input
            pointer += 2

        elif opcode == 4:  # Output
            pos1 = input_code[pointer + 1]
            output_value = get_param_value(pos1, mode1)
            print(f"Output: {output_value}")  # Outputs the value
            pointer += 2

        else:
            print(f"Error: Unknown opcode {opcode}")
            break

    return input_code[0]


b = WWC2(code2)
print(f"Position 0 output: {b}")

print("")
print("")
print("")
print("NEW 2b")

def WWC2b(arr):
    input_code = arr[:]
    pointer = 0

    # Function to determine parameter values based on mode
    def get_param_value(param, mode):
        return param if mode == 1 else input_code[param]

    while True:
        instruction = input_code[pointer]
        opcode = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10

        if opcode == 99:  # Halt
            break

        elif opcode == 1:  # Addition
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            input_code[pos3] = get_param_value(pos1, mode1) + get_param_value(pos2, mode2)
            pointer += 4

        elif opcode == 2:  # Multiplication
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            input_code[pos3] = get_param_value(pos1, mode1) * get_param_value(pos2, mode2)
            pointer += 4

        elif opcode == 3:  # Input
            pos1 = input_code[pointer + 1]
            user_input = int(input("Provide input: "))  # Input ID as per instructions
            input_code[pos1] = user_input
            pointer += 2

        elif opcode == 4:  # Output
            pos1 = input_code[pointer + 1]
            output_value = get_param_value(pos1, mode1)
            print(f"Output: {output_value}")  # Outputs the value
            pointer += 2

        elif opcode == 5:  # Jump-if-true
            param1 = get_param_value(input_code[pointer + 1], mode1)
            param2 = get_param_value(input_code[pointer + 2], mode2)
            if param1 != 0:
                pointer = param2
            else:
                pointer += 3

        elif opcode == 6:  # Jump-if-false
            param1 = get_param_value(input_code[pointer + 1], mode1)
            param2 = get_param_value(input_code[pointer + 2], mode2)
            if param1 == 0:
                pointer = param2
            else:
                pointer += 3

        elif opcode == 7:  # Less than
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            input_code[pos3] = 1 if get_param_value(pos1, mode1) < get_param_value(pos2, mode2) else 0
            pointer += 4

        elif opcode == 8:  # Equals
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            input_code[pos3] = 1 if get_param_value(pos1, mode1) == get_param_value(pos2, mode2) else 0
            pointer += 4

        else:
            print(f"Error: Unknown opcode {opcode}")
            break

    return input_code[0]


# Provide input of 5 as per challenge instructions
c = WWC2b(code2)
print(f"Position 0 output: {b}")




print("")
print("")
print("")
print("NEW 3")

ex = [1102,34915192,34915192,7,4,7,99,0]

def WWC2b(arr):
    input_code = arr[:] + [0] * 10000  # Extend memory to handle larger operations
    pointer = 0
    relative_base = 0  # New relative base for relative mode

    # Function to determine parameter values based on mode
    def get_param_value(param, mode):
        if mode == 0:  # Position mode
            return input_code[param]
        elif mode == 1:  # Immediate mode
            return param
        elif mode == 2:  # Relative mode
            return input_code[relative_base + param]
        return 0

    # Function to determine write location based on mode
    def get_write_address(param, mode):
        if mode == 0:  # Position mode
            return param
        elif mode == 2:  # Relative mode
            return relative_base + param
        raise ValueError("Invalid mode for write operation")

    while True:
        instruction = input_code[pointer]
        opcode = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10
        mode3 = (instruction // 10000) % 10

        if opcode == 99:  # Halt
            break

        elif opcode == 1:  # Addition
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            input_code[get_write_address(pos3, mode3)] = get_param_value(pos1, mode1) + get_param_value(pos2, mode2)
            pointer += 4

        elif opcode == 2:  # Multiplication
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            input_code[get_write_address(pos3, mode3)] = get_param_value(pos1, mode1) * get_param_value(pos2, mode2)
            pointer += 4

        elif opcode == 3:  # Input
            pos1 = input_code[pointer + 1]
            input_code[get_write_address(pos1, mode1)] = int(input("Provide input: "))  # Input value as required
            pointer += 2

        elif opcode == 4:  # Output
            pos1 = input_code[pointer + 1]
            print(f"Output: {get_param_value(pos1, mode1)}")  # Outputs the value
            pointer += 2

        elif opcode == 5:  # Jump-if-true
            param1 = get_param_value(input_code[pointer + 1], mode1)
            param2 = get_param_value(input_code[pointer + 2], mode2)
            if param1 != 0:
                pointer = param2
            else:
                pointer += 3

        elif opcode == 6:  # Jump-if-false
            param1 = get_param_value(input_code[pointer + 1], mode1)
            param2 = get_param_value(input_code[pointer + 2], mode2)
            if param1 == 0:
                pointer = param2
            else:
                pointer += 3

        elif opcode == 7:  # Less than
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            if get_param_value(pos1, mode1) < get_param_value(pos2, mode2):
                input_code[get_write_address(pos3, mode3)] = 1
            else:
                input_code[get_write_address(pos3, mode3)] = 0
            pointer += 4

        elif opcode == 8:  # Equals
            pos1 = input_code[pointer + 1]
            pos2 = input_code[pointer + 2]
            pos3 = input_code[pointer + 3]
            if get_param_value(pos1, mode1) == get_param_value(pos2, mode2):
                input_code[get_write_address(pos3, mode3)] = 1
            else:
                input_code[get_write_address(pos3, mode3)] = 0
            pointer += 4

        elif opcode == 9:  # Adjust relative base
            param1 = input_code[pointer + 1]
            relative_base += get_param_value(param1, mode1)
            pointer += 2

        else:
            print(f"Error: Unknown opcode {opcode}")
            break

    return input_code[0]




c = WWC2b(ex)
print(f"Position 0 output: {c}")


