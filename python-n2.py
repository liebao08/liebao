x = 4
if x == 5:
    print("yes")
else:
    print("no")

num = 7
if num == 5:
    print("number is 5")
else:
    if num == 11:
        print ("numbers is 11")
    else:
        if num == 7:
            print("Number is 11")
        else:
            print("Number isn't 5,11 or 7")

print(1 == 1 and 2 == 2)

print(1 == 1 and 2 == 3)

print(1 != 1 and 2 == 2)

print(2 < 1 and 3> 6)

print(1 == 1 or 2 == 2)

print(1 == 1 or 2 == 3)

print(1 != 1 or 2 == 2)

print(2 < 1 or 3> 6)

print(not 1 == 1)
print(not 1 > 7)

print(False == False or True)
print(False == (False or True))
print((False == False) or True)

#i = 1

#while 1 <5:
#    print(i)
#    i = i + 1
    
#print("Finished!")

#while 1 == 1:
#    print("in the loop")

e = 0
while 1==1:
    print(e)
    e = e + 1
    if e >= 5:
        print("Breaking")
        break
    
print("Finished")

nums = [7,7,7,7,7]
nums[2] = 5
print(nums)

number = [1,2,3]
print(number +[4,5,6])
print(number * 3)

words = ["spam","egg","spam","sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

numb = [1,2,3]
print(not 4 in numb)
print(4 not in numb)
print(not 3 in numb)
print(3 not in numb)

numero = [1,2,3]
numero.append(4)
print(numero)
numero.append([5,6])
print(numero)

list = ['a','b','c',123,456]#per mettere le lettere ci devono essere ''
print(list)
print(list[0])
list2 = []
print(list2)

list3 = ['a','b',['abc',2,3,4],'c']
print(list3)
print(list3[2][0])

list4 = [1,2,3,4]
list4[2] = 10
print(list4)
print("---------------------------------------")
list5 = [1,2,3]
print(list5+[4,5,6])
print(list5*2)

list6 = [1,2,3,4,5,6,7,'a','b','c']
print(len(list6))

list7 = [1,2,3,4]
list7.insert(2,100)
print(list7)

list8 = [1,2,3,4]
print(list8.index(2))#primo numero vuol dire che:che numero vuoi cercare
print(list8.index(2,1))#secondo numero da quale posto vuo cominciare a cercare

list9 = [1,2,3,4,5,2]
print(max(list9))
print(min(list9))
print(list9.count(2))
list9.remove(3)
print(list9)
list9.reverse()
print(list)