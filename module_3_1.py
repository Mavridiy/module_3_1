
calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    len_ = len(string)
    a = string.upper()
    b = string.lower()
    tup_ = (len_, a, b)
    print(tup_)


def is_contains(string, list_to_search):
    count_calls()
    list_to_search_ = list_to_search
    string_ = string
    res = any(ele in string_ for ele in list_to_search_)
    print(res)


string_info('CAPYBARA')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)


