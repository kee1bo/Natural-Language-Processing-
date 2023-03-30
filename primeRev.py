# cook your dish here
t= int(input())
for i in range(t):
    N = int(input())
    A = input()
    B = input()
    countA0= 0 
    # countA1= 0
    countB0=0 
    # countB1=0
    for i in range(N):
        if A[i]=='0':
            countA0+=1
            
        elif B[i]=='0':
            countB0+=1 
        # print(A[i],B[i])
        
    print(countA0,countB0)
    # if countA0!=countB0:
    #     print('NO')
    # else:
    #     print('Yes')
            