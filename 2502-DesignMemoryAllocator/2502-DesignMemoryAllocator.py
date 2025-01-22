class Allocator:

    def __init__(self, n: int):
        self.memory = [None] * n
        
    def allocate(self, size: int, mID: int) -> int:
        lp = 0
        rp = None
        for i in range(len(self.memory)):
            if self.memory[i] != None:
                lp = i+1
            if (i - lp) +1 == size:
                rp = i
                break

        
        if rp == None:
            return -1
        else:
            for i in range(lp,rp+1):
                self.memory[i] = mID
            return lp



    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = None
                freed += 1
        return freed      


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)