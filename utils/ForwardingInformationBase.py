class ForwardingInformationBase:
    def __init__(self, size):
        self.fib = {}
        self.size = size

    def add(self, name, interface):
        if len(self.fib) >= self.size:
            print("FIB is full")
            return False
        self.fib[name] = interface
        return True


    def lookup(self, name):
        return self.fib[name]