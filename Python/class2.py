class Vehicle:
    color=""
    brand=""
    regNo=""
    def __init__(self, col, band, rNo):
        Vehicle.color=col
        Vehicle.brand=band
        Vehicle.regNo=rNo
    
    def getData(self):
        print(Vehicle.color, Vehicle.brand, Vehicle.regNo)

obj=Vehicle("Blue","GM","WB26BB1001")
obj.getData()

obj1=Vehicle("White","HM","WB50BQ5021")
obj1.getData()