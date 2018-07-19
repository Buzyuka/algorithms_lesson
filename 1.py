# Написать программу, которая будет складывать, вычитать, умножать или
# делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а
# должна запрашивать новые данные для вычислений. Завершение программы
# должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.
#
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=a2_1.xml#R7R1bc6O2%2Btd4st2ZdBB3HmMn6Tkzu3s63d1p%2B7RDbNamxcYH403SX18JJEDSh41tEDh2HhwQEoLvfpMYGZPlyy%2BJv158jGdBNNK12cvIuB%2Fpumdp%2BJc0vOYNlmXkDfMknOVNqGz4HP4T0EY6br4NZ8GG65jGcZSGa75xGq9WwTTl2vwkiZ%2F5bt%2FjiJ917c8DqeHz1I%2Fk1t%2FDWbrIW13dKdv%2FE4TzBZsZ2V5%2B5cmf%2Fj1P4u2KzjfSje%2FZX3556bN70RfdLPxZ%2FFxpMh5GxiSJ4zQ%2FWr5MgoiAloEtH%2FdYc7V47iRYpU0GsBGb9JW9ezDDoKCncZIu4nm88qOHsnWcvV9A7qDhs0W6jPAhwofBS5j%2BQZp%2FtujZn%2BzKanZH8IJPp5G%2F2YTTvPExjNjgv4I0faWk4G%2FTGDeV03%2BI4zXtlz8wecrad2YvFW%2BTKe1F6S%2F1k3lQYK0AOKbjIF4GafKK%2ByRB5KfhD%2F72PqWoedGvhCo%2BoICFgUzn%2FuFHW3rTEYacd09%2Bx9oIv5XrsGP8O85%2BH2TERBGmf4KA50WYBp%2FXfvZyz5gDeTTQ6YIkDV52w0h%2BeTpAdymBUgZmp88lNyBGw4sKJ5ja6eAyJXAlQbpNVuS2IzLpmDDaSLcjPOn4KcFH87R47Z4AVkCDAswAIOZ2BDBbFQ%2Fj5%2FqjevJn0a8p8878zSKbVRAKq3gVcBJBO5rTLZnTjRMZPRuKH9V%2FrXRYx%2BEq3VTu%2FCtpKCnCNHiKsFxeEu%2FpjjRNoIH8AUqKKN6kEZFYshASqQYrozU5xABOQz%2F6DWtWfzWPGjDQU5ym8ZKeJJS6yXGaYV4Tu3zHSJ7EUZyUqMcEmYar%2BQSjNkgIld3mlJXEKUZSvMItntYOr0qYkVnVAFgVWaezqithISDHfhq8m8bLNQYFpqmfGsg2%2FPZp60LMNC0OMOy0AhgHAIzRggwDyLFbIUYvFWJsCEYKYrZu1Uqx%2BhBehsmziGRHCv2RvbP%2FydKLQYYTXzmTrJOAcUlmHpCLGru4WfsrdjV74LwZT1e9UuG9kTW%2Bm0y%2Bfvz64e7L%2F34bWfe4AboZ%2Fv%2F%2FbZzN779GsT8rG2omwfcCGPuplUf%2B9PXj%2BEHB027C%2Bap4YO4JPv%2F3l08tz1%2B5UsGxJCZ4IaDA0hNIHUHqwwbEpN2GmDS6EJPsuLTnSjEp23r9i0nAxEP2iWKyMQZMVYpqgFA2FQEZydZqRfRk0ucG%2B4E3sjBYxMun7aYXl6%2Fw5fa4fG4bcsBSJQf6pkIb4HVHERkayqJjQzZKAQzkfowKQWDvFwS3%2FYoBXTSVVYqBTkI%2F52YOOICIUEWgxtVvhTGge6pEhNPEVnjsV0gYon%2BsUEgYnfgMQ7RYXZkMDQ3GS%2FtkKIf2JDJ83y8Rmm6PmkoGD5fVuR0NL6cjanaVOR3d2w0vcqPhQUwUcyohxqLQdRB7P0B4iRypFF6OKrUwYMvFMAGVoSqUZMiZ7iz1P%2BTCACQKRUCHdFcZoMnv%2FiYtGQPwuQ1VBrUh%2B9xArmVH0yz8wSGJhfpJzvLWj4hVZNzhHlHwPeUSAXU3rmZkdqVLNEi8g%2BmFLF2x61ao8a1o7mXXzfSaoXUZjqI1g2TDvoPKkRQFbixJogNioqskiXv1yZm44EWIq6ziTbZeAbauJBAL7rHGI2dPCnERROtvWf3D3iRiJmZ23y0rxcv1bv5rZb9m9utmOpi161WVnF9CvGLe9zzgk0wqz9howMG51FowfCK1N8c%2FAEZvOPPTOGn4CP50ul1uIzLiWznWua%2BFy85nqkjmQZMMPnB4uw7%2F3l2JZc8jkOiJQCWTmhmaKephU8lVsJxAK6vt8ikQZEpZQAJSxqDMJa2m3IqrvIO8qjbMJdO9mku6CSwQMFXlmc0zXCFgazzJOs7PcrVod5EAZVU4w6h550gVKswxGuOv28JRx%2BLJwrIoWdRVjooDPIcfcHLpqHmtfK8FtgkxbVe172Z9XKmq0UEn4V026Kc9xoTqennHFurldQCcXVXMM1RettoGKg9MVYFS61qMC2PA0lUZTnLtR36436MSTX6FeXhbDI5akBjuKhNv7sgsf0m2pdtWOl7F0YDsTcUGpwUsQCEmuknN8v36Jgk24T%2F%2BU9aBMDK1pIxszQR2VrHmw8y5yfmUDKCZkvssTYJ9Ygy9cOpHd7Q5MzCI5pxi4%2BFLxsW3ZlsEavKwbmwn6G2AWq8lUNtfkpdePW3WNTGERz%2FanBJ5YFEbLDDGLHonB3HGVK7QDvftxXF65DBHXNgCcljBTa1zGJANFxFeOsUWDaC9Kb5zNEfAgAZgAEJAG3xnXw1K4q8C5owygxJwVc8tDmQhW6levrDNDzhahUxvqzEC1QaCTM88MBJkGXbLoSBLdhck6rnYUJAL8W1XsSBLLgeG7DIpr9PcpDuTiJGLFIaM7E5WDZ6bhgcKY2xVhTGW7HxDxBtucprvMt0bYCwk35bBZkM2Q2MFOEdFX8VYiuL0qSWaIJ4nC7KuDBD7GgRk%2FCPwlKogoH0tZK%2FBgKpCdjZ5RaqVEmxAgVbbkQVDV2FWW45iQVK4CL0eILl70A7Dj1bZgNBHXldCH1658aZjU0iEtyHBu7PIlHeV8FSaCxJe1TJ3u1nuvki%2BZbbkISKtdqOrBr7d%2FspP4B6HbGXVTfEkdBdu16sGczZ9%2F74tdKG%2B0QGEdWeJBUeWxG9zrxwbWP%2FuqPJsHdUVeYOU0RAGVO1AYMsxtao8zgSdRuZYzUZ5eX31Sv97ZFhCbMwFrHXQomvDXGchN6gqgs8pC1Kdk7NlRQCfJ6bF%2Fvg3u0l1MQh3%2BsBGyT0t7hJdVIKPH49Lcx8dFlVp44tqw1OqNmSn9hzqZFwhGOZCflFXwTAHKGS%2FtBy%2BkFdxXRn%2BXflJTBC%2B%2BfXxDpCld1Rl6Z0zzNKLe1VaSKVUuOAcvQPk6J2h5OgLq6fI0TtVvO7tb9F13m3l551rfr4eN4Ae6So77zTLzgsrdM89N6%2B7Ym7elCDeVWaeuTodZAsKH%2FCQaNxh%2Faum7%2Fj2PXlrxSuWOauS%2Bk1mxaV6zLSywUpyi7XXbvY7ofW%2B5Nhjw8E1%2B4VTdtDy%2Fwe%2BQ3Zbesmlc9GV1I2h16MtIXwkxPJcwMCFTIkWbC9XtSkxxCiTC%2BR63VM%2FE9IYA8BCCGhrFwyxOPr2d%2FA62rUzUr5PQMMw9iYN1jvvtk92DG3Zv7hLUlGkomSXpOuy%2F1Llc6ykatm%2FW%2BNIokp0BFHNU6qRauyk0FGC%2BsKndkW93FE%2FtM6WjjAYP4TLMO2H7E3IGYXIvg0N4imLkQyZ7AGv1FUVP3EhL08W5kVOthD5XJY2UwY70qW9y3ZN8CYa16e0QeSy33yBRA4U%2Bnqq0qEu4NDdCxtCMbeA2P51JhDPERWj6ljXuRI%2F8aMoiOJ54i%2BJ8RYkIX7LIBGv%2FVpe6GN%2FWUvlp2e9S%2Fm4kwe4EN6pn0ltDOV6FwJWAH1V4hR6Zz%2Ff9a1ukMerG9uWy%2FOKz6tz0SunBYRevXLGPgJLqfLKPTDxOoTKYdF2O5aZD9gSEGbnd33Lk8Gun0GaIDwcw4XWnUPiow1rFc9%2FlR%2B6B4QikKYrEiAIdWL6nNk6JggHnqpwkCeHg%2BQwaiZMb0i1nmTpE%2FfCldsrUdNsMGrgJCj9jGbhBbOKGSAcpEMWfxt1f0i7xoMYjQt0ryoe5AHxoOouPMc7zKT7nVbJ0TksDVgtpSzydRo9znNxznj3V8FvqDlwQ07LPczfnkcufqTINYCEH%2BiRt0EcNXGUuog44ImoLLOyDR5WniXLMjh6YbQhywDH%2Bv6tblKGTF2oF9dluuxqjzKkdbOVQr25BNS09a42qHkq2qzKvhKOOglzn5nNCiMBqQp0F9PvCT1IdeDHr3c%2BYr2b0s%2FCCyuTPVuOYHe16hxp3WT1AZZojex3cdexLAF81u%2FkChm4JhZrAiFhISYi8oegw0pUHlqsixlN2J9Ro75LXbmuNMI0NYGYTqvXLeDcvukO7j9wOOMP3bbWBNvaU5ntQlqN5yUszzmiHPec7EhdsCM9R93OBojFVC9oJwlUrFRlAAcCPt0BvBPD%2FdxsRgTkfxFSlQAupt%2B3wICGLvVx1ueQLBQ6Ph6jPP1iaqJit7zGe6i2go5OdtDaxRMDjIFS8hd5QtUeWsX0TXmCulP0K2gHsocxSM%2FJtvh958vvoqlwnZgWuuhMACV4kQtU7TNUTN%2B0NggMzfdaLRSQR%2FfT4N1w8%2F3iHgHYk9QlPjOgCmwW%2Bj8Jx0yPndGGPLvCsMcyGrBXTEcxCow3xCHc9rqJUZQ2OqMstCdGIY1oPUaB5MWs3EIihpse%2BdGTIjsdhgHwaRITAVcCFL%2FU4mM8C0iPfwE%3D


def accumulator_validator(value):
    try:
        int(value)
        return True, ""
    except:
        return False, "Вы ввели не число"


def number_validator(value):
    is_valid, error_message = accumulator_validator(value)

    if not is_valid:
        return is_valid, error_message

    value = int(value)
    sign = components[SIGN]["payload"]

    if value == 0 and sign == "/":
        return False, "Делить на ноль н§ельзя"

    return True, ""


def sign_validator(value):
    return value in "+-*/", "Не допустимый знак, введите один из: +-*/"


ACCUMULATOR = 0
SIGN = 1
NUMBER = 2

components = (
    # Сюда мы складываем результат
    {
        "help_text": "Введите число",
        "payload": None,
        "validator": accumulator_validator
    },
    # Тут сохраняется знак введенный пользователем
    {
        "help_text": "Введите знак",
        "payload": None,
        "validator": sign_validator
    },
    # Число с которым провозится операция, к примеру
    # если знак +, то будет сложен резултат с этим числом.
    {
        "help_text": "Введите число",
        "payload": None,
        "validator": number_validator
    },
)


def evaluate():
    a = int(components[ACCUMULATOR]["payload"])
    b = int(components[NUMBER]["payload"])
    sign = components[SIGN]["payload"]

    return {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b
    }[sign]


print("для завершения введите 0")
control_key = None
step = 0

while True:
    component = components[step]
    control_key = input(component["help_text"] + ": ")
    component["payload"] = control_key
    is_valid, error_message = component["validator"](component["payload"])

    if control_key == '0' and step == 1:
        break

    if not is_valid:
        print(error_message)
        continue

    step += 1

    if step >= 3:
        components[ACCUMULATOR]["payload"] = evaluate()
        step = 1

print(f"Результат: {components[ACCUMULATOR]['payload']}")
