import math
import numpy as np


def readinput(input_file_dir) -> object:
    """ This is a function to read a file and store the lines from the file in a list"""
    with open(input_file_dir,'r') as file:
        lines = file.readlines()

    arrays =[]
    for line in lines:
        data = np.fromstring(line, dtype=int,sep= ' ')
        arrays.append(data)
    return np.array(arrays, dtype=object)


def safe_reports(reports):
    diffs = np.diff(reports)
    is_ass = np.all(diffs>=1) and np.all(diffs<=3)
    is_desc = np.all(diffs>=-3) and np.all(diffs<=-1)
    if is_ass or is_desc:
        return 1
    else:
        return 0

def is_single_level_bad(reports):
    is_safe = safe_reports(reports)
    if is_safe == 0:
        for i in range(len(reports)):
            if safe_reports(np.delete(reports,[i])):
                return 1
        return 0
    return is_safe

def how_many_reports_safe(reports):
    return np.sum([safe_reports(r) for r in reports])

def dampned_reports(reports):
    return np.sum([is_single_level_bad(r) for r in reports])

if __name__=="__main__":
    safe_report = how_many_reports_safe(readinput('input_day2.txt'))
    dampnedreports = dampned_reports(readinput('input_day2.txt'))
    print(safe_report)
    print(dampnedreports)