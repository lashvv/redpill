class Matrix:
    def __init__(self, data):
        self.data = data

        self.is_empty()

        self.rows = len(data)
        self.columns = len(data[0])

        self.validate()

    def validate(self):
        for row in self.data:
            if len(row) != self.columns:
                raise ValueError("All rows must have the same number of columns.")
    def is_empty(self):
        if len(self.data) == 0 or len(self.data[0]) == 0:
            raise ValueError("Matrix cannot be empty.")
