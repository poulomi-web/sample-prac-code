from datetime import datetime

class Person:
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth
        
    @classmethod
    def create(cls, name, date_of_birth):
        try:
            year_of_birth_obj = datetime.strptime(date_of_birth,'%Y-%m-%d')
            year_of_birth = year_of_birth_obj.year
        except:
            raise ValueError("Please provide input date in the following format YYYY-MM-DD")
        
        return cls(name=name, year_of_birth=year_of_birth)
    
    def age_calc(self):
        return datetime.now().year - self.year_of_birth
