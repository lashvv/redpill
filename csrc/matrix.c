#include "matrix.h"
#include <stdlib.h>

Matrix *matrix_create(size_t rows, size_t columns)
{
    Matrix *matrix = malloc(sizeof(Matrix));

    if (matrix == NULL)
        return NULL;

    matrix->rows = rows;
    matrix->columns = columns;
    matrix->data = malloc(rows * columns * sizeof(double));

    if (matrix->data == NULL)
    {
        free(matrix);
        return NULL;
    }

    return matrix;
}

void matrix_free(Matrix *matrix)
{
    if (matrix == NULL)
        return;

    free(matrix->data);
    free(matrix);
}