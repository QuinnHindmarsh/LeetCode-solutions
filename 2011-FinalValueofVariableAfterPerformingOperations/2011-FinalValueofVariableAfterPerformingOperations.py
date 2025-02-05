class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for o in operations:
            x += 1 if o[1] == '+' else -1

        return x