## Usage of guzi.py

```
guzi.py --play
guzi.py -p
```
Those commands will run a "game" where you will make some tests
First you need to enter names of each players (usually "P1", "P2", etc) and his daily quotient, when you have all the players you want, enter "End" or "E".
Then informations of each player are display and you are prompt again. You can now run days.
```
>> <source> <target> <amount> <unit>
```
Where source and target are players names, amount an integer and unit G|GA|g|ga (Guzi or Guza)

```
>> End | E # This ends the day
```



## Child spending
### Spending nothing until 18
```
python guzi.py -b 1 -d 6570
    total earned = 289835.10, quotient = 66.18
```

### Spending half until 18
```
python guzi.py -b 1 -d 6570 -s 0.5
total earned = 102511.44, quotient = 46.80
```

### Child spending all he gets each year:

```
python guzi.py -b 1 -d 365 -s 0.05555555555555555 // 1/18
    total earned = 3487.04, quotient = 15.16
python guzi.py -b 3487 -d 365 -s 0.111111111111 // 2/18
    total earned = 9423.66, quotient = 21.12
python guzi.py -b 9423 -d 365 -s 0.12 // 3/18
    total earned = 16963.56, quotient = 25.69
python guzi.py -b 16963 -d 365 -s 0.2222222222222222 // 4/18
    total earned = 24756.00, quotient = 29.14
python guzi.py -b 24756 -d 365 -s 0.2777777777777778 // 5/18
    total earned = 32822.44, quotient = 32.02
python guzi.py -b 32822 -d 365 -s 0.3333333333333333 // 6/18
    total earned = 40912.64, quotient = 34.46
python guzi.py -b 40912 -d 365 -s 0.3888888888888889 // 7/18
    total earned = 48833.13, quotient = 36.55
python guzi.py -b 48833 -d 365 -s 0.4444444444444444 // 8/18
    total earned = 48833.13, quotient = 36.55
python guzi.py -b 48833 -d 365 -s 0.5                // 9/18
    total earned = 56428.75, quotient = 38.36
python guzi.py -b 56428 -d 365 -s 0.5555555555555556 // 10/18
    total earned = 62762.84, quotient = 39.74
python guzi.py -b 62762 -d 365 -s 0.6111111111111112 // 11/18
    total earned = 68486.37, quotient = 40.91
python guzi.py -b 68486 -d 365 -s 0.6666666666666666 // 12/18
    total earned = 73523.47, quotient = 41.89
python guzi.py -b 73523 -d 365 -s 0.7222222222222222 // 13/18
    total earned = 77811.01, quotient = 42.69
python guzi.py -b 77811 -d 365 -s 0.7777777777777778 // 14/18
    total earned = 81299.29, quotient = 43.32
python guzi.py -b 81299 -d 365 -s 0.8333333333333334 // 15/18
    total earned = 83948.49, quotient = 43.79
python guzi.py -b 83948 -d 365 -s 0.8888888888888888 // 16/18
    total earned = 85730.00, quotient = 44.09
python guzi.py -b 85730 -d 365 -s 0.9444444444444444 // 17/18
    total earned = 86625.67, quotient = 44.25
```

### Child spending all he gets each year + tutor spending all too:

```
python guzi.py -b 1 -d 365 -s 0.5277777777777778
    total earned = 1241.80, quotient = 10.75
python guzi.py -b 1241 -d 365 -s 0.5555555555555556
    total earned = 3343.13, quotient = 14.95
python guzi.py -b 3343 -d 365 -s 0.5833333333333334
    total earned = 5857.36, quotient = 18.03
python guzi.py -b 5857 -d 365 -s 0.6111111111111112
    total earned = 8593.25, quotient = 20.48
python guzi.py -b 8593 -d 365 -s 0.6388888888888888
    total earned = 11429.09, quotient = 22.53
python guzi.py -b 11429 -d 365 -s 0.6666666666666666
    total earned = 14276.04, quotient = 24.26
python guzi.py -b 14276 -d 365 -s 0.6944444444444444
    total earned = 17065.03, quotient = 25.75
python guzi.py -b 17065 -d 365 -s 0.7222222222222222
    total earned = 19740.59, quotient = 27.03
python guzi.py -b 19740 -d 365 -s 0.75
    total earned = 22256.64, quotient = 28.13
python guzi.py -b 22256 -d 365 -s 0.7777777777777778
    total earned = 24575.99, quotient = 29.07
python guzi.py -b 24575 -d 365 -s 0.8055555555555556
    total earned = 26666.95, quotient = 29.88
python guzi.py -b 26666 -d 365 -s 0.8333333333333333
    total earned = 28503.88, quotient = 30.55
python guzi.py -b 28503 -d 365 -s 0.8611111111111112
    total earned = 30065.45, quotient = 31.09
python guzi.py -b 30065 -d 365 -s 0.8888888888888888
    total earned = 31334.82, quotient = 31.53
python guzi.py -b 31334 -d 365 -s 0.9166666666666667
    total earned = 32297.78, quotient = 31.85
python guzi.py -b 32297 -d 365 -s 0.9444444444444444
    total earned = 32944.91, quotient = 32.06
python guzi.py -b 32944 -d 365 -s 0.9722222222222222
    total earned = 33269.56, quotient = 32.16
```

### Child spending nothing but tutor spending all:

```
python guzi.py -b 1 -d 365 -s 0.4722222222222222
    total earned = 1465.09, quotient = 11.36
python guzi.py -b 1465 -d 365 -s 0.4444444444444444
    total earned = 4292.16, quotient = 16.25
python guzi.py -b 4292 -d 365 -s 0.4166666666666667
    total earned = 8180.84, quotient = 20.15
python guzi.py -b 8180 -d 365 -s 0.3888888888888889
    total earned = 13062.55, quotient = 23.55
python guzi.py -b 13062 -d 365 -s 0.3611111111111111
    total earned = 18921.36, quotient = 26.65
python guzi.py -b 18921 -d 365 -s 0.3333333333333333
    total earned = 25761.41, quotient = 29.53
python guzi.py -b 25761 -d 365 -s 0.3055555555555556
    total earned = 33597.67, quotient = 32.27
python guzi.py -b 33597 -d 365 -s 0.2777777777777778
    total earned = 42451.54, quotient = 34.88
python guzi.py -b 42451 -d 365 -s 0.25
    total earned = 52349.14, quotient = 37.41
python guzi.py -b 52349 -d 365 -s 0.2222222222222222
    total earned = 63319.21, quotient = 39.86
python guzi.py -b 63319 -d 365 -s 0.19444444444444445
    total earned = 75391.65, quotient = 42.24
python guzi.py -b 75391 -d 365 -s 0.16666666666666666
    total earned = 88597.83, quotient = 44.58
python guzi.py -b 88597 -d 365 -s 0.1388888888888889
    total earned = 102970.80, quotient = 46.87
python guzi.py -b 102970 -d 365 -s 0.1111111111111111
    total earned = 118544.37, quotient = 49.12
python guzi.py -b 118544 -d 365 -s 0.08333333333333333
    total earned = 135353.16, quotient = 51.34
python guzi.py -b 135353 -d 365 -s 0.05555555555555555
    total earned = 153431.66, quotient = 53.54
python guzi.py -b 153431 -d 365 -s 0.027777777777777776
    total earned = 172814.22, quotient = 55.70
```
