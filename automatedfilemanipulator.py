# imports for fileManipulator() and concat() func
import csv
import shutil
# for parsing through every file in the outputs dir
import os

def splitter_step_one():
    # making a split_files directory
    os.mkdir('split_files',mode = 0o777, dir_fd = None)
    chunk_size = 50000  # lines

    def write_chunk(part, lines):
        # making multiple data part outputs with new numbers at the end to signify what fraction of the file it correlates to
        with open('split_files\data_part_'+ str(part) +'.csv', 'w') as f_out:
            f_out.write(header)
            f_out.writelines(lines)
    # you can change the harcoded file path to anything that refers to first sheet of many records
    with open(r'data.csv', 'r') as f:
        count = 0
        header = f.readline()
        lines = []
        for line in f:
            count += 1
            lines.append(line)
            if count % chunk_size == 0:
                write_chunk(count // chunk_size, lines)
                lines = []
        # write remainder
        if len(lines) > 0:
            write_chunk((count // chunk_size) + 1, lines)

def fileManipulator(inputfilename):
    file = open("split_files\\" + inputfilename)
    type(file)
    csvreader = csv.reader(file)
    header = []
    rows = []
#   extract all the hroizontal rows in sheet1 data
    for row in csvreader:
        if not str(row) == "[]":
            rows.append(row)

    sheet2file = open('sheet2.csv')
    type(file)
    csvreader2 = csv.reader(sheet2file)
    rows_column_0_strs = []
    for row2 in csvreader2:
        if not str(row2) == "[]":
            rows_column_0_strs.append(str(row2[0]))

    matches = []

    for  row in rows:
        if str(row[21]) in rows_column_0_strs:
            matches.append(row)

    for row in rows:
        if row in matches:
            row[29] = "N"

    print("filepath: " + inputfilename)

    with open("outputs\\" + str(inputfilename[:-4]) + '_output.csv', 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(rows)
        file = open('sheet2.csv')
        type(file)
        csvreader_sheet2 = csv.reader(file)
        csvreader_sheet2_rows = []
        for sheet2rowiteratorrow in csvreader_sheet2:
            csvreader_sheet2_rows.append(sheet2rowiteratorrow)

        for matched_row in matches:
            for sheet2_row in csvreader_sheet2_rows:
                if str(sheet2_row[0]) == str(matched_row[21]):
                    matched_row[21] = sheet2_row[1]
                    matched_row[29] = "Y"

        print("writing rows - final step")
        csvwriter.writerows(matches)


    file.close()

    print(rows_column_0_strs)
    print("MATCHED ROWS NUMBER")
    print(len(matches))
    print("DONE! - fileManipulator: " + str(inputfilename))

def concat(files_array_input):

  # opening the csv file by specifying
  # the location
  # with the variable name as csv_file
    with open((files_array_input[0])) as csv_file:
      # creating an object of csv reader
      # with the delimiter as ,
        csv_reader = csv.reader(csv_file, delimiter = ',')

      # list to store the names of columns
        list_of_column_names = []

      # loop to iterate through the rows of csv
        for row in csv_reader:

          # adding the first row
            list_of_column_names.append(row)

          # breaking the loop after the
          # first iteration itself
            break

  # printing the result
    print("List of column names : ",
          list_of_column_names[0])

    with open('header.csv', 'w') as wfile:
        csvwriter = csv.writer(wfile)
        csvwriter.writerow(list_of_column_names[0])
        print('wrote the headers to header.csv')

# adding merged datas
    with open('final_combined_output.txt','wb') as wfd:
        with_header_files_array = files_array_input.append(r'header.csv')
        for f in files_array_input:
            with open(f,'rb') as fd:
                if not str(files_array_input[0]) == str(f):
                    next(fd)
                    shutil.copyfileobj(fd, wfd)
                    print('this file isnt the header file')

                else:
                    shutil.copyfileobj(fd, wfd)
                    print('this file is the header file')

if __name__ == '__main__':
    # starts with splitting the original giant file with the user only having
    #  to create and place a data.csv and a sheet2.csv file under the same directory as this file
    splitter_step_one()
    # step two which consists running the file manipulation func on every 50000 line chunk of the original file
    # and making a outputs dir before we run it for every file in split files
    os.mkdir('outputs',mode = 0o777, dir_fd = None)
    for file in os.listdir("split_files"):
        fileManipulator(file)
    inputfiles_array = []
    for output_file in os.listdir("outputs"):
        inputfiles_array.append("outputs\\" + output_file)
    # final step to merge all the outputted files after step 2
    concat(inputfiles_array)
    print("done with entire process!")
