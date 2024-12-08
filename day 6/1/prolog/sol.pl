direction('^', -1, 0).
direction('>', 0, 1).
direction('v', 1, 0).
direction('<', 0, -1).

turn_right('^', '>').
turn_right('>', 'v').
turn_right('v', '<').
turn_right('<', '^').

readfile(Count) :-
    FileName = '../../input.txt',
    open(FileName, read, Stream),
    read_stream_to_codes(Stream, Codes),
    close(Stream),
    string_codes(String, Codes),
    split_string(String, "\n", "", Lines),
    maplist(string_chars, Lines, Grid),
    find_positions(['^', '>', 'v', '<'], Grid, X, Y, Dir),
    simulate(Grid, X, Y, Dir, UpdatedGrid),
    count_hashes(UpdatedGrid, Count).


count_hashes([], 0).

count_hashes([Head|Tail], TotalCount) :-
    count_in_list(Head, HeadCount),
    count_hashes(Tail, TailCount),
    TotalCount is HeadCount + TailCount.

count_in_list(List, Count) :-
    include(==('X'), List, Filtered),
    length(Filtered, Count).

find_positions(Dirs, Grid, X, Y, Dir) :-
    member(Dir, Dirs),
    nth0(X, Grid, Row),
    nth0(Y, Row, Dir), !.

simulate(Grid, X, Y, Dir, UpdatedGrid) :-
    direction(Dir, DX, DY),
    NX is X + DX,
    NY is Y + DY,
    (out_of_bounds(Grid, NX, NY) ->
        UpdatedGrid = Grid;
        nth0(NX, Grid, Row),
        nth0(NY, Row, Cell),
        (   Cell = '#' -> 
            turn_right(Dir, NewDir),
            simulate(Grid, X, Y, NewDir, UpdatedGrid)
        ;
            replace(Grid, NX, NY, 'X', TempGrid),
            simulate(TempGrid, NX, NY, Dir, UpdatedGrid)
        )
    ).


out_of_bounds(Grid, X, Y) :-
    length(Grid, Rows),
    nth0(0, Grid, Row),
    length(Row, Cols),
    (
        X < 0; X >= Rows;
        Y < 0; Y >= Cols
    ),
    !.

replace(Grid, X, Y, Value, UpdatedGrid) :-
    nth0(X, Grid, Row),
    nth0(Y, Row, _, RestRow),
    nth0(Y, NewRow, Value, RestRow),
    nth0(X, Grid, Row, RestGrid),
    nth0(X, UpdatedGrid, NewRow, RestGrid).
