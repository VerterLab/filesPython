# Справочник
def add_contact():
    last_name, first_name, second_name = '', '', ''
    with open(file_contact, 'a') as data:
        while last_name == '':
            last_name = input('Введите фамилию:- ')
        while first_name == '':
            first_name = input('Введите имя:- ')
        while second_name == '':
            second_name = input('Введите отчество:-')
        phone_number = input('Введите номер телефона:- ')
        if phone_number == '':
            phone_number = 'none'

        contact = f'{last_name} {first_name} {second_name} {phone_number}\n'
        data.write(contact)
        print('Контакт добавлен')


def found_contact():
    count_contact = 0
    with open(file_contact, 'r') as data:
        found_contact = input('Введите значение: ')
        if found_contact == '':
            print('Вы ничего не ввели')
            return None
        for line in data:
            line_f = line .split()
            # print(line_f[0])
            if found_contact == line_f[0] or found_contact == line_f[1] or \
                    found_contact == line_f[2] or found_contact == line_f[3]:
                count_contact += 1
                print(line)
        if count_contact == 0:
            print('Контакт не найден')


def read_contact():
    with open(file_contact, 'r') as data:
        for line in data:
            print(line)


def copy_contact():
    with open(file_contact, 'r') as data:
        # print('Введите номер контакта: ')
        numb_contact = int(input('Введите номер контакта:- '))
        if numb_contact == '':
            print('номер не введён :(')
            return None
        count_str = 0
        for line in data:
            # line_f = line.split()
            if count_str == numb_contact-1:
                with open(file_copy, 'a') as data:
                    data.write(line)
                    print('Контакт добавлен в избранное')
            count_str += 1
        if count_str <= numb_contact:
            print('Номер превышает количество контактав')


file_contact = 'contact.txt'
file_copy = 'favorites_contact.txt'

print()
print('                   Телефонный справочник')
print()

type_menu = ''
while type_menu != 'r' and type_menu != 'a' and \
        type_menu != 'f' and type_menu != 'q':
    print(
        'Просмотр - "r"    Поиск - "f"    Добавить контакт - "a"  '
        'Копировать в избранное - "c"  Выход - "q"'
    )
    type_menu = input('Выбирете пункт меню: ')
    if type_menu == 'r':
        print(' Фамилия    Имя    Отчество    Телефон')
        read_contact()
    elif type_menu == 'a':
        add_contact()
    elif type_menu == 'f':
        print(' Фамилия    Имя    Отчество    Телефон')
        found_contact()
    elif type_menu == 'c':
        copy_contact()
    elif type_menu == 'q':
        quit()
    type_menu = ''
