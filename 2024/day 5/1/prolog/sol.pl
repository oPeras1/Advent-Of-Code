% Read the grid from the file
readfile(Count) :-
    FileName = '../../input.txt',
    open(FileName, read, Stream),
    read_string(Stream, _, Data),
    close(Stream),

    %% Cant understand why this work but this not ---->   split_string(Data, "\n\n", "", [Part1, Part2]),
    %% Anyways, ty copilot for the help
    split_input(Data, Part1, Part2),

    process_part1(Part1, Data1),
    process_part2(Part2, Data2),

    writeln(Data1),
    writeln(Data2),

    % Count valid updates
    %count_valid_updates(Data1, Data2, 0, Count),
    !.

% Split the input data into two parts
split_input(Data, Part1, Part2) :-
    split_string(Data, "\n", "", Lines), % Split into lines
    split_on_empty(Lines, Part1, Part2).  % Split by the first empty line

% Split a list of lines into two parts at the first empty line
split_on_empty(["" | Rest], [], Rest).  % The first empty line divides the parts
split_on_empty([Line | Rest], [Line | Part1], Part2) :- 
    split_on_empty(Rest, Part1, Part2).

process_part1(Part1, Data1) :-
    split_string(Part1, "\n", "", Lines),
    maplist(string_to_int_list, Lines, "|", Data1).

% Process the second part (data2) into a list of lists of integers
process_part2(Part2, Data2) :-
    split_string(Part2, "\n", "", Lines),
    maplist(string_to_int_list, Lines, ",", Data2).

% Convert a line into a list of integers
string_to_int_list(Line, Splitter, List) :-
    writeln(Line),
    split_string(Line, Splitter, "", StringList),
    maplist(atom_number, StringList, List).