# find all subsequences in a string that form a palindrome.
# e.g.
# findPalindromes('abxscbayya') will output:
#    a, b, x, s, c, y,
#    aa, bb, yy,
#    aaa,
#    aba, axa, asa, aca, aya, bxb, bsb, bcb,
#    abba, ayya,
#    abxba, absba, abcba,
#


def checkPalindrome(str):
    """Helper function to check if a given string is a palindrome.
    """
    l = len(str)
    for i in xrange(l / 2):
        if not (str[i] == str[l-i-1]):
            return False
    return True


def expandPalindromes(c, st, out):
    """Helper function to create a superset of the given set 
    which contains all the strings from original set, plus strings
    created by appending char c before and after each string.

    Args:
    c: character to append before and after
    st: original set
    out: output set to update
    """
    for str in st:
        out.add(str)
        out.add(c + str + c)


def findPalindromesInTable(str, ptable):
    """
    Find all palindromic subsequences in given string and memoize 
    the result in ptable. If the given string has already been computed
    lookup the result in ptable first.
    """
    if (str in ptable.keys()):
        return ptable[str]

    l = len(str)
    out = set()
    if (l == 0):
        pass
    elif (l == 1):
        out.add(str)
    elif (l == 2):
        out.add(str[0])
        if (str[0] == str[1]):
            out.add(str)
        else:
            out.add(str[1])
    else:
        # when first and last character are the same (e.g. aXYZa)
        # we can obtain palindromes by appending 'a' before and after
        # all the palindromes for the substring XYZ. Also need to add
        # {a, aa} as palindromes.
        if (str[0] == str[-1]):
            out.add(str[0])
            out.add(str[0] + str[-1])
            expandPalindromes(str[0], findPalindromesInTable(str[1:-1], ptable), out)
        else: 
            # when first and last char are different (e.g. aXYZb)
            # we can take union of palindromes in aXYZ and XYZb.
            # Also add {a, b} as palindromes.
            out.add(str[0])
            out.add(str[-1])
            out.update(findPalindromesInTable(str[1:], ptable))
            out.update(findPalindromesInTable(str[:-1], ptable))
    ptable[str] = out
    return out


def findPalindromes(str):
    """Given a string return the set of all palindromic subsequences within it.

    Calls findPalindromesInTable to do the actual work.
    """
    ptable = {}
    findPalindromesInTable(str, ptable)
    return ptable[str]


print(findPalindromes(''))
print(findPalindromes('a'))
print(findPalindromes('aa'))
print(findPalindromes('ab'))
print(findPalindromes('aba'))
print(findPalindromes('abxscbayya'))
print(findPalindromes('abxscbayyaa'))
print(findPalindromes('abxscbayyaax'))

# now for some testing
expected = set(['a', 'b', 'x', 's', 'c', 'y', 'aa', 'bb', 'yy', 'aaa',
 'aba', 'axa', 'asa', 'aca', 'aya', 'bxb', 'bsb', 'bcb', 'abba', 'ayya',
  'abxba', 'absba', 'abcba'])
testout = findPalindromes('abxscbayya')
print(testout ^ expected)

