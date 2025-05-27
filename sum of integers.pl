% Recursive method
sum_to_n(1, 1).
sum_to_n(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_to_n(N1, PartialSum),
    Sum is PartialSum + N.

% Formula method
sum_to_n_formula(N, Sum) :-
    Sum is N * (N + 1) // 2.

% Main entry point
main :-
    write('Enter a positive integer N: '),
    read(N),
    integer(N), N > 0,
    
    sum_to_n(N, RecursiveSum),
    format('Recursive sum from 1 to ~d is ~d~n', [N, RecursiveSum]),

    sum_to_n_formula(N, FormulaSum),
    format('Formula sum from 1 to ~d is ~d~n', [N, FormulaSum]).

