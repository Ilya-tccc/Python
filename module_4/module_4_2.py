def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function() Вызов невозможен, т.к. функция определена только в пределах функции test_function