from currency_converter import CurrencyConverter
from random import randint
import Utils


def get_money_interval(usd_amount, difficulty):
  """
  Will get the current currency rate from USD to ILS
  and will generate an interval as follows:
    For given difficulty d,
    and
    total value of money t
    the interval will be:
    (t - (5 - d), t +(5 - d))
  """
  t = CurrencyConverter().convert(usd_amount, 'USD', 'ILS')
  print(int(t))
  return int(t - (5 - difficulty)), int(t + (5 - difficulty))


def get_guess_from_user(usd_amount):
  """
  A method to prompt a guess from the user to enter
  a guess of value to a given amount of USD
  """
  output = f"Guess the ILS conversion from USD for {usd_amount}"
  usd_guess = Utils.is_digit(output)
  return int(usd_guess)


def play(difficulty):
  """
  Will call the functions above and play the game.
  Will return True / False if the user lost or won.
  """
  usd_amount = randint(1, 100)
  interval = get_money_interval(usd_amount, difficulty)
  return interval[0] <= get_guess_from_user(usd_amount) <= interval[1]

