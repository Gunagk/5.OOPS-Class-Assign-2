class Multiplefunctions():
    def subfields():
        lists =['Machine Learning',"Neural Network","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in lists:
            print(temp)

            
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==1):
            print(num,"is Odd number")
        else:
            print(num,"is Even number")


    def elegibility():
        Gen=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gen=="Male"):
            if(Age<21):
                print("Not Elegibile")
            else:
                print("Elegibile")
        elif(Gen=="Female"):
            if(Age<18):
                print("Not Elegibile")
            else:
                print("Elegibile")

 
    def percentage():
        sub1=98
        sub2=87
        sub3=95
        sub4=95
        sub5=93
        Marksscored=sub1+sub2+sub3+sub4+sub5
        Totalmarks=500
        percentage=((Marksscored)/(Totalmarks)*100)
        sub1=int(input("sub1="))
        sub2=int(input("sub2="))
        sub3=int(input("sub3="))
        sub4=int(input("sub4="))
        sub5=int(input("sub5="))
        print("Total:",Marksscored)    
        print("percentage:",percentage) 

        
    def Triangle():
        Height=(int(input("Height:")))
        Breadth=(int(input("Breadth:")))
        Areaformula=(Height*Breadth)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle",Areaformula)
        Height1=(int(input("Height1:")))
        Height2=(int(input("Height2:")))
        Breadth=(int(input("Breadth:")))
        Perimeterformula=(Height1+Height2+Breadth)
        print("Perimeter formula:Height1+Height2+Breadth")
        print("Perimeter of Triangle",Perimeterformula)