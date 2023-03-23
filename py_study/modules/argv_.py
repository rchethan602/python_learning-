import sys
#print('hello')
#print(sys.argv)

if len(sys.argv) !=3:
    print("usage:")
    print(f"{sys.argv[0]} <your request string> <lower|upper|title")
    sys.exit(2)

usr_str=sys.argv[1]
usr_action=sys.argv[2]

if usr_action == "lower":
    print(usr_str.lower())
elif usr_action == "upper":
    print(usr_str.upper())
else:
    print(usr_str.title())
