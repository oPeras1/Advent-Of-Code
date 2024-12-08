read_file_lines(Lines) :-
    open("../../input.txt", read, Stream),
    read_lines_to_lists(Stream, Lines),
    close(Stream),
    !.

read_lines_to_lists(Stream, []) :-
    at_end_of_stream(Stream), !.
read_lines_to_lists(Stream, [CharList|Rest]) :-
    \+ at_end_of_stream(Stream),
    read_line_to_string(Stream, Line),
    string_chars(Line, CharList),
    read_lines_to_lists(Stream, Rest).

group_positions_by_char(Lines, CharsPos) :-
    findall([Char, [I1, I2]], (
        nth0(I1, Lines, Line),
        nth0(I2, Line, Char),
        Char \= '.'
    ), AllCharPositions),
    group_by_char(AllCharPositions, GroupedResults),
    findall(Positions, (
        member([_, Positions], GroupedResults)
    ), CharsPos).

group_by_char(AllCharPositions, GroupedResults) :-
    foldl(insert_char_position, AllCharPositions, [], GroupedResults).

insert_char_position([Char, Pos], Acc, UpdatedAcc) :-
    ( select([Char, Positions], Acc, Rest) ->
        append(Positions, [Pos], NewPositions),
        UpdatedAcc = [[Char, NewPositions]|Rest]
    ; UpdatedAcc = [[Char, [Pos]]|Acc]
    ).

get_solution(Solution) :-
    read_file_lines(Lines),
    length(Lines, LengthX),
    nth0(0, Lines, FirstLine),
    length(FirstLine, LengthY),
    MaxL is max(LengthX, LengthY),
    group_positions_by_char(Lines, CharsPos),
    maplist(group_positions, CharsPos, GroupedLists),
    findall(Group, (
        member(GroupList, GroupedLists),
        member(Group, GroupList)
    ), FlattenedGroups),
    findall([NodeX, NodeY], (
        member(CoordsList, FlattenedGroups),
        nth0(0, CoordsList, [X1, Y1]),
        nth0(1, CoordsList, [X2, Y2]),
        DifX is X1 - X2,
        DifY is Y1 - Y2,
        between(0, MaxL, A),
        NodeX is X1 + A*DifX,
        NodeY is Y1 + A*DifY,
        NodeX >= 0, NodeX < LengthX,
        NodeY >= 0, NodeY < LengthY
    ), Coords1),
    findall([NodeX, NodeY], (
        member(CoordsList, FlattenedGroups),
        nth0(0, CoordsList, [X1, Y1]),
        nth0(1, CoordsList, [X2, Y2]),
        DifX is X1 - X2,
        DifY is Y1 - Y2,
        between(0, MaxL, A),
        NodeX is X2 - A*DifX,
        NodeY is Y2 - A*DifY,
        NodeX >= 0, NodeX < LengthX,
        NodeY >= 0, NodeY < LengthY
    ), Coords2),
    merge_unique_with_findall(Coords1, Coords2, AntiNodes),
    length(AntiNodes, Solution),
    !.

merge_unique_with_findall(List1, List2, Merged) :-
    append(List1, List2, Combined),
    findall(Element,
            (member(Element, Combined), 
             forall(member(Elem, Combined), 
                    (Elem = Element -> true ; Elem \= Element))),
            TempMerged),
    remove_duplicates(TempMerged, Merged).

remove_duplicates([], []).
remove_duplicates([Head|Tail], [Head|Result]) :-
    \+ member(Head, Tail), 
    remove_duplicates(Tail, Result).
remove_duplicates([Head|Tail], Result) :-
    member(Head, Tail),
    remove_duplicates(Tail, Result).

group_positions(Positions, Groups) :-
    findall(Group, (
        select(Pos1, Positions, Rest),
        member(Pos2, Rest),
        Pos1 @< Pos2,
        Group = [Pos1, Pos2]
    ), Groups).