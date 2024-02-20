import time


def hello():
    return "Hello, world from function!"


print(hello())


def hello_gen():
    yield "Hello, world from generator!"


gen = hello_gen()
print(next(gen))


# Up until 100 million elements, the list is faster than the generator


def my_range(max_count):
    current = 0
    while current < max_count:
        yield current
        current += 1


list_count = 2*10**8


def run_generator():
    start_time = time.time()
    gen = my_range(list_count)
    about_to_start_time = time.time()
    print(f"Starting time: {about_to_start_time - start_time:.6f}")
    for i in gen:
        if i % 10000000 == 0:
            print(i)
    end_time = time.time()
    print(f"List processing time: {end_time - about_to_start_time:.6f}")
    print(f"Elapsed time: {end_time - start_time}")


def run_list():
    start_time = time.time()
    eager_loaded_list = list(my_range(list_count))
    about_to_start_time = time.time()
    print(f"Starting time: {about_to_start_time - start_time:.6f}")
    for i in eager_loaded_list:
        if i % 10000000 == 0:
            print(i)
    end_time = time.time()
    print(f"List processing time: {end_time - about_to_start_time:.6f}")
    print(f"Elapsed time: {end_time - start_time}")