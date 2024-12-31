import ecommerce
from ecommerce import shipping # Importing the package
from ecommerce.shipping import calc_shipping # Importing the function only from the package
from ecommerce import shipping as sh # Importing the package as an alias

ecommerce.shipping.calc_shipping()  # Calling the function from the package

shipping.calc_shipping()  # Calling the function from the package

calc_shipping()  # Calling the function from the package

sh.calc_shipping()  # Calling the function from the package