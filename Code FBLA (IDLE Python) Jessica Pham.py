"""
You have been hired by your state or local area’s tourism bureau
to develop a program that suggests attractions (can be tourist attractions,
restaurants, shopping, things to do, etc.) to potential visitors. 
Your program will allow users to search for attractions in the area
based on desired attributes, such as location, type of attraction, and amenities.
Your program must include at least 50 attractions, and users must be 
able to define at least five desired attributes to search for an attraction.
"""

print("Welcome to Florida's Tourism Guide!")




# attributes: city, type of attraction, popularity, 


# Defining variables of attraction list





a1 = "Jamaica Kitchen"
a2 = "Casa Prado Restaurant"
a3 = "Crandon Park Beach"
a4 = "Star Island"
a5 = "Dolphin Mall"
a6 = "Aventura"
a7 = "Matheson Hammock Park"
a8 = "Biscayne National Park"
a9 = "Urban Pizza Cafe"
a10 = "Greenstreet Cafe"
a11 = "Biscayne Bay"
a12 = "Sunny Isles Beach"
a13 = "Mall at 163rd Street"
a14 = "The Shops at Sunset Place"
a15 = "Lummus Park"
a16 = "Bayfront Park"
a17 = "Wood Tavern"
a18 = "Christy's Restaurant"
a19 = "Haulover Beach"
a20 = "Mid-Beach"
a21 = "Miami Merchandise Market"
a22 = "Fifth and Alton"
a23 = "Sewell Park"
a24 = "The Doral Yard"
a25 = "Tio's Urban Dominican Food"
a26 = "El Tucan Miami"
a27 = "South Beach"
a28 = "Miami Beach"
a29 = "Cocowalk"
a30 = "Brickell City Centre"
a31 = "South Point Park"
a32 = "Brickell Key Park"
a33 = "Mrs. Potato Restaurant"
a34 = "Anh Hong Restaurant"
a35 = "Cocoa Beach"
a36 = "Vero Beach"
a37 = "Indialantic Beach"
a38 = "The Mall at Millenia"
a39 = "Kelly Park"
a40 = "Epcot"
a41 = "Streetwise Urban Food"
a42 = "The Hampton Social - Orlando"
a43 = "Port Canaveral"
a44 = "Daytona Beach"
a45 = "Mount Dora Marketplace"
a46 = "International Drive"
a47 = "Lake Eola Park"
a48 = "Universal Studios"
a49 = "Tako Cheena"
a50 = "The Capital Grille at Orlando"
a51 = "St. Augustine Beach"
a52 = "Flagler Beach"
a53 = "Lake Buena Vista Factory Stores"
a54 = "The Florida Mall"
a55 = "Sebastian Inlet State Park"
a56 = "ICON Park"
a57 = "Ace Cafe Orlando"
a58 = "Hamilton's Kitchen"
a59 = "Ormond Beach"
a60 = "New Smyrna Beach"
a61 = "Winter Park Avenue"
a62 = "Disney Spring Shops"
a63 = "Orlando Urban Trail"
a64 = "Disney's Magic Kingdom"
a65 = "Chicken Salad Chick"
a66 = "The Capital Grille"
a67 = "Clearwater Beach"
a68 = "Indian Rocks Beach"
a69 = "Westfield Citrus Mall"
a70 = "University Mall"
a71 = "Lettuce Lake Park"
a72 = "Lowry Park"
a73 = "Samaria Cafe"
a74 = "Ulele"
a75 = "Madeira Beach"
a76 = "Belleair Shores"
a77 = "Hyde Park Village"
a78 = "International Plaza"
a79 = "Cotanchobee Fort Brooke Park"
a80 = "Curtis Hixon Waterfront Park"
a81 = "Metro Diner"
a82 = "Eddie V's Prime Seafood"
a83 = "Sunset Beach"
a84 = "Redington Beach"
a85 = "WestShore Plaza"
a86 = "Centro Asturiano de Tampa"
a87 = "Ballast Point Park"
a88 = "Cypress Point Park"
a89 = "The Dubliner Irish Pub"
a90 = "Bern's Steak House"
a91 = "Pass-a-Grille Beach"
a92 = "St. Pete Beach"
a93 = "Centro Cantina"
a94 = "Centro Ybor"
a95 = "Kiley Gardens"
a96 = "Busch Gardens"
a97 = "Canopy Road Cafe"
a98 = "Lucilla"
a99 = "Cape San Blas"
a100 = "St. George Island"
a101 = "Miracle Plaza"
a102 = "Governor's Square"
a103 = "San Luis Mission Park"
a104 = "Sky Zone Trampoline Park"
a105 = "Hopkins Eatery"
a106 = "The Edison"
a107 = "Navarre Beach"
a108 = "Seaside, Florida"
a109 = "Sparkle Tallahassee"
a110 = "Bannerman Crossings Shopping Center"
a111 = "McCarty Park"
a112 = "Ponce De Leon Park"
a113 = "Aaru's Multicuisine Restaurant"
a114 = "Masa"
a115 = "Carrabelle Beach"
a116 = "Grayton Beach"
a117 = "Market Square Shopping Center"
a118 = "New Square"
a119 = "Lake Ella Park"
a120 = "Dorothy B. Oven Park"
a121 = "D.P. Dough Tallahassee"
a122 = "Andrew's Downtown"
a123 = "Panama City Beach"
a124 = "Pelican Beach"
a125 = "The Gallery at Market Street"
a126 = "Northampton Shopping Center"
a127 = "Bloxham Park"
a128 = "Cascades Park"




#attributes and made them all lowercase and invalid responses included

city = str(input("Which city? (Choose 1 between Miami, Orlando, Tampa, Tallahassee): "))
city = city.lower()

if city != "miami" and city != "orlando" and city != "tampa" and city != "tallahassee":
    print("Invalid response. Please start again.")




time = str(input("Daytime or nighttime?: "))
time = time.lower()

if time != "daytime" and time != "nighttime":
    print("Invalid response. Please start again.")





area = str(input("Suburban or urban?: "))
area = area.lower()

if area != "suburban" and area != "urban":
    print("Invalid response. Please start again.")




amenity = str(input("Which type of amenity? \n (Choose 1: restaurant, beach, shopping, park): "))
amenity = amenity.lower()

if amenity != "restaurant" and amenity != "beach" and amenity != "shopping" and amenity != "park":
    print("Invalid response. Please start again.")




budget = str(input("Is your budget low or high?: "))
budget = budget.lower()

if budget != "low" and budget != "high":
    print("Invlaid response. Please start again.")









placeholder = "The best place to go is "



# all if statements written below for input user


if city == "miami" and time == "daytime" and area == "suburban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a1)


if city == "miami" and time == "daytime" and area == "suburban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a2)


if city == "miami" and time == "daytime" and area == "suburban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a3)


if city == "miami" and time == "daytime" and area == "suburban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a4)


if city == "miami" and time == "daytime" and area == "suburban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a5)


if city == "miami" and time == "daytime" and area == "suburban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a6)


if city == "miami" and time == "daytime" and area == "suburban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a7)


if city == "miami" and time == "daytime" and area == "suburban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a8)


if city == "miami" and time == "daytime" and area == "urban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a9)


if city == "miami" and time == "daytime" and area == "urban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a10)


if city == "miami" and time == "daytime" and area == "urban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a11)


if city == "miami" and time == "daytime" and area == "urban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a12)


if city == "miami" and time == "daytime" and area == "urban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a13)


if city == "miami" and time == "daytime" and area == "urban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a14)


if city == "miami" and time == "daytime" and area == "urban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a15)


if city == "miami" and time == "daytime" and area == "urban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a16)


if city == "miami" and time == "nighttime" and area == "suburban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a17)


if city == "miami" and time == "nighttime" and area == "suburban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a18)


if city == "miami" and time == "nighttime" and area == "suburban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a19)


if city == "miami" and time == "nighttime" and area == "suburban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a20)


if city == "miami" and time == "nighttime" and area == "suburban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a21)


if city == "miami" and time == "nighttime" and area == "suburban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a22)


if city == "miami" and time == "nighttime" and area == "suburban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a23)


if city == "miami" and time == "nighttime" and area == "suburban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a24)



if city == "miami" and time == "nighttime" and area == "urban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a25)


if city == "miami" and time == "nighttime" and area == "urban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a26)


if city == "miami" and time == "nighttime" and area == "urban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a27)


if city == "miami" and time == "nighttime" and area == "urban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a28)


if city == "miami" and time == "nighttime" and area == "urban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a29)


if city == "miami" and time == "nighttime" and area == "urban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a30)


if city == "miami" and time == "nighttime" and area == "urban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a31)


if city == "miami" and time == "nighttime" and area == "urban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a32)


if city == "orlando" and time == "daytime" and area == "suburban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a33)


if city == "orlando" and time == "daytime" and area == "suburban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a34)


if city == "orlando" and time == "daytime" and area == "suburban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a35)


if city == "orlando" and time == "daytime" and area == "suburban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a36)


if city == "orlando" and time == "daytime" and area == "suburban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a37)


if city == "orlando" and time == "daytime" and area == "suburban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a38)


if city == "orlando" and time == "daytime" and area == "suburban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a39)


if city == "orlando" and time == "daytime" and area == "suburban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a40)


if city == "orlando" and time == "daytime" and area == "urban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a41)


if city == "orlando" and time == "daytime" and area == "urban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a42)


if city == "orlando" and time == "daytime" and area == "urban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a43)


if city == "orlando" and time == "daytime" and area == "urban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a44)


if city == "orlando" and time == "daytime" and area == "urban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a45)


if city == "orlando" and time == "daytime" and area == "urban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a46)


if city == "orlando" and time == "daytime" and area == "urban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a47)


if city == "orlando" and time == "daytime" and area == "urban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a48)


if city == "orlando" and time == "nighttime" and area == "suburban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a49)


if city == "orlando" and time == "nighttime" and area == "suburban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a50)


if city == "orlando" and time == "nighttime" and area == "suburban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a51)


if city == "orlando" and time == "nighttime" and area == "suburban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a52)


if city == "orlando" and time == "nighttime" and area == "suburban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a53)


if city == "orlando" and time == "nighttime" and area == "suburban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a54)


if city == "orlando" and time == "nighttime" and area == "suburban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a55)


if city == "orlando" and time == "nighttime" and area == "suburban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a56)


if city == "orlando" and time == "nighttime" and area == "urban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a57)


if city == "orlando" and time == "nighttime" and area == "urban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a58)


if city == "orlando" and time == "nighttime" and area == "urban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a59)


if city == "orlando" and time == "nighttime" and area == "urban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a60)


if city == "orlando" and time == "nighttime" and area == "urban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a61)


if city == "orlando" and time == "nighttime" and area == "urban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a62)


if city == "orlando" and time == "nighttime" and area == "urban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a63)


if city == "orlando" and time == "nighttime" and area == "urban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a64)


if city == "tampa" and time == "daytime" and area == "suburban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a65)


if city == "tampa" and time == "daytime" and area == "suburban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a66)


if city == "tampa" and time == "daytime" and area == "suburban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a67)


if city == "tampa" and time == "daytime" and area == "suburban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a68)


if city == "tampa" and time == "daytime" and area == "suburban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a69)


if city == "tampa" and time == "daytime" and area == "suburban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a70)


if city == "tampa" and time == "daytime" and area == "suburban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a71)


if city == "tampa" and time == "daytime" and area == "suburban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a72)


if city == "tampa" and time == "daytime" and area == "urban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a73)


if city == "tampa" and time == "daytime" and area == "urban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a74)


if city == "tampa" and time == "daytime" and area == "urban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a75)


if city == "tampa" and time == "daytime" and area == "urban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a76)


if city == "tampa" and time == "daytime" and area == "urban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a77)


if city == "tampa" and time == "daytime" and area == "urban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a78)


if city == "tampa" and time == "daytime" and area == "urban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a79)


if city == "tampa" and time == "daytime" and area == "urban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a80)


if city == "tampa" and time == "nighttime" and area == "suburban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a81)


if city == "tampa" and time == "nighttime" and area == "suburban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a82)


if city == "tampa" and time == "nighttime" and area == "suburban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a83)


if city == "tampa" and time == "nighttime" and area == "suburban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a84)


if city == "tampa" and time == "nighttime" and area == "suburban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a85)


if city == "tampa" and time == "nighttime" and area == "suburban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a86)


if city == "tampa" and time == "nighttime" and area == "suburban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a87)


if city == "tampa" and time == "nighttime" and area == "suburban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a88)


if city == "tampa" and time == "nighttime" and area == "urban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a89)


if city == "tampa" and time == "nighttime" and area == "urban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a90)


if city == "tampa" and time == "nighttime" and area == "urban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a91)


if city == "tampa" and time == "nighttime" and area == "urban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a92)


if city == "tampa" and time == "nighttime" and area == "urban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a93)


if city == "tampa" and time == "nighttime" and area == "urban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a94)


if city == "tampa" and time == "nighttime" and area == "urban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a95)


if city == "tampa" and time == "nighttime" and area == "urban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a96)


if city == "tallahassee" and time == "daytime" and area == "suburban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a97)


if city == "tallahassee" and time == "daytime" and area == "suburban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a98)


if city == "tallahassee" and time == "daytime" and area == "suburban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a99)


if city == "tallahassee" and time == "daytime" and area == "suburban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a100)


if city == "tallahassee" and time == "daytime" and area == "suburban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a101)


if city == "tallahassee" and time == "daytime" and area == "suburban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a102)


if city == "tallahassee" and time == "daytime" and area == "suburban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a103)


if city == "tallahassee" and time == "daytime" and area == "suburban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a104)


if city == "tallahassee" and time == "daytime" and area == "urban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a105)


if city == "tallahassee" and time == "daytime" and area == "urban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a106)


if city == "tallahassee" and time == "daytime" and area == "urban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a107)


if city == "tallahassee" and time == "daytime" and area == "urban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a108)


if city == "tallahassee" and time == "daytime" and area == "urban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a109)


if city == "tallahassee" and time == "daytime" and area == "urban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a110)


if city == "tallahassee" and time == "daytime" and area == "urban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a111)


if city == "tallahassee" and time == "daytime" and area == "urban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a112)


if city == "tallahassee" and time == "nighttime" and area == "suburban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a113)


if city == "tallahassee" and time == "nighttime" and area == "suburban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a114)


if city == "tallahassee" and time == "nighttime" and area == "suburban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a115)


if city == "tallahassee" and time == "nighttime" and area == "suburban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a116)


if city == "tallahassee" and time == "nighttime" and area == "suburban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a117)



if city == "tallahassee" and time == "nighttime" and area == "suburban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a118)


if city == "tallahassee" and time == "nighttime" and area == "suburban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a119)


if city == "tallahassee" and time == "nighttime" and area == "suburban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a120)


if city == "tallahassee" and time == "nighttime" and area == "urban" and amenity == "restaurant" and budget == "low":
    print("")
    print(placeholder + a121)


if city == "tallahassee" and time == "nighttime" and area == "urban" and amenity == "restaurant" and budget == "high":
    print("")
    print(placeholder + a122)


if city == "tallahassee" and time == "nighttime" and area == "urban" and amenity == "beach" and budget == "low":
    print("")
    print(placeholder + a123)


if city == "tallahassee" and time == "nighttime" and area == "urban" and amenity == "beach" and budget == "high":
    print("")
    print(placeholder + a124)


if city == "tallahassee" and time == "nighttime" and area == "urban" and amenity == "shopping" and budget == "low":
    print("")
    print(placeholder + a125)


if city == "tallahassee" and time == "nighttime" and area == "urban" and amenity == "shopping" and budget == "high":
    print("")
    print(placeholder + a126)


if city == "tallahassee" and time == "nighttime" and area == "urban" and amenity == "park" and budget == "low":
    print("")
    print(placeholder + a127)


if city == "tallahassee" and time == "nighttime" and area == "urban" and amenity == "park" and budget == "high":
    print("")
    print(placeholder + a128)
