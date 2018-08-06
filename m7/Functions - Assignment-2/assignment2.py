''' Assignment-2 - Paying Debt off in a Year '''

def payingdebtoffinayear(balance, annualinterestrate):
    '''returns amount of monthly payment to clear debt in year  '''
    payment_ = 10
    while True:
        balance_copy = balance
        for i in range(12):
            ub_ = balance_copy - payment_
            balance_copy = ub_ + (annualinterestrate*ub_/12)
            i += 1
        if balance_copy <= 0.05:
            return "Lowest Payment: "+str(payment_)
        payment_ += 10


def main():
    '''gets user from input and prints payment value'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoffinayear(data[0], data[1]))

if __name__ == "__main__":
    main()
