from replit import clear
from art import logo
print(logo)

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}    
def calculator():
    num_1=float(input("Enter the 1st number = "))

    for symbol in operation:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol=="+" or operation_symbol=="-" or operation_symbol=="*" or operation_symbol=="/" : 
            num_2 = float(input("What's the 2nd number?: "))
            calculation_function = operation[operation_symbol]
            answer=calculation_function(num1=num_1,num2=num_2)
            print(f"{num_1} {operation_symbol} {num_2} = {answer}")
            user_choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or Type 's' to stop the calculation: ").lower()
            if  user_choice== 'y':
                num_1 = answer
            elif user_choice =='n':
                should_continue = False
                clear()
                print(logo)
                calculator()
            elif user_choice =='s':
                should_continue = False
            else:
                print("Invalid choice.")
                should_continue = False    
        else:
            print("Invalid Operation.")
            should_continue=False   

calculator()