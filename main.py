# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

print(add_time("11:06 AM", "2:55", "monday"))
print("\n")
print(add_time("3:00 PM", "3:10"))
print("\n")
print(add_time("11:30 AM", "2:32", "Monday"))
print("\n")
print(add_time("11:43 AM", "00:20"))
print("\n")
print(add_time("10:10 PM", "3:30"))
print("\n")
print(add_time("11:43 PM", "24:20", "tueSday"))
print("\n")
print(add_time("6:30 PM", "205:12"))
print("\n")

print(add_time("6:30 PM", "35:12"))
print("\n")
print(add_time("7:00 AM", "24:12"))
print("\n")
print(add_time("7:43 PM", "25:12", "friday"))
print("\n")
print(add_time("11:30 PM", "25:12"))
print("\n")
print(add_time("6:30 AM", "205:12", "tuesday"))
print("\n")
print(add_time("6:30 PM", "205:12", "monday"))
print("\n")

# Run unit tests automatically
#main(module='test_module', exit=False)
