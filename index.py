from pyscript import when

@when("click", "button")
def hello():
    print("hello")