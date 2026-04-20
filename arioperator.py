# Arithmetic Operators

# Addition
from ast import Not


x = 10;
y = 30;
val = x + y;
print(val);

# Subtraction
val = x - y;
print(val);

# Multiplication
val = x * y;
print(val);

# Division
val = x / y;
print(val);

# Modulus
val = x % y;
print(val);

# Exponentiation
val = x ** y;
print(val);

# Floor Division
val = x // y;
print(val);

# Comparison Operators an if action to get a result
# Equal
val = x == y;
print(val);

# Not Equal
val = x != y;
print(val);

val = x <= y;
print(val);

val = x < y;
print(val);

# Logical operator
val = (x == 5 and x < 6);
print(val);


val = (x == 10 or x < 6);
print(val);


val = not(x == 5);
print(val);

# identity operator is | is not;

val = x is y;
print(val);

val = x is not y;
print(val);

# Membership operator in | is not;
fruit = ["orange", "apple", "mango"];
result = "tomato" in fruit;

print(result);

result = "tomato" not in fruit;

print(result);