#Создание пользователей	
class User():
	'''Вывод информации о пользователе'''
	def __init__(self, first_name, last_name, age, city, phone):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.city = city.title()
		self.phone = phone
		
    #Количество попыток входа
		self.login_attempts = 1
		
  #Подсчёт попыток входа
	def increment_login_attempts(self):
		self.login_attempts += 1
	
  #Обнуление счётчика
	def reset_login_attempts(self):
		self.login_attempts = 0
		
  #Описание пользователя на основе переданных аргументов
	def describe_user(self):
		print('Information about user '+self.first_name+':')
		print('\tLast name: '+self.last_name)
		print('\tAge: '+str(self.age))
		print('\tCity: '+self.city)
		print('\tPhone: '+str(self.phone))
		print('\tNumber of login accempts: '+str(self.login_attempts))
	
  #Приветствие пользователя
	def greet_user(self):
		print('\nDear '+self.first_name+' '+self.last_name+', '+
		'welcome to our website!')

#Класс с привилегиями администратора
class Privileges():
	def __init__(self, privileges=None):
		self.privileges = ['разрешено добавлять сообщения',
		'разрешено удалять пользователей', 
		'разрешено банить пользователей']
	
  #Вывод привелегий на экран
	def show_privileges(self):
		print('Пользователь является '+
		'Администратором, поэтому он имеет следующие возможности: ')
		for privilege in self.privileges:
			print('- '+privilege)

#Создание администратора			
class Admin(User):
	'''Описание возможностей пользователя-администратора'''
	def __init__(self, first_name, last_name, age, city, phone):
		super().__init__(first_name, last_name, age, city, phone)
		self.privileges = Privileges()

#Примеры создания пользователей
vitaly = User('vitaly','prikhodkov',21,'volgograd',89275848291)
vitaly.greet_user()
vitaly.increment_login_attempts()
vitaly.increment_login_attempts()
vitaly.increment_login_attempts()
vitaly.describe_user()
vitaly.reset_login_attempts()
vitaly.describe_user()

aleksandra = User('aleksandra','semagina',19,'moscow',79880156627)
aleksandra.greet_user()
aleksandra.describe_user()

#Пример создания администратора
dmitry = Admin('dmitry','prikhodkov',47,'voljsky',89275195239)
dmitry.greet_user()
dmitry.increment_login_attempts()
dmitry.describe_user()
dmitry.privileges.show_privileges()
