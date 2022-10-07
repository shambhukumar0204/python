stack = []
while(True):
    ch=input('1.Push 2.Pop 3.Display 4.Quit')
    if(ch=='1'):
           ele=input('Enter the element to insert:')
           stack.append(ele)
    elif(ch =='2'):
        try:
                  ele = stack.pop()
                  print('delete element =',ele)
        except:
                  print('stack is empty')
    elif(ch =='3'):
        print('list of element in stack are', stack)
    else:
        break
print('END OF PROGRAM')        


    
        
            

