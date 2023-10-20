#!/usr/bin/python3

text = "There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch."

sliced_text1 = text[26:44]
sliced_text2 = text[56:59]
var_name = "unless"
sliced_var_name = var_name[0:6]
result = sliced_text1 + " " + sliced_text2 + " " + sliced_var_name

print(result)
