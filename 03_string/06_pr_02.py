letter = '''Dear <|NAME|>,
Greeting to ABS House, I am happy to tell you about your selection
you are selected!
have a great day ahead!
Thanks and regards,
Bill

Date: <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter  Date\n")
letter=letter.replace("|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)