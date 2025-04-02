from abc import ABC,abstractmethod

class HumanInteractionsMixin:
    def interacting_with_humans(self, interaction_type: str):
        if interaction_type in ["zookeper", "owner"]:
            return f"{self.name} goes to interact with the {interaction_type}"
        else:
            return f"{self.name} is wary of the {interaction_type}"

class Animal(ABC, HumanInteractionsMixin):
    def __init__(self,name,age,place,hunger,energy):
        self.__name=name    #private monacemebi mati shecvla sheudzlebeli iqneba
        self.__age=age    #in years
        self.__place=place
        self._hunger = hunger
        self._energy = energy
        self.is_alive=True

    @property   #getterebi rom mivwvdet classis private monacemebs
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


    @property
    def place(self):
        return self.__place

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter      # setteri  food values mixedvit shecvlis shimshilis  dones
    def hunger(self, food):
        if food >= 0:
            self._hunger = food
        else:
            print("Can not set hunger variable")


    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        if value >=0:
            self._energy = value
        else:
            print("Can not set energy variable")


    @abstractmethod
    def movement(self,speed:float):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def reproduce(self):
        pass

    def __str__(self):
        return f"This Animal is {self.__class__.__name__}, \nIt's name is {self.name},\n{self.name} is {self.age} years old,\n{self.name} lives in {self.place}"

    def __repr__(self):
        if self.is_alive:
            return f"{self.__class__.__name__}('{self.name}', {self.age}, '{self.place}', {self.hunger}, {self.energy})"
        else:
            return f"{self.__class__.__name__} {self.name} is dead"


class Mammal(Animal,ABC):

    @abstractmethod
    def breast_feed(self,cub):
        pass

class Zebra(Mammal):
    def movement(self,speed:float):
        if 30<speed <50:
            self.energy-=15
        elif 50<speed<65:
            self.energy-=25
        else:
            self.energy-=10

    def make_sound(self):
        return "Zebra Screams"

    def reproduce(self):
        zebra_cub=Zebra('zebra cub',0,self.place,0,0)
        return zebra_cub

    def breast_feed(self,cub):
        if cub.age<0.5:
            cub.hunger-=10
            return f"{cub.name} has been breast fed,hunger level decreased [{cub.hunger}]"
        else:
            return "To big for breast Milk"




class Lion(Mammal):

    def movement(self,speed:float):
        if 20<speed<30:
            self.energy-=5
        elif 30<speed<50:
            self.energy-=10
        elif speed>50:
            self.energy-=15
        else:
            self.energy-=2

    def make_sound(self):
        return "Lion Roars"

    def reproduce(self):
        lion_cub=Lion('lion cub',0,self.place,0,0)
        return lion_cub

    def breast_feed(self,cub):
        if cub.age<0.5:
            return f"{cub.name} has been breast fed"
        else:
            return "To big for breast Milk"

class MixinKill:
    def kill(self,prey):
        if isinstance(prey,Animal):    #aucilebelia shevamowmot rom argumenti namdvilad iyos animali.
            print("Prey died")
            prey.energy=0
            prey.is_alive=False
        else:
            return "this is not prey"


class Predator(MixinKill):              #predator clasi functionirebs kompoziciis dzalit
    def __init__(self,animal:Animal):   #predatoris konstruktors gadavcemt Animal tipis obieqts
        self.animal=animal               #im logikit rom es iqneba animal romelsac sheedzleba nadiroba

    def hunt(self,prey:Animal):         #prey aseve Animal tipis obieqti romelsac dabridavs self.animal
        if isinstance(prey,Animal):    #validacia shevamowmot prey namdvilad animal tipis aris tu ara

            """ამ წინადადებას შემდეგი შინაარსი აქვს.თუ მსხვერპლის ენერგია ნაკლებია მტაცებლის ენერგიაზე,ის მოინადირება შემდეგ ხაზებზე"""

            if prey.energy<self.animal.energy:
                self.animal.hunger -=10
                print( f'{self.animal.name} hunted {prey.name}.Hunger level of {self.animal.name} decreased.  Current->{self.animal.hunger}')
                self.kill(prey)
            else:
                print( f'Hunt failed, {prey.name} is alive')


""" vinaidan predator aeqstendebs mixinkill class shegvidzlia gamoviyenot misi funcia killic current objectistvis(self)
    romelic parametrad miighebs preys da washlis mas mexsierebidan"""



""" Reptiles Section """

class Reptiles(Animal, ABC):
    def __init__(self, name, age, place, hunger, energy, shedding_stage):
        super().__init__(name, age, place, hunger, energy)
        self._shedding_stage = shedding_stage

    @property
    def shedding_stage(self):
        return self._shedding_stage

    @shedding_stage.setter
    def shedding_stage(self, value):
        if value in ["not shedding", "starting to shed", "shedding", "fully shed"]:
            self._shedding_stage = value
        else:
            print("Invalid shedding stage")

    @abstractmethod
    def shed_skin(self):
        pass

class Snake(Reptiles):
    def movement(self, speed):
        if speed == 0:
            self.energy -= 0
        elif 1 <= speed <= 5:
            self.energy -= 10
        elif 5 < speed <= 15:
            self.energy -= 20
        else:
            return "Not Possible"

    def make_sound(self):
        return "Hissss"

    def shed_skin(self):
        if self.energy < 20:
            return f"{self.name} is too tired to shed skin!"
        self.energy -= 15
        self.shedding_stage = "fully shed"
        return f"{self.name} shed its skin successfully!"

    def reproduce(self, baby_snake):
        return Snake(baby_snake, 0, self.place, 0, 0, "not shedding")


class Lizard(Reptiles):
    def movement(self, speed):
        if speed == 0:
            self.energy -= 0
        elif 1 <= speed <= 10:
            self.energy -= 15
        elif 10 < speed <= 25:
            self.energy -= 30
        else:
            return "Not Possible"

    def make_sound(self):
        return "growl"

    def shed_skin(self):
        if self.energy < 30:
            return f"{self.name} is too tired to shed skin!"
        self.energy -= 20
        self.shedding_stage = "fully shed"
        return f"{self.name} shed its skin successfully!"

    def reproduce(self, baby_lizard):
        return Lizard(baby_lizard, 0, self.place, 0, 0, "not shedding")



""" Birds Section """

class Birds(Animal, ABC):

    def __init__(self, name, age, place, hunger, energy, eggs):
        super().__init__(name, age, place, hunger, energy)
        self._eggs = eggs

    @property
    def eggs(self):
        return self._eggs
    
    @eggs.setter
    def eggs(self, value):
        self._eggs = value

    @abstractmethod
    def lay_eggs(self):
        pass


class Penguin(Birds):
    def movement(self, speed: float):
        if speed == 0:
            self.energy -=0
        elif 1 <= speed <= 7:
            self.energy -= 15
        elif 7 < speed <= 15:
            self.energy -= 25
        else:
            return "Unrealistic speed"
        
    def make_sound(self):
        return "Penguin sounds"
    
    def lay_eggs(self):
        if self.energy < 30:
            return f"{self.name} is too tired to lay eggs!"
        self.eggs += 1
        self.energy -= 25  
        return f"{self.name} laid an egg! Total eggs: {self.eggs}, Energy left: {self.energy}"
    
    def reproduce(self, chick_name):
        penguin_chick = Penguin(chick_name,0,self.place,0,0,0)
        return penguin_chick
    
class Eagle(Birds):
    def movement(self, speed):
        if speed == 0:
            self.energy -=0
        elif 1 <= speed <= 30:
            self.energy -= 15
        elif 30 < speed <= 70:
            self.energy -= 25
        elif 70 < speed <= 100:
            self.energy -= 35
        else:
            return "Unrealistic speed"
        
    def make_sound(self):
        return "Eagle sounds"
    
    def lay_eggs(self):
        if self.energy < 50:
            return f"{self.name} is too tired to lay eggs!"
        self.eggs += 1
        self.energy -= 45  
        return f"{self.name} laid an egg! Total eggs: {self.eggs}, Energy left: {self.energy}"
    
    def reproduce(self, eaglet_name):
        eaglet = Eagle(eaglet_name,0,self.place,0,0,0)
        return eaglet 


""" Test Of Lion Object """
lion1=Lion('lion',5,'savannah',50,100)
print(lion1.make_sound())
lion1.movement(40)
print(lion1)   #edzaxis __str__ s
print("\n\n")

lion_cub1=lion1.reproduce()

print(lion_cub1)
print(lion1.breast_feed(lion_cub1))

print("\n\n")

print(repr(lion1))  #dabechdavs lion1 s

print("\n\n")

"""sheiqmna predator klasis obieqti lion_predator romelic gamoiyenebs hunt funqcionals"""
lion_predator=Predator(lion1)

""" Create zebra object"""
zebra1=Zebra('zebra',3,'savannah',10,30)
print(zebra1.make_sound())
zebra1.movement(10)
print(repr(zebra1))

print("\n\n")
print("Lion starts hunting")
lion_predator.hunt(zebra1)
print("Zebra is Done")
print("\n\n")

print(repr(lion1))
print(repr(zebra1))      #abrunebs zebra is dead repr funqciashi validaciis pirobis gamo


""" Test of Reptiles """

snake1 = Snake("Kaa", 3, "Monkey City", 10, 100, "not shedding")
lizard1 = Lizard("Komodo", 5, "Island of Komodo", 15, 120, "starting to shed")

print(snake1)
print(snake1.shed_skin())
print(snake1.reproduce("Baby Kaa"))
print("\n")
print(lizard1)
print(lizard1.shed_skin())
print(lizard1.reproduce("Baby Dragon"))
print("\n")


"""Tests for Birds"""

penguin1 = Penguin("Rico", 5, "Madagascar", 10, 100, 0)
print(penguin1)
print(repr(penguin1))

print("----------------------------------------------------")

eagle1 = Eagle("Ethan", 7, "Piggy Island", 20, 100, 0)
print(eagle1)
print(repr(eagle1))

print("----------------------------------------------------")

penguin1.movement(6)
print(penguin1.energy)
print(penguin1.make_sound())
print(penguin1.lay_eggs())
print(penguin1.reproduce("Rico Junior"))
print(penguin1.interacting_with_humans("zookeper"))

print("----------------------------------------------------")

eagle1.movement(50)
print(eagle1.energy)
print(eagle1.make_sound())
print(eagle1.lay_eggs())
print(eagle1.reproduce("Ethan Junior"))
print(eagle1.interacting_with_humans("owner"))

print("----------------------------------------------------")

Predator(eagle1).hunt(penguin1)