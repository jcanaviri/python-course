black_hair = {'John', 'Mary', 'Susan'}
blonde_hair = {'Dave', 'Eva', 'Jennifer'}
brown_eyes = {'Mary', 'Eva'}
less_than_30 = {'John', 'Mary', 'Dave'}

# Union all brown eyes and blonde hair
print(brown_eyes.union(blonde_hair))

# Intersection brown eyes and blonde black_hair
print(brown_eyes.intersection(blonde_hair))

# Difference black hair without brown eyes
print(black_hair.difference(brown_eyes))

# Symmetric difference black hairn or bronw eyes, but no both
print(black_hair.symmetric_difference(brown_eyes))
