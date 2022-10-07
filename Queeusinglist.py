import queue


print("Quee operation")
queue  = []
while True:
    print("1.insert Rear 2.Delete front 3.Display")
    ch = int(input())
    if(ch==1):
           print("Enter the element to insert:")
           ele = input()
           queue.append(ele)
    elif ch == 2:
        try:
                  
                  print("delete element =", queue.pop(0))
        except:
                  print("queue is empty")
    elif ch == 3:
        print("queue Element ",queue)
    else:
        break
print('END OF PROGRAM')        


    
        
            

