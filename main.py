import xml.etree.ElementTree as ET
import re
import os
import sys


def main():
    print(sys.argv[1])
    xml = ET.parse('./' + sys.argv[1])
    # xml = ET.parse('./E__Web_KYOPSWeb_Public_Reports_Extracts_ExtractData_UNIVERSITY+OF+KENTUCKY+POLICE_CSBA229@UKY.EDU_Field+Information08252021190419 (2).xml')

    root = xml.getroot()

    output = open(sys.argv[1] + '-output.csv', 'w')
    printxml('', root, output)


def printxml(path, root, output):
    paths = []
    pathsF = []
    print(root)
    print(root.tag.split('}'))
    if path+root.tag not in paths or path+root.tag not in pathsF:
        output.write(path+root.tag + "\n")
        paths.append(path+root.tag)

    for f in root:
        print(type(f))
        if len(f) != 0:
            printxml(path + f.tag.split('}')[0] + '/', f, output)
        else:
            if path + f.tag.split('}')[0] not in pathsF:
                if f.items():
                    output.write(path + f.tag.split('}')[0] + "|" + str(f.text) + "|" + str(f.items()) + "\n")
                else:
                    output.write(path + f.tag.split('}')[0] + "|" + str(f.text) + "|" + " " + "\n")


if __name__ == '__main__':
    main()
