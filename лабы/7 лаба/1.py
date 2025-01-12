class Employee:
    id = 0
    def __init__(self, name=None, **kwargs):
        self.name = name
        self.id = Employee.id
        Employee.id += 1

    def get_info(self):
        return f'id: {self.id}, name: {self.name}'

    def change_name(self, new_name):
        self.name = new_name

class Manager(Employee):
    post = 'manager'
    def __init__(self, name=None, department=None, **kwargs):
        super().__init__(name=name, department=department, **kwargs)
        self.department = department
        self.projects = []

    def get_info(self):
        return f'id: {self.id}, name: {self.name}, post: {Manager.post}, department: {self.department}'

    def manage_project(self, name, project_id, priority):
        project = [project_id, name, priority]
        self.projects.append(project)

    def projects_info(self):
        for i in self.projects:
            print('project_id: ' + str(i[0]) + ', ' + i[1] + ', the priority is ' + i[2])

class Technician(Employee):
    post = 'technician'
    def __init__(self, name=None, specialization=None,  **kwargs):
        super().__init__(name=name, specialization=specialization,  **kwargs)
        self.specialization = specialization
        self.contracts = []

    def get_info(self):
        return f'id: {self.id}, name: {self.name}, post: {Technician.post}, specialization: {self.specialization}'

    def perform_maintenance(self, object, period, requirement):
        сontract = [object, period, requirement]
        self.contracts.append(сontract)

    def contracts_info(self):
        for i in self.contracts:
            print('обслуживание ' + i[0] + ', for ' + i[1] + ', the requirement is ' + i[2])

class TechManager(Technician, Manager):
    post = 'techManager'

    def __init__(self, name=None, specialization=None, department=None):
        super().__init__(name=name, specialization=specialization, department=department)
        self.subordinates = []

    def get_info(self):
        return f'id: {self.id}, name: {self.name}, post: {TechManager.post}, department: {self.department}, specialization: {self.specialization}'

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        for empoyee in self.subordinates:
            print(empoyee.get_info())

Masha_regular_employee =  Employee(name='Иванова Мария Андреевна')
print(Masha_regular_employee.get_info())

Vanya_regular_employee = Employee(name='Петров Иван Евгеньевич')
print(Vanya_regular_employee.get_info())

Nastya_manager = Manager(name='Байкова Анастасия Сергеевна', department='отдел инновационных решений')
print(Nastya_manager.get_info())
Nastya_manager.manage_project(name='придумать новые проекты', project_id=27, priority='the highest')
Nastya_manager.manage_project(name='придумать имена будующим сотрудникам', project_id=28, priority='the lowest')
Nastya_manager.projects_info()

Danya_technician = Technician(name='Слонов Даниил Павлович', specialization='обслуживание СЛОН')
print(Danya_technician.get_info())
Danya_technician.perform_maintenance(object='СЛОН', period='november', requirement='-')
Danya_technician.contracts_info()

Katya_techManager = TechManager(name='Гончарова Екатерина Александровна', specialization='обслуживание странных устройств с названиями животных', department='зоопарк')
print(Katya_techManager.get_info())

Katya_techManager.manage_project(name='придумать новые названия обслуживаемых устройств', project_id=29, priority='the highest')
Katya_techManager.projects_info()

Katya_techManager.perform_maintenance(object='КОТ', period='november', requirement='гладить!')
Katya_techManager.perform_maintenance(object='СЛОН', period='november', requirement='-')
Katya_techManager.contracts_info()

Katya_techManager.add_employee(Danya_technician)
Katya_techManager.add_employee(Vanya_regular_employee)
Katya_techManager.get_team_info()


