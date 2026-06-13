name = []
name1 = input("Enter the palindrome name: ")

copy_name1 = name1
copy_name1.reverse()

if (copy_name1 == name1):
    print("the name is a palindrome name")
elif copy_name1 != name1 :
    print ("the name is not a palindrome ")
    