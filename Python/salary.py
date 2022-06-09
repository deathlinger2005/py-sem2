def netSalary(basic,hra):
    totalSalary = 2*(basic + hra)
    return totalSalary

# a = netSalary(8500,4400)
# print(a)

def updatedNetSalary(func):
    def inner(basic, hra):
        if basic < 10000:
            basic = 10000
        if hra < 5000:
            hra = 5000
        return func(basic,hra)
    return inner

netSalary1 = updatedNetSalary(netSalary)
updatedSalary = netSalary1(8500,4400)
print(updatedSalary)