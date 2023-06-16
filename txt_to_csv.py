"""
University of Arizona SensorLab LoadSol 
Purpose: 
    This script reads a LoadSol .txt file and saves an equivalent .csv file with more legible headers.
Instructions:
    * Collect LoadSol data and download a .txt data file. Follow the instructions in the pdf 
      found at sensorlab.arizona.edu > Equipment > Equipment Resources > LoadSol
    * Save the .txt file in the same folder as this Python script, and change the variable
      'filename' below to the name of your file.
    * Open this script in Visual Studio Code. Click Run > Start Debugging
"""

filename = "loadsolASCII_23-06-16 11-27-05-434.txt"


def createHeaders(line):
    devices = line.split()
    headers = ""
    for d in devices:
        headers += d + '_Time[sec]' + ','
        headers += d + '_Force[N]' + ','
    return headers


def main():
    csvFilename = filename.split('.')[0] + '.csv'
    file = open(filename, 'r')
    lines = file.readlines()
    linesToSave = []

    count = 0
    for line in lines:
        if count < 2: # filename and comment
            count += 1
        elif count == 2: # line 2 contains device names
            linesToSave.append(createHeaders(line))
            linesToSave.append('\n')
            count += 1
        elif count > 3: # data
            csvLine = ",".join(line.split('\t'))
            linesToSave.append(csvLine)
            count += 1
        else: # line 3 contains repeated 'Time[sec]' and 'Force[N]' values
            count += 1

    csv = open(csvFilename, "w")
    csv.writelines(linesToSave)
    csv.close()

main()
