from my_input import sample_input
from my_input import my_input

import re
import numpy

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

def solve(input_s, debug = False):
    acc = 0
    for match in re.findall(pattern, input_s):
        acc += numpy.prod([ int(n) for n in match])
    print(acc)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())