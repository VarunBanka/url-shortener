import pyshorteners
def start():
    print("*     *   *****  *")
    print("*     *   *  *   *")
    print("*     *   ****   *")
    print("*     *   **     *")
    print("*******   * *    *****")
    print("\n")
    print("     ****   *    *   ****   ****   *****   *****   **    *   *****   *****")
    print("     *      *    *   *  *   *  *     *     *       * *   *   *       *   *")
    print("     ****   ******   *  *   ****     *     ***     *  *  *   ***     *****")
    print("        *   *    *   *  *   **       *     *       *   * *   *       **")
    print("     ****   *    *   ****   * *      *     *****   *    **   *****   * *")

    link = input("Enter the link:   ")
    s = pyshorteners.Shortener()
    print("here's your link \n")
    #code by Varun Banka
    print(s.tinyurl.short(link))
start()

def restart_and_exit():
    print("do you want to restart ? \n")
    restart = input("y/n \n")
    if restart == "y":
        start()
    if restart == "n":
        print("okay, exiting.....")
        print("end of program")
        exit()

restart_and_exit()

