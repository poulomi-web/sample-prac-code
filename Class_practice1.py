from datetime import datetime
class Person:
    def __init__(self,name,date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return ("Determines age of {} with DOB {}".format(self.name,self.date_of_birth))

    def __str__(self):
        return "Age calculator of a person"

    def age_calc(self):
        current_year = datetime.now().year
        # year_of_birth = self.date_of_birth[4:]
        try:
            year_of_birth_obj = datetime.strptime(self.date_of_birth,'%Y-%m-%d')
            year_of_birth = year_of_birth_obj.year
        except:
            raise ValueError("Please provide input date in the following format YYYY-MM-DD")
        age = current_year - year_of_birth
        return ('{} is {} years old'.format(self.name,age))

if __name__ == "__main__":
    A = Person("Peter","19880113")
    print(A.age_calc())
    print(repr(A))
    print(str(A))

