import csv
import re

fr = open('reportViewer.csv', 'rb')
reader = csv.reader(fr)

fw = open('2013_virginia_beach_budget.csv', 'wb')
writer = csv.writer(fw)

year = "2013"

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

uniqueID = 0
title = "ID", "Year", "Fund Number", "Fund Name", "Fund Type", "Department", "Amount"
writer.writerow(title)

for row in reader:
    col1 = row[0]
    if any(c.isdigit() for c in col1) and "Fiscal Year" not in col1:
        fundNum = col1[:3]
        fundName = col1[3:].strip()
    
    if "Appropriation Units:" in col1:
    	fundType = "Appropriation"
    elif "Revenue Sources:" in col1:
    	fundType = "Revenue"

    if is_number(row[8].replace(',','')) and "Totals" not in row[2] and (row[1] or row[2]):

        if row[1]:
        	dept = row[1]
        elif row[2]:
        	dept = row[2]

        uniqueID += 1
        amount = row[8].replace(",","")
        parsed_row = uniqueID, year, fundNum, fundName, fundType, dept, amount
        writer.writerow(parsed_row)
        
        
#    if any("Appropriation Totals" in s for s in row):
#        appropriation = row[8]
#        new_data = fundID, fund, appropriation
#        writer.writerow(new_data)

fr.close()
fw.close()
