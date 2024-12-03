from my_input import sample_input
from my_input import my_input

import re
import numpy

pattern = r'(mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\)|do\(\))'

def solve(input_s, debug = False):
    acc = 0
    enabled = True
    for match in re.findall(pattern, input_s):
        if match[0].startswith("mul"):
            if enabled:
                acc += numpy.prod([ int(match[1]), int(match[2]) ])
        elif match[0].startswith("don't()"):
            enabled = False
        else:
            enabled = True
    print(acc)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())