AI = {101, 102, 103, 104}
DS = {103, 104, 105, 106}
CS = {104, 106, 107, 108}

print("UNIVERSITY COURSE REGISTRATION")
print("------------------------------")

# Students enrolled in at least one course
print("All students:", AI | DS | CS)

# Students enrolled in all three courses
print("Enrolled in all three:", AI & DS & CS)

# Students enrolled only in AI
print("Only AI:", AI - (DS | CS))

# Students enrolled in exactly one course
exactly_one = (
    (AI - (DS | CS)) |
    (DS - (AI | CS)) |
    (CS - (AI | DS))
)

print("Exactly one course:", exactly_one)
