import check50

@check50.check()
def exists():
    """hello.c exists."""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """no syntax errors in hello.c."""
    check50.run("gcc hello.c -ohello").exit(0)

@check50.check(compiles)
def prints():
    """prints 3 messages"""
    check50.run("./hello").stdout("Hello world!\nHello world!\nHello world!\n").exit(0)
