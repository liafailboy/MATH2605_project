# MATH2605_project
Calc lll for CS at Georgia Tech.

## Sam

Problems d) and e) and writing section 1 (Hilbert Matrix)

## Jessica

Writing code to read/write matrix files, a), and writing sections 2 and 3 (Iterative Method and Power Method)

## Shotaro
b) and c)

# Execution Instructions

## (a) `lu_fact`: LU Decomposition

TODO: Add instructions on running this part of the code.

## (b) `qr_fact_house` and `qr_fact_givens`: QR Factorization

TODO: Add instructions on running this part of the code.

## (c) `solve_lu`, `solve_qr_house`, and `solve_qr_givens`: Solving Factorizations

TODO: Add instructions on running these parts of the code.

## (d) `jacobi_iter`, `gs_iter`: Iteration Methods

The actual "math" part of these functions can be found in `iterative_methods.py`.

To test `jacobi_iter`, run:

    python jacobi_driver.py <path_to_augmented_matrix> <path_to_x_0> <e> <m>
    python jacobi_driver.py test/iter_aug.dat test/iter_x_0.dat 0.0001 10

Testing `gs_iter` is the same as Jacobi. Run:

    python gs_driver.py <path_to_augmented_matrix> <path_to_x_0> <e> <m>
    python gs_driver.py test/iter_aug.dat test/iter_x_0.dat 0.0001 10

## (e) `power_method`: Power Method

To test `power_method`, run:

    python power_driver.py <path_to_matrix_A> <path_to_x_0> <path_to_w> <e> <m>
    python power_driver.py test/power_A.dat test/power_x_0.dat test/power_w.dat 0.0001 30
