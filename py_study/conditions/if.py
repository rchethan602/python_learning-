import os

given_str=input("Enter your string: ")
print(given_str)

usr_conf=input("Do you want to align this(yes/no): ")
usr_conf_case=usr_conf.lower()

if usr_conf_case == 'yes' :
    t_w=os.get_terminal_size().columns
    print(given_str.center(t_w).title())
    print(given_str.ljust(t_w).title())
    print(given_str.rjust(t_w).title())
