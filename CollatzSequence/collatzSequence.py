#Ask user for input
num = int(input("Enter positive number or '0' to terminate program: "))

#Define some necessary values
count = 0
sum = num
avg = 0
zero = 0

#Start infinite loop
while(True):
  count+=1
  if count>1:
    num = int(input("Enter next number or '0' to terminate program: "))
  count=zero
  sum=num
  #Check first entered number
  if num==0:
    print("\nHave a nice day!")
    break
    #Program ends if first number is 0
  else:
    print(" ", num, end="\t")
    #Start loop for first number until the result = 1
    while num!=1:
      count+=1
      #Check and set condition for even number
      if num%2==0:
        num=num//2
      #Check and set condition for odd number
      elif num%2!=0:
        num=(num*3)+1
      #Set only 5 numbers per line
      if (count+1)%5==0:
        print(num)
      else:
        print(" ", num, end="\t")
      sum+=num
    avg=sum/count
    #Display results
    if (count+1)%5==0:
        print("It took ",count, "iterations to arrive to 1")
    else:
        print("\nIt took ",count, "iterations to arrive to 1")
    print("Average number is: ",format(avg, '.2f'), end="\n")
    print()#Go to the beginning of loop
