import math


print(''' Investment : to calculate the amount of interest you'll earn in your investment

        Bond : to calculate the amount you'll have to pay on a home loan
        
        Enter either 'Investment' or 'bond' from the menu below to proceed:\n ''')

#Input from user select Investment 

invest_or_bond = input(str("Please enter Investment or Bond\n" )).lower()

if invest_or_bond  == "investment":
    
        #ask the amount of deposition
        p = float(input("How much are you depositing?\n")) 
        
        #ask at which interest rate percentile
        r = float(input("At which interest rate percentile?\n" )) 
        r = (r/100)    
        
        #ask in how many years is the investing plan
        t = float(input("How many years are you planning to invest for? \n"))  
        simple_compound= str(input("Choose 'Simple_compound' or 'Compound' interest. \n")).lower() 
        
        if simple_compound== "simple":
            
            simple_compound = p*(1 + r * t) #variable name changed
            
            print (f"Your interest earned over years will be {simple_compound} ".format())
        else :
            simple_compound = p*math.pow((1+r),t) #variable name changed
            
            print (f"Your interest earned over years will be {simple_compound}".format()) 

#Bond is another conditional select bond
elif invest_or_bond == "bond":
    
        #ask what is the current value of the house in case of bond
        p = float(input("What is the current value of the house?\n"))
         
        #ask what is the interest rate percentile
        i = float(input("At which interest rate percentile?\n" )) 
        i = (i/100)/12
        
        #ask in how many month to refund
        n = float(input("How many months you plan to repay? \n")) 
        monthly = float(math.floor((i*p)/(1 - (1+i)**(-n)))) 
        print(f"Your monthly repayment will be {monthly}".format())

else:
    print("Please enter a valid input. Try again.") 


