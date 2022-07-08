
def banner():
    print("")
    print("\033[1;31m88888888888Y88b   d88P           d8888 .d8888b.  ")
    print("\033[1;31m    888     Y88b d88P           d88888d88P  Y88b ")
    print("\033[1;31m    888      Y88o88P           d88P888888    888 ")
    print("\033[1;33m    888       Y888P           d88P 888888        ")
    print("\033[1;33m    888       d888b          d88P  888888        ")
    print("\033[1;33m    888      d88888b        d88P   888888    888 ")
    print("\033[1;31m    888     d88P Y88b      d8888888888Y88b  d88P ")
    print("\033[1;31m    888    d88P   Y88b    d88P     888 'Y8888P' ʙʏ ᴍʀ.ᴛʜᴇɴᴜx  ")
    print("")

banner()

def areacalculator():
    
    print("")
    print("\033[1;34m[ \033[1;33m1 \033[1;34m] \033[1;34mSquare")
    print("\033[1;36m[ \033[1;33m2 \033[1;36m] \033[1;36mCircle")
    print("\033[1;34m[ \033[1;33m3 \033[1;34m] \033[1;34mRectangle")
    print("\033[1;36m[ \033[1;33m4 \033[1;36m] \033[1;36mTriangle")
    print("")

    _input_ = input("\033[1;32mEnter the Number of the Shape you want to Calculate the Area of :  \033[1;33m")
    area = 0
    pie = 3.14
    if _input_ == "1":
        side = int(input("\033[1;32mEnter the Value of Side: \033[1;33m"))
        area = area + (side ** 2)
    elif _input_ == "2":
        radius = int(input("\033[1;32mEnter the Value of Radius: \033[1;33m"))
        area = area + (2 * pie * radius)
    elif _input_ == "3":
        length = int(input("\033[1;32mEnter the Value of Length: \033[1;33m"))
        width = int(input("\033[1;32mEnter the Value of Width: \033[1;33m"))
        area = area + (length * width)
    elif _input_ == "4":
        base = int(input("\033[1;32mEnter the Value of Base: \033[1;33m"))
        height = int(input("\033[1;32mEnter the Value of Height: \033[1;33m"))
        area = area +(0.5 * base * height)
    else:
        print ("\033[1;31mSelect a valid Shape!")
    print ("\033[1;32mAnswer: \033[1;33m%.2f" % area)

areacalculator()