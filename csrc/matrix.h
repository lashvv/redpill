#ifndef REDPILL_MATRIX_H
#define REDPILL_MATRIX_H

#include <stddef>

typedef struct {
    double *data;
    size_t rows;
    size_t columns;
} Matrix;

#endif