class PendingInterestTable:
    def __init__(self, size):
        self.table = {}
        self.size = size

    def lookup(self, name):
        return self.table.get(name)

    def insert(self, name, interest, incoming_face=None, outgoing_face=None):
        if len(self.table) >= self.size:
            print("PIT is full")
            return False
        if name in self.table:
            self.table[name].add_incoming_face(incoming_face)
            self.table[name].add_outgoing_face(outgoing_face)
        else:
            self.table[name] = PITInterest(interest, incoming_face, outgoing_face)
        return True



class PITInterest:
    def __init__(self, interest, incoming_face=None, outgoing_face=None):
        self.interest = interest
        self.incoming_faces = [incoming_face]
        self.outgoing_faces = [outgoing_face]

    def get_interest(self):
        return self.interest

    def get_incoming_face(self):
        return self.incoming_faces

    def get_outgoing_face(self):
        return self.outgoing_faces

    def add_incoming_face(self, face):
        self.incoming_faces.append(face)

    def add_outgoing_face(self, face):
        self.outgoing_faces.append(face)

    def __str__(self):
        return self.interest.get_name()

