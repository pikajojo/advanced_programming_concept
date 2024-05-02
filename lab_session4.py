import numpy as np
from functools import reduce

##########Mapping############
data = [np.random.randint(0,11) for i in range(10)]
result = [2 * i for i in data]
func = lambda x: 2*x
result2 = map(func, data)

data3 =[1,2,3,4,5,6,7,8,9,10]
result_square = map(lambda x: x**2, data3)
data4 = [i for i in range(0,21)]
data_4 = list(range(0,21))
result_square2 = map(lambda x: x**2, data4)

########Filtering#############
result3 = [i for i in data if i < 10]
result4 = filter(lambda x: x <10, data)
result_even = filter(lambda x: x%2 ==0, data3)
result_even2 = filter(lambda x: x%2 ==0, data4)

########Combined Mapping and Filtering#############
result5 = [2 * i for i in data if i<10]

result6 = map(lambda x: 2*x, filter(lambda x:x<10, data))
result6 = list(result6)

result_even_square = map(lambda x: x**2, filter(lambda x: x%2 ==0, data3))
result_even_square2 = map(lambda x: x**2, filter(lambda x: x%2 ==0, data4))


########Combined data and data2####################
data2 = [np.random.randint(0, 11) for _ in range(10)]
result7 = [(i, j) for i in data for j in data2]

#zip function
result8 = [(i, j) for i, j in zip(data, data2)]


########Reducing#############
#reduce needs 3 element, but the last one can be None
result9 = reduce(lambda x,y: x+y, data, 0)

#use reduce to calculate the 2 times the list
result10 = reduce(lambda x,y: x+[2*y], data, [])


#######################################
def find_longest_word(word_list):
    max_length = 0
    longest_word = None
    for word in word_list:
        if len(word)>max_length:
            longest_word = word
            max_length = len(word)
    return longest_word

def filter_long_words(words_list, n):
    return list(filter(lambda x: len(x)>n, words_list))

dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar" }
def translate(English_words, dict):
    return list(map(lambda word:dict.get(word,"unknown"), English_words))

def max_in_list(numbers):
    return reduce(lambda x,y: max(x,y), numbers)





def Reduce_2(func, data, init = None):
    if (arg1:= init) is None:
        arg1 = data[0]
        data = data[1:]

    for i, arg2 in enumerate(data):
        print(f"loop count {i}")
        print(f"tList:{data[i:]}")

        print(f"targ1: {arg1}")
        print(f"targ2: {arg2}")

        arg1 = func(arg1, arg2)
        print(f"the result is {arg1}")















if __name__ == "__main__":
    print(data)
    print(list(result2))
#ps. for map object, we need to cast it into list
    print(f"filtering the data for values under 10:{result3}")
    print(f"filtering the data for values under 10:{list(result4)}")
#ps. for filter object, we also need to cast it into list
    print(f"2 times the filtered data under 10:{result5}")
    print(f"2 times the filtered data under 10:{result6}")
    print(data2)
    print(result8)
    print(f"the reduction of data using sum is:{result9}")
    print(f"the reduction of data using 2 * list is:{result10}")
    english_words = ["merry", "christmas", "and", "happy", "new", "year"]
    swedish_words = translate(english_words, dict)
    print("Swedish translation:", swedish_words)
    print(f"max in list: {max_in_list([22,33,44,55,66,11])}")

