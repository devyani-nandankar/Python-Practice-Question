def testfun(arg):
    print("Inside the fun",id(arg))
var="Hello This Is My First Program"
print("Before the passing",id(var))
testfun(var)