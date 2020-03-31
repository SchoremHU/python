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

# for i in range(-3,4):
#     if i < 0:
#         pro = -i
#     else:
#         pro = i
#     print(' '*pro + '*'*(7-pro*2))

# for k in range(-3,4):
#     if k < 0:
#         print(' '*(-k)+'*'*(4+k))
#     elif k > 0:
#         print(' '*3+'*'*(4-k))
#     else:
#         print('*'*7)


# 100以内斐波那契数列
            # x = (x-1)+(x-2) , x>=1
# x = 0
# y = 1
# print (0)
# print (1)
# while True:
#     k = x+y
#     if k > 100:break
#     x = y
#     y = k
#     print(k)

# 第101项斐波那契数列
# x = 0
# y = 1
# z = 1
# print (0)
# print (1)
# while True:
#     k = x + y
#     z += 1
#     if z == 102:break
#     x = y
#     y = k
#     print(k,z)


# 10万内质数
    # 10以内质数，步骤记录分析
y = 2 #为了打印出出事 y 值
for x in range(2,10,1):
    print('__________')
    print('x:',x,'y:',y)
    for y in range(2,x,1):  #此时跳过次循环，直接打印 x2- ，range（2,2,1）为合法的空的迭代器
        print ('**** x1',x , y)
        print('****', x % y == 0)
        if x % y == 0:
            break #用 x1 依次对 y 内的所有数取模，直到满足条件跳过并进入else打印x2-，否则进入 for y 循环
    else: print('x2-',x)