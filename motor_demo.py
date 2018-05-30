#!/usr/bin/env python3

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import motor

def main():
  recognizer = aiy.cloudspeech.get_recognizer()
  recognizer.expect_phrase('on')
  recognizer.expect_phrase('off')

  aiy.audio.get_recorder().start()

  while True:
    print('Listening')
    text = recognizer.recognize()
    if text is None:
      print('waiting')
    else:
      print('Heard "', text, '"')
      if 'drive' in text:
        motor.forward(0.5, 2)
      elif 'left' in text:
        motor.leftturn(0.5, 2)
      elif 'right' in text:
        motor.rightturn(0.5, 2)
if __name__ == '__main__':
  main()

