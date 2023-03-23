import os

path=input("provide your new workin=g directory: ")

def main():
    try:
        os.chdir(path)
        print("now your current directory is:", os.getcwd())
    except FileNotFoundError:
        print("Gvien path is not valid")
    except NotADirectoryError:
        print("not a directory")
    except PermissionError:
        print("no permission")

if __name__=="__main__":
    main()
