import csv
import os
# csv_file = input('Enter the name of input file: ')
# txt_file = input('Enter the name of the output file: ')

arr = os.listdir('src/text-classification-on-embedding/data/political-data')
print(arr)

path = 'src/text-classification-on-embedding/data/political-data/'
for input_file in arr:
    output_file = path + input_file[:-4]
    csv_file = path + input_file
    with open(output_file, "w") as output_file:
        with open(csv_file, "r") as input_file:
            [output_file.write("".join(row)+'\n')
             for row in csv.reader(input_file)]
            os.remove(csv_file)
            output_file.close()
