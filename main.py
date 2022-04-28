print("------ WELCOME TO MORCE CODER! -------")
text=input("type anything : ").lower()

#convert the text to morce code
letters={'a':'.-','b':'-..','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',' ':'/',}


#between letter I made space two times and between words is "/"
morce_code=""
for l in text:
    morce_code+="  "+letters[l] 

print(f"the morce code of your message is:{morce_code}")              
