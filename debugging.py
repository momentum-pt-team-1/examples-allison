def add_underscores(word):
    new_word = '_'
    for i in range(len(word)):
        # breakpoint()
        print(f'new_word = {new_word}')
        print(f'i = {i}')
        new_word += word[i] + "_"
    return new_word

# ******************************
our_word = "hello"

# print(add_underscores(our_word))

def show_people_in_class():
    class_list = []
    done = "NO"
    while done == "NO" and len(class_list) < 5:
        person = input("Name a person in the class ")
        done = input("Are you finished? Type 'NO' if not. ")
        class_list.append(person)

    for person in class_list:
        print(person)

show_people_in_class()
        

'''1. Guess which section of the code has the bug
2. Use breakpoint() (formerly pdb.set_trace()) to pause the code and inspect it
- Python shell
- n -> next - one line at a time
- c -> continue - until the next breakpoint()
- quit()
3. Make the necessary changes
4. Rinse and repeat as necessary'''