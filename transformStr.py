def transformStr(Str):

 if len(Str)>5:
    if Str[0]=="L"  or Str[0]=="l": 
       print (str.lower(Str[:5] +"..."))
    if Str[0]=="U"  or Str[0]=="u":
        print (str.upper(Str[:5] +"..."))
    else: print (Str[:5] +"...")
 if len(Str)<=5:
    if Str[0]=="L" or Str[0]=="l":
       print (str.lower(Str))
    if Str[0]=="U" or Str[0]=="u":
       print (str.upper(Str))
    else: print (Str)


transformStr ("uio") 
transformStr ("uiopasd")
transformStr ("dfg")
transformStr ("dfghjkl")
transformStr ("Lzx")
transformStr ("Lzxcvbnm")
