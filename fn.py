def f1():
    s= "hello"
    def f2():
        s="Good Morning"
        print(s)
    f2()
    print(s)
f1()