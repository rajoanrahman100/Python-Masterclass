import converter # Importing the module
import utils # Importing the module

from converter import lbs_to_kg # Importing the function only from the module

print(f"{lbs_to_kg(100):.2f}") # Calling the function from the module

print(converter.kg_to_lbs(100)) # Calling the function from the module

maxNumber=utils.find_max_number([1,2,3,4,5,6,7,8,9,10])
print(f"The final Output {maxNumber}")