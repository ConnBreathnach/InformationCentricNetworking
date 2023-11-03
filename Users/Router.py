from ..utils import PendingInterestTable, ForwardingInformationBase, ContentStore


class Router:
    def __init__(self, PIT_size, FIB_size, CS_size):
        self.PIT = PendingInterestTable(PIT_size)
        self.FIB = ForwardingInformationBase(FIB_size)
        self.CS = ContentStore(CS_size)


