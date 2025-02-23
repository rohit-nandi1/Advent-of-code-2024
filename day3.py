from re import findall


def readinput(input_file_dir) ->str:
    with open(input_file_dir,'r') as file:
        lines = file.readlines()
    s="".join(lines)
    return s

def findallpattern(memory:str):
    pattern = r'mul\((\d+),(\d+)\)'
    print(pattern)
    matches = findall(pattern, memory)
    print(matches)
    finalsum=0
    for match in matches:
        num1=int(match[0])
        num2=int(match[1])
        result = num1*num2
        finalsum = finalsum +result
    return finalsum

if __name__ == "__main__":
    memory=readinput('input_day3')
    print(findallpattern(memory))