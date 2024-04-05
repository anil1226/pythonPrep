text = "hello"
print(text)
text2 = "world"
print(text + text2)
print(len(text))
print(text.upper())
text3 = text.replace("o","o world")
print(text3)
text4 = " anil k "
text4Split = text4.split(" ")
print(text4Split)
print(text4.strip())
text5 = "k"
if text5 in text4:
    print("found in text")