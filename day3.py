from re import findall
def readinput(input_file_dir) ->str:
    with open(input_file_dir,'r') as file:
        lines = file.readlines()
    s="".join(lines)
    return s

def findallpattern(memory:str):
    """ This function loops through the string and finds the pattern mentioned and stores 
    it a list. Then the numbers from the list are used to find the product and sum.
    """
    pattern = r'mul\((\d+),(\d+)\)'
    matches = findall(pattern, memory)
    #print(type(matches))
    part1sum=0
    for match in matches:
        num1=int(match[0])
        num2=int(match[1])
        result = num1*num2
        part1sum = part1sum +result
    return part1sum

def findnewpattern(memory:str):
    """
    This function does the same thing as the function above but it further checks for 
    2 words do() and don't() and performs the same operation accordingly.
    """
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = findall(pattern, memory)
    part2sum =0
    enable = True
    for mat in matches:
        if mat == 'do()':
            enable = True
        elif mat == "don't()":
            enable = False
        else:
            x, y = map(int, mat[4:-1].split(','))
            if enable:
                part2sum += (x * y)
    return part2sum            

if __name__ == "__main__":
    memory=readinput('input_day3.txt')
    print(findallpattern(memory))
    print(findnewpattern(memory))