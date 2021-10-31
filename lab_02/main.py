from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():

    r = Rectangle("оранжевого", 2, 2)
    c = Circle("белого", 2)
    s = Square("синего", 2)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
