import inspect


app = []


def register_dependency(func):
    app.append(func)


indentation = "    "

def dep_1():
    print("print preprocessor 1")
    yield "Hello, world from generator 1!"
    print("print postprocessor 1")


def dep_2():
    print(f"{indentation}print preprocessor 2")
    return f"{indentation}Hello, world from generator 2!"


def dep_3():
    print(f"{indentation * 2}print preprocessor 3")
    yield f"{indentation * 2}Hello, world from generator 3!"
    print(f"{indentation * 2}print postprocessor 3")


def route():
    return f"{indentation * 3}Hello, world from route!"


register_dependency(dep_1)
register_dependency(dep_2)
register_dependency(dep_3)


def process_request():
    generators = []
    for dep in app:
        if inspect.isgeneratorfunction(dep):
            gen = dep()
            generators.append(gen)
            print(next(gen))
        else:
            print(dep())
    print(route())
    for gen in generators[::-1]:
        try:
            print(next(gen))
        except StopIteration:
            pass
