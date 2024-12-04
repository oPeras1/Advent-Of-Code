% Read the grid from the file
readfile(Count) :-
    FileName = '../../input.txt',
    open(FileName, read, Stream),
    read_lines(Stream, Lines),
    close(Stream),
    maplist(atom_chars, Lines, Grid),
    findall(_, find_xmas(Grid, _), Matches),
    length(Matches, Count),
    !.

% Read all lines from the file into a list of atoms
read_lines(Stream, []) :-
    at_end_of_stream(Stream).
read_lines(Stream, [Line|Lines]) :-
    \+ at_end_of_stream(Stream),
    read_line_to_string(Stream, Line),
    read_lines(Stream, Lines).

find_xmas(Grid, Pos) :-
    find_horizontal(Grid, Pos);
    find_vertical(Grid, Pos);
    find_diagonal(Grid, Pos).

find_horizontal(Grid, Pos) :-
    member(Row, Grid),
    atomic_list_concat(Row, RowAtom),
    (sub_atom(RowAtom, Pos, 4, _, 'XMAS'); sub_atom(RowAtom, Pos, 4, _, 'SAMX')).

find_vertical(Grid, (RowIdx, ColIdx)) :-
    transpose(Grid, TransposedGrid),
    nth0(ColIdx, TransposedGrid, Column),
    atomic_list_concat(Column, ColumnAtom),
    (sub_atom(ColumnAtom, RowIdx, 4, _, 'XMAS'); sub_atom(ColumnAtom, RowIdx, 4, _, 'SAMX')).

find_diagonal(Grid, (RowIdx, ColIdx)) :-
    length(Grid, N),
    between(0, N, RowIdx),
    between(0, N, ColIdx),
    (diagonal_matches(Grid, RowIdx, ColIdx, 1, 1, 'XMAS'); diagonal_matches(Grid, RowIdx, ColIdx, -1, -1, 'SAMX')).


find_diagonal(Grid, (RowIdx, ColIdx)) :-
    length(Grid, N),
    between(0, N, RowIdx),
    between(0, N, ColIdx),
    (diagonal_matches(Grid, RowIdx, ColIdx, 1, -1, 'XMAS'); diagonal_matches(Grid, RowIdx, ColIdx, -1, 1, 'SAMX')).

diagonal_matches(Grid, Row, Col, RowStep, ColStep, Word) :-
    atom_chars(Word, [H|T]),
    nth0(Row, Grid, CurrentRow),
    nth0(Col, CurrentRow, H),
    check_diagonal(Grid, Row, Col, RowStep, ColStep, T).

check_diagonal(_, _, _, _, _, []).
check_diagonal(Grid, Row, Col, RowStep, ColStep, [H|T]) :-
    NewRow is Row + RowStep,
    NewCol is Col + ColStep,
    nth0(NewRow, Grid, NewRowData),
    nth0(NewCol, NewRowData, H),
    check_diagonal(Grid, NewRow, NewCol, RowStep, ColStep, T).

transpose([], []).
transpose([F|Fs], Ts) :-
    transpose(F, [F|Fs], Ts).

transpose([], _, []).
transpose([_|Rs], Ms, [Ts|Tss]) :-
    lists_firsts_rests(Ms, Ts, Ms1),
    transpose(Rs, Ms1, Tss).

lists_firsts_rests([], [], []).
lists_firsts_rests([[F|Os]|Rest], [F|Fs], [Os|Oss]) :-
    lists_firsts_rests(Rest, Fs, Oss).
