from pyscript import when

while True:
    print("loop")

@when("click", "button")
def hello():
    print("hello")