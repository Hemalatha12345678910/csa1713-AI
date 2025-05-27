% Match a list starting with 'a'
starts_with_a([a | _]) :- write('List starts with a'), nl.

% Match a list ending with 'z'
ends_with_z(List) :- append(_, [z], List), write('List ends with z'), nl.

% Match a list with exactly three elements
three_elements([_, _, _]) :- write('List has three elements'), nl.
