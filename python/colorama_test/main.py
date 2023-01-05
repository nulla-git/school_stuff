#Blake Reneau 01/05/23
#colorama test
from colorama import Fore, Back, Style

#this is just an ansii escape code example, doesn't relate to colorama.
print("\033[1;32;40m Bright Green \n")
print(Fore.RED + "some red test")
print(Back.GREEN + "some with a green background")
print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")
print(Fore.BLUE + "B" + Fore.GREEN + "l" + Fore.CYAN + "a" + Fore.MAGENTA + "k" + Fore.LIGHTBLUE_EX + "e")
print(Fore.LIGHTCYAN_EX + "R" + Fore.YELLOW + "e" + Fore.LIGHTYELLOW_EX + "n" + Fore.LIGHTMAGENTA_EX + "e" + Fore.LIGHTGREEN_EX + "a" + Fore.LIGHTRED_EX + "u")
print(Style.RESET_ALL)
