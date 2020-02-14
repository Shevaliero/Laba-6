while True:
    from enum import Enum
    class month (Enum):
        Jan=1
        Feb=2
        Mar=3
        Apr=4
        May=5
        Jun=6
        Jul=7
        Aug=8
        Sep=9
        Oct=10
        Nov=11
        Dec=12
    class season (Enum):
        Win=1
        Spr=2
        Sum=3
        Aut=4
    try:
        s=month[input('month:')]
    except KeyError:
        print('Only:Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec')
        continue
    if s==month.Feb or s== month.Jan or s==month.Dec:
        print(season.Win.name)
    elif s==month.May or s==month.Mar or s==month.Apr:
        print(season.Spr.name)
    elif s==month.Aug or s==month.Jun or s==month.Jul:
        print(season.Sum.name)
    elif s==month.Sep or s==month.Oct or s==month.Nov:
        print(season.Aut.name)
    s=input('Rerun proggram?\nif yes press: 1\nelse press anything\n')
    if s=='1':
        continue
    else:
        break

