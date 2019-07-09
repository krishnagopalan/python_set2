k=int(input())
if k>1:
    for a in range(2,k):
        if(k%a==0):
            print('no')
            break;
    else:
        print('yes')
