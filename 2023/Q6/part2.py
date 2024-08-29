from my_input import sample_input
from my_input import my_input

def solve(input, debug = False):
    lines = input.split("\n")
    timeL = lines[0]
    disL = lines[1]
    times = [ int(timeL.split(":")[1].replace(" ", "")) ]
    dis = [ int(disL.split(":")[1].replace(" ", "")) ]
    if debug: print(times, dis)
    for i in range(len(times)):
        way = 0
        time = times[i]
        distance = dis[i]
        for j in range(1, time):
            if j*(time-j) > distance:
                way+=1
        print(way)

solve(sample_input.strip(), True)
print()
solve(my_input.strip())