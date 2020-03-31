# for i in range (1,10):
#     for j in range (1,i+1):
#         print(str(j)+'*'+str(i)+'='+str(i*j)+'\t',end='')
#     print()
# for i in range (1,10):
#     line =''
#     for j in range (1,i+1):
#         line += '{}*{}={:<4}'.format(j,i,i*j)
#     print(line)
# for i in range (1,10):
#     for j in range (1,i+1):
#         pro = i*j 
#         if j > 1 and pro < 10:
#             pro = str(pro)+' '
#         else:
#             pro = str(pro)

#         print(str(j)+'*'+str(i)+'='+pro,end=' ')
#     print()

# for i in range(1,10):
#     line = ''
#     for j in range(1,10):
#         if i > j:
#             line = '{} {} {:<4}'.format(' ',' ',' ')
#         else:
#             line = '{}*{}={:<4}'.format(i,j,i*j)
#         print (line,end=' ')
#     print()

for i in range(-3,4):
    if i < 0:
        pro = -i
    else:
        pro = i
    print(' '*pro + '*'*(7-pro*2))

for k in range(-3,4):
    if k < 0:
        print(' '*(-k)+'*'*(4+k))
    elif k > 0:
        print(' '*3+'*'*(4-k))
    else:
        print('*'*7)