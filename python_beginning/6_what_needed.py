
my_string = "There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch."

modified_string = my_string.split ("and")[1].split(".")[0].strip()

print(modified_string)






