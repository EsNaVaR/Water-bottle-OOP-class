'''Emiliano Navarrete
10.1 
I ued this weeks lectures to help me with this assignment,
 I also used the fruit baskit example for reference
'''
#creating class
class Waterbottle:
    #defines the method
    def __init__(self, color, brand, water):
        self._color = color
        self._brand = brand
        self._water = water

    #defines the get_brand method
    def get_brand(self):
        return self._brand
    #defines the get_color method
    def get_color(self,):
        return self._color
    
    def get_water(self):
        return self._water
    #used so you can redifine the color
    def set_color(self, color):
        self._color = color 
    #used so you can redifine the brand
    def set_brand(self, brand):
        self._brand = brand

    #defines brand of waterbottle

    #function to fill water bottle 
    def fill_water(self, liquid):
        #makes them privte
        self._liquid = liquid
        result = self._water + self._liquid
        self._result = result
        #determines if the watter bottle ha too much water in it or not
        if self._result > Waterbottle.size:
            #prints how much 
            print(f"Your bottle is overflowing! The maximum amount of water is 60 oz. but you have {self._result} oz.")        
        else:
            print("You filled your waterbottle.")
            #prints how much of the waterbottle is full
        print(f"You filled your waterbottle with {self._result} ounces.")
        self._water = self._result
    #funciton to drink water
    def drink_water(self, liquid):
        self._liquid = liquid
        self._water -= self._liquid
        if self._water <= 0:
            print("Your waterbottle is empty.")
            self._water = 0
        else:
            #prints how much water is left
            print(f"You have drank {self._liquid} ounces of your water.")

#defines main function
def main():
    waterbottle1 = Waterbottle("Red", "Hydroflask", 12)
    print(waterbottle1.get_water())
    (waterbottle1.drink_water(4))
    print(waterbottle1.get_water())
    watterbottle2 = Waterbottle("Blue", "Camel", 14)
    print(f"The color is {watterbottle2.get_color()}.")
    watterbottle3 = Waterbottle("Pink", "Nike", 6)
    print(f"The brand is {watterbottle3.get_brand()}.")

#runs the code
if __name__ == "__main__":
    main()