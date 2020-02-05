class Person :
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        return("Hello {}, I am {}:".format(other_person.name, self.name))
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")
    def add_friend(self, new_friend):
        self.friends.append(new_friend)

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

print(sonny.greet(jordan))
print(jordan.greet(sonny))

print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)

sonny.print_contact_info()

#Make your own Vehicle class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        return("{} {} {}").format(self.year, self.make, self.model)

#Links to class Vehicle - which then gets formatted based on print_info 
#to be year, Make, Model
car = Vehicle("Nissan", "Leaf", "2015")
print(car.print_info())


