# A byte literal contains a non-ASCII character
s = b'№5№5'

# Assignments to 'for' loop or 'with' statement parameter
for i in range(5):
  for i in range(20, 25):
      print("Inner", i)
  print("Outer", i)

# Incorrect type
def foo() -> str:
    return 123 # Expected str, got int

a: int
a = foo() # Expected int, got str

# Unreachable code
if True:
    print('Yes')
else:
    print('No')

condition = 123 > 122
if condition or not condition:
    print('Yes')
else:
    print('No')


