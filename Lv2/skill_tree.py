def solution(skill: str, skill_trees: list):
    skill_trees = list(map(lambda x: ''.join(filter(lambda y: y in skill, x)), skill_trees))
    return len([tree for tree in skill_trees if skill.startswith(tree)])

if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))