#^ | Matches the expression to its right at the start of a string. It matches every such instance before each \n in the string.

#$ | Matches the expression to its left at the end of a string. It matches every such instance before each \n in the string.

#. | Matches any character except line terminators like \n.

#\ | Escapes special characters or denotes character classes.

#A|B | Matches expression A or B. If A is matched first, B is left untried.

#+ | Greedily matches the expression to its left 1 or more times.

#* | Greedily matches the expression to its left 0 or more times.

#? | Greedily matches the expression to its left 0 or 1 times. But if ? is added to qualifiers (+, *, and ? itself) it will perform matches in a non-greedy manner.

#{m} | Matches the expression to its left m times, and not less.

#{m,n} | Matches the expression to its left m to n times, and not less.

#{m,n}? | Matches the expression to its left m times, and ignores n. See ? above.

#Character Classes (a.k.a. Special Sequences)
#\w | Matches alphanumeric characters, which means a-z, A-Z, and 0-9. It also matches the underscore, _.

#\d | Matches digits, which means 0-9.

#\D | Matches any non-digits.

#\s | Matches whitespace characters, which include the \t, \n, \r, and space characters.

#\S | Matches non-whitespace characters.

#\b | Matches the boundary (or empty string) at the start and end of a word, that is, between \w and \W.

#\B | Matches where \b does not, that is, the boundary of \w characters.

#\A | Matches the expression to its right at the absolute start of a string whether in single or multi-line mode.

#\Z | Matches the expression to its left at the absolute end of a string whether in single or multi-line mode.