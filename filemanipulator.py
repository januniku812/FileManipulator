import csv

def fileManipulator():
    file = open('data_part_1.csv')
    type(file)
    csvreader = csv.reader(file)
    header = []
    rows = []
#   extract all the hroizontal rows in sheet1 data
    for row in csvreader:
        if not str(row) == "[]":
            rows.append(row)

    print(rows)

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
            print("MATCH FOUND")
            matches.append(row)

    for row in rows:
        if row in matches:
            row[29] = "N"

    with open('data_part_1_output.csv', 'w', newline='') as csvfile:
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
                    print("changing matche key values")
                    matched_row[29] = "Y"
                    print("changing matched rows back to y")

        print("writing rows - final step")
        csvwriter.writerows(matches)


    file.close()

    print(rows_column_0_strs)
    print("MATCHED ROWS NUMBER")
    print(len(matches))
    print("DONE!")

fileManipulator()
