def posfun(arg1,*vartuple):
    print("Output is:",arg1)
    for var in vartuple:
        print(var)
    return;
posfun(10)
posfun(23,45,43)