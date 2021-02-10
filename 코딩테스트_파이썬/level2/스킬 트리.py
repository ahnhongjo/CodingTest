def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        change = []
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                change.append(skill_tree[i])

        if skill == change:
            answer = answer + 1
        else:
            same = 1
            for i in range(len(change)):
                if skill[i] != change[i]:
                    same = 0
            answer = answer + same

    return answer