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
    (all_increasing(Report); all_decreasing(Report)), % Check if it's all increasing or all decreasing
    valid_differences(Report). % Check if the differences are valid

% Check if a report becomes safe by removing a single element
is_safe_after_removal(Report) :-
    length(Report, Len),
    Len > 1, % Ensure there are more than one element
    between(1, Len, Index),
    remove_element(Report, Index, NewReport), % Remove the element at Index
    is_safe(NewReport).

% Check if a report is safe or if removing an element makes it safe
is_safe_report(Report) :-
    is_safe(Report); is_safe_after_removal(Report).

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

% Predicate to remove the Nth element from the list
remove_element([_ | Tail], 1, Tail). % Remove the first element
remove_element([Head | Tail], N, [Head | Rest]) :-
    N > 1,
    N1 is N - 1,
    remove_element(Tail, N1, Rest).

% Predicate to count the number of safe reports
count_safe_reports([], 0). % Base case: no reports left
count_safe_reports([Report | Rest], Count) :-
    is_safe_report(Report), 
    count_safe_reports(Rest, RestCount), 
    Count is RestCount + 1.
    
count_safe_reports([_ | Rest], Count) :- 
    count_safe_reports(Rest, Count). % Skip unsafe reports