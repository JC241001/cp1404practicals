

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = TARIFF_11

print('Electricity bill Estimator 2.0')

tariff_type = int(input('Which tariff?'))
daily_usage_per_kWh = float(input('Enter daily use in kWh: '))
num_billing_days = int(input('Enter number of billing days: '))

if tariff_type == '31':
    tariff = TARIFF_31

bill = tariff * daily_usage_per_kWh * num_billing_days

print('Estimated Bill: ${:.2f}'.format(bill))

