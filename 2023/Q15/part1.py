from my_input import sample_input
from my_input import my_input

def hash(c, val):
    val += ord(c)
    val *= 17
    val = val % 256
    return val

def solve(input, debug = False):
    commands = input.split(",")
    
    result = 0
    for command in commands:
        val = 0
        for c in command:
            val = hash(c, val)
        result += val
        # print(val)
    print(result)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())