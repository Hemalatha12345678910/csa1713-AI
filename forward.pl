% Sample rules using generic facts
rule(c) :- fact(a), fact(b).
rule(d) :- fact(c).
rule(e) :- fact(d), fact(f).

% Ask user to assert known facts
ask_facts :-
    write('Enter known facts one by one (end with "stop.").'), nl,
    read_facts.

read_facts :-
    read(Fact),
    (Fact == stop -> true ; assertz(fact(Fact)), read_facts).

% Forward chaining engine
forward :-
    forward_step,
    !,
    forward.  % Repeat until no new facts can be derived
forward :-
    write('Final derived facts: '), nl,
    list_facts.

% One step of forward chaining
forward_step :-
    rule(NewFact),
    \+ fact(NewFact),
    assertz(fact(NewFact)),
    format('Derived: ~w~n', [NewFact]).

% List all known facts
list_facts :-
    fact(F), writeln(F), fail.
list_facts.  % To succeed after listing

% Entry point
start :-
    retractall(fact(_)),
    ask_facts,
    forward.
