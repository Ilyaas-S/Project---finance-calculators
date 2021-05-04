import math 

#Display a menue for the user to decide from 
print("Choose either 'Investment' or 'bond' from the menu below to proceed:") 
print("Investment - to calculate the amount of interest you will earn on interest") 
print("bond - to calculate the amount you will have to pay on a home loan")

menu = input("-")
#if the user chooses investment
if menu == "Investment".lower() or menu == "Investment".upper():

#collect the data needed to use in the investment calculations
  deposit = int(input("Please enter the amount of money you will Deposit: ")) 
  interest_rate = float(input("Enter the interest rate(%), as a number:"))
  num_years = int(input("The number of years you are going to invest:"))
  interest = input("Would you like 'simple' or 'compound' interest: ")
  
  #if the user wants it in simple interest
  if interest == "simple":                                                              #if the user chooses simple interest
   simple_interest = deposit*(1 + interest_rate*num_years)                              #simple interest formula
   print("The Investment amount is: " + "R", round(simple_interest, 2))
   
  #if the user wants it in compound interest
  elif interest == "compound":                                                          #if the user chooses compound interest
    compound_interest = deposit*math.pow((1 + interest_rate), num_years)                #compound interest formula
    print("Amount = " + "R", round(compound_interest, 2))
    
    print("Thank you")

#if the user chooses bond
#collect data needed to perform calculations  
elif menu == "bond".lower() or menu == "bond".upper():
  house_value = float(input("Please enter the current value of your house:"))
  interest_rate = float(input("Enter the interst rate%, as a number:"))
  num_months = int(input("Enter the amount of months you would like to repay the Bond: "))
 
  repayment = (interest_rate*house_value)/(1 - (1 + interest_rate)**(-num_months))    #monthly repayment formula
  print("Your monthly repayment = " "R", round(repayment, 2))

  print("Thank you")
#if the user might incorrectly spell bond or investment, let the user know to retry
else:
 print("PLease Retry and make sure the spelling is correct as 'investment' or 'bond'. ")
