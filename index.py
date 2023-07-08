from pyscript import when

@when("click", "button")
def press():
    print("hello")