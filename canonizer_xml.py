import xml.etree.ElementTree as ET
import shutil
import re
import sys
import os

def parse_xml(xml_file, before):
    word_list=[]
    result_list=[]
    xmlpath=xml_file
    tree = ET.parse(xmlpath)
    root = tree.getroot()

    for data in root.iter("Word"):
        word_list.append(data.text)

    before_file=before
    after_file=os.path.basename(before_file)+"_after.txt"
    shutil.copy(before_file, after_file)

    word_list = set(word_list)

    with open(before_file, 'r', encoding='utf-8') as f:
        lines = f.read().split()
        l_lines=[]
        for data in lines:
            l_lines.append(data.lower())
         
        result_list = [x for x in l_lines if x not in word_list]
        result_data=' '.join(result_list)
        d = open(after_file, 'w', encoding='utf-8')
        d.write(result_data)
        
if len(sys.argv) > 0:
    if len(sys.argv) == 1:
        print("Please Enter 3 Argument.")
    elif len(sys.argv) == 2:
        print("Please Enter 2 Argument.")
    elif len(sys.argv) >= 4:
        print("Too many Arguments Entered.")
    else:
        parse_xml(sys.argv[1], sys.argv[2])
else:
    print("Not Enter the 3 Arguments.")
