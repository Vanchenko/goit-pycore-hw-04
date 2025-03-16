from colorama import Fore, init, Style

init(autoreset=True)
# парсер команд бота
def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except ValueError:
        return "", []
# функція додавання контакта
def add_contact(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError(Fore.RED + "Two arguments are required (name and phone)." + Style.RESET_ALL)
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return print(Fore.RED + f"Error adding contact: {type(e).__name__}, {e}" + Style.RESET_ALL)

# функція видачі всіх контактів зі словника
def get_all_contacts(contacts: dict):
    if not contacts:
        return print(Fore.RED + "Contacts are empty"+ Style.RESET_ALL)
    else:
        output = "Contacts:"
        for name, phone in contacts.items():
            output += f"\n{name}: {phone}"
        return output

# функція видачі одного контакту зі словника
def get_contact(args: list, contacts: dict):
    try:
        if len(args) != 1:
            raise ValueError(Fore.RED + "Argument (name) is required." + Style.RESET_ALL)
        name = args[0]
        if name not in contacts:
            return print(Fore.RED + "Contact does not exist" + Style.RESET_ALL)
        return contacts[name]
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return print(Fore.RED + f"Error getting contact: {type(e).__name__}, {e}" + Style.RESET_ALL)

# функція зміни телефону у одного контакту зі словника
def change_contact(args: list, contacts: dict) -> str:
    try:
        if len(args) != 2:
            raise ValueError(Fore.RED + "Two arguments are required (name and phone)." + Style.RESET_ALL)
        name, phone = args
        if name not in contacts:
            return "Contact does not exist"
        contacts[name] = phone
        return "Contact updated."
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return print(Fore.RED + f"Error changing contact: {type(e).__name__}, {e}" + Style.RESET_ALL)

# головна функція боту
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    # довічний цикл
    while True:
        # ввод команди Користувачем
        user_input = input(Fore.GREEN + "Enter a command: " + Style.RESET_ALL)
        command, *args = parse_input(user_input)
        # аналіз введеної команди і виклик відповідної функції
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(Fore.YELLOW + add_contact(args, contacts) + Style.RESET_ALL)
        elif command == "all":
            print(Fore.YELLOW + get_all_contacts(contacts) + Style.RESET_ALL)
        elif command == "phone":
            print(Fore.YELLOW + get_contact(args, contacts) + Style.RESET_ALL)
        elif command == "change":
            print(Fore.YELLOW + change_contact(args, contacts) + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid command." + Style.RESET_ALL)

# перевірка точки "входу" і запуск бота
if __name__ == "__main__":
    main()