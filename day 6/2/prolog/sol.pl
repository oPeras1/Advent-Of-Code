direction('^', -1, 0).
direction('>', 0, 1).
direction('v', 1, 0).
direction('<', 0, -1).

turn_right('^', '>').
turn_right('>', 'v').
turn_right('v', '<').
turn_right('<', '^').

find_valid_obstructions(Count) :-
    FileName = '../../input.txt',
    open(FileName, read, Stream),
    read_stream_to_codes(Stream, Codes),
    close(Stream),
    string_codes(String, Codes),
    split_string(String, "\n", "", Lines),
    maplist(string_chars, Lines, Grid),
    find_positions(['^', '>', 'v', '<'], Grid, GX, GY, GDir),
    findall((X, Y),
        (nth0(X, Grid, Row),
         nth0(Y, Row, '.', _),
         simulate_with_obstruction(Grid, X, Y, GX, GY, GDir)
        ),
        ValidPositions),
    length(ValidPositions, Count).

simulate_with_obstruction(Grid, ObX, ObY, GX, GY, GDir) :-
    replace(Grid, ObX, ObY, '#', UpdatedGrid),
    simulate(UpdatedGrid, GX, GY, GDir, [], Looping),
    Looping = true.

simulate(Grid, X, Y, Dir, Visited, true) :-
    member((X, Y, Dir), Visited), !.

simulate(Grid, X, Y, Dir, Visited, Looping) :-
    direction(Dir, DX, DY),
    NX is X + DX,
    NY is Y + DY,
    (out_of_bounds(Grid, NX, NY) ->
        Looping = false
    ;
        nth0(NX, Grid, Row),
        nth0(NY, Row, Cell),
        (   Cell = '#' -> 
            turn_right(Dir, NewDir),
            simulate(Grid, X, Y, NewDir, [(X, Y, Dir)|Visited], Looping)
        ;
            simulate(Grid, NX, NY, Dir, [(X, Y, Dir)|Visited], Looping)
        )
    ).

find_positions(Dirs, Grid, X, Y, Dir) :-
    member(Dir, Dirs),
    nth0(X, Grid, Row),
    nth0(Y, Row, Dir), !.

out_of_bounds(Grid, X, Y) :-
    length(Grid, Rows),
    nth0(0, Grid, Row),
    length(Row, Cols),
    (
        X < 0; X >= Rows;
        Y < 0; Y >= Cols
    ), !.

replace(Grid, X, Y, Value, UpdatedGrid) :-
    nth0(X, Grid, Row),
    nth0(Y, Row, _, RestRow),
    nth0(Y, NewRow, Value, RestRow),
    nth0(X, Grid, Row, RestGrid),
    nth0(X, UpdatedGrid, NewRow, RestGrid).
