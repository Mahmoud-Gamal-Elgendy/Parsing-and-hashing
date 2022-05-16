import argparse                     #to create your parser
from hashing import hashtext        #to use hash function
from readhw import Readw            #to read any file

#call the fuctions
HF=hashtext()
RF=Readw()

#create the parser
parser=argparse.ArgumentParser()
#add the arguments of the parser 
parser.add_argument("-f","--filename",type=str,help="Enter The Path of file")
parser.add_argument("-t","--hashtype",type=str,help="Enter The hash type")
args=parser.parse_args()

#cheack if the argument is null or not and print the hash of content in file
if args.filename==None or args.hashtype==None:
    print(parser.usage)
else:
    readall=RF.Readwlist(args.filename)
    for i in readall:
        i=i.rstrip("\n")
        hash=HF.hashing(i,args.hashtype)
        print(i+" : "+hash)