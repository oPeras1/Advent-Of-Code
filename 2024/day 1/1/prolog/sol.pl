% Main predicate to read and process the file
readfile(Diff) :-
    FileName = '../../input.txt',
    open(FileName, read, Stream), 
    process_lines(Stream, N1, N2),  % Process lines into two lists
    msort(N1, N1Sorted),            % Sort the first list
    msort(N2, N2Sorted),            % Sort the second list
    diff(N1Sorted, N2Sorted, Diff), % Compute the difference between the two lists
    close(Stream).                 % Close the file

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
diff([], [], 0).                                   % Base case: No difference
diff([H1|T1], [H2|T2], Diff) :-
    %convert h1 and h2 to integers
    diff(T1, T2, SubDiff),  
    Diff is abs(H1 - H2) + SubDiff.                % Add the absolute difference of the heads

% Helper predicate to remove all spaces from a string
remove_spaces(Input, Output) :-
    atom_chars(Input, Chars),         % Convert the string to a list of characters
    exclude(=(32), Chars, Cleaned),  % Remove space characters (ASCII code 32)
    atom_chars(Output, Cleaned).      % Convert the cleaned list back to an atom