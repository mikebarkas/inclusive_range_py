#!/usr/bin/python


class InclusiveRange:

    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1:
            raise TypeError('Requires at least one argument')

        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('maximum 3 arguments')

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

def main():

    for i in InclusiveRange(30):
        print(i)

if __name__ == "__main__":
    main()
