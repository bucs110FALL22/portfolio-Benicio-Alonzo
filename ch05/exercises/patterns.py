def rstar_pyramid(r):

    while r != 0:
        print("*" * r)
        r -= 1


def star_pyramid():
    print("How many rows of stars do you want? ")
    row = int(input(""))
    for i in range(row):
      
      print("*" * (i+1))
    rstar_pyramid(row)


star_pyramid()
