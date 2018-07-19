# Написать программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n – любое натуральное число.
#
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=a2_7.xml#R3Vpbb%2BMoFP41ltqVWvkCTvLYpu3sw652tF1pO48kJjY7jrEwadL59Qs2%2BAZp04njTFtpPHAMwXznOxeO7QTz9e4LQ3nyJ41w6vhutHOCO8f3Z9AVVyl4qQQQBpUgZiSqRF4jeCQ%2FsBKqefGGRLjoDOSUppzkXeGSZhle8o4MMUa33WErmnZXzVGMDcHjEqWm9F8S8aSSTv1JI%2F8dkzjRK3vhrLqzQMvvMaObTK3n%2BMGq%2FKtur5H%2BLbXRIkER3bZEwb0TzBmlvGqtd3OcSmg1bNW8hz136%2BdmOOOHTFAbKviL3jqOBBKqSxlPaEwzlN430ttye1j%2BgCt6CV%2BnoumJJt4R%2FiTF11D1vuk7WXQj1SK6yxQVBVlWwgeS6sn%2FYc5fFBPQhlMhapb%2Fg9JcjTN3qDZd0A1bqk34ijOIxViNCiuR3F5rmkLlC6ZrzNmLGMBwijh57hIBKT7F9bgGU9FQsNohVs%2FyjNKN%2BlFHADe7k9db1xGbmk50W1xvy%2Bu9qZc0FeyX%2BG8TwvFjjsrNboX9dbWwF6BnzDjevbp5fVfTU5nvZCI0Wgq2jTXUg5KWJQD3eMCCsTgpnuup3flWjzuUjBEqknLVHskzmuEOw91DmQtM5vpDM7ecKh4VvbQG5JRkvGj98lcpaDjhT7qcgFBx4uHACbNJd4JoVM%2FQkKLezEE8AaZh9Ykj3GsumwJ0TlD6t4gVKIvTA6xoQTmna9VhiuCyzUvlu%2F0hK6HnOU0pa7QvOMlJFs%2BFujGTRLuqyMUoF3qimZDMXuXF4QbbxxrYDDaw2KsHj7dXaOhh5V3sLh0%2FTLmEiYlWzOuNttQjdscHd17%2BFHax8C1YTCxYBAP4rtnIvkvdqr3XGWJtaHqs6bliLQCnwN9rod8C%2FKkGvBM7Bse%2FB%2BPPKMQLRlJAaPiCnejKluy4nqEeltD1YlOMk9aArpf0QtdwDFOLY5gO4BimBjAM8w3LrKCcM9erdztGqqfPe%2F3kGKiE%2BO2AUXBGv%2BNe5LUEY5SSWEbcZRmNhUAiRMSJ70bdWJMo2psYdF3EEKh7PdShiTqwgO4PAXpggq5idc5wE6wNkQjr2ZWWFznK9A1PC8XSbfmltH1fSN2sNcKySF96Rnuo%2Ba%2BdxKj2YPrP1mERlodFM8s1rYLhgvxAi3KAZKxK7sVoeOvAO2kPIuwUVQTyWuaR4hW3GEeZ9EqVL0VC%2B08Zn67AQHgHPbwnwWiWACyu98Ona%2B9NF3QNqJ0vANeus%2BGLI5PXCH%2By6ohBTwtKexkLXe%2B6e8QY00XoTOKTlkcM9naoOjOp2tRk39TfaQskIezT4s0SiTll8CKJhuyTVEmOMlwT7lHrJIGZ7K784wolx8ExnXXBACMWSoAl87dklvUhaU%2BGaZtzIcf%2FJv5dZHX%2B%2BY7p%2B5JZ29jLKsN9eN8K%2FhtjXyHCmHEOTPvmYjsw17KhAx34qO%2Bm3puAAWhJwMKREjBgVm9%2F%2BQQsCLtHhsBGy1PlX9CMn5%2BUlpY6IhyrkAvhSVB2PlQh16qBYyu5P5XbBr0iIQh7nxW8MT7sfoZw%2FKs%2Fe52ZlOXU62vPLf8MCulEN8E7FMvU8jbHjIh1ZUVQS79qkX8WZwbAmM5s7PcllsPk2c0M6i%2BMzhF%2F9eItJgsMBKEu1EvU5uVJeVi43EvqnNElLg54k9J8o%2FTXhqckw85wZO69YYH%2BiAkjtNa10VpuP1sU8r8ytblRKYy8tgur4S%2BV1ITu6fyA6DafmFXut%2FmML7j%2FHw%3D%3D

memoized = {}


def f1(n):
    if n == 1:
        return 1

    if n not in memoized.keys():
        memoized[n] = f1(n-1) + n

    return memoized[n]


def f2(n):
    return (n * (n + 1)) / 2


# Для первого миллиона чисел данное равенство выполняется.
for x in range(1, 1000000):
    assert(f1(x) == f2(x))
