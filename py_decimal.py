from decimal import Decimal 

result = Decimal('0.1') + Decimal('9.9')
result /= 3 

print(f"{result:4.2f}")