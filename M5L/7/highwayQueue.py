from highway import Highway

class HighwayQueue:
    def __init__(self):
        self.HWhead = None
        self.HWtail = None
        
    def isEmpty(self):
        return self.HWhead == None
    
    def push(self, name):
        newHighway = Highway(name)
        
        if self.isEmpty():
            self.HWhead = newHighway
            self.HWtail = newHighway
        else:
            newHighway.nextCity = self.HWhead
            self.HWhead = newHighway
            
    def print(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            temp = self.HWhead
            while temp:
                print(f"{temp.name} ")
                temp.printCities()
                print()
                temp = temp.nextCity
            
    def pop(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            penult = self.HWhead
            last = self.HWhead
            while last.nextCity:
                penult = last
                last = last.nextCity
            penult.nextCity = None
            self.HWtail = penult
            
    def searchHighway(self, highway):
        if self.isEmpty():
            print("Empty List")
        else:
            temp = self.HWhead
            while temp:
                if temp.name == highway:
                    return temp
                temp = temp.nextCity
            return None