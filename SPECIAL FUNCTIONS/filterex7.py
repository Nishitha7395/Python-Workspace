#filterex7.py
print("Enter the Line of Text seperate by space:")
lst=[str(x) for x in input().split()]
print("-"*50)
print("Original Elements of list:{}".format(lst))
print("-"*50)
vowels=list(filter(lambda n: n in 'aeiou',lst))
print("Vowels in the given line of text={}".format(vowels))
print(vowels)

