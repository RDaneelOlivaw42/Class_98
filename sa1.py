# 1
# f = open("test.txt")
# fileLines = f.readlines()
# print(fileLines)

# for line in fileLines:
#     print(line)


# 2
# intoString = "My name is Yoshikage Kira. I am 33 years old."
# words = intoString.split(' ')
# print(words)


# 3
# def greet (name) :
#     print("Hello", name, ". Very nice to see ye.")

# greet("Raskolnikov")


# 4
def count_words ():
    ask = input("Hello, give me a file name ")
    file_source = open(ask)
    file_content = file_source.readlines()
    number_of_words = 0
    
    for line in file_content: 
        words = line.split(' ')
        number_of_words = number_of_words + len(words)
        
    print("Number of words are", number_of_words)
        

count_words()