import sys
import xmltodict
from bs4 import BeautifulSoup as Soup


def splitXML(infile, outfile):
    handler = open(infile).read()
    soup = Soup(handler,"lxml")
    file_object  = open(outfile, "w")
    for message in soup.findAll('post'):
        file_object.write(message.getText())
    file_object.close()

if len(sys.argv)!=3:
    if len(sys.argv)!=2:
        print("no input or output file")
    else:
        splitXML(sys.argv[1], "outfile.txt")
else:
    splitXML(sys.argv[1], sys.argv[2])
