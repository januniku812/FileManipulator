# FileManipulator
Python code made to help work with a excel/csv task by parsing through rows in two file, saving them, manipulating and changing data, and lastly writing it all to a 
a csv output file. Specifically, for this program, there is a "sheet one" and a "sheet 2" for which sheet 1, in one  column there are certains keys that have corresponding values in the second column of sheet 2. We need to find matched rows(ones whose key is in sheet 2's column one), switch out a column's keys and their corresponding values in sheet 2, change another cell in the matched row to say 'N', and copy and pasted those matched rows below the original data. Since this is for big files there is a concat file python program to merge all the split up files from the split_file program run on the original big file first which are run after and before the filemanipulation program respectively. 

There is a python file called automatedfilemanipulator.py that takes all the other 3 python files steps I described above and makes it a one-time program that only needs a sheet1 and sheet2 of desire supplied to it by the user and gives a file called final_combined_output.txt(which can easily be changed to csv) with our result! It also creates a header.csv, a outputs folder, and a split files folder which are for reference & program during run time. These 3 files/folders can be deleted once the program displays 'done with the entire process!' and exits the program.

***NOTE: This is a backup/upload that is specific (to solve) one of my personal programs/tasks but the concat_file and split_file python programs can still be used and run when hardcoded paths are changed for whoever is interested.

