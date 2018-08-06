''' gives remaining balance '''
def payingdebtoffinayear(balance, annual_interestrate, monthly_paymentrate):
    '''returns the remaining balance '''
    balance_copy = balance
    for i in range(12):
        ub_ = balance_copy - (monthly_paymentrate*balance_copy)
        balance_copy = ub_ + (annual_interestrate*ub_/12)
        i = i + 1
    return "Remaining balance: " + str(round(balance_copy, 2))

def main():
    '''gets user data '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoffinayear(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()
