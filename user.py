class User:		# declare a class and give it name User
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0.00
    
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance + amount	
    def make_withdrawal(self, amount):
        self.account_balance -= amount	
    def display_user_balance(self):
        print('User: ' + self.name + ',Balance: $' + str(self.account_balance))
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

jordan = User("Jay Wade", "email@email.com")
matthew = User("Matthew Wade", "mat@email.com")
oliver = User("Oliver Wade", "oli@email.com")

jordan.make_deposit(100)
jordan.make_deposit(200)
jordan.make_deposit(300)
jordan.display_user_balance()

matthew.make_deposit(25)
matthew.make_deposit(35)
matthew.make_withdrawal(30)
matthew.make_withdrawal(40)
matthew.display_user_balance()

oliver.make_deposit(25000)
oliver.make_withdrawal(500)
oliver.make_withdrawal(1500)
oliver.make_withdrawal(3500)
oliver.display_user_balance()

jordan.transfer_money(oliver, 200)
jordan.display_user_balance()
oliver.display_user_balance()