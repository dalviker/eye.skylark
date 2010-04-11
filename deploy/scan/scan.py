#!/usr/bin/python
# coding = utf-8
import sys
from serialmodify import *

class Scan:
    scandir=None
    fileExtList=[".java"]
    fileList=[]
    def listDirectory(self):  
        "get list of file info objects for files of particular extensions"
        for root ,dirs,files in os.walk(self.scandir):
            for dirname in dirs:
                #print dirname
                pass
            for filename in files:
                #print filename 
                #print os.path.splitext(filename)
                if os.path.splitext(filename)[1] in self.fileExtList:
                    #print "add "+ filename
                    self.fileList.append(os.path.join(root,filename))
    
    def __serialmodify__(self):
        for i in self.fileList:
            serm = SerialModify(i,i)
        pass


    def __init__(self, scandir):
        self.scandir = scandir
        self.listDirectory()
        print self.fileList
        self.__serialmodify__()
        pass


if __name__ == "__main__":
    scan = Scan(sys.argv[1])


    
