import concurrent.futures
import multiprocessing
import random as rd
import time
import threading


class Trapezoid:
    def __init__(self, digit=None):
        if digit is None:
            digit = [0, 0, 0]
        self.side1 = digit[0]
        self.side2 = digit[1]
        self.height = digit[2]

    def __str__(self):
        return f'Trapezoid sides are: first side = {self.side1}, second side = {self.side2}, and height = {self.height}'

    def area(self):
        return ((self.side1 + self.side2) / 2) * self.height

    def __lt__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() < other.area()
        return False

    def __eq__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() == other.area()

    def __ge__(self, other):
        if isinstance(other, Trapezoid):
            return not self.__lt__(other)
        return False


class Rectangle(Trapezoid):
    def __init__(self, digit):
        super().__init__(digit)
        # super().__init__([self.side1, self.side1, self.height])
        self.height = None

    def __str__(self):
        return f'Rectangle sides are: First Side = {self.side1} and Second Side = {self.side2}'

    def area(self):
        return self.side1 * self.side2


class Square(Rectangle):
    def __init__(self, digit):
        super().__init__(digit)
        # super().__init__([self.side1, self.side1, self.height])
        self.side2 = None
        self.height = None

    def __str__(self):
        return f'Square Sides are: {self.side1}'

    def area(self):
        return self.side1 * self.side1


# functions to calculate generate areas
def trapezoid_area(arr):
    for i in arr:
        T = Trapezoid(i)
        T.area()
        # you can print here parameters if you want
        # print(T, "Area", T.area())


def rectangle_area(arr):
    for i in arr:
        R = Rectangle(i)
        R.area()
        # you can print here parameters if you want
        # print(R, "Area",  R.area())


def square_area(arr):
    for i in arr:
        S = Square(i)
        S.area()
        # you can print here parameters if you want
        # print(S, "Area", S.area())


# this function is used to calculate time to compute areas of 10 000 trapezoid, rectangle and square in general without threads or processes
def regular(arr):
    start = time.perf_counter()

    trapezoid_area(arr)
    rectangle_area(arr)
    square_area(arr)

    finish = time.perf_counter()

    print('in general Finished in: ', round(finish - start, 2), 'second(s)')


# this function is used to calculate time to compute areas of 10 000 trapezoid, rectangle and square using threads
def threads(params):
    thread_list = []
    start1 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # here I give any range of page to map function which take any params and forms it into list
        thread_results = list(executor.map(Trapezoid, params))
        thread_list.extend(thread_results)  # Here I'm extending size of thread_list with results
    finish1 = time.perf_counter()
    print('with threads Finished in: ', round(finish1 - start1, 2), 'second(s)')


# def threads(arr):
#     start1 = time.perf_counter()
#
#     t1 = threading.Thread(target=trapezoid_area, args=(arr,))
#     t1.start()
#     t2 = threading.Thread(target=rectangle_area, args=(arr,))
#     t2.start()
#     t3 = threading.Thread(target=square_area, args=(arr,))
#     t3.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#
#     finish1 = time.perf_counter()
#     print('with threads Finished in: ', round(finish1 - start1, 2), 'second(s)')


# this function is used to calculate time to compute areas of 10000 trapezoid, rectangle and square using processes
def multiprocess(arr):
    start2 = time.perf_counter()
    ranges = [(1, 21), (20, 41), (40, 61), (60, 81), (80, 101)]  # range where threads should move
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = list(executor.map(threads, [arr] * len(ranges)))  # Pass arr to threads for each range
    finish2 = time.perf_counter()
    print('with pools Finished in: ', round(finish2 - start2, 2), 'second(s)')
    return result


# def multiprocess(arr):
#     start2 = time.perf_counter()
#
#     p1 = multiprocessing.Process(target=trapezoid_area, args=(arr,))
#     p2 = multiprocessing.Process(target=rectangle_area, args=(arr,))
#     p3 = multiprocessing.Process(target=square_area, args=(arr,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#
#     finish2 = time.perf_counter()
#     print('with pools Finished in: ', round(finish2 - start2, 2), 'second(s)')

# First Try
# in general Finished in:  0.23 second(s)
# with pools Finished in:  0.57 second(s)
# with threads Finished in:  0.24 second(s)

# Second Try
# in general Finished in:  0.23 second(s)
# with pools Finished in:  0.58 second(s)
# with threads Finished in:  0.24 second(s)


if __name__ == "__main__":
    # Generating parameters for 10,000 trapezoid: big base, small base, and height
    trapezoids = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for _ in range(10000)]

    # Generating parameters for 10,000 rectangles: width and height
    rectangles = [[rd.randint(1, 200), rd.randint(1, 200)] for _ in range(10000)]

    # Generating parameters for 10,000 squares
    squares = [rd.randint(1, 200) for _ in range(10000)]

    # print(result_multiprocess)  # Print or process the result as needed

    regular(trapezoids)
    multiprocess(trapezoids)
    threads(trapezoids)

# after lot try I think best time is this
# in general Finished in:  0.01 second(s)
# with threads Finished in:  0.15 second(s)
# with threads Finished in:  0.17 second(s)
# with threads Finished in:  0.15 second(s)
# with threads Finished in:  0.16 second(s)
# with threads Finished in:  0.17 second(s)
# with pools Finished in:  0.4 second(s)
# with threads Finished in:  0.11 second(s)
