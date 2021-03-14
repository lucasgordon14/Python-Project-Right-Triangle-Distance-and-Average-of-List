
side1 = int(input("Side 1 "));
print("\n");
side2 = int(input("Side 2 "));
print("\n");
side3 = int(side1^2 + side2^2);
print("\n");

if(side1^2+side2^2 == side3^2):
        print("It is a Right Triangle");






initialHeight = int(input("Initial Height "));
bounces = int(input("Number of Bounces "));
bouncyIndex = 0.6;

if(bounces == 1):
        totalDistance = (initialHeight + (initialHeight*bouncyIndex))
        print(totalDistance);

elif(bounces == 2):
        totalDistance = (initialHeight + (initialHeight*bouncyIndex) + (initialHeight*bouncyIndex)*bouncyIndex)
        print(totalDistance);



print("\n");
userNum = []
length = int(input("Enter list length"))
print("Enter Values")
for i in range(length):
    data = int(input());
    userNum.append(data);

print("List: ", userNum);
print("Sum: "+ str(sum(userNum)));
print("Average: ", str(sum(userNum)/length));


#
#isRunning = True;
#userNums = [];
#size = 10;
#i = 0;

#print("Print 3 sequential 0's and Enter to end.");

#while(i < size):
 #       userNums = int(input("Input Values Here: "));
  #      i+=1;

   #     if(i == size):
    #            break


#for x in str(userNums):
 #       print((str(userNums)));
  #      print(str(userNums));
   #     print(str(userNums));
    #    print(str(userNums.__radd__(userNums)));
     #   print((userNums[:]));
        #sum = sum + userNums;
      #  sum = 0;
       # print(("Sum:" + str(sum)));
        #print(str("Average" + str(sum/userNums.__sizeof__())));
        #for i in userNums:
          #      if(i == 0):
           #             isRunning = False;
            #            break;

#if(i == size):

        #break
  #      print(userNums);
