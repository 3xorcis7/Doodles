print("Check you are not robot (For Safe)")
print("Question 1: 12+4-6:2=?")
check = int(input("Enter your answer:"))
if check== 13:
  print("Checked!")
  print("        Hello ,there")
  print("    Which do you want to upgrade")
  print("""        1.Update App /JUST UPDATED/
        2.Update Driver /MOST CHOICE/
        3.Update Software /No2 PROTECTOR/
        4.Update Your Brain /HOT/
        5.Enter Error Code /NEWEST/
         """)
  choice = int(input("      Enter your choice"))
  while(1):
  
    if choice == 1 :
      print("Checking for update...")
      print("Updated : Ver 1.05")
      choice = int(input("          Enter your choice again"))
  
    elif choice == 2 :
      print("Uppdatig....")
      print("ErrorCode= 303")
      print("Please enter this code in Feedback tab")
      choice = int(input("          Enter your choice again"))
    elif choice == 3 :
      print("...")
      print("Scanning.")
      n= 52632
      print('Number of scanned file(s)    :',n)
      print("Powered by BKAV-No1 Protector in Vietnam \n Thank you for use our app!")
      choice = int(input("          Enter your choice again"))
    elif choice == 4 :
      print("...")
      print("Go to the hospitallllllllll!")
      break
    elif choice == 5 :
      print("Enter your error code (If you see)")
      code = int(input("Code:"))
      print("10Q!!! We will fix that bug soon as we can!")
      choice = int(input("          Enter your choice again"))
    else :
      print("Invalid!")
      break
else :
    print("Wrong Answer! ")
    print("Try Again")
    
      