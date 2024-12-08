readfile(Count) :-
    FileName = '../../input.txt',
    open(FileName, read, Stream),
    read_string(Stream, _, Text),
    extract_mul(Text, MulList),
    multiplyAndSum(MulList, Count),
    close(Stream),
    !.

multiplyAndSum([], 0).
multiplyAndSum([mul(X, Y)|T], Count) :-
    multiplyAndSum(T, Count1),
    Count is Count1 + X * Y.

multiplyAndSum([_|T], Count) :-
    multiplyAndSum(T, Count).

% Extract valid mul(A, B) instructions from the string
extract_mul(Content, MulList) :-
    findall(mul(A, B), (
        sub_string(Content, Start, _, _, 'mul('),
        AfterStart is Start + 4,  % Skip 'mul('
        sub_string(Content, AfterStart, _, 0, SubString),

        sub_string(SubString, 0, Length, _, Rest), 
        sub_string(Rest, _, _, 0, ')'), % Ensure the substring ends with ')'

        sub_string(SubString, 0, Length, After, Rest),
        % Check format ending with ')'
        sub_string(Rest, BeforeComma, 1, AfterCommaLength, ','),
        BeforeComma >= 1,
        sub_string(Rest, 0, BeforeComma, _, AStr),
        AfterCommaIndex is BeforeComma + 1,
        sub_string(Rest, AfterCommaIndex, RemainingLength, 1, BStr),
        RemainingLength is AfterCommaLength - 1,
        number_string(A, AStr),
        number_string(B, BStr)
    ), MulList).