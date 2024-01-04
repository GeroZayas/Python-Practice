def looping():
    names = "Mar Gero Manel Silvia".split()
    for name in names:
        pass
    print(name)
    print("LOCALS INSIDE function")
    print(locals())


r = looping()
print(r)

print("LOCALS OUTSIDE function")
print(locals())
