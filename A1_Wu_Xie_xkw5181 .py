"""
Full Name: Xie Wu          Bowen Wu        Ran Hao
ID:        948858339       997668725       926758299
Date:      02/13/2022
Filename:  A1_Wu_Xie_xkw5181.py
Purpose:   1. to practice with the constructs learned so far which includes functions,
              iterations, conditionals, and list
           2. collaborate and communicate within teams -- one of the successful
              measure of this indicator is performance itself
           3. understand the difference between a number and an string
"""

#Containing functionality: creates a list and returns an empty list.
#Explaination: create an empty list in function and return it.
#Precondition and postcondition: The input is empty and the output is an empty list.
#Fail condition: If we put a parameter in the input, it will fail.
def create_list():
    mylist = []
    return mylist


#Containing functionality: prints the entire list on one line.
#Explaination: return the list directly to get one line
#Precondition and postcondition: The input is a list and the output is entire list on one line.
#Fail condition: If we put other types but not list, it will fail.
def print_list(list1):
    return list1


#Containing functionality: prints the elements of the list one by one
#Explaination: use a while loop to pritn every elements of the list
#Precondition and postcondition:The input is a list and the output is the elements of the list one by one.
#Fail condition: use other types but not list will fail.
def print_members(list2):
    i = 0
    while i < len(list2):
        print(list2[i])
        i = i + 1


#Containing functionality: creates another list, copy the elements of one list to new list, and return new list.
#Explaination: use a new variable and let it equal to parameter list to get a new list
#Precondition and postcondition: The input is a list and the output is a new list.
#Fail condition: use other types but not list will fail.
def copy(list3):
    mylist1 = list3
    return mylist1


#Containing functionality: creates a new list copy elements from 1st number to 2nd number.
#Explaination: write a for loop to add every number between number1 and number2 in to new list.
#Precondition and postcondition: The input are list and two number. The output is a list.
#Fail condition: when the enter is not a list and two int will fail
def copy_part(list4, number1, number2):
    list4 = []
    for i in range(number1, number2 + 1,1):
        list4 = list4 + [i]
    return list4


#Containing functionality: compares both list and return true if they have same elements returns false otherwise
#Explaination: check length of each list then check each element in lists.
#Precondition and postcondition: The input are two list and the output is a boolean value.
#Fail condition: if two parameters are not list type then it will fail
def is_equal(list5,list6):
    m = 0
    t = 0
    if len(list5) != len(list6):
        return False
    while m < len(list5):
        if list5[m] == list6[m]:
            m = m + 1
            t = t + 1
        else:
            m = m + 1
    if t == len(list5):
        return True
    else:
        return False



#Containing functionality: adds an element at the end of the list. The function returns the updated list.
#Explaination: using '+' operator to add an element to list
#Precondition and postcondition: The input are list and number. The output is a list.
#Fail condition: if the element is wrong type, it will fail.
def append(list7, element):
    mylist2 = [element]
    list7 = list7 + mylist2
    return list7


#Containing functionality: returns the number of elements with the specified value
#Explaination: use a for loop to count number.
#Precondition and postcondition: The input are a list and a item. The output the number of elements.
#Fail condition: if the item is not int will fail.
def count(list8,item):
    num = 0
    for i in list8:
        if i == item:
            num = num + 1
        else:
            num = num + 0
    return num


#Containing functionality: combines both lists and return combined list while keeping parameters unchanged.
#Explaination: Use "+" to add two list together get a new list.
#Precondition and postcondition: The input are two list. The output is a list
#Fail condition: if parameter is not list type will fail.
def extend(list9,list10):
    mylist3 = list9 + list10
    return mylist3


#Containing functionality: returns the index of the first element with the specified value
#Explaination: use for loop to get the index of number
#Precondition and postcondition: The input are list and number. The output is a number.
#Fail condition: if the num is not int type will fail
def index(list11, num):
    m = 0
    for i in list11:
        if i != num:
            m = m + 1
        else:
            return m


#Containing functionality: adds an element at the specified position indicated by index. This function returns the updated list.
#Explaination: use list identity to split list and add element to specific index
#Precondition and postcondition: The input is a list, an int, and an item. The output is a list.
#Fail condition: if the index is out of list12 range, it will fail.
def insert(list12, num, item):
    mylist4 = list12[:num]
    mylist5 = [item]
    mylist6 = list12[num:]
    list12 = mylist4 + mylist5 + mylist6
    return list12


#Containing functionality: removes the element at the specified position by replace with "null"
#Explaination: directly find the index in list and replace it with "null"
#Precondition and postcondition: The input is a list and a item. The output is a list.
#Fail condition: If the item is out of the lenth of list, it will fail.
def pop(list13, item):
    list13[item] = 'null'
    return list13


#Containing functionality: removes the first item with the specified value. This function returns the updated list.
#Explaination: Use while loop and if statement to split list and find the index of specified value then remove it.
#Precondition and postcondition: The input is a list and a item. The output is a list
#Fail condition: if the item is bot in the list then the function will return none
def remove(list14, item):
    i = 0
    while i < len(list14):
        if i+1 != item:
            i = i + 1
        else:
            mylist7 = list14[:i]
            mylist8 = list14[i+1:]
            list14 = mylist7 + mylist8
            return list14


#Containing functionality: creates a new list and reverses the order of the list
#Explaination: use variable to save first value then use variable to get the save value to get the reverse goal
#Precondition and postcondition: The input is a list. The output is also a list.
#Fail condition: if the parameter is not a list will fail
def reverse(list15):
    mylist9 = list15
    m = 0
    n = len(list15)-1
    while m < n:
        fix_first = mylist9[m]
        mylist9[m] = mylist9[n]
        mylist9[n] = fix_first
        m = m + 1
        n = n - 1
    return mylist9


#Containing functionality: creates a new list and return sorted list
#Explaination: use while loop and for loop to compare each element and sort value in list
#Precondition and postcondition: The input is a list and the output is a new list.
#Fail condition: if the parameter is not a list then it will fail
def sort(mylst):
    for i in range(1, len(mylst)):
        key = mylst[i]
        j = i - 1
        while j >=0 and key < mylst[j] :
            mylst[j+1] = mylst[j]
            j =j - 1
            mylst[j+1] = key
    return mylst



#Write a testing function test_mylist.
def test_mylist():
    print(create_list())
    print(print_list([1,2,3,4,5]))
    print_members([1,2,3,4,5])
    print(copy([1,2,3,4,5]))
    print(copy_part([1,2,3], 2, 10))
    print(is_equal([2,1,3,4,5],[1,2,4,3,5]))
    print(append([1,2,3,4,5], "psu"))
    print(count([1,2,3,4,1,1,1], 1))
    print(extend([1,2,3], [4,5,6]))
    print(index([2,3,1,4,5], 1))
    print(insert([1,2,3,4,5], 6, 6))
    print(pop([1,2,3,4,5], 3))
    print(remove([1,2,3,4,5], 3))
    print(reverse([1,2,3,4,5]))
    print(sort([-1,-3,0,1,-5,7,2,4]))
          

test_mylist()




































