# PROGRAM: Window Quotes
# AUTHOR: Robert Depweg
# DESCRIPTION:
# INPUT: The number of buildings and number of windows for said buildings
# OUTPUT: The individual cost for each building's windows, the total cost, 
#         as well as a thank you message.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\033c")                 # Clear Terminal

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - CONSTANT DECLARATIONS
CALL_FEE: float = 10.00              # The fee added onto every order
FIRST_5_FEE: float = 2.00            # Fee for windows 1 through 5
NEXT_5_FEE: float = 1.50             # Fee for windows 6 through 10
ADDITIONAL_FEE: float = 1.00         # Fee after ten windows
FIVE_WINDOWS: int = 5                # Amount of five windows
TEN_WINDOWS: int = 10                # Amount of ten windows

#  - - - - - - - - - - - - - - - - - - - - - - - - - -  VARIABLE INITIALIZATION
building_num: int = 0                # Number of buildings to be quoted
total_cost: float = 0.0              # Accumulated total of quotes
quote: float = 0.0                   # Individual quote cost           
number_of_windows: int = 0           # Num windows in an individual building
windows_left: int = 0                # Temp var for calculations

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - INPUT
# Gets number of buildings to be quoted from user
building_num = int(input(f'How many buildings do you ' +
                         'want to generate quotes for? '))
print()

# The building loop tracks each building's amount of windows
for buildings in range(1,building_num+1):
    number_of_windows = int(input(f'How many windows to be '+
                                  'cleaned in building {buildings}: '))
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  CALCULATIONS
    # Quote amount resets after each loop
    quote = 0
    
    # For each window, the amount is added based on what number the
    # window is through the if-elif-else loop
    for windows_left in range(1,number_of_windows+1):
        if windows_left <= FIVE_WINDOWS:
            quote += FIRST_5_FEE # For windows 1 through 5
        elif windows_left > FIVE_WINDOWS and windows_left <= TEN_WINDOWS:
            quote += NEXT_5_FEE # For windows 6 through 10
        else: 
            quote += ADDITIONAL_FEE # For windows after 10
    
    # After the for statement is finished, the call fee is added
    # to the quote, which is then added to the overall total
    quote += CALL_FEE
    print(f'Your quote for building {buildings}: {"$"}{quote:,.2f}')
    print()
    total_cost += quote

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  OUTPUT
print(f'Your total cost will be: {"$"}{total_cost:,.2f}')
print()
print(f'Thank you for your business!')
 

