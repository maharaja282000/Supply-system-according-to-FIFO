import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import random as r
import socket
TCP_IP = '10.74.14.88'
TCP_PORT = 9100
BUFFER_SIZE = 1024
alphanum=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"
          "Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
#from pyfirmata import Arduino
#board=Arduino("COM8")
#board.digital[7].write(1)
#time.sleep(5)
#board.digital[7].write(0)
print("                            Rane ZF - Trichy                        ")
print("                         THREAD CONE SUPPLY SYSTEM      ")
print("-----------------------------------------------------------------------------------------------")
print("List of Threads available:")
df=pd.read_csv("file1.csv")
print(df)
print("-----------------------------------------------------------------------------------------------")
readerlist=[]
threadtype=[]
month=[]
rackno=[]
boxno=[]
quantity=[]
otime=[]
csvfile= open("file1.csv",'r+',newline="")
print("Reading the data from file!")
reader=csv.reader(csvfile)
for line in reader:
    threadtype.append(line[0])
    month.append(line[1])
    rackno.append(line[2])
    boxno.append(line[3])
    quantity.append(line[4])
    otime.append(line[5])
print("Data recorded successfully!")
tri=int(input("\n Scan QRcode(Show Stock) to See the boxes available"))
if(tri==160):
    print("Boxes available in stock")
    count248A=0
    count143A=0
    count217A=0
    for i in range(0,len(threadtype)):
        if(threadtype[i]=="P92000248A"):
            count248A=count248A+1
    for i in range(0,len(threadtype)):
        if(threadtype[i]=="P92000143A"):
            count143A=count143A+1
    for i in range(0,len(threadtype)):
        if(threadtype[i]=="P92000217A"):
            count217A=count217A+1
    print("The number of 248A boxes available is : ",count248A)
    print("The number of 143A boxes available is : ",count143A)
    print("The number of 217A boxes available is : ",count217A)
    xdata=["P92000248A","P92000143A","P92000217A"]
    ydata=[count248A,count143A,count217A]
    c1=["green","green","green"]
    c2=["red","red","red"]
    c3=["green","green","red"]
    c4=["red","green","green"]
    c5=["green","red","green"]
    c6=["green","red","red"]
    c7=["red","green","red"]
    c8=["red","red","green"]
    if(count248A>=2 and count143A>=2 and count217A>=2):
        plt.bar(xdata,ydata,width=.5,color=c1,label="Red-low \n Green-OK stock")
        plt.xlabel("Thread types",size="24",color="blue")
        plt.ylabel("Quantity",size="24",color="orange")
        plt.title("Thread cone available in stock")
        plt.legend()
        plt.show()
    elif(count248A<2 and count143A<2 and count217A<2):
        plt.bar(xdata,ydata,width=.5,color=c2,label="Red-low \n Green-OK stock")
        plt.xlabel("Thread types",size="24",color="blue")
        plt.ylabel("Quantity",size="24",color="orange")
        plt.title("Thread cone available in stock")
        plt.legend()
        plt.show()
    elif(count248A>=2 and count143A>=2 and count217A<2):
        plt.bar(xdata,ydata,width=.5,color=c3,label="Red-low \n Green- OK stock")
        plt.xlabel("Thread types",size="24",color="blue")
        plt.ylabel("Quantity",size="24",color="orange")
        plt.title("Thread cone available in stock")
        plt.legend()
        plt.show()
    elif(count248A<2 and count143A>=2 and count217A>2):
        plt.bar(xdata,ydata,width=.5,color=c4,label="Red-low \n  Green- OK stock")
        plt.xlabel("Thread types",size="24",color="blue")
        plt.ylabel("Quantity",size="24",color="orange")
        plt.title("Thread cone available in stock")
        plt.legend()
        plt.show()
    elif(count248A>=2 and count143A<2 and count217A>=2):
        plt.bar(xdata,ydata,width=.5,color=c5,label="Red-low \n Green- OK stock")
        plt.xlabel("Thread types",size="24",color="blue")
        plt.ylabel("Quantity",size="24",color="orange")
        plt.title("Thread cone available in stock")
        plt.legend()
        plt.show()
    elif(count248A>=2 and count143A<2 and count217A<2):
        plt.bar(xdata,ydata,width=.5,color=c6,label="Red-low \n Green- OK stock")
        plt.xlabel("Thread types",size="24",color="blue")
        plt.ylabel("Quantity",size="24",color="orange")
        plt.title("Thread cone available in stock")
        plt.legend()
        plt.show()
    elif(count248A<2 and count143A>=2 and count217A<2):
        plt.bar(xdata,ydata,width=.5,color=c7,label="Red-low \n Green- OK stock")
        plt.xlabel("Thread types",size="24",color="blue")
        plt.ylabel("Quantity",size="24",color="orange")
        plt.title("Thread cone available in stock")
        plt.legend()
        plt.show()
    elif(count248A<2 and count143A<2 and count217A>=2):
        plt.bar(xdata,ydata,width=.5,color=c8,label="Red-low \n Green- OK stock")
        plt.xlabel("Thread types",size="24",color="blue")
        plt.ylabel("Quantity",size="24",color="orange")
        plt.title("Thread cone available in stock")
        plt.legend()
        plt.show()
else:
    print("switching to data")
print("\n")
print("                    Scan QRcode(Take a box)                    ")
print("                            (Or)                               ")
print("                    Scan QRcode(Add a box)                     ")
x=int(input("\nWaiting for Scanner input<>"))
if(x==1):
    out_time=time.time()
    syst2=time.ctime(out_time)
    index=[]
    m1=[]
    rc1=[]
    c=input("Enter the thread to take.... ")
    for i in range(0,len(threadtype)):
        if(threadtype[i]==c):
            index.append(i)
            continue
    print(index)
    for b in index:
        m1.append(int(month[b]))
        rc1.append(rackno[b])
    print(m1,"the list")#month list
    Firstmonth=min(m1)# here it is not taking minimum!
    print(Firstmonth,"the minimum of list")#minimum
    ind=m1.index(Firstmonth)
    rowoffm=rc1[ind]
    disl=[]
    for q in range(0,len(rackno)):
        if(rackno[q]==rowoffm and threadtype[q]==c):
            setq=q
    print(setq)#main
    xs=month[setq]
    y=rackno[setq]
    z=boxno[setq]
    xy=quantity[setq]
    timez=otime[setq]
    disl.append(c)
    disl.append(xs)
    disl.append(y)
    disl.append(z)
    disl.append(xy)
    disl.append(timez)
    print("\n The Thread you need to take is....")
    valuelist=["Threadname","month","Rack","box number","Quantity","time"]
    print(valuelist)
    print(disl)
    dummydisl=[]
    for values in disl:
        dummydisl.append(values)
    print("\n","Results:")
    print("      Thread name------>",disl[0])
    print("      Rack number------>",disl[2])
    print("      Box number------->",disl[3])
    print("\n","                  Final control check activated!!       ")
    csvfile.close()
    name_of_operator=input("1.)please enter your name or scan the Id card : ")
    dummydisl.append(syst2)
    dummydisl.append(name_of_operator)
    scanracknumber=input("2.)please scan the rack number : ")
    scanthreadcode=input("3.)please scan the thread code : ")
    scanboxnumber=input("4.)Please scan the boxnumber : ")
    if(scanracknumber==disl[2] and scanthreadcode==disl[0] and scanboxnumber==disl[3]):
        print("Correct box is taken out....thank you!")
        #board.digital[7].write(1)
        #time.sleep(5)
        #board.digital[7].write(0)
        #time.sleep(4)
        df.loc[setq-1,"threadname"]="0"
        df.loc[setq-1,"1111"]="1000000"
        df.loc[setq-1,"rackno"]="0"
        df.loc[setq-1,"12345"]="0"
        df.loc[setq-1,"987654"]="0"
        df.loc[setq-1,"time"]="0"
        df.to_csv("file1.csv",index=False)
        csvfile2= open("file2.csv",'a+',newline="")
        writer= csv.writer(csvfile2)
        writer.writerow(dummydisl)
        csvfile2.close()
    else:
        print("Data mismatch error....please repeat the process")
        #board.digital[6].write(1)
        #time.sleep(5)
        #board.digital[6].write(0)
        #time.sleep(5)
elif(x==2):
    ct=time.time()
    syst=time.ctime(ct)
    csvfile= open("file1.csv",'a+',newline="")
    writer= csv.writer(csvfile)
    sd=[]
    tt=input("Enter thread name.... ")
    mon=int(input("enter month.... "))
    rn=input("Enter Rackno........ ")
    r.shuffle(alphanum)
    tmp=(alphanum[0:4])
    bxn1=""
    for elements in tmp:
        bxn1+=elements
    bxn=bxn1
    print("Your Generated box number is   : ",bxn)
    zpl2=str(bxn)
    zpl = """
    ^XA
    ^FO150,40^BY3
    ^BCN,110,Y,N,N
    ^FD"""+zpl2+"""^FS
    ^XZ 
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytes(zpl, "utf-8"))
    s.close()
    print("Please take the label and paste it in the box !")
    qnty=int(input("Enter quantity.... "))
    sd.append(tt)
    sd.append(mon)
    sd.append(rn)
    sd.append(bxn)
    sd.append(qnty)
    sd.append(syst)
    writer.writerow(sd)
    valuelist=["Threadname","month","Rack","box number","Quantity","time"]
    print(valuelist)
    print(sd)
    print("Your thread is successfully added....,Thankyou!")
    #board.digital[7].write(1)
    #time.sleep(5)
    #board.digital[7].write(0)
    #time.sleep(4)
    csvfile.close()





    
    
    

#with open("writerfile1.csv",'w',newline='')as file:
    #writer= csv.writer(file)
    #writer.writerow(['peak time range','peak voltage'])
    #for bc in v1:
            #writer.writerows(zip(t1,v1))  


#df=pd.read_csv("file1.csv")
#df.loc[2,"threadname"]="rename"
#df.to_csv("file1.csv",index=False)
#print(df)




        
