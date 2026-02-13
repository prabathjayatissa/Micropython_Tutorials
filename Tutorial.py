{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# MicroPython Tutorial: Raspberry Pi Pico\n",
    "This notebook covers MicroPython basics for the Raspberry Pi Pico, including LED control, button input, PWM, and reading sensors."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Setup\n",
    "# Ensure you have MicroPython firmware on your Pico and Thonny IDE or ampy installed.\n",
    "!pip install pyserial"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Hello MicroPython\n",
    "print(\"Hello, Raspberry Pi Pico!\")"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Blinking the Onboard LED\n",
    "from machine import Pin\n",
    "import time\n",
    "\n",
    "led = Pin(25, Pin.OUT)\n",
    "\n",
    "for i in range(10):\n",
    "    led.value(1)  # LED on\n",
    "    time.sleep(0.5)\n",
    "    led.value(0)  # LED off\n",
    "    time.sleep(0.5)"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Button Input\n",
    "button = Pin(14, Pin.IN, Pin.PULL_DOWN)\n",
    "\n",
    "while True:\n",
    "    if button.value():\n",
    "        print(\"Button pressed!\")\n",
    "    time.sleep(0.1)"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# PWM LED Brightness\n",
    "from machine import Pin, PWM\n",
    "import time\n",
    "\n",
    "led = PWM(Pin(25))\n",
    "led.freq(1000)\n",
    "\n",
    "for duty in range(0, 65535, 2000):\n",
    "    led.duty_u16(duty)\n",
    "    time.sleep(0.05)"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Analog Sensor (ADC)\n",
    "from machine import ADC, Pin\n",
    "import time\n",
    "\n",
    "sensor = ADC(Pin(26))\n",
    "\n",
    "while True:\n",
    "    value = sensor.read_u16()\n",
    "    print(\"Sensor value:\", value)\n",
    "    time.sleep(0.5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Conclusion\n",
    "- ✅ Basics covered:\n",
    "  - Printing\n",
    "  - GPIO input/output\n",
    "  - PWM\n",
    "  - Reading analog sensors\n",
    "- You are now ready to explore more advanced MicroPython projects!"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 }, 
 "nbformat": 4,
 "nbformat_minor": 5
}
