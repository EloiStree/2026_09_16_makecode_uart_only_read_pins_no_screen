def parse_int_360_to_b62(num: number):
    int_to_b62_char("" + str(Math.round(Math.map(num, 0, 360, 0, 61))))

def on_bluetooth_connected():
    global bluetooth_connected
    bluetooth_connected = 1
    basic.show_leds("""
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global bluetooth_connected
    bluetooth_connected = 0
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        """)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def parse_int_1023_to_b62(num2: number):
    int_to_b62_char("" + str(Math.round(Math.map(num2, 0, 1023, 0, 61))))
def five_boolean_to_base32(bool2: bool, bool22: bool, bool3: bool, bool4: bool, bool5: bool):
    five_boolean_to_base_32_char(False,
        False,
        False,
        False,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "0")
    five_boolean_to_base_32_char(False,
        False,
        False,
        False,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "1")
    five_boolean_to_base_32_char(False,
        False,
        False,
        True,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "2")
    five_boolean_to_base_32_char(False,
        False,
        False,
        True,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "3")
    five_boolean_to_base_32_char(False,
        False,
        True,
        False,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "4")
    five_boolean_to_base_32_char(False,
        False,
        True,
        False,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "5")
    five_boolean_to_base_32_char(False,
        False,
        True,
        True,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "6")
    five_boolean_to_base_32_char(False,
        False,
        True,
        True,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "7")
    five_boolean_to_base_32_char(False,
        True,
        False,
        False,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "8")
    five_boolean_to_base_32_char(False,
        True,
        False,
        False,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "9")
    five_boolean_to_base_32_char(False,
        True,
        False,
        True,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "A")
    five_boolean_to_base_32_char(False,
        True,
        False,
        True,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "B")
    five_boolean_to_base_32_char(False,
        True,
        True,
        False,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "C")
    five_boolean_to_base_32_char(False,
        True,
        True,
        False,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "D")
    five_boolean_to_base_32_char(False,
        True,
        True,
        True,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "E")
    five_boolean_to_base_32_char(False,
        True,
        True,
        True,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "F")
    five_boolean_to_base_32_char(True,
        False,
        False,
        False,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "G")
    five_boolean_to_base_32_char(True,
        False,
        False,
        False,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "H")
    five_boolean_to_base_32_char(True,
        False,
        False,
        True,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "I")
    five_boolean_to_base_32_char(True,
        False,
        False,
        True,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "J")
    five_boolean_to_base_32_char(True,
        False,
        True,
        False,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "K")
    five_boolean_to_base_32_char(True,
        False,
        True,
        False,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "L")
    five_boolean_to_base_32_char(True,
        False,
        True,
        True,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "M")
    five_boolean_to_base_32_char(True,
        False,
        True,
        True,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "N")
    five_boolean_to_base_32_char(True,
        True,
        False,
        False,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "O")
    five_boolean_to_base_32_char(True,
        True,
        False,
        False,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "P")
    five_boolean_to_base_32_char(True,
        True,
        False,
        True,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "Q")
    five_boolean_to_base_32_char(True,
        True,
        False,
        True,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "R")
    five_boolean_to_base_32_char(True,
        True,
        True,
        False,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "S")
    five_boolean_to_base_32_char(True,
        True,
        True,
        False,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "T")
    five_boolean_to_base_32_char(True,
        True,
        True,
        True,
        False,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "U")
    five_boolean_to_base_32_char(True,
        True,
        True,
        True,
        True,
        bool2,
        bool22,
        bool3,
        bool4,
        bool5,
        "V")
def parse_int_255_to_b62(num3: number):
    int_to_b62_char("" + str(Math.round(Math.map(num3, 0, 255, 0, 61))))

def on_uart_data_received():
    global received_ble
    received_ble = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    if received_ble == "PING":
        bluetooth.uart_write_line("PONG")
    if received_ble == "?":
        push_uart()
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

def if_value_equals_set_to_b58(value: str, is_equals: str, set_to: str):
    if value == is_equals:
        list_analog_char.append(set_to)
def int_to_b62_char(int_value: str):
    if_value_equals_set_to_b58(int_value, "0", "0")
    if_value_equals_set_to_b58(int_value, "1", "1")
    if_value_equals_set_to_b58(int_value, "2", "2")
    if_value_equals_set_to_b58(int_value, "3", "3")
    if_value_equals_set_to_b58(int_value, "4", "4")
    if_value_equals_set_to_b58(int_value, "5", "5")
    if_value_equals_set_to_b58(int_value, "6", "6")
    if_value_equals_set_to_b58(int_value, "7", "7")
    if_value_equals_set_to_b58(int_value, "8", "8")
    if_value_equals_set_to_b58(int_value, "9", "9")
    if_value_equals_set_to_b58(int_value, "10", "A")
    if_value_equals_set_to_b58(int_value, "11", "B")
    if_value_equals_set_to_b58(int_value, "12", "C")
    if_value_equals_set_to_b58(int_value, "13", "D")
    if_value_equals_set_to_b58(int_value, "14", "E")
    if_value_equals_set_to_b58(int_value, "15", "F")
    if_value_equals_set_to_b58(int_value, "16", "G")
    if_value_equals_set_to_b58(int_value, "17", "H")
    if_value_equals_set_to_b58(int_value, "18", "I")
    if_value_equals_set_to_b58(int_value, "19", "J")
    if_value_equals_set_to_b58(int_value, "20", "K")
    if_value_equals_set_to_b58(int_value, "21", "L")
    if_value_equals_set_to_b58(int_value, "22", "M")
    if_value_equals_set_to_b58(int_value, "23", "N")
    if_value_equals_set_to_b58(int_value, "24", "O")
    if_value_equals_set_to_b58(int_value, "25", "P")
    if_value_equals_set_to_b58(int_value, "26", "Q")
    if_value_equals_set_to_b58(int_value, "27", "R")
    if_value_equals_set_to_b58(int_value, "28", "S")
    if_value_equals_set_to_b58(int_value, "29", "T")
    if_value_equals_set_to_b58(int_value, "30", "U")
    if_value_equals_set_to_b58(int_value, "31", "V")
    if_value_equals_set_to_b58(int_value, "32", "W")
    if_value_equals_set_to_b58(int_value, "33", "X")
    if_value_equals_set_to_b58(int_value, "34", "Y")
    if_value_equals_set_to_b58(int_value, "35", "Z")
    if_value_equals_set_to_b58(int_value, "36", "a")
    if_value_equals_set_to_b58(int_value, "37", "b")
    if_value_equals_set_to_b58(int_value, "38", "c")
    if_value_equals_set_to_b58(int_value, "39", "d")
    if_value_equals_set_to_b58(int_value, "40", "e")
    if_value_equals_set_to_b58(int_value, "41", "f")
    if_value_equals_set_to_b58(int_value, "42", "g")
    if_value_equals_set_to_b58(int_value, "43", "h")
    if_value_equals_set_to_b58(int_value, "44", "i")
    if_value_equals_set_to_b58(int_value, "45", "j")
    if_value_equals_set_to_b58(int_value, "46", "k")
    if_value_equals_set_to_b58(int_value, "47", "l")
    if_value_equals_set_to_b58(int_value, "48", "m")
    if_value_equals_set_to_b58(int_value, "49", "n")
    if_value_equals_set_to_b58(int_value, "50", "o")
    if_value_equals_set_to_b58(int_value, "51", "p")
    if_value_equals_set_to_b58(int_value, "52", "q")
    if_value_equals_set_to_b58(int_value, "53", "r")
    if_value_equals_set_to_b58(int_value, "54", "s")
    if_value_equals_set_to_b58(int_value, "55", "t")
    if_value_equals_set_to_b58(int_value, "56", "u")
    if_value_equals_set_to_b58(int_value, "57", "v")
    if_value_equals_set_to_b58(int_value, "58", "w")
    if_value_equals_set_to_b58(int_value, "59", "x")
    if_value_equals_set_to_b58(int_value, "60", "y")
    if_value_equals_set_to_b58(int_value, "61", "z")
def five_boolean_to_base_32_char(wb1: bool, wb2: bool, wb3: bool, wb: bool, wb5: bool, b1: bool, b2: bool, b3: bool, b4: bool, b5: bool, text: str):
    if wb1 == b1 and (wb2 == b2 and (wb3 == b3 and (wb == b4 and wb5 == b5))):
        list_digit_text.append(text)
def push_uart():
    global pin_digit_08, pin_digit_12, pin_digit_13, pin_digit_14, pin_digit_15, pin_digit_16, string_builder
    while len(list_analog_char) > 0:
        list_analog_char.shift()
    while len(list_digit_text) > 0:
        list_digit_text.shift()
    basic.pause(500)
    parse_int_1023_to_b62(pins.analog_read_pin(AnalogPin.P0))
    parse_int_1023_to_b62(pins.analog_read_pin(AnalogReadWritePin.P1))
    parse_int_1023_to_b62(pins.analog_read_pin(AnalogReadWritePin.P2))
    pin_digit_08 = pins.digital_read_pin(DigitalPin.P8) == 1
    pin_digit_12 = pins.digital_read_pin(DigitalPin.P12) == 1
    pin_digit_13 = pins.digital_read_pin(DigitalPin.P13) == 1
    pin_digit_14 = pins.digital_read_pin(DigitalPin.P14) == 1
    pin_digit_15 = pins.digital_read_pin(DigitalPin.P15) == 1
    pin_digit_16 = pins.digital_read_pin(DigitalPin.P16) == 1
    five_boolean_to_base32(input.button_is_pressed(Button.A),
        input.button_is_pressed(Button.B),
        input.logo_is_pressed(),
        False,
        False)
    five_boolean_to_base32(pin_digit_08,
        pin_digit_12,
        pin_digit_13,
        pin_digit_14,
        pin_digit_15)
    five_boolean_to_base32(pin_digit_16,
        input.sound_level() > 100,
        input.light_level() > 120,
        input.is_gesture(Gesture.LOGO_UP),
        input.is_gesture(Gesture.LOGO_DOWN))
    five_boolean_to_base32(input.is_gesture(Gesture.SCREEN_UP),
        input.is_gesture(Gesture.SCREEN_DOWN),
        input.is_gesture(Gesture.TILT_LEFT),
        input.is_gesture(Gesture.TILT_RIGHT),
        False)
    five_boolean_to_base32(input.is_gesture(Gesture.THREE_G),
        input.is_gesture(Gesture.SIX_G),
        input.is_gesture(Gesture.EIGHT_G),
        input.is_gesture(Gesture.FREE_FALL),
        input.is_gesture(Gesture.SHAKE))
    parse_int_360_to_b62(input.compass_heading())
    parse_int_1023_to_b62(input.acceleration(Dimension.X))
    parse_int_1023_to_b62(input.acceleration(Dimension.Y))
    parse_int_1023_to_b62(input.acceleration(Dimension.Z))
    parse_int_1023_to_b62(input.acceleration(Dimension.STRENGTH))
    parse_int_255_to_b62(input.sound_level())
    parse_int_255_to_b62(input.light_level())
    int_to_b62_char("" + str(Math.round(input.temperature())))
    basic.pause(500)
    string_builder = ""
    for value2 in list_analog_char:
        string_builder = "" + string_builder + value2
    bluetooth.uart_write_line("A|" + string_builder)
    string_builder = ""
    for value3 in list_digit_text:
        string_builder = "" + string_builder + value3
    bluetooth.uart_write_line("B|" + string_builder)
    bluetooth.uart_write_line("?" + str(pins.digital_read_pin(DigitalPin.P12)))
    basic.pause(500)
string_builder = ""
pin_digit_16 = False
pin_digit_15 = False
pin_digit_14 = False
pin_digit_13 = False
pin_digit_12 = False
pin_digit_08 = False
received_ble = ""
bluetooth_connected = 0
list_digit_text: List[str] = []
list_analog_char: List[str] = []
bluetooth.set_transmit_power(7)
basic.show_leds("""
    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    """)
list_analog_char = []
list_digit_text = []

def on_forever():
    basic.pause(500)
    if bluetooth_connected == 1:
        push_uart()
basic.forever(on_forever)
