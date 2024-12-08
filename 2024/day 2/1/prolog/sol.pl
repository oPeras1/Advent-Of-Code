readfile(Count) :-
    FileName = '../../input.txt',
    open(FileName, read, Stream),
    read_lines(Stream, Diff),
    count_safe_reports(Diff, Count),
    close(Stream),
    !.

read_lines(Stream, []) :-
    at_end_of_stream(Stream). % Base case: Stop when reaching the end of the stream
    
read_lines(Stream, [LineList|Rest]) :-
    \+ at_end_of_stream(Stream), % Check not at the end
    read_line_to_string(Stream, LineString), % Read a line as a string
    split_string(LineString, " ", "", LineParts), % Split the line into parts
    maplist(number_string, LineList, LineParts), % Convert strings to numbers
    read_lines(Stream, Rest). % Recursive call for the rest of the lines

% Main predicate to check if a report is safe
is_safe(Report) :-
    all_increasing(Report), 
    valid_differences(Report).
is_safe(Report) :-
    all_decreasing(Report), 
    valid_differences(Report).

% Check if all elements in the list are increasing
all_increasing([_]). % A single element is trivially increasing
all_increasing([X, Y | Rest]) :-
    X < Y, 
    all_increasing([Y | Rest]).

% Check if all elements in the list are decreasing
all_decreasing([_]). % A single element is trivially decreasing
all_decreasing([X, Y | Rest]) :-
    X > Y, 
    all_decreasing([Y | Rest]).

% Check if all consecutive differences are between 1 and 3
valid_differences([_]). % A single element has no consecutive differences
valid_differences([X, Y | Rest]) :-
    Diff is abs(X - Y),
    Diff >= 1,
    Diff =< 3,
    valid_differences([Y | Rest]).

% Predicate to count the number of safe reports in a list of reports
count_safe_reports([], 0). % Base case: no reports left
count_safe_reports([Report | Rest], Count) :-
    is_safe(Report), 
    count_safe_reports(Rest, RestCount), 
    Count is RestCount + 1.
    
count_safe_reports([_ | Rest], Count) :- 
    count_safe_reports(Rest, Count). % Skip unsafe reports