"""

import recipes.flavours

print(recipes.flavours.elachai_chai)
print(recipes.flavours.ginger_chai)

"""


"""


from recipes.flavours import elachai_chai, ginger_chai


print(elachai_chai())
print(ginger_chai())

"""


from .recipes.flavours import elachai_chai as elachai, ginger_chai as ginger


print(elachai())
print(ginger())