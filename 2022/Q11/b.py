from collections import deque

from puzzle_input import input_data
from sample import sample_data

# data = sample_data.split("\n\n")
data = input_data.split('\n\n')

class Monkey:
    def __init__(self, startingItems: list, operationStr: str, testDivisor: int, targetTrue: int, targetFalse: int) -> None:
        self.items = deque(startingItems)
        [operant1, operator, operant2] = operationStr.split(" ")
        self.operator = operator
        self.isOperantNumber = [operant1.isnumeric(), operant2.isnumeric()]
        self.operant1 = int(operant1) if operant1.isnumeric() else operant1
        self.operant2 = int(operant2) if operant2.isnumeric() else operant2
        self.testDivisor = testDivisor
        self.target = {True: targetTrue, False: targetFalse}
        self.inspectCount = 0
    
        print(self.operator, self.isOperantNumber, self.operant1, self.operant2, self.testDivisor, self.target)
    
    def inspect(self):
        self.inspectCount += 1
        self.worryLevel = self.items.popleft()
        op1 = self.operant1 if self.isOperantNumber[0] else self.worryLevel
        op2 = self.operant2 if self.isOperantNumber[1] else self.worryLevel
        if self.operator == '+':
            self.worryLevel = op1 + op2
        else:
            self.worryLevel =  op1 * op2
    
    def test(self):
        return self.worryLevel % self.testDivisor == 0
    
    
    def throw(self):
        # self.worryLevel = self.worryLevel // 3
        return (self.worryLevel, self.target[self.test()])

monkeys = []
# parse monkey

for monkeyDetails in data:
    monkeyDetails = monkeyDetails.split("\n")[1:]
    # print(monkeyDetails)
    startLine = monkeyDetails[0].split(": ")[1]
    operationLine = monkeyDetails[1].split(": ")[1]
    testLine1 = monkeyDetails[2].split(": ")[1]
    testLine2 = monkeyDetails[3].split(": ")[1]
    testLine3 = monkeyDetails[4].split(": ")[1]
    
    items = [ int(x) for x in startLine.split(", ") ]
    operationStr = operationLine.split("= ")[1]
    testDivisor = int(testLine1.split(" ")[-1])
    target1 = int(testLine2.split(" ")[-1])
    target2 = int(testLine3.split(" ")[-1])

    monkeys.append( Monkey(items, operationStr, testDivisor, target1, target2) )

cap = 1
for i in range(len(monkeys)):
    cap = cap * monkeys[i].testDivisor

for round in range(1, 10001):
    for i in range(len(monkeys)):
        while monkeys[i].items:
            monkeys[i].inspect()
            (item, target) = monkeys[i].throw()
            monkeys[target].items.append(item % cap)
    # print(round, [ m.items for m in monkeys ])

ans = []
for monkey in monkeys:
    ans.append(monkey.inspectCount)
ans.sort()
ans = ans[-2:]

print(ans[0], ans[1], ans[0]*ans[1])

