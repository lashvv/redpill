#ifndef REDPILL_MATRIX_H
#define REDPILL_MATRIX_H

#include <stddef.h>

typedef struct {
    double *data;
    size_t rows;
    size_t columns;
} Matrix;

#endif

Matrix *matrix_create(size_t rows, size_t columns);
void matrix_free(Matrix *matrix);