calls=0

def count_calls():
   global calls
   calls+=1

def string_info(string):
    count_calls()
    tuple_=(len(string),string.lower(),string.upper())
    return tuple_

def is_contains(string,list_to_search):
    count_calls()
    string=string.upper()
    for i in range(len(list_to_search)):
        list_to_search[i]=list_to_search[i].upper()
    # print(list_to_search)
    return True if string in list_to_search else False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)