def greeting(name: str, surname: str):
    print(f"Hello {name} {surname}! You just delved into Python. Great start!")


def draw_figure():
    thickness = 5
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

        # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

        # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6))


def make_title(text: str):
    print(text.title())


def money_format(money: int):
    print("{0:,}".format(money))


def mat_designer(height: int):
    width = 3 * height

    for stick_count in range(1, height, 2):
        print((':X:' * stick_count).center(width, '*'))

    print('WELCOME'.center(width, '-'))

    for stick_count in range(height - 2, 0, -2):
        print((':X:' * stick_count).center(width, '*'))




def main():
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    greeting(name, surname)

    draw_figure()

    string = input("Please enter any sequence of words: ")
    make_title(string)

    money = float(input("Please enter amount of money: "))
    money_format(money)

    height = int(input("Please enter mat's height: "))
    mat_designer(height)


if __name__ == '__main__':
    main()
