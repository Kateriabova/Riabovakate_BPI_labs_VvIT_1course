
Лабораторная работа № 5 Работа с классами

Цель работы: Получить практический опыт работы с ООП в Python.


Задание 1:  Базовый класс и методы

1.	Определите класс Book, который имеет три атрибута: title (название), author (автор), и year (год издания).
Будем считать, что эти три атрибута – атрибуты класса и будем определять их для всего класса (перед инитом). Добавим еще один атрибут класса – счетчик экземпляров. Тогда при инициализации нового объекта класса мы будем увеличивать счетчик на единицу. 
2.	Добавьте метод get_info(), который возвращает информацию о книге в формате: "Название книги: [title], Автор: [author], Год издания: [year]".
Используем вывод форматированной строки и синтаксис self.title; self.author и self.year.

Задание 2: Работа с конструктором

1.	Определите класс Circle для представления круга.
2.	Используйте конструктор __init__ для инициализации радиуса круга (radius). Передаем в конструктор на вход self (как бы объект класса) и число – радиус. Создаем атрибут класса – radius и одновременно присваиваем ему входной значение. 
3.	Добавьте метод get_radius(), который возвращает значение радиуса. На вход обязательно передаем self – экземпляр класса. Обращаемся к атрибуту следующей конструкцией - self.radius. Возвращаем полученное значение.
4.	Добавьте метод set_radius(new_radius), который позволяет изменить радиус круга. Передаем на вход сам объект и число – новое значение радиуса. Присваиваем атрибуту класса новое значение конструкцией self.radius = new_radius. 
5.	Создайте объект класса Circle, измените его радиус и выведите новый радиус на экран. Объект создаем следующей конструкцией: объект = Класс(аргументы).



