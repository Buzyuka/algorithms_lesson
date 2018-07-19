# Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
#
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=a2_5.xml#R7Vpbc9sqEP41mkkempHQxfJjnKTtwzkznUlnzukjkYlEi4WKcG3313cR6K4kVm3LmTZ%2B0MCygNjd72MFttyb1faDwFnyL18SZiF7ubXcWwuhuW%2FDUwl2WuDPQy2IBV1qkVML7ulPYoSmX7ymS5K3FCXnTNKsLYx4mpJItmRYCL5pqz1y1p41wzHpCe4jzPrS%2F%2BhSJloaolkt%2F0honJQzO8Fctzzg6Fss%2BDo181nIfSx%2BunmFy7HMQvMEL%2FmmIXLvLPdGcC51abW9IUyZtjSb7vf%2BidbqvQVJ5T4dzGvnclcunSzBEqbKhUx4zFPM7mrpolgeUQPYUEvkikHRgSLZUvm%2FEl%2F5pvalbEml2DWaVPWLGYCky2vlMqhGDOc5jbTwPWXlwF%2BJlDsTJXgtOYjqV%2FuH88zo6cWoFTxpDiPK%2BVpERss1AYZFTIxWULkCIpzwFYH3BRVBGJb0R3t0bGItrvRqe0PBmHzY%2FGbqH5itzaAW2GR%2Bq54L24JFhbOyDM9F8bzr%2B4wxQIbyzSahktxnuFjbBrDZ9pCZjghJts%2BbqL9408EtQ9dA2zPVTY0Tp1RJGhgp9Q4xlzdsrmtjFvXUpvML0wWvylAzNKGlKn45ObDPDN6gD17HHvbL0dEb9MMRBQzeYpEJAsVYFRlNoWwX7bblLyz%2FttSC8RuKPYe13TF9wDqTBqz3thOhsB%2FM3kSxHA5TKyqIVO87qEGznuVel2H8IOoQ1pI8w2lD9n3NdcluVioMdLR7I1x95TS9UDi6fKFX8006wQSJVqaK4AHMGGE8FnilkEoEBWMR0W37VDecAXvBlNuqc5ossIG8Btiqpgp5pu3M2Cs%2FPZrgCw8EX9EVloV3DYUMolnmjZE%2FKUEdCshuh0IvhX9BPwjsjvP1G9ShUC1lP2Z2%2F5JUYigCnCdge3T%2BLScfSCaaTEfhExvdaCbdlz%2B349RpOk6fpOsVEViSEX0uRugKnManGttFI5RHG95RBLK39uURdreEbDGAobOvGWm1o6FJtrRqa9p1eKqxpaHwVOkk%2BltIqzwea5IWmoq0nL1IS6VuVzjLwC5jwPnYyBZnC8xonIJzZrfvoDZimCgRY9hjewlT%2FFaeegB%2Bp%2F7Uq3C369Sb2LRPlW7OpsLmK%2F7Uc9AAbt2pcBuewgOO1U%2F4X4WVD83geym3H3TPQDuw0F41vTp%2BGZd9l3HyAsVeFIkhvMViZIoyjt9gaH%2FkBPY4fbVEfVS2f5%2BXdJ8j3oSvHtb5JKTrOu2ocYM%2B6TreAOmGxyBd%2F410DcF2SHeqEzbnicuetyO28xyxeQM5z%2BmO2Abuok6z4xr4OdYrPGLzBuB36GXNb52xdTdwP3z%2BjK2r3zmTO%2FiMzenfbBYfTREjWFxc9retM18N%2BUNb18muhvxh4mxe9aI9%2BAmWL9uWESSnP%2FFDoaAMacIGtPU9nbtQIMg1HlSH4iMUyow8qqGUTWmE2bURSwUQRawRTePPBVreecfxgOd3koeZ1%2FPAUO6AjuGAgYtO5QDP%2FDXhjzK0Ow%2Bv%2FPZG4QU9U7vHMTVU6%2F%2F6aN6o%2F0%2Fl3v0C

line = []

for idx, x in enumerate(range(32, 128)):
    aligned = f" {x}" if x < 100 else x
    line.append(f"{aligned}-{chr(x)}")

    if (idx + 1) % 10 == 0:
        print(" ".join(line))
        line.clear()

print(" ".join(line))
