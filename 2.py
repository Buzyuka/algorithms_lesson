# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и
# 2 нечетные (3 и 5).
#
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=a2_2#R7VnNctsgEH6WHjQTXzoSsmz5aDtOe2hnMpNDm1MHW0RSi4QG4dju0xcESOgvtZtaTpv4wMCyy7LLfrsIW%2B4y2X%2BgMIs%2BkwBhC9jB3nKvLQBmns1bQThIgjfzJSGkcSBJTkW4i38iRVRy4TYOUF5jZIRgFmd14oakKdqwGg1SSnZ1tgeC61ozGKIW4W4DcZv6JQ5YJKk%2BmFb0jygOI63ZmczkzBpufoSUbFOlzwLuQ%2FGT0wnUaylD8wgGZGeQ3JXlLikhTPaS%2FRJh4VrtNil30zNb7puilB0joAzK2UGbjgLuCTUklEUkJCnEq4q6KMxDYgGbjyKWYN51eBftY%2FZVkN97anSvZ1JGD8aUGN6rBVAazMWR8eEGwzyPN5J4E2O98HfE2EFFCdwywknV1j4Rkik%2BaYywoNcdipSTLd0oLqACDNIQKS6vPAoe4YgkiO%2BXs1CEIYsf66tDFWthyVf5m3eUy7vdr1Q%2FQrxVi1rcJ7Nr0S5sixvlT3Wft4uiXbXPDGOODHE2uyhm6C6DhW07js36CSl1iDK0f9pFbeOVAPBV6Cpoj9VwV%2BHE0dEdGRjRfM9xl9vtrrlyi2il67zCdZOX5ShvQE%2F5b7iWIK7jejIQrr3uQC3aBTDCdWy5cwtMMN%2FfYk15L2SFvZKSZzDVtDjNtuxbABnUs3wTJkPXMo0Y4NUmE13uOIgxwiSkMOGMGaIxtxHR5txtNXEBxJToGAIxjtNy1%2BuDzKQNGcfuPrO%2FjplJCzPpNlnz0OMnLoayBN4Umd3WWb4EkmPQZTs1ZoFRUEHRLosFeccxiLYhMi8ortYLDH65Dd76BkVLKX5f7QGYVdzk91RFbwZdPaTODzqnATpgt0Hnngt0s%2FNjzn7pmHPbmHMHgpzjvuW88puzlvTAUCdgt28Kqo5nFOlCjh5RWqXBjssBjnPWcy246uJ%2FiLEo6idIYJisA2iobwjti4sMTyqCw%2BvZJuiXF7b1mtcr1MFrgWW%2FFllR8tGofVkiQfCfu%2FjdZR1sSBihffn65zXqn99R%2F%2FxzXTrHQyXgSyfZ5yZUJXpLYq6lPDx3XD%2B88htbLyGTupJqnEu5jeOOquetRt4cF8%2F4shPs86nxbgH0S0a5sHdlTRcnYBSLenE095WoLyNrej2SGeZEXf2J8UllT2aI3yah6pnMq9%2BxL%2BRCXj4G86DSdVLOPtrX%2F9aTgTOrJwB30pG97Y7s3UwUf5S9vVeSvYf7ROHD6s8PmaWrP5jc1S8%3D

input_data = input("Введите число: ")
numbers = list(map(int, input_data))

even = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))

print(f"Четные({len(even)}): {list(even)}")
print(f"Не четные({len(odd)}): {list(odd)}")
