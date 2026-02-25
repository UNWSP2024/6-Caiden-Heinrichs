#Week 6, Program 2 - Tax Rate
#Caiden Heinrichs
#02/27/26

STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025


def calculateTax(sales):
    stateTax = round(sales * STATE_TAX_RATE, 2)
    countyTax = round(sales * COUNTY_TAX_RATE, 2)
    totalTax = stateTax + countyTax
    return stateTax, countyTax, totalTax


def main():
    sales = float(input("Input total sales for the month: $"))
    stateTax, countyTax, totalTax = calculateTax(sales)
    print(f'State Tax: ${stateTax}')
    print(f'County Tax: ${countyTax}')
    print(f'Total Tax: ${totalTax}')


if __name__ == '__main__':
    main()
