#BigO - O(n log n)
def anagram_solution(s1, s2):
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    a_list_1.sort()
    a_list_2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list_1[pos] == a_list_2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


if __name__ == "__main__":
    s1 = "heart"
    s2 = "earth"
    is_anagram = anagram_solution(s1, s2)
    if(is_anagram):
        print("%r is an anagram of %r" % (s1, s2))
    else:
        print("%r is NOT an anagram of %r" % (s1, s2))