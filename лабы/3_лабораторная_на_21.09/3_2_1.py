text = input("введите текст: ") # пользователь клацает на клавиатурке
with open("user_input.txt", 'w', encoding='utf-8') as f: # открываем файл функцией, которая сразу по окончании закроет файлик
    # (чтобы не вешать оперативку) на запись и используем кодировку utf-8,
    # потому что пользователь наверняка патриот и будет вводить текст на русском
    f.write(text) # стандартная запись в файл (с 1-ой позиции) определенного набора символов

