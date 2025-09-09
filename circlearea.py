#computes the area of the circle
def area(radius):
    return radius ** 2 * 3.1416
#checks if the value can be a float, if yes converts it to a float and returns it, and if not, returns an error and exits
def check(value):
    try: 
        return float(value)
    except ValueError:
        print("Sorry, that is not a float!")
        exit(1)
def checkp(value):
    if 0 >= value:
        print("Sorry, radius must be positive!")
        exit(1)
    return value
#taking the input
iradius = input("What is the radius of the circle?\n")
#checking if output radius 
radius = checkp(check(iradius))
#outputting the result
print(f"The area of your circle is: {round(area(radius), 2)}")