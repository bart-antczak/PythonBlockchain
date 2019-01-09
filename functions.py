def unlimited_arguments(*args):
    print(args)
    for argument in args:
        print(argument)


unlimited_arguments(*[1, 2, 3, 4])
