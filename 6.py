# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше
# загаданного введенное пользователем число. Если за 10 попыток число не отгадано,
# то вывести его.
#
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=%20a2_6.xml#R7Vpbc%2BMmFP41nmkfmtHVlh9jJ2kf2pnMZGe6%2B7SDZSKpRUJFaOPsry8IkEAisbWx5biNH2R0OIA4l4%2FDgZm%2Fzne%2FElCmf%2BAtRDPP2e5m%2Fs3M85ahw56c8CwI4TIShIRkW0FyO8JD9h1KomyX1NkWVgYjxRjRrDSJMS4KGFODBgjBTybbI0bmqCVI4IDwEAM0pP6ZbWkqqJG36Oi%2FwSxJ1cjufClqNiD%2BOyG4LuR4M89%2FbH6iOgeqLznRKgVb%2FKSR%2FNuZvyYYU1HKd2uIuGiV2ES7uxdq2%2B8msKAHNZAtKvqs5g63TBTyFROa4gQXAN121FUzP8h7cNhbSnPEii4rwl1GP3PyVSjfvqiagpJnrYq%2FfpEdwGJ7zXXGXmMEqiqLBfEuQ6rjvyClz9JMQE0xI3Wf9jvGpeQTk%2BEzeFEeasK4JrHk8qSFAZJAyeW3umAmDnEO2fcyFgIRoNk3s3cgjS1p%2BTqBs4KUuV3%2BcuhvANVQWcwcsY9YVSUoWDnh5aLOGVNT7xBQbHF%2Bxf%2Bygv6k2NlAegtbL84I3pm35iMe3sB1xnD%2FvId3QzpKzzxN43tKMwofStCo8olhkWmQUrqQULh73SKGupYNvKV0VQllrnLdpw4Y3EjSUg0UAuft5uF6U7nnmV3QH7pgMJEL%2Bge5YFXHMayq1g1HGPsdQBW8HIP3PdPgPcdi8N6pDN7%2FWI%2BE5ZvOMJ%2FIGYKDnCGFqPyaM3dgcZDmEovVCK%2F4ROp9TmHQ%2FOtxXsf%2B%2F6lxU2JaXS74ky2B%2FOlr5UAr32jP2%2BYZ8jGZJiPRPGrKblNeSTZPtF1LftkDY1s3z0j1037NyEV4iA9HBZ5LkrGrtVodS8aLm3ETPlQd5w5b%2BigeDVHcPxmKBx8oLiDbRPHFRCg%2BPwjFCaxqRC8Mx73G41cKM%2FxXwWYlEeViwHcOcg4FxaYqx36tIaU7DSnvpMT402so10osjvZ6qy1dLRJrMpSo3IDuB9BqQDs3gdafD4G2BdWjA234AbQqKacDbTQR0Honkb%2BrSV8T%2BGddGXrd%2B5P%2FmzfvTVM2LfCsMZQ4K2il9XzPCZ0rzhemKwbzXvJzD39kJktZQXxBZwrtVA6yjsWLy3BJ4Gvo94jJy4tkplUZ9GLcwupcXY3gdvd1zcjGrHpuUaWg5MUU7gAzOy4DSDImTEg66r0ieZNAt%2B%2F27CWwZDpOBt2LqaD7zPAQDeHBnSqdEQ09UAaRLKbxtLgnEOFXL%2BZI6ibltzdFp4ybSQIgBBFOCMh7Jm7U3XcVZ8johbYU9sn2gs5AXP%2B%2FEGVpWSIncoGl3QVu1DapDfcdM%2BXS1xlCWVnBs9irDZZPZq7LiSM65x1GdK4ld%2BFOFlNPdub1jgHDpoGXvOboGnCt%2BSMjNSFXxiZj1CSNmiPq%2FlY8xfmmribCjNDAjLnt1Mq1gEZ0BNBQCbfTg8a5zfKtIHDYRmzeR3LhBrJVTy%2Fj9mTuMCTsH%2B3SJqN55rRSEPVEMmXMpvp9BQCaIELlWvvCYtOmpkQIrLLvYNMwcAHKrTzjDlezkGHIihtrJeyWNwAoS9gu8QbBR94Vl2UWA3QtyZQbMt%2BgxlmRfGqs%2BpfgSJIPfFPy7lDyvkXw3jEEf5rj78uKPtobf0c8OfmhfFJ780FawiJ4PZ%2FU5%2B%2Fln96cT1ITtGxnRYb%2FoE3t%2FgP9UF04Uz4vEzyOWPWZu%2F7wZZZ3vlP2wp7GLajbJvyPjrrRSZz%2FsgJf2%2BWXyc5NbddfjHzRG92sf%2BIattfK%2Fss%2B1c%2ByWyJz72SRjCUHzzXaO%2FMUV3eYdi2B%2FBkTH5Hl0saxgj722l0zF4tRd5Xfv%2F0X

import random

num = random.randint(0, 100)
success = False

help_messages = {
    True: "Загаданное число меньше",
    False: "Загаданное число больше"
}

result_messages = {
    True: "Вы угадали",
    False: "Попытки кончились"
}

for i in range(0, 10):
    guess = int(input("Угадайте число: "))

    if guess == num:
        success = True
        break
    else:
        print(help_messages[num < guess])

print(result_messages[success])
