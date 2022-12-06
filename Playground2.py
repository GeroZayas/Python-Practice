class User:
    def __init__(self, rank=None, progress=None):
        if rank is None:
            rank = -8
        if progress is None:
            progress = 0

        self.rank = rank
        self.progress = progress


user = User()

print(user.rank)
print(user.progress)
