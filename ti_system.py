# JuliNator99 - juli.schwers@gmail.com
from pynput import keyboard

# Start of INIT
__current_key = None


# INTERNAL FUNCTIONS
def __get_key(key):
  if type(key) == keyboard.Key: return str(key).removeprefix("Key.")
  return key.char


def __on_press(key):
  global __current_key
  pressed = __get_key(key)
  __current_key = pressed


def __on_release(key):
  global __current_key
  pressed = __get_key(key)

  if __current_key != pressed: pass
  __current_key = None


# TI FUNCTIONS
def get_key():
  global __current_key
  if __current_key is None: return ""

  key = __current_key
  __current_key = None
  return key


listener = keyboard.Listener(on_press=__on_press, on_release=__on_release)
listener.start()