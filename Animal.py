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
        self._hunger = food

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy = value

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
        return f"This animal is {self.name},\n{self.name}'s age is {self.age},\n{self.name} lives in {self.place}"
    
    def __repr__(self):
        return f"Animal(name='{self.name}', age={self.age}, place='{self.place}')"




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
            cub.hunger-=10
            return f"{cub.name} has been breast fed,hunger level decreased [{cub.hunger}]"
        else:
            return "To big for breast Milk"

class MixinKill:
    def kill(self,prey):
        if isinstance(prey,Animal):    #aucilebelia shevamowmot rom argumenti namdvilad iyos animali.
            print("Prey died")
            prey.energy=0
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
                print( f'{self.animal.name} hunted {prey.name}.Hunger level of {self.animal.name}decreased.Current->{self.animal.hunger}')
                self.kill(prey)
            else:
                print( f'Hunt failed, {prey.name} is alive')

""" vinaidan predator aeqstendebs mixinkill class shegvidzlia gamoviyenot misi funcia killic current objectistvis(self)
    romelic parametrad miighebs preys da washlis mas mexsierebidan"""




class Reptiles(Animal):
    pass


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



# lion1=Lion('lion',5,'savannah',50,100)
# print(lion1)   #edzaxis __str__ s

# lion_cub1=lion1.reproduce()
# print(lion_cub1)
# print(lion1.breast_feed(lion_cub1))

# lion_predator=Predator(lion1)

# zebra1=Zebra('zebra',3,'savannah',10,30)
# lion_predator.hunt(zebra1)



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

Predator(eagle1).hunt(penguin1)





