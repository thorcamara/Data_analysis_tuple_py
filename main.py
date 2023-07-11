numbers = (int(input('Type a number: ')),
           int(input('Enter other number: ')),
           int(input('Type one more number: ')),
           int(input('Enter the last number: '))
           )
print(f'You typed \033[4;33m{numbers}\033[m')
if 9 in numbers:
    print(f'The number \033[4;32m9\033[m apeared \033[4;32m{numbers.count(9)}\033[m times')
else:
    print(f'The number \033[4;32m9\033[m apeared \033[4;31m{numbers.count(9)}\033[m times')
if 3 in numbers:
    print(f'The number \033[4;32m3\033[m apeared in the \033[4;32m{numbers.index(3)+1}\033[m position (last)')
else:
    print('The number \033[4;31m3\033[m was not typed in any position')
print('The \033[4;32mpair\033[m numbers entered were ', end='')
for n in numbers:
    if n % 2 == 0:
        print(f'\033[4;32m{n}\033[m', end=' ')

