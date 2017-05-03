def createRooms():

	global currentRoom

	# create the rooms and give them meaningful names
	A1 = Room("Room A1")
	A2 = Room("Room A2")
	A3 = Room("Room A3")
	A4 = Room("Room A4")
	A5 = Room("Room A5")
	A6 = Room("Room A6")
	A7 = Room("Room A7")
	A8 = Room("Room A8")

	B1 = Room("Room B1")
	B2 = Room("Room B2")
	B3 = Room("Room B3")
	B4 = Room("Room B4")
	B5 = Room("Room B5")
	B6 = Room("Room B6")
	B7 = Room("Room B7")
	B8 = Room("Room B8")

	C1 = Room("Room C1")
	C2 = Room("Room C2")
	C3 = Room("Room C3")
	C4 = Room("Room C4")
	C5 = Room("Room C5")
	C6 = Room("Room C6") 
	C7 = Room("Room C7")
	C8 = Room("Room C8")

	D1 = Room("Room D1 : Exit")
	D2 = Room("Room D2")
	D3 = Room("Room D3")
	D4 = Room("Room D4")
	D5 = Room("Room D5")
	D6 = Room("Room D6")
	D7 = Room("Room D7")
	D8 = Room("Room D8")

	E1 = Room("Room E1")
	E2 = Room("Room E2")
	E3 = Room("Room E3")
	E4 = Room("Room E4")
	E5 = Room("Room E5")
	E6 = Room("Room E6")
	E7 = Room("Room E7")
	E8 = Room("Room E8 : Entrance")

	F1 = Room("Room F1")
	F2 = Room("Room F2")
	F3 = Room("Room F3")
	F4 = Room("Room F4")
	F5 = Room("Room F5")
	F6 = Room("Room F6")
	F7 = Room("Room F7")
	F8 = Room("Room F8")

	G1 = Room("Room G1")
	G2 = Room("Room G2")
	G3 = Room("Room G3")
	G4 = Room("Room G4")
	G5 = Room("Room G5")
	G6 = Room("Room G6")
	G7 = Room("Room G7")
	G8 = Room("Room G8")

	H1 = Room("Room H1")
	H2 = Room("Room H2")
	H3 = Room("Room H3")
	H4 = Room("Room H4")
	H5 = Room("Room H5")
	H6 = Room("Room H6")
	H7 = Room("Room H7")
	H8 = Room("Room H8")
	

	A1.addExit("east", B1)
	A1.addExit("south", A2)

	A2.addExit("north", A1)
	A2.addExit("east", B2)

	A3.addExit("east", B3)
	A3.addExit("south", A4)

	A4.addExit("north", A3)

        A5.addExit("east," B5)
        A5.addExit("south", A6)

        A6.addExit("north", A5)
        A6.addExit("east", B6)

        A7.addExit("east", B7)
        A7.addExit("south", A8)

        A8.addExit("north", A7)
        A8.addExit("east", B8)

	B1.addExit("west", A1)
	
	B2.addExit("west", A2)
	B2.addExit("south", B3)
	
	B3.addExit("north", B2)
	B3.addExit("west", A3)
	B3.addExit("south", B4)

	B4.addExit("south", B5)
	B4.addExit("north", B3)

	B5.addExit("north", B4)
	B5.addExit("west", A5)

	B6.addExit("west", A6)
	B6.addExit("south", B7)

        B7.addExit("north", B6)
        B7.addExit("west", A7)

        B8.addExit("west", A8)
        B8.addExit("east", C8)

        C1.addExit("east", D1)
        C1.addExit("south", C2)
        
        C2.addExit("north", C1)
        C2.addExit("south", C3)
        
        C3.addExit("north", C2)
        C3.addExit("south", C4)
        
        C4.addExit("north", C3)
        C4.addExit("south", C5)
        
        C5.addExit("north", C4)
        C5.addExit("east", D5)
        
        C6.addExit("east", C5)
        C6.addExit("south", C7)
        
        C7.addExit("north", C6)
        C7.addExit("east", D7)
        
        C8.addExit("east", D8)
        C8.addExit("west", B8)

        D1.addExit("west", C1)

        D2.addExit("east", E2)

        D3.addExit("east", E3)
        D3.addExit("south", D4)

        D4.addExit("north", D3)
        D4.addExit("east", E4)

        D5.addExit("west", C5)
        D5.addExit("east", E5)

        D6.addExit("west", C6)
        D6.addExit("east", E6)

        D7.addExit("west", C7)
        D7.addExit("east", E7)
        D7.addExit("south", D8)

        D8.addExit("west", C8)
        D8.addExit("east", E8)

        E1.addExit("east", F1)
        E1.addExit("south", E2)
        
        E2.addExit("north", E1)
        E2.addExit("east", F2)
        E2.addExit("west", D2)

        E3.addExit("west", D3)
        E3.addExit("east", F3)

        E4.addExit("west", D4)

        E5.addExit("west", D5)
        E5.addExit("south", E6)

        E6.addExit("north", E5)
        E6.addExit("west", D6)

        E7.addExit("west", D7)
        E7.addExit("east", F7)
    
        E8.addExit("east", F8)

        F1.addExit("west", E1)

        F2.addExit("west", E2)
        F2.addExit("east", G2)

        F3.addExit("west", E3)
        F3.addExit("east", G3)
        F3.addExit("south", F4)

        F4.addExit("north", F3)
        F4.addExit("east", G4)
        F4.addExit("south", F5)

        F5.addExit("north", F4)
        F5.addExit("south", F6)

        F6.addExit("north", F5)
        F6.addExit("south", F7)

        F7.addExit("north", F6)
        F7.addExit("west", E7)

        F8.addExit("west", E8)
        F8.addExit("east", G8)

        G1.addExit("south", G2)
        G1.addExit("east", H1)

        G2.addExit("west", F2)
        G2.addExit("north", G1)

        G3.addExit("west", F3)

        G4.addExit("west", F4)
        G4.addExit("east", H4)

        G5.addExit("east", H5)
        G5.addExit("south", G6)

        G6.addExit("north", G5)
        G6.addExit("south", G7)

        G7.addExit("north", G6)
        G7.addExit("south", G8)
        G7.addExit("east", H7)

        G8.addExit("west", F8)
        G8.addExit("north", G7)
        
        H1.addExit("west", G1)
        H1.addExit("south", H2)

        H2.addExit("north", H1)
        H2.addExit("south", H3)

        H3.addExit("north", H2)
        H3.addExit("south", H4)

        H4.addExit("north", H3)
        H4.addExit("south", H5)
        H4.addExit("west", G4)

        H5.addExit("north", H4)
        H5.addExit("south", H6)
        H5.addExit("west", G5)

        H6.addExit("north", H5)

        H7.addExit("west", G7)
        H7.addExit("south", H8)

        H8.addExit("north", H7)
        
        # set room E8 as the current room at the beginning of the game
	currentRoom = E8
