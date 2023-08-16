list_sum([],0).

list_sum([Head|Tail],Sum):-
    list_sum(Tail,Rest_sum),
    Sum is Head + Rest_sum.
