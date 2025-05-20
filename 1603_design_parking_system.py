class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_capacity = big
        self.medium_capacity = medium
        self.small_capacity = small

        self.big_spots_available = big
        self.medium_spots_available = medium
        self.small_spots_available = small

    def addCar(self, carType: int) -> bool:
        match carType:
            case carType if carType == 1 and self.big_spots_available:
                self.big_spots_available -= 1
                return True
            case carType if carType == 2 and self.medium_spots_available:
                self.medium_spots_available -= 1
                return True
            case carType if carType == 3 and self.small_spots_available:
                self.small_spots_available -= 1
                return True
        return False
        

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

