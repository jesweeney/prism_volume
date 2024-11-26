#Jessica Sweeney
print("************\n")


length = float(input("Please enter prism length=>"))
height = float(input("Please enter prism height=>"))
base_w = float(input("Please enter prism base width=>"))
top_w = float(input("Please enter prism top width=>"))
#gaathering and storing information about the prism from the user to be used in calculations later

#r_length = str(round(length, 1))
#r_height = str(round(height, 1))
#r_base_w = str(round(base_w, 1))
#r_top_w = str(round(top_w, 1))
#the four lines of code was my original process of how I was going to round the decimal place of the numbers before going over using f strings to round in class

volume = length*height*((base_w+top_w)/2)

print(f"Prism length is: {length:.1f}")
print(f"Prism height is: {height:.1f}")
print(f"Prism base width: {base_w:.1f}")
print(f"Prism top width: {top_w:.1f}")
print(f"Prism volume: {volume:.1f}")
print("  ")
#displaying rounded prism measurements and volume using f strings to round

length = length-(length*.25)
height = height-(height*.25)
base_w = base_w-(base_w*.25)
top_w = top_w-(top_w*.25)
volume = length*height*((base_w+top_w)/2)
#calculations done to reduce given measurements by 25 percent. calculates colume after measurements have been reduced

print("Prism measurements after 25% reduction")
print("  ")
print(f"Prism reduced length is: {length:.1f}")
print(f"Prism reduced height is: {height:.1f}")
print(f"Prism reduced base width: {base_w:.1f}")
print(f"Prism reduced top width: {top_w:.1f}")
print(f"Prism reduced volume: {volume:.1f}")
#displaying prism measurements and volume after being reduced by 25 percent

print("\n************")