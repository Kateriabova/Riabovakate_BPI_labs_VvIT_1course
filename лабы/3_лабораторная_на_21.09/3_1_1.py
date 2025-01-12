with open("example.txt", 'w') as f: # открытие файла (его создание) на запись
    # с конструкцией, которая после выполнения задачи заакроет файл.
    f.write("Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. \n")
    f.write("They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.")
    # запись в файл (c первого знака) первого абзаца Гарри Поттера. Готово!
