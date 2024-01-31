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

#_______________________________________________________________________________
# Subsetting lists
# Print out second element from areas
print("\n")
print("Printing the second element from areas:")
print(areas[1])

# Print out last element from areas
print("\n")
print("Printing the last element from areas:")
print(areas[-1])

# Print out the area of the living room
print("\n")
print("Printing the area of the living room:")
print(areas[2][1])

#Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[1][1] + areas[3][1]
print("\n")
print("Printing the sum of kitchen and bedroom area:")
print(eat_sleep_area)

#_______________________________________________________________________________
# Slicing and dicing
# Use slicing to create downstairs
downstairs = areas[:6]
print("\n")
print("Printing the list downstairs:")
print(downstairs)

# Use slicing to create upstairs
upstairs = areas[6:]
print("\n")
print("Printing the list upstairs:")
print(upstairs)

#_______________________________________________________________________________
# Manipulating lists
# Change "bathroom" to "chill zone"
areas[-1] = "chill zone"
print("\n")
print("Printing the list areas after changing bathroom to chill zone:")
print(areas)

# Extend the list areas with poolhouse and garage
areas_1 = areas + ["poolhouse", 24.5]
areas_1 = areas_1 + ["garage", 15.45]
print("\n")
print("Printing the list areas after extending with poolhouse and garage:")
print(areas_1)

# Replace the 15.45 in areas_1 with 16.45
areas_1[8] = 16.45
print("\n")
print("Printing the list areas after replacing 15.45 with 16.45:")
print(areas_1)

# Remove the last two elements from areas_1
areas_1[-2:] = []
print("\n")
print("Printing the list areas after removing the last two elements:")
print(areas_1)