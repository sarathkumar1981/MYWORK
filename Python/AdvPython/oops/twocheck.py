# file two.py
import onecheck

print("top-level in two.py")
onecheck.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")

