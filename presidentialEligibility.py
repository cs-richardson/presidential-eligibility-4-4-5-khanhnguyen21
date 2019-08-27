age = int(input('Age:'))
bornUS = input('Born in the US? y/n')
yrR = int(input('Years of Residency:'))
if age >= 35 and bornUS  == 'y' and yrR >= 14:
    print('You are eligible to run for president!')
else:
    print('You are not eligible to run for president.')
