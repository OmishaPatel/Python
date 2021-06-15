def edit_distance(s1, s2):
    if s1 == s2:
        return 0
    elif not s1:
        return len(s2)
    elif not s2:
        return len(s1)

    if s1[0] == s2[0]:
        return edit_distance(s1[1:], s2[1:])

    return 1 + min(
        edit_distance(s1[1:], s2), # deletion from s1
        edit_distance(s1, s2[1:]), # addition to s1
        edit_distance(s1[1:], s2[1:]) # modification to s1
    )
    


print(edit_distance("execution", "intention"))