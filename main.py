bottleCounter = 100
scndBottleCounter = 99

for index in range(99):
    bottleCounter -= 1
    print('\n\n', bottleCounter, ' bottles of beer on the wall, ', bottleCounter, ' bottles of beer.')
    scndBottleCounter -=1
    if scndBottleCounter == 0:
        print('Take one down and pass it around, no more bottles of beer on the wall.')
    else:
        print('Take one down and pass it around, ', scndBottleCounter , ' bottles of beer on the wall.')

print('\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')