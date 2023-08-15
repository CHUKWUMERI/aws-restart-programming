import test

print(test.hello("Morgana"))


def grader(score):
    assert score > -1, "Invalid Score"
    assert score <= 100, "Invalid score"

    print(score)

grader(100)
