x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])
"test"
["t","e","s","t"]

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)

sentence = input("Please input a sentence: ")
def count_words(sentence):
    words = sentence.split()
    count = 0

    for word in words:
        count+=1

    return count
print(count_words(sentence))

day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

x = "test"
print(f"hello {x}")
temp = 75
if temp > 68:
    print('warm')
elif temp ==68:
    print('perfect')
else:
    print('cold')

service = input("bad,okay,good, or great service: ")
def tip(bill,service):
    if service=="bad":
        return bill * 0
    elif service=="okay":
        return bill*0.15
    elif service=="good":
        return bill * 0.20
    elif service=="great":
        return bill * 0.25
    else:
        return "Invalid service rating"
bill = float(input("Enter the bill: "))
print("Tip: ", tip,(bill, service))

number = int(input("Please input a number: "))
def odd_or_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

print(odd_or_even(number))
    