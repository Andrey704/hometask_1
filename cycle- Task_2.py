#name_arr = []
salary_arr = []
sum = 0

n = int(input("How many employees take into account: "))

#for i in range(n):
    #name_arr.append(input("Enter name of " + str(i + 1) + " employee"))

for i in range (n):
    salary_arr.append(input("Enter salary of " + str(i + 1) + " employee: "))


for salary in salary_arr:
    sum += int(salary)

print(sum)
avarage = int(sum)/n


print("Avarage salary of " + str(n) + " employees " + (str(round(avarage,1))))
