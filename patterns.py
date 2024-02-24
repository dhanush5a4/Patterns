# patter 14
# n=int(input())
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=' ')
#     for j in range(2*i+1):
#         print("*",end=' ')
#     for j in range(n-i-1):
#         print(" ",end=' ')
#     print()
# output:
"""
5
        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 
"""



# pattern 15
# n=int(input())
# for i in range(n):
#     for j in range(i):
#         print(" ",end=' ')
#     for j in range((n*2)-(2*i+1)):
#         print("*",end=' ')
#     for j in range(i):
#         print(" ",end=' ')
#     print()

# output
"""
5
* * * * * * * * * 
  * * * * * * *   
    * * * * *     
      * * *       
        *         
"""
    

 # pattern 16

# n=int(input())
# for i in range(n-1):                            
#     for j in range(n-i-1):                  
#         print(" ",end=' ')
#     for j in range(2*i+1):
#         print("*",end=' ')
#     for j in range(n-i-1):
#         print(" ",end=' ')
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end=' ')
#     for j in range((n*2)-(2*i+1)):
#         print("*",end=' ')
#     for j in range(i):
#         print(" ",end=' ')
#     print()

# output
"""
5
        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 
  * * * * * * *   
    * * * * *     
      * * *       
        *         
"""


# pattern 17

# n=int(input())

# for i in range(n-1):
#     for j in range(i+1):
#         print("*",end=' ')
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=' ')
#     print()
    
    
    # same but different approach


# # pattern 18
# n=int(input())
# row=0
# for i in range(1,2*n):  
#     row=i
#     if row>n:
#         row=((2*n)-i)
   
#     for j in range(1,row+1):
#         print("*", end=" ")
#     print()


# output
"""
5
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""

# # pattern 19
# n=int(input())
# for i in range(1,n+1):
    
#     for j in range(1,i+1):
#         if ((i+j) %2==0) :
#             print(1,end=' ')
#         else:
#             print(0,end=' ')
#     print()

# output

"""
5

1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
"""
    
 
# pattern  20
# n=int(input())
# space=2*(n-1)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
    
#     for j in range(space):
#         print(" ",end=' ')
    
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()
#     space-=2

# output 

"""
4

1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1 

"""

# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         ch=chr(ord('A')+j)
#         print(ch,end=' ')
#     print()

"""
5
 
A 
A B 
A B C 
A B C D 
A B C D E 

# """
# n=int(input())
# for i in range(n):
#     for j in range(n-i):
#         ch=chr(ord('A')+j)
#         print(ch,end=' ')
#     print()

""""
5

A B C D E 
A B C D 
A B C 
A B 
A 

"""


# n=int(input())
# for i in range(n):
#     for j in range(n-i):
#         ch=chr(ord('A')+i)
#         print(ch,end=' ')
#     print()


# n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         ch=chr(ord('A')+i)
#         print(ch,end=' ')
#     print()

"""
5

A A A A A 
B B B B 
C C C 
D D 
E 
----
5

A 
B B 
C C C 
D D D D 
E E E E E 

"""

# n=int(input())
# for i in range(n):
#     for ch in range(ord('E')-i, ord('E')+1):
#         print(chr(ch),end=' ')
#     print()
    
"""
5

E 
D E 
C D E 
B C D E 
A B C D E 

"""

# n=int(input())
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=' ')
#     breakPoint=(2*i+1)/2
#     ch='A'
#     for j in range(2*i+1):
#         print(ch,end=' ')
#         if j<breakPoint:
#             ch=chr(ord(ch)+1)
#         else:
#             ch=chr(ord(ch)-1)
#     for j in range(n-i-1):
#         print(" ",end=' ')
#     print()
    
""""

5

        A         
      A B C       
    A B C D C     
  A B C D E D C   
A B C D E F E D C 

""""

