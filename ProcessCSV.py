# Get file name
print("What is the name of the file?")
fileName = raw_input()
outputFileName = fileName.split('.')[0] + "_Transformed.txt"

# The file with the data from SQL
file1 = open(fileName, "r")

# The result file
file2 = open(outputFileName, "w")

# Read first line to get variable names
firstLine = file1.readline()
columnNames = firstLine.split(",")

# Read rest of the lines in sqldata.txt for the data
dataObjects = file1.readlines()
first = True

file2.write("{\n")
# Foreach line, split the string by comma or tab
for obj in dataObjects:
    if first:
        first = False
    else:
        file2.write(",\n")

    file2.write("\t{\n")
    values = obj.split(",")
    ctr = 0
    first2 = True

    for v in values:
        if first2:
            first2 = False
        else:
            file2.write(",\n")
            
        test = "\t\t\"" + columnNames[ctr].split("\n")[0] + "\": \"" + v.split("\n")[0] + "\""
        ctr += 1
        file2.write(test)
    
    file2.write("\n\t}")

file2.write("\n}\n")

# Close all files
file1.close()
file2.close()

input("Script is complete. Press anything to continue...")