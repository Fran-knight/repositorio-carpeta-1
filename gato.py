import datetime


class Gatete:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.species = ''
        self.birthday = datetime.date.today()

    def meow(self):
        print(f"({self.name}) Miauuuu!!!")

    def purr(self):
        print(f"({self.name}) Mrrrrrr!!!")

    def eat(self, food):
        print(f"({self.name}) ", end="")
        if food == "pescado":
            print("Hmmmm, gracias :-)")
        else:
            print("Lo siento, yo solo como pescado.")

    def fight_with(self, opponent):
        print(f"({self.name}) ", end="")
        if self.sex == "hembra":
            print("No me gusta pelear.")
        elif opponent.sex == "hembra":
            print("No peleo contra gatitas.")
        else:
            print(f"Ven aquí {opponent.name}, que te vas a enterar :-@")