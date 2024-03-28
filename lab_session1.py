######################list comprehension#######################
list1 = [1, -1, 3, -5]

list2 = [1, 0, 3, 0]
modified_list2 = [-1 if x == 0 else x for x in list2]

list3 = ["a","b","C","d"]
modified_list3 = [char.upper() if char.islower() else char for char in list3]

list4 = [i for i in range(1,11)]
modified_list4 = [x**2 for x in list4]

list5 = [ [], [0,1,2], [], [3,6,7,21] ]
modified_list5 = [list for list in list5 if len(list) > 0]

list6 = ['Hello', 'Me']
modified_list6 = [(word,len(word)) for word in list6]

list7 = [10, 1, 2, 100, 200, 909]
modified_list7 = [0 if '0' == str(n)[-1] else n for n in list7]
# [0 if x % 10 == 0 else x for x in list7]

a = ["apple", "pie"]
b = [6, 7, 8, 9, 10]
modified_list8 =[(fruit, number) for fruit in a for number in b]
#原来两个for直接前后并列即可

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
modified_list9 = [(a[i], b[i]) for i in range(len(a))]
######################list comprehension#######################

######################Filter and Lambda########################
#Write a lambda function that increments its argument by one.
increment = lambda x: x + 1

#Write a lambda function that returns the sum of its two arguments.
sum_up = lambda x,y: x+y

#Write a lambda function that returns the square root of its argument.
square = lambda x: x**2

#Write a lambda function that takes two arguments and returns the minimum
minimum = lambda x,y: x if x < y else y


#Write a lambda function that returns the result of the expression x2 + 2x − 5 where x is its argument.
expression = lambda x: x**2 +2*x -5

#Use filter() to find intersection of the two lists: a=[1,2,3,5,7,9], b = [2,3,5,6,7,8].
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
intersection = list(filter(lambda x: x in b, a))
#Write a program using lambda and filter which prints out all the even number between 1 and 20 (both included).
def even_num():
    return list(filter(lambda x:x%2 ==0, range(1,21)))
#Write a program using lambda and filter which prints out only the positive numbers of the list: a = [-5,8,1,-3,10,-9]. Write the same using list comprehensions.
def positive_num():
    a = [-5, 8, 1, -3, 10, -9]
    return list(filter(lambda x:x>0, a))

a = [-5, 8, 1, -3, 10, -9]
modified_a = [i for i in a if i > 0]



if __name__ == '__main__':
    print([abs(i) for i in list1])
    print([i for i in list1 if i > 0])
    print(modified_list2)
    print(modified_list3)
    print(modified_list4)
    print(modified_list5)
    print(modified_list6)
    print(modified_list7)
    print(modified_list8)
    print(modified_list9)
    print(increment(5))
    print(sum_up(3,2))
    print(square(8))
    print(minimum(4,9))
    print(expression(9))
    print(intersection)
    print(even_num())
    print(positive_num())
    print(modified_a)

