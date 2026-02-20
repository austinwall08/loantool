import os 


def loantool() :
    idx = 10
    while idx > 0 :
        print(idx)
        idx = idx-1

  
   

# loantool()
def loan_data() :
    prin = input("What is the principal for your loan?")

    rate = input("What is the rate of Intrest?")

    term = input("How long is the loan for?")

    return(prin, rate, term)


   
    

data = list(loan_data())
print(data)
    


# for d in data   


    
# obj - determine which payment method would save most money and gain most back, 
# Step 1 - input principal, intrest, term, Step 2 - calculate monthly payment plus intrest needing to be paid, Step 3 - 
