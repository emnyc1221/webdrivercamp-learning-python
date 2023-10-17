#!/usr/bin/python3
my_string = "Webdriver Awesome Camp"
current_word = ""
for char in my_string:
    if char == " ":
        print(current_word)
        current_word = ""
    else:
        current_word += char
print(current_word)




