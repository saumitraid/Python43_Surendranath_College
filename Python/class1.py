class Vehicle:
    color=""
    brand=""
    regNo=""
    def setData(self,col, band, rNo):
        Vehicle.color=col
        Vehicle.brand=band
        Vehicle.regNo=rNo

    def moveForward(self):
        print("Move forward")
    
    def moveBackward(self):
        print("Move Backward")
    
    def stop(self):
        print("Stop....")
    
    def getData(self):
        print(Vehicle.color, Vehicle.brand, Vehicle.regNo)

obj=Vehicle()
obj.moveBackward()
obj.moveForward()
obj.stop()
obj.setData("Cherry","BMW","WB12D1025")
obj.getData()