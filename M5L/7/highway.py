from city import City

class Highway:
    def __init__(self, name):
        self.name = name
        self.nextCity = None
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def printCities(self):
        if self.isEmpty():
            print("Empty list")

        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        
    def append(self, cityName):
        newCity = City(cityName)
        
        if self.isEmpty():
            self.head = newCity
            self.tail = newCity
        else:
            self.tail.next = newCity
            self.tail = newCity

        
        
        
    