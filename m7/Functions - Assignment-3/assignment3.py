''' illustrates payment for scaling loan in a year using bisection'''
def payingdebtoffinayear(balance, annualinterestrate):
    '''returns payment for scaling loan in a year using bisection'''
    epsilon_ = 0.01
    minn = balance / 12
    maxx = balance * ((1+(0.2/12))**12)/12
    payment_ = (minn+maxx)/2

    while True:
        balance_copy = balance
        for i in range(12):
            ub_ = balance_copy - payment_
            balance_copy = ub_ + (annualinterestrate * ub_ / 12)
            i += 1
        if balance_copy > 0 and balance_copy > epsilon_:
            minn = payment_
        elif balance_copy < 0 and balance_copy < -1*epsilon_:
            maxx = payment_
        else:
            return "Lowest Payment: "+ str(round(payment_, 2))
        payment_ = (minn+maxx)/2


def main():
    ''' gets user input and calls debt func'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoffinayear(data[0], data[1]))

if __name__ == "__main__":
    main()
