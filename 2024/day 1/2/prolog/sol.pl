% Main predicate to read and process the file
readfile(Count) :-
    FileName = '../../input.txt',
    open(FileName, read, Stream), 
    process_lines(Stream, N1, N2),  % Process lines into two lists
    count_N1_In_N2(N1, N2, Count), % Count the number of occurrences of each number in the other list
    close(Stream),                % Close the file
    !.

% Base case: stop processing when at the end of the file
process_lines(Stream, [], []) :-
    at_end_of_stream(Stream), !.                   

% Recursive case: process a line and continue
process_lines(Stream, [N1|Tn1], [N2|Tn2]) :-
    \+ at_end_of_stream(Stream),                   % Ensure not at the end
    read_line_to_string(Stream, Line),             % Read a line
    split_string(Line, " ", " ", Parts),   % Split the line by spaces
    exclude(==( ""), Parts, [N1Str, N2Str]), % Remove empty strings and get the two parts
    number_string(N1, N1Str),                      % Convert the first number to an integer
    number_string(N2, N2Str),                      % Convert the second number to an integer
    process_lines(Stream, Tn1, Tn2).               % Recursively process the next lines

% Compute the difference between two sorted lists
count_N1_In_N2([], _, 0).                                   % Base case: No difference
count_N1_In_N2([H1|T1], L, Count) :-
    count_N1_In_N2(T1, L, Count1),                     % Recursively process the rest of the first list
    count_occurrences(H1, L, N),             % Count the number of occurrences of H1 in the second list
    Count is Count1 + N*H1.                           % Increment the count

% Helper predicate to remove all spaces from a string
remove_spaces(Input, Output) :-
    atom_chars(Input, Chars),         % Convert the string to a list of characters
    exclude(=(32), Chars, Cleaned),  % Remove space characters (ASCII code 32)
    atom_chars(Output, Cleaned).      % Convert the cleaned list back to an atom

count_occurrences(_, [], 0).  % Base case: number does not appear in an empty list
count_occurrences(X, [X|T], N) :-  % Case when the head of the list matches X
    count_occurrences(X, T, N1),
    N is N1 + 1.
count_occurrences(X, [_|T], N) :-  % Case when the head of the list does not match X
    count_occurrences(X, T, N).