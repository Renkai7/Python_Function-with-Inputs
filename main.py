# Simple Function
def greet():
  print("Hello")
  print("Konnichiwa")
  print("Bonjour")
# greet()

# Function that allows for input
def greet_with_name(name):
  print(f"Hello, {name}")
  print(f"Konnichiwa, {name}")
  print(f"Bonjour, {name}")
# greet_with_name("Mike")

# Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")
# greet_with("Jack Buaer", "Nowhere")

# Functions with keyword arguments
greet_with(name = "Jack", location = "Nowhere")

