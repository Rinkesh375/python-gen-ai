"""

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elachi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}



data = {
item  for value in recipes.values()
 for item in value 

    
}


print(data)

"""





"""

students = {
    "Rinkesh": ["Python", "JavaScript"],
    "Nitish": ["Java", "Python"],
    "Manish": ["React", "JavaScript"]
}

subjects = {
    subject
    for subject_list in students.values()
    for subject in subject_list
}

print(subjects)

"""
