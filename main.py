import glob
import os

from xhair import XHair

def xhairlist() -> list or None:
    paths = glob.glob(f"./crosshairs/*.png")
    filenames = list(map(os.path.basename, paths))
    return filenames
    
def main():
    options: dict = {}
    xhairfiles = xhairlist()
    if xhairfiles == None:
        print("No crosshairs found.")
    else:
        for c, i in enumerate(xhairfiles, start=1):
            options[str(c)] = i
            print(f"{c}: {i}")
        while True:
            option = input("Number of your crosshair: ")
            if option in options.keys():
                break
            else:
                print("Invalid answer.")
                print("")
                continue

        chosen = options[option]
        print(chosen)
        print(f"Choosing {chosen}")
        print("")

        r = input("Ratio (in px, same number will be user for both width and height): ")

        xhair = XHair(r=int(r))
        xhair.use(imgpath=f"crosshairs/{chosen}")




if __name__ == '__main__':
    main()