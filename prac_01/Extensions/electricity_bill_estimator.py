

print('Electricity bill Estimator')

cents_per_kWh = int(input('Enter cents per kWh: '))/100

daily_usage_per_kWh = float(input('Enter daily use in kWh: '))

num_billing_days = int(input('Enter number of billing days: '))

bill = cents_per_kWh * daily_usage_per_kWh * num_billing_days

print('Estimated Bill: ${}'.format(bill))

