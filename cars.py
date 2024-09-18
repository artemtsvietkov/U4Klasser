import os

class Brand:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def __str__(self):
        return f"{self.brand} {self.model}"
    
    def __repr__(self):
        return f"{self.brand} {self.model}"
        

class Fleet:
    def __init__(self, cars=None): 
        if cars is None:
            cars = []
        self.cars = cars
        
    def show_all(self):
        for car in self.cars: 
            print(f"{car}")

    def show(self, num_cars):
        if num_cars > len(self.cars):
            raise ValueError("Not enough cars left to show")
        
        showed_cars = self.cars[:num_cars]
        self.cars = self.cars[num_cars:]  # Remove showed cars from the fleet
        
        return showed_cars
    @staticmethod           
    def make_fleet():  
        cars = [] 
        brands = {
            "Toyota": ["Corolla", "Camry", "RAV4", "Yaris", "Highlander"],
            "BMW": ["X5", "M3", "i8", "X3", "Z4"],
            "Tesla": ["Model S", "Model 3", "Model X", "Model Y", "Roadster"],
            "Ford": ["Fiesta", "Mustang", "Focus", "Explorer", "F-150"],
            "Mercedes": ["C-Class", "E-Class", "S-Class", "GLA", "GLE"]
        }
       
        for brand, models in brands.items():  
            for model in models:  
                cars.append(Brand(brand, model)) 
                
        return cars


os.system('cls' if os.name == 'nt' else 'clear')

cars = Fleet.make_fleet()

fleet = Fleet(cars)

fleet.show_all()