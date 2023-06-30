import math


#print("first commit")


the_world_python3 = True
if the_world_python3:
    print("hogehoge")
    
num = "1"
name = "yuta"

new_num = int(num)

print(num,type(num))
print(new_num,type(new_num))

#sep=","で区切る
print("hi","yuta",sep=",",end=".\n")

#end=""はデフォルトで改行
print("hi","yuta",sep=",",end="\n")
print("---------------------------------")

result = math.sqrt(25)
print(result,type(result),end=".\n")


print("""
    line1
    line2
    line3
""" )

print("my name is {0} {1}" .format("yuta","matsui"))