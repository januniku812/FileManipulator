import shutil
import csv

def main():

  # opening the csv file by specifying
  # the location
  # with the variable name as csv_file
    with open('outputs\data_part_1_output.csv') as csv_file:

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

# adding mamas merged datas
    with open('final_combined_output.txt','wb') as wfd:
        files_array = [r'header.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_1_output.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_2_output.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_3_output.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_4_output.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_5_output.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_6_output.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_7_output.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_8_output.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_9_output.csv',r'C:\Users\jshar\OneDrive\Desktop\outputs\data_part_10_output.csv']
        for f in files_array:
            with open(f,'rb') as fd:
                if not str(files_array[0]) == str(f):
                    next(fd)
                    shutil.copyfileobj(fd, wfd)
                    print('this file isnt the header file')

                else:
                    shutil.copyfileobj(fd, wfd)
                    print('this file is the header file')




if __name__ == '__main__':
    main()
