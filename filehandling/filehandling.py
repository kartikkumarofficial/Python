
# f = open('mytext.txt','r')
# reads as string 
# text = f.read()
# print(text)

with open('mytext.txt','w+') as f2:
    print(f2.readlines()) 
# reads as list 


# seek function 
    f2.seek(5)
    # makes the initial cursor/starting point  in the file at 5th index
    print(f2.read(5))
    # tells the current index
    print(f2.tell())
    # making the file limited to a certain size limit that is trunking it  ( actually changes content)
    f2.truncate(5)