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
    find_diagonal(Grid, Pos).

find_diagonal(Grid, (RowIdx, ColIdx)) :-
    length(Grid, N),
    between(0, N, RowIdx),
    between(0, N, ColIdx),
    MainDiagonalX is ColIdx - 1,
    MainDiagonalY is RowIdx - 1,
    AntiDiagonalX is ColIdx - 1,
    AntiDiagonalY is RowIdx + 1,
    (
        (diagonal_matches(Grid, MainDiagonalY, MainDiagonalX, 1, 1, 'MAS');
        diagonal_matches(Grid, MainDiagonalY, MainDiagonalX, 1, 1, 'SAM')),
        (diagonal_matches(Grid, AntiDiagonalY, AntiDiagonalX, -1, 1, 'MAS');
        diagonal_matches(Grid, AntiDiagonalY, AntiDiagonalX, -1, 1, 'SAM'))
    ).

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
