readfile(Count) :-
    FileName = '../../input.txt',
    open(FileName, read, Stream),
    read_string(Stream, _, Text),
    extract_instructions(Text, Instructions),
    sort_list(Instructions, RealInstructions),
    writeln(RealInstructions),
    calculate_sum(RealInstructions, Count),
    close(Stream),
    !.

calculate_sum(Instructions, Sum) :-
    calculate_sum(Instructions, 1, 0, Sum). % Start with enabled (1) and initial sum 0

calculate_sum([], _, CurrentSum, CurrentSum).
calculate_sum([mul(X, Y)|T], Enabled, CurrentSum, Sum) :-
    (Enabled =:= 1 ->  NewSum is CurrentSum + X * Y ; NewSum = CurrentSum),
    calculate_sum(T, Enabled, NewSum, Sum).

calculate_sum([do()|T], _, CurrentSum, Sum) :-
    calculate_sum(T, 1, CurrentSum, Sum).

calculate_sum(['don\'t()'|T], _, CurrentSum, Sum) :-
    calculate_sum(T, 0, CurrentSum, Sum).

calculate_sum([_|T], Enabled, CurrentSum, Sum) :-
    calculate_sum(T, Enabled, CurrentSum, Sum).

sort_list(Input, Output) :-
    sort(1, @=<, Input, Sorted),  
    maplist(second_element, Sorted, Output).

% Predicado para extrair o segundo elemento de cada sublista
second_element([_, Elemento], Elemento).

% Extract valid mul(A, B), do(), and don't() instructions from the string
extract_instructions(Content, Instructions) :-
    findall(Instruction, (
        (   sub_string(Content, Start, _, _, 'mul('),
            AfterStart is Start + 4,  % Skip 'mul('
            sub_string(Content, AfterStart, _, 0, SubString),

            sub_string(SubString, 0, Length, _, Rest), 
            sub_string(Rest, _, _, 0, ')'), % Ensure the substring ends with ')'

            sub_string(SubString, 0, Length, After, Rest),
            sub_string(Rest, BeforeComma, 1, AfterCommaLength, ','),
            BeforeComma >= 1,
            sub_string(Rest, 0, BeforeComma, _, AStr),
            AfterCommaIndex is BeforeComma + 1,
            sub_string(Rest, AfterCommaIndex, RemainingLength, 1, BStr),
            RemainingLength is AfterCommaLength - 1,
            number_string(A, AStr),
            number_string(B, BStr),
            Instruction = [Start, mul(A, B)]
        )
        ;   (sub_string(Content, Start1, _, _, 'do()'), Instruction = [Start1,do()])
        ;   (sub_string(Content, Start2, _, _, 'don\'t()'), Instruction = [Start2,'don\'t()'])
    ), Instructions).