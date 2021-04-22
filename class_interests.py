pt_class = ["Kim", "Allison", "Chris", "Tijuan", "Beyoncé"]
my_greeting = {"French": "Bon soir",
                "English": "Good evening",
                "Japanese": "Konban wa"}

my_language = "English"

def greet(group, greeting, language):
    for person in group:
        if language == "French":
            print(f'{person}, bon soir, how are you?')
        elif language == "English":
            print(f'{person}, good evening, how are you?')
        elif language == "Japanese":
            print(f'{person}, konban wa, how are you?')
        else:
            print("I need more information")

def add_member_to_class(group, student):
    group.append(student)
    return group



greet(pt_class, my_greeting, my_language)
bigger_class = add_member_to_class(pt_class, "Ewan McGregor")
greet(bigger_class, my_greeting, my_language)
