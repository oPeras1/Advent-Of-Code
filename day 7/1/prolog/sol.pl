:- use_module(library(dcg/basics)).
:- use_module(library(dcg/high_order)).
:- use_module(library(pio)).

process_file() :-
    open("../../input.txt", read, Stream),
    read_lines(Stream, Lists),
    solve(Lists, X1),
    writeln(X1),
    close(Stream),
    ! .

solve(Lists, X) :-
    findall(TestValue, (member([TestValue|Numbers], Lists), valid_equation(TestValue, Numbers)), ValidEquations),
    sum_list(ValidEquations, X).

valid_equation(TestValue, Numbers) :-
    generate_all_expressions(Numbers, Expressions),
    member(Expression, Expressions),
    writeln(Expressions),
    flatten_expression(Expression, FlatExpression),
    evaluate(FlatExpression, TestValue).

flatten_expression(Term, Flat) :-
    (   atomic(Term)
    ->  Flat = [Term]
    ;   Term =.. [Op, Left, Right],
        flatten_expression(Left, FlatLeft),
        flatten_expression(Right, FlatRight),
        append(FlatLeft, [Op|FlatRight], Flat)
    ).

generate_all_expressions([Num], [Num]).
generate_all_expressions([Num1, Num2 | Rest], Expressions) :-
    generate_all_expressions([Num2 | Rest], RestExpressions),
    findall(
        Num1 + Expr, % Adding operator
        member(Expr, RestExpressions),
        Expressions1
    ),
    findall(
        Num1 * Expr, % Multiplying operator
        member(Expr, RestExpressions),
        Expressions2
    ),
    append(Expressions1, Expressions2, Expressions).

evaluate([Num], Num).
evaluate([Num1, Op | Rest], Result) :-
    evaluate(Rest, RestResult),
    (
        Op = +, Result is Num1 + RestResult;
        Op = *, Result is Num1 * RestResult
    ).


% Reads each line from the file and processes it
read_lines(Stream, Lists) :-
    read_line_to_string(Stream, Line),
    ( Line \= end_of_file
    ->  process_line(Line, ParsedLine),
        read_lines(Stream, RestLists),
        Lists = [ParsedLine | RestLists]
    ;   Lists = []
    ).

% Processes a single line: separates numbers before and after the colon
process_line(Line, ParsedLine) :-
    split_string(Line, ":", "", [Left, Right]),  % Split by ':'
    string_trim_spaces(Left, TrimmedLeft),        % Trim leading/trailing spaces from the left part
    string_trim_spaces(Right, TrimmedRight),      % Trim leading/trailing spaces from the right part
    number_string(LeftNumber, TrimmedLeft),       % Convert the left part to a number
    split_string(TrimmedRight, " ", "", Numbers), % Split the right part into numbers
    maplist(number_string, NumList, Numbers),     % Convert the strings to numbers
    append([LeftNumber], NumList, ParsedLine).    % Combine the left number with the right list of numbers

% Manually trims leading and trailing spaces from a string
string_trim_spaces(String, Trimmed) :-
    string_codes(String, Codes),
    trim_spaces(Codes, TrimmedCodes),
    string_codes(Trimmed, TrimmedCodes).

% Trim leading and trailing spaces (space code is 32)
trim_spaces(Codes, TrimmedCodes) :-
    trim_leading_spaces(Codes, Trimmed1),
    trim_trailing_spaces(Trimmed1, TrimmedCodes).

% Remove leading spaces
trim_leading_spaces([], []).
trim_leading_spaces([32|T], Trimmed) :- 
    trim_leading_spaces(T, Trimmed).
trim_leading_spaces([H|T], [H|T]).

% Remove trailing spaces
trim_trailing_spaces([], []).
trim_trailing_spaces([32], []).
trim_trailing_spaces([32|T], Trimmed) :-
    trim_trailing_spaces(T, Trimmed).
trim_trailing_spaces([H|T], [H|T]).