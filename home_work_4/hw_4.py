def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None: 
                return "Contact not found."
            return result
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return "Give me name and phone please"
        except IndexError:
            return "Enter the argument for the command."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise ValueError("Contact does not exist.")
    contacts[name] = phone
    return "Contact updated successfully"

@input_error
def show_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    
def all_contacts(contacts):
    for name, phone in contacts.items():
        print(f"Name: {name}, Phone: {phone}")
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_contact(args, contacts))   
        elif command == "all": 
            all_contacts(contacts)             
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
