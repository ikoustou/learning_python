income =15000
if income < 10000:
	tax_multiplier =0.0
elif income < 30000:
	tax_multiplier=0.2
elif income < 100000:
	tax_multiplier=0.35
else:
	tax_multiplier=0.45

print(' I will pay : ' , income* tax_multiplier, ' in taxes')