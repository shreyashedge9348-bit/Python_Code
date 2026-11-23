maths = float(input("Enter Mathematics marks (%): "))
physics = float(input("Enter Physics marks (%): "))
chemistry = float(input("Enter Chemistry marks (%): "))
overall = (maths + physics + chemistry) / 3

# Example criteria: >= 50% in each and >= 60% overall
if maths >= 50 and physics >= 50 and chemistry >= 50 and overall >= 60:
    print("Eligible for admission")
else:
    print("Not eligible for admission")
print("Overall percentage:", overall)
