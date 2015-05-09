# Name - Kakali Mahapatra
# File I/O

def main():

#reading the file SALES.txt
    grandtotal=0
    readfile = open('SALES.txt','r')
    print("writing these total values into the TOTAL file")
    print("Please check the TOTAL.txt file for the result")
    outfile = open('TOTAL.txt','w')
    print("name", "             ","total", file=outfile)
    for i in range(16):
        data = readfile.readline()
        stringdata = data.split()
        #print(stringdata)
        name = stringdata[0]
        print(name)
        sale1 = eval(stringdata[1])
        sale2 = eval(stringdata[2])
        sale3 = eval(stringdata[3])
        sale4 = eval(stringdata[4])
        total = sale1+sale2+sale3+sale4
        print(total)
        grandtotal = grandtotal+total
        print(name,"     ", total, file=outfile)

    print("Total", "             ",grandtotal, file=outfile)
main()
