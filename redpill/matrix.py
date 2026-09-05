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

    def shape(self):
        return (self.rows, self.columns)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        if self.shape() != other.shape():
            return False

        for i in range(self.rows):
            for j in range(self.columns):
                if self.data[i][j] != other.data[i][j]:
                    return False
        
        return True

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only add another Matrix.")

        if self.shape() != other.shape():
            raise ValueError("Matrices must have the same dimensions for addition.")

        result_data = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self.data[i][j] + other.data[i][j])
            result_data.append(row)

        return Matrix(result_data)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only subtract another Matrix.")

        if self.shape() != other.shape():
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        result_data = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self.data[i][j] - other.data[i][j])
            result_data.append(row)

        return Matrix(result_data)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Can only multiply by a scalar")

        result_data = []
        for i in range(self.rows):
            rows = []
            for j in range(self.columns):
                rows.append(self.data[i][j] * scalar)
            result_data.append(rows)

        return Matrix(result_data)

    def __str__(self):
        rows = []

        for row in self.data:
            row_string = " ".join(str(value) for value in row)
            rows.append(f"[{row_string}]")

        return "\n".join(rows)