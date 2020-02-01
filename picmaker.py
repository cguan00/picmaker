from random import seed
from random import randint

#250000 total pixels

def main():
    seed(2)
    output = "P3\n500 500\n255\n" #header

    for i in range(10):
        a = randint(0,256)
        b = randint(0,256)
        c = randint(0,256)

        d = randint(0,256)
        e = randint(0,256)
        f = randint(0,256)

        for j in range(25000):

            if j % 10 < 3:
                output += str(a) + " " + str(b) + " " + str(c)
                output += "\n"
            else:
                output += str(d) + " " + str(e) + " " + str(f)
                output += "\n"


    f = open("pic.ppm", "w+")
    f.write(output)
    f.close()

main()
