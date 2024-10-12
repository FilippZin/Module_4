def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

# Работает
test_function()
# Не работает - так как находится только в зоне видимоти test_function
#inner_function()

