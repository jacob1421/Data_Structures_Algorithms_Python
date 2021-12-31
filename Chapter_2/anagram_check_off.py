#BigO - O(n^2)
def anagram_solution(s1, s2):
    """
    anagram_solution checks if the two strings are anagrams of each other

    :param s1: first string to check against the second string
    :param s2: second string to check against the first string
    :return: returns True if the two strings are anagrams of each other. Otherwise, False is returned.
    """
    a_list = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            a_list[pos2] = None
        else:
            still_ok = False

        pos1 = pos1 + 1

    return still_ok


if __name__ == "__main__":
    s1 = "heart"
    s2 = "earth"
    is_anagram = anagram_solution(s1, s2)
    if(is_anagram):
        print("%r is an anagram of %r" % (s1, s2))
    else:
        print("%r is NOT an anagram of %r" % (s1, s2))