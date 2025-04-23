# if elif else statements 
class statement():
    def __init__(self):
        self.age = 19
        
        # Short Hand if-else
        print("Travel for free" if self.age<=12 else "pay 50%" if self.age<= 20 else "Pay for ticket" )

    def if_else(self):
        super().__init__()
        if self.age <= 12:
            print("Travel for free.")
        elif self.age <= 20:
            print("pay 50%")
        else:
            print("Pay for ticket.")

run = statement()
run.if_else()
