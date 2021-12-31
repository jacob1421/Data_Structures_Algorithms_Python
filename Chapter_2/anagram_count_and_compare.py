#BigO - O(n)
#Requries additional space to reach O(n)
def anagram_solution(s1, s2):
    character_counter_s1 = [0] * 26
    character_counter_s2 = [0] * 26

    for char_idx in range(len(s1)):
        alphabet_pos = ord(s1[char_idx]) - ord('a')
        character_counter_s1[alphabet_pos] += 1

    for char_idx in range(len(s2)):
        alphabet_pos = ord(s2[char_idx]) - ord('a')
        character_counter_s2[alphabet_pos] += 1

    return character_counter_s1 == character_counter_s2


if __name__ == "__main__":
    s1 = "heart"
    s2 = "earth"
    is_anagram = anagram_solution(s1, s2)
    if(is_anagram):
        print("%r is an anagram of %r" % (s1, s2))
    else:
        print("%r is NOT an anagram of %r" % (s1, s2))