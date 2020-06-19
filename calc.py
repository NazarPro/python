import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int, default=0)
parser.add_argument('--payment', type=int, default=0)
parser.add_argument('--periods', type=int, default=0)
parser.add_argument('--interest', type=float, default=0)
args = parser.parse_args()
if args.type == "annuity":
    if args.principal != 0 and args.periods != 0 and args.interest != 0.0:
        prin = args.principal
        cper = args.periods
        crint = args.interest
        i = crint / (12 * 100)
        ap = math.ceil(prin * ((i * math.pow((1 + i), cper)) / ((math.pow((1 + i), cper) - 1))))
        op = ap * cper - prin
        print('Your annuity payment = {ap}!'.format(ap=ap))
        print('Overpayment = {op}'.format(op=op))
    elif args.payment != 0 and args.periods != 0 and args.interest != 0.0:
        monp = args.payment
        cper = args.periods
        crint = args.interest
        i = crint / (12 * 100)
        n = math.log((monp / (monp - i * cper)), 1 + i)
        cp = math.ceil(monp / ((i * math.pow((1 + i), cper)) / ((math.pow((1 + i), cper) - 1))))
        op = cp - monp * cper
        print('Your credit principal = {cp}!'.format(cp=cp))
        print('Overpayment = {op}'.format(op=op))
    elif args.principal != 0 and args.payment != 0 and args.interest != 0.0:
        prin = args.principal
        monp = args.payment
        crint = args.interest
        i = crint / (12 * 100)
        n = math.log((monp / (monp - i * prin)), 1 + i)
        ny = math.floor(n / 12)
        nm = math.ceil(n - ny * 12)
        if nm < 12:
            pass
        elif nm == 12:
            nm = 0
            ny += 1
            if ny > 1:
                if nm > 1:
                    print('You need {ny} years and {nm} months to repay this credit!'.format(ny=ny, nm=nm))
                elif nm == 0:
                    print('You need {ny} years to repay this credit!'.format(ny=ny))
                else:
                    print('You need {ny} years and {nm} month to repay this credit!'.format(ny=ny, nm=nm))
            elif ny == 0:
                if nm > 1:
                    print('You need {nm} months to repay this credit!'.format(nm=nm))
                else:
                    print('You need {nm} month to repay this credit!'.format(nm=nm))
            else:
                if nm > 1:
                    print('You need {ny} year and {nm} months to repay this credit!'.format(ny=ny, nm=nm))
                elif nm == 0:
                    print('You need {ny} year to repay this credit!'.format(ny=ny))
                else:
                    print('You need {ny} year and {nm} month to repay this credit!'.format(ny=ny, nm=nm))
        op = monp * (ny * 12 + nm) - prin
        print('Overpayment = {op}'.format(op=op))
    else:
        print('Incorrect parameters.')
elif args.type == "diff":
    if args.principal != 0 and args.periods != 0 and args.interest != 0.0:
        prin = args.principal
        cper = args.periods
        crint = args.interest
        i = crint / (12 * 100)
        m = 1
        sum = 0
        while m <= cper:
            d = prin / cper + i * (prin - (prin * (m - 1) / cper))
            d = math.ceil(d)
            sum += d
            print('Month {m}: paid out {d}'.format(m= m, d= d))
            m += 1
        op = sum - prin
        print(sum)
        print('Overpayment = {op}'.format(op=op))
    else:
        print('Incorrect parameters.')