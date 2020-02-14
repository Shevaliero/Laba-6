while True:
    from enum import Enum
    class converter (Enum):
        USD =1
        EUR =2
        CZK =3
        PLN =4
    try:
        x=float(input('Amount of money:'))
    except ValueError:
        print('Only numbers!')
        continue
    try:
        p=converter[input('currency:')]
    except KeyError:
        print('Only USD, EUR, CZK,PLN')
        continue
    if p==converter.USD:
        print(x * 24.5)
    elif p==converter.EUR:
        print(x * 27.3)
    elif p==converter.CZK:
        print(x * 5.6)
    elif p==converter.PLN:
        print(x * 6.5)
    s=input('Rerun proggram?\nif yes press: 1\nelse press anything\n')
    if s=='1':
        continue
    else:
        break

