#hello() prints a greeting and returns nothing
def hello():
    print("Hello, dear user!")
#pack() takes three arguments and returns a list of all three
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]
#eat_lunch accepts a list and eats the things in the list
def eat_lunch(list):
    for i, food in enumerate(list):
        if i == 0:
            print("First I eat " + food)
        else:
            print("Next I eat " + food)
    print("my lunchbox is empty!")

#call the functions
hello()
packed_lunch = pack("apple","PB&J","cookie")
eat_lunch(packed_lunch)
