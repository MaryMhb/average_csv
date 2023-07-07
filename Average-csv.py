import csv
from statistics import mean 
from collections import OrderedDict 

def calculate_averages(input_file_name, output_file_name):
    with open (input_file_name) as csvfile:
        fin = csv.reader (csvfile)
        dic = OrderedDict ()
        for line in fin:
            line = list(line)
            name = line[0]
            average = mean (map(float, line[1:]))
            dic[name] = average
        with open (output_file_name , 'w') as csvfile:
            for char in dic:
                s = char + ',' + str (dic[char]) + '\n'
                csvfile.write (s)


def calculate_sorted_averages(input_file_name, output_file_name):
    with open (input_file_name) as csvfile:
        fin = csv.reader (csvfile)
        dic = OrderedDict ()
        for line in fin:
            line = list(line)
            name = line[0]
            average = mean (map(float, line[1:]))
            dic[name] = average
            dic_sorted = {k : v for k,v in sorted(dic.items(), key= lambda item: (item[1] , item[0]))}
    with open (output_file_name , 'w') as csvfile:
        for v in dic_sorted:
            s = v + ',' + str (dic_sorted[v]) + '\n'
            csvfile.write (s)


def calculate_three_best(input_file_name, output_file_name):
    with open (input_file_name) as csvfile:
        fin = csv.reader (csvfile)
        dic = OrderedDict ()
        for line in fin:
            line = list(line)
            name = line[0]
            average = mean (map(float, line[1:]))
            dic[name] = average
            dic_sorted = {k : v for k,v in sorted(dic.items(), key= lambda item: (-item[1] , item[0]))}
            lis = list(dic_sorted.keys())
        with open (output_file_name , 'w') as csvfile:
            for i in range (0 , 3):
                s = lis[i] + ',' + str (dic_sorted[lis[i]]) + '\n'
                csvfile.write (s)


def calculate_three_worst(input_file_name, output_file_name):
    with open (input_file_name) as csvfile:
        fin = csv.reader (csvfile)
        dic = OrderedDict ()
        for line in fin:
            line = list(line)
            name = line[0]
            average = mean (map(float, line[1:]))
            dic[name] = average
            lis = list(dic.values())
            lis.sort ()
        with open (output_file_name , 'w') as csvfile:
            for i in range (0 , 3):
                s = str (lis[i]) + '\n'
                csvfile.write (s)
 


def calculate_average_of_averages(input_file_name, output_file_name):
    with open (input_file_name) as csvfile:
        fin = csv.reader (csvfile)
        dic = OrderedDict ()
        for line in fin:
            line = list(line)
            name = line[0]
            average = mean (map(float, line[1:]))
            dic[name] = average
            lis = list(dic.values())
        averages = mean (map(float , lis))
        averages = str(averages)
    with open (output_file_name , 'w') as csvfile:
        csvfile.write (averages)
