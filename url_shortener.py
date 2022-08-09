#dont steal my code ffs
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
 print(" ")
    import pyshorteners
    link = input("Enter the link:   ")
    s = pyshorteners.Shortener()
    #code by DevVarun (malware)
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

xyz_pro_plus = 1

while (xyz_pro_plus < 2):
    restart_and_exit()