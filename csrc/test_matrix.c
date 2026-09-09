#include "matrix.h"
#include <stdio.h>

int main(void)
{
    Matrix *matrix = matrix_create(2, 2);

    if (matrix == NULL)
    {
        printf("Failed to create matrix\n");
        return 1;
    }

    for (int i = 0; i < matrix->rows * matrix->columns; i++)
    {
        matrix->data[i] = i + 1;
    }

    printf("%f %f\n", matrix->data[0], matrix->data[1]);
    printf("%f %f\n", matrix->data[2], matrix->data[3]);

    matrix_free(matrix);

    return 0;
}