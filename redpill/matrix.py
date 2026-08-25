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

    def __getitem__(self, index):
        row, column = index
        return self.data[row][column]

    def __setitem__(self, index, value):
        row, column = index
        self.data[row][column] = value

    def __str__(self):
        rows = []

        for row in self.data:
            row_string = " ".join(str(value) for value in row)
            rows.append(f"[{row_string}]")

        return "\n".join(rows)

# A = Matrix([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])