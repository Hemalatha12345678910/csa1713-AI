% Disease rules
disease(flu) :- symptom(fever), symptom(cough).
disease(cold) :- symptom(cough), symptom(sneezing).
disease(covid19) :- symptom(fever), symptom(cough), symptom(loss_of_taste_smell).

% Ask symptom from user
ask(S) :-
    format('Do you have ~w? (yes/no): ', [S]),
    read(Ans),
    Ans == yes.

% Start diagnosis
diagnose :-
    retractall(symptom(_)),
    (ask(fever) -> assertz(symptom(fever)); true),
    (ask(cough) -> assertz(symptom(cough)); true),
    (ask(sneezing) -> assertz(symptom(sneezing)); true),
    (ask(loss_of_taste_smell) -> assertz(symptom(loss_of_taste_smell)); true),
    (   disease(D) -> format('You may have ~w.~n', [D])
    ;   write('No diagnosis found based on your symptoms.') ).
