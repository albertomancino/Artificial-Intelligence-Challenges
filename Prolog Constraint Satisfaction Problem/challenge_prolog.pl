time(antonio,40).
time(claudio,80).
time(felice,100).
time(walter,20).
persona(antonio).
persona(claudio).
persona(felice).
persona(walter).

next_move(forward,backward).
next_move(backward,forward).

problem(Solution):-
    problem([antonio,claudio,felice,walter],[],0,forward,[],Solution).

problem([],_,Time,_,Moves,Moves):-
    Time =< 240.

problem(Start,Finish,Time,Direction,Moves,Solution):-
    move(Start,Finish,First,Second,Direction),
    result(Start,Finish,First,Second,Direction,StartN,FinishN),
    new_time(Time,First,Second,Direction,TimeN),
    next_move(Direction,DirectionN),
    add_move(Moves,First,Second,Direction,TimeN,MovesN),
    problem(StartN,FinishN,TimeN,DirectionN,MovesN,Solution).


move(Start,_,First,Second,forward):-
    choose(Start,LN,First),
    choose(LN,_,Second).

move(_,Finish,First,_,backward):-
    choose(Finish,_,First).

choose(L,LN,Persona):-
    persona(Persona),
    is_in(L,Persona),
    revome_with_previous(L,Persona,LN).

revome_with_previous([H|T],H,T).
revome_with_previous([H|T],X,NewList):-
    H \== T,
    revome_with_previous(T,X,NewList).

is_in([H|_],H):-!.
is_in([H|T],X):-
    X \== H,
    is_in(T,X),!.

result(Start,Finish,First,Second,forward,StartNN,FinishNN):-
    delete(Start,First,StartN),
    delete(StartN,Second,StartNN),
    insert(First,Finish,FinishN),
    insert(Second,FinishN,FinishNN).


result(Start,Finish,First,_,backward,StartN,FinishN):-
    delete(Finish,First,FinishN),
    insert(First,Start,StartN).

insert(X,L,[X|L]):-!.

new_time(Time,First,Second,forward,TimeN):-
    time(First,TimeFirst),!,
    time(Second,TimeSecond),!,
    max(TimeFirst,TimeSecond,Delta),!,
    TimeN is Time + Delta,!.

new_time(Time,First,_,backward,TimeN):-
    time(First,TimeFirst),!,
    TimeN is Time + TimeFirst,!.

max(A,B,A):-
    A >= B,!.
max(A,B,B):-
    B >= A,!.


add_move(Moves,First,Second,forward,Time,MovesN):-
    append(Moves,[[First,Second,'forward',Time]],MovesN).
add_move(Moves,First,_,backward,Time,MovesN):-
    append(Moves,[[First,'backward',Time]],MovesN).
