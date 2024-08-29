from my_input import sample_input
from my_input import my_input

def solve(input, debug = False):
    lines = input.split("\n")
    timeL = lines[0]
    disL = lines[1]
    times = [ int(x) for x in timeL.split(":")[1].strip().split(" ") if len(x) > 0 ]
    dis = [ int(x) for x in disL.split(":")[1].strip().split(" ") if len(x) > 0 ]
    if debug: print(times, dis)
    result = 1
    for i in range(len(times)):
        way = 0
        time = times[i]
        distance = dis[i]
        for j in range(1, time):
            if j*(time-j) > distance:
                way+=1
        result *= way
    print(result)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())