
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


limits = {
    'PASSIVE_COOLING': (0, 35),
    'HI_ACTIVE_COOLING': (0, 45),
    'MED_ACTIVE_COOLING': (0, 40),
}

def check_and_alert(alert_target, battery_char, temperature_in_c):
    lower_limit, upper_limit = limits[battery_char['coolingType']]
    breach_type = infer_breach(temperature_in_c, lower_limit, upper_limit)

  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
