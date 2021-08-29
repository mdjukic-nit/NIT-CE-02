import check50

@check50.check()
def exists():
    """pozdrav.c exists."""
    check50.exists("pozdrav.c")

@check50.check(exists)
def compiles():
    """no syntax errors in pozdrav.c."""
    check50.run("gcc pozdrav.c -opozdrav").exit(0)

@check50.check(compiles)
def prints():
    """prints 3 messages"""
    check50.run("./pozdrav").stdout("Pozdrav svete!\nPozdrav svete!\nPozdrav svete!\n").exit(0)
