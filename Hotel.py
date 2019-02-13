'''
Created on Nov 4, 2018

@author: Marius Popescu

'''

# the room class will have: room number, bed type, smoking, rate, occupied and occupant name
class Room (object):

    __occupantName = "Not Occupied"

    def __init__(self, roomNr, bedType, smoking, rate):
        self.__roomNr = roomNr
        self.__bedType = bedType
        self.__smoking = smoking
        self.__rate = rate
        self.__occupied = False
    #setters and getters
    def getBedtype(self):
        return self.__bedType

    def getSmoking(self):
        return self.__smoking

    def getRoomNr(self):
        return self.__roomNr

    def getRoomRate(self):
        return self.__rate

    def getOccupant(self):
        return self.__occupantName

    def setOccupied(self, bool):
        self.__occupied = bool

    def setOccupant(self, name):
        self.__occupantName = name

    def setRoomNr(self, nr):
        self.__roomNr = nr

    def setBedType(self, bed):
        self.__bedType = bed

    def setRate (self, rate):
        self.__rate = rate

    def setSmoking (self, smoks):
        self.__smoking = smoks

    def isOccupied (self):
        return self.__occupied

    def __str__(self):
        return "Room Number: "+ str(self.__roomNr)+"\nOccupant name: "+self.__occupantName+"\nSmoking room: "+self.__smoking+"\nBed Type: "+self.__bedType+"\nRate: "+str(self.__rate)

#The hotel class has name, location, list of rooms, occupied counter
class Hotel(object):

    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.theRooms = []
        self.occupiedCnt = 0
        self.numOfRooms = 0
    # addRoom method will add a room to the hotel
    def addRoom(self, room):
        self.theRooms.append(room)
        self.numOfRooms += 1
    #isFull method will chek if all the rooms in the hotel are occupied and will return a boolean
    def isFull(self):
        if self.numOfRooms == self.occupiedCnt:
            return True
        else:
            return False
    #isEmpty method returns a boolean that is true if all the rooms in the hotel are unoccupied.
    def isEmpty(self):
        return self.occupiedCnt == 0
    #addReservation will complete a reservation adding a guest to a room acording with his requests
    def addReservation(self, occupantName, smoker, bed):    #provide guest requests
        for rm in self.theRooms: #for all rooms in the hotel
            #check if we can find a available room acording to the guest's requirement
            if rm.isOccupied() == False and rm.getBedtype() == bed and rm.getSmoking() == smoker:
                rm.setOccupant(occupantName)
                rm.setOccupied(True)
                self.occupiedCnt += 1
                print("The reservation was made")
                break
        else:
            print("We did not find a room to match your requests")
    #__findReservation will search the rooms for for a reservation with the occcupant name and will return the index in the list
    def __findReservation(self, occupantName):
        for rm in self.theRooms:
            if rm.getOccupant() == occupantName:
                return self.theRooms.index(rm)
            else:
                return -1
    #cancelReservation will cancel a reservation, will search for the name of the visitor in each room.
    # If it is found, the occupied attribute will be set to false. A message will be printed
    def cancelReservation(self, occupantName):
        i = self.__findReservation(occupantName)
        if i == -1:
            print("NOT_FOUND")
        else:
            self.theRooms[i].setOccupied(False)
            self.theRooms[i].setOccupant("Not Occupied")
            self.occupiedCnt -= 1
            print("The reservation was cancelled!")
    #printReservation will scan through all the rooms and display all details for only those rooms that are occupied.
    def printReservationList(self):
        for rm in self.theRooms:
            if rm.isOccupied() == True:
               print(self.theRooms[self.theRooms.index(rm)])
    #getDailySales will scan the room list, adding up the dollar amounts of the room rates of all occupied rooms only.
    def getDailySales(self):
        sale = 0
        for rm in self.theRooms:
            if rm.isOccupied() == True:
                sale += self.theRooms[self.theRooms.index(rm)].getRoomRate()
        return "$ " + str(sale)
    #occupancyPercentage will provide an occupancy percentage.
    def occupancyPercentage(self):
        return str(self.occupiedCnt/self.numOfRooms*100) + ' %'
    #__str__ returns a nicely formatted string giving hotel and room details for all the rooms in the hotel.
    def __str__(self):
        s = "Hotel Name: "+self.getHotelName()+"\nNumbers of Rooms: "+str(self.numOfRooms)+"\nNumber of Occupied Rooms: "+str(self.occupiedCnt)+"\n\nRoom Details are:\n\n"
        for rm in self.theRooms:
            s += str(self.theRooms[self.theRooms.index(rm)]) + "\n\n"
        return s
    #setters and getters
    def getHotelName(self):
        return self.__name

    def getLocation(self):
        return self.__location

    def setHotelName(self, name):
        self._namr = name

    def setLocation(self, loc):
        self.__location = loc

#test case class, will provide a test for the project
class Test(object):
    def __init__(self, h):
        self.h = h

    def testMe(self):

        # Print Hotel details
        print("_1___________Printing Hotel details_________")
        print(h)
        print("_2_______Calling isEmpty, isFull, occupacyPercentage ___________")
        print(h.isEmpty())
        print(h.isFull())
        print(h.occupancyPercentage())
        # Add reservations
        h.addReservation("John", "s", "queen")
        h.addReservation("George", "n", "king")
        h.addReservation("Ana", "s", "twin")
        # Print Hotel details
        print("_3___________Printing Hotel details_________")
        print(h)
        print("_4_______Calling isEmpty, isFull, occupacyPercentage ___________")
        print(h.isEmpty())
        print(h.isFull())
        print(h.occupancyPercentage())
        print("_5__________Printing ReservationList___________")
        h.printReservationList()
        # Cancel reservations
        print(h.cancelReservation("John"))
        print(h.cancelReservation("Arthur"))
        print("_6___________Printing Hotel details_________")
        print(h)
        print("_7_______Calling isEmpty, isFull, occupacyPercentage ___________")
        print(h.isEmpty())
        print(h.isFull())
        print(h.occupancyPercentage())
        print("_8______DailySale_______")
        print(h.getDailySales())

# Creating the hotel
h = Hotel("Beach Mariott", "Pensacola")
# Creating the rooms
r1 = Room(101, "queen", "s", 100)
r2 = Room(102, "king", "n", 110)
r3 = Room(103, "king", "n", 88)
r4 = Room(104, "twin", "s", 100)
r5 = Room(105, "queen", "n", 99)
# Adding rooms to the hotel
h.addRoom(r1)
h.addRoom(r2)
h.addRoom(r3)
h.addRoom(r4)
h.addRoom(r5)
# Creating and executing the test
t = Test(h)
t.testMe()
