% Dynamic fact storage
:- dynamic known/1.

% Sample rules (generic)
prove(c) :- prove(a), prove(b).
prove(d) :- prove(c).
prove(e) :- prove(d), prove(f).

% Base case: already known
prove(Fact) :-
    known(Fact),
    !.

% Ask the user if fact is not already known
prove(Fact) :-
    \+ known(Fact),
    ask(Fact).

% Ask user if a fact is true
ask(Fact) :-
    format('Is ~w true? (yes/no): ', [Fact]),
    read(Reply),
    (Reply == yes ->
        assertz(known(Fact))
    ;   fail).

% Entry point: clear memory and start backward chaining
start :-
    retractall(known(_)),
    write('Enter the goal to prove (e.g., prove(d).)'), nl.
