def main():
    cricket =[]
    badminton=[]
    football=[]
    

    while True:
        
        print("1)Accept Data")
        print("2)Display Data")
        print("3)List of student who play both cricket and badminton")
        print("4)list of studeny who play either cricket or badminton but not both ")
        print("5)nmber jof student who play neither cricekt nor basminton")
        print("6)number of student who play cricket and football but not badminton")
        print("7)End")


        print("Enter your choice :")
        ch=int(input())

        if(ch==1):
            print("Enter Data for badminton")
            accept(badminton)

            print("Enter Data for cricket")
            accept(cricket)

            print("Enter Data for football")
            accept(football)
        
        elif(ch==2):
            print("Data for cricket")
            print(cricket)

            print("Data for badminton")
            print(badminton)

            print("Data for football")
            print(football)
        
        elif(ch==3):
            cricket_and_badminton(cricket,badminton)
        
        elif(ch==4):
            cricket_or_badminton(cricket,badminton)
        
        elif(ch==5):
            neither_cricket_nor_badminton(cricket,badminton,football)
        
        elif(ch==6):
            cricket_and_football_not_badminton(cricket,football,badminton)
        
        elif(ch==7):
            break

def accept(player):
    n = input("Ente thr nu,mber of students:")
    for i in range(n):
        x=input("Enter the name: ")
        player.append(x)


            
def cricket_and_badminton(cricket,badminton):
    cr_bad=[]
    for i in range(len(cricket)):
        x=cricket[i]
        if x in badminton:
            cr_bad.append(x)
    
    print("The list of studenyt who play both cricekt and badminton are :")
    print(cr_bad)


def cricket_or_badminton(cricket,badminton):
    final=[]
    for i in range(len(cricket)):

        final.append(cricket[a])
    output=[]
    for i in range(len(badminton)):
        if(badminton[i] not in cricket):
            final.append(badminton[i])
    
    intersection=[]
    for i in range(len(cricket)):
        if(cricket[i] not in badminton):
            final.append(cricket[i])


    for i in range(len(final)):
        if(final[i] not in intersection):
            output.append(final[i])
    print("the list of students who play either cricket or badminton are :")
    print(output)

        
def neither_cricket_nor_badminton(cricket,badminton,football)  :
    final=[]
    for i in range(len(cricket)):
        final.append(cricket[i])
    for i in range(len(badminton)):
        if (badminton[i] not in final ):
            final.append(badminton[i])
    output=[]
    for i in range(len(football)):
        if (football[i] not in final):
            output.append(football[i])
    print("the numebr of students neither playt cricket nor badminton are :")
    print(output)

def cricket_and_football_not_badminton(cricket , football, badminton):
    cr_ft=[]
    final=[]

    for i in range(len(cricket)):
        if (cricket[i] in football):
            cr_ft.append(cricket[i])

        
    
   
    for i in range(len(cr_ft)):
        final.append(cr_ft[i])
    
    print("The number of students who pllay cricketand football and not badminton are :")
    print(final)
    
main()







       

