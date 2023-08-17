# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def sumacplx(c1,c2):
    parteR=c1[0]+c2[0]
    parteI=c1[1]+c2[1]
    return (parteR,parteI)

def multcplx(a,b):
    realx = a[0]*b[0] - a[1]*b[1]
    imagx = b[0]*a[1] + b[1]*a[0]
    return realx, imagx


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(sumacplx((3,2),(-5, 5.2)))
    print(multcplx((3,2),(-5, 5.2)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
