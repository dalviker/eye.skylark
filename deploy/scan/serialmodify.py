#!/usr/bin/python
# coding: utf-8

import sys,os,re

class SerialModify:
    srcfilename=None
    targetfilename = None
    srcData = ""
    replacelist=[]
    def readSrc(self):
        try:
            f = open(self.srcfilename,"r",0);
            self.srcData = f.read()
            f.close()
            #print self.srcData
        except IOError:
            pass
    
    def scanSrc(self):
        #pattern = re.compile(r'(static)(\W+)(class)(\W+)(\S+)')
        pattern = re.compile(r'(static)(\W+)(class)(\W+)(\S+).*?({)',re.S)
        subpattern = re.compile(r'(implements)(\W+)(Serializable)',re.S)
        if self.srcData != "" :
            print "start scan and replace\n "
            #print pattern.findall(self.srcData)
            #search: search only once
            #m = pattern.search(self.srcData)
            #print m.group()
            for i in pattern.finditer(self.srcData):
                print i.group()
                m = subpattern.search(i.group())
                if m != None :
                    print m.group()
                    pass
                else:
                    self.replacelist.append(i.group())

            #print self.replacelist
        else:
            print "srcData is null \n"

    def replaceSrc(self):
        for i in self.replacelist:
            j = i 
            #print i
            #print j.replace("{" , "implements Serializable{")
            subpattern = re.compile(r'(implements)',re.S)
            m = subpattern.search(i)
            if m != None:
                print m.group()                
                self.srcData = self.srcData.replace(i ,j.replace("{" , " , java.io.Serializable {"))
            else:
                self.srcData = self.srcData.replace(i ,j.replace("{" , "implements java.io.Serializable {"))

        #print self.srcData
    
    def outputfile(self):
        try:
            f = open(self.targetfilename,"w");
            f.write(self.srcData)
            f.close()
            #print self.srcData
        except IOError:
            pass
        
    
    def __init__(self,srcfilename,targetfilename ):
        print srcfilename
        print targetfilename
        self.srcfilename = srcfilename
        self.targetfilename = targetfilename
        self.readSrc()
        self.scanSrc()
        self.replaceSrc()
        self.outputfile()
if __name__ == "__main__":
#    serm = SerialModify("AddressBookEntry.java","AddressBookEntrynew.java")
    serm = SerialModify(sys.argv[1] ,sys.argv[2] )
