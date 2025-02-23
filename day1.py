import math

def readinput(input_file_dir):
    with open(input_file_dir,'r') as file:
        lines = file.readlines()
    list1=[]
    list2=[]
    for line in lines:
        data = line.split()
        list1.append(int(data[0]))
        list2.append(int(data[1]))
    return list1, list2

def calculatedistance(list1,list2):
    list1.sort()
    list2.sort()
    distance =0
    for i in range(len(list1)):
        distance += (math.fabs(list1[i]-list2[i]))
    return distance

def calculate_similarity(list1, list2):
    number_occurance_map = {}
    similarityScore = 0
    for number in list2:
        if number not in number_occurance_map:
            number_occurance_map[number] = 1
        else:
            currentCount = number_occurance_map[number]
            number_occurance_map[number] = currentCount +1
    for number in list1:
        if number in number_occurance_map:
            count = number* number_occurance_map[number]
            similarityScore +=count
    return similarityScore

if __name__ == "__main__":

    list1, list2 = readinput('input_day1.txt')
    totaldistance = calculatedistance(list1,list2)
    print(totaldistance)
    print(calculate_similarity(list1,list2))