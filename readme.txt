"
/*
 * This regular expression is designed to match valid floating-point numbers.
 * 
 * Breakdown of the regex:
 * ^[+-]?                - Matches an optional leading '+' or '-' sign at the start of the string.
 * (?=\d+\.?\d*$|\.?\d+) - Positive lookahead to ensure the string is a valid number format:
 *                         - \d+\.?\d*$: Matches one or more digits followed by an optional decimal point and zero or more digits until the end of the string.
 *                         - \.?\d+: Matches an optional decimal point followed by one or more digits.
 * (\d+(?:\.\d+)?|\.\d+) - Matches the actual number:
 *                         - \d+(?:\.\d+)?: Matches one or more digits followed by an optional decimal point and one or more digits.
 *                         - \.\d+: Matches a decimal point followed by one or more digits.
#  todo : hasta aqui no se si es correcto, todo lo demas si
 * (?:[eE][+-]?\d+)?     - Matches an optional exponent part:
 *                         - [eE]: Matches 'e' or 'E'.
 *                         - [+-]?: Matches an optional '+' or '-' sign.
 *                         - \d+: Matches one or more digits.
 * $                     - Ensures the entire string is matched.
 */

^[+-]?(?=\d+\.?\d*$|\.?\d+)(\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?$


"

# TODO documentacion del regex, esta todo regado jaja

^ : indica el inicio del regex

[+-]? : define un signo sea positivo o negativo opcional (0 o 1 vez)
# Match a single character present in the list below matches the previous token between zero and one times, as many times as possible, giving back as needed (greedy)
# +- matches a single character in the list +- (case sensitive)

lookahead: un lookahead permite coincidir un patron predefinido si hay algo delante de él.
# Positive Lookahead (?=\d+\.?\d*$|\.?\d+)
lookbehind: un lookbehind permite coincidir un patrón solo si hay algo anterior a él.

Positive Lookahead (?=\d+\.?\d*$|\.?\d+)
Assert that the Regex below matches

1st Alternative \d+\.?\d*$
\d matches a digit (equivalent to [0-9])
\. matches the character . with index 4610 (2E16 or 568) literally (case sensitive)
\d matches a digit (equivalent to [0-9])

$ asserts position at the end of the string, or before the line terminator right at the end of the string (if any)

2nd Alternative \.?\d+
\. matches the character . with index 4610 (2E16 or 568) literally (case sensitive)
\d matches a digit (equivalent to [0-9])

1st Capturing Group (\d+(?:\.\d+)?|\.\d+)
1st Alternative \d+(?:\.\d+)?
2nd Alternative \.\d+
Non-capturing group (?:[eE][+-]?\d+)?

? matches the previous token between zero and one times, as many times as possible, giving back as needed (greedy)
Match a single character present in the list below [eE]
Match a single character present in the list below [+-]
\d matches a digit (equivalent to [0-9])
$ asserts position at the end of the string, or before the line terminator right at the end of the string (if any)