## match case + nested 
class conditions():
    def __init__(self):
        self.age = None
        self.check_number()

    def nested(self, age):
        self.age = age
        is_member = True

        if self.age >= 60:
            if is_member:
                print("30% senior discount!")
            else:
                print("20% senior discount.")
        else:
            print("Not eligible for a senior discount.")
        
        self.check_number()

    def check_number(self):
        if self.age is None:
            print("Age is not set")
            return
            
        match self.age:
            case age if age <= 12:
                print("Eligible for child benefits.")
            case _:
                print("Not eligible for child benefits.")
    
    

conditions().nested(3)