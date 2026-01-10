#wap to calculate the percentage of student based on marks  of any 5 subject
s1=int(input("English:"))
s2=int(input("Marathi:"))
s3=int(input("Maths:"))
s4=int(input("Science:"))
s5=int(input("Hindi:"))
#calculate percentage
total=s1+s2+s3+s4+s5
percentage=(total/500)*100
#display result
print("percentage:",percentage)
print("Total mark:",total )