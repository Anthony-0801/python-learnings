# Creating a list out of variables
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print("Printing the list areas:")
print(areas)

#_______________________________________________________________________________
# Print the list with different types of elements
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]
print("\n")
print("Printing the list areas with different types of elements:")
print(areas)

#_______________________________________________________________________________
#Printing the list with list
areas = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]
print("\n")
print("Printing the list areas with list:")
print(areas)
print(type(areas))