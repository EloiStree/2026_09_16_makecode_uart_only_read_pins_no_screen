/**
 * WARNING
 * 
 * THEY ARE NO PULL UP IN THE DIGIT PIN
 * 
 * EXCEPT ON TH 5 11 THAT ARE BUTTON AB
 */
function parse_int_360_to_b62 (num: number) {
    int_to_b62_char("" + Math.round(Math.map(num, 0, 360, 0, 61)))
}
function push_uart_digital () {
    while (list_digit_text.length > 0) {
        list_digit_text.shift()
    }
    pin_digit_08 = pins.digitalReadPin(DigitalPin.P8) == 1
    pin_digit_12 = pins.digitalReadPin(DigitalPin.P12) == 1
    pin_digit_13 = pins.digitalReadPin(DigitalPin.P13) == 1
    pin_digit_14 = pins.digitalReadPin(DigitalPin.P14) == 1
    pin_digit_15 = pins.digitalReadPin(DigitalPin.P15) == 1
    pin_digit_16 = pins.digitalReadPin(DigitalPin.P16) == 1
    pin_digit_06 = pins.digitalReadPin(DigitalPin.P6) == 1
    pin_digit_07 = pins.digitalReadPin(DigitalPin.P7) == 1
    pin_digit_09 = pins.digitalReadPin(DigitalPin.P9) == 1
    five_boolean_to_base32(input.buttonIsPressed(Button.A), input.buttonIsPressed(Button.B), input.logoIsPressed(), input.soundLevel() > 100, input.lightLevel() > 120)
    five_boolean_to_base32(input.isGesture(Gesture.ThreeG), input.isGesture(Gesture.SixG), input.isGesture(Gesture.EightG), input.isGesture(Gesture.LogoUp), input.isGesture(Gesture.LogoDown))
    five_boolean_to_base32(input.isGesture(Gesture.ScreenUp), input.isGesture(Gesture.ScreenDown), input.isGesture(Gesture.TiltLeft), input.isGesture(Gesture.TiltRight), input.isGesture(Gesture.Shake))
    five_boolean_to_base32(pin_digit_12, pin_digit_13, pin_digit_14, pin_digit_15, pin_digit_16)
    five_boolean_to_base32(pin_digit_06, pin_digit_07, pin_digit_08, pin_digit_09, input.isGesture(Gesture.FreeFall))
    string_builder = ""
    for (let value of list_digit_text) {
        string_builder = "" + string_builder + value
    }
    bluetooth.uartWriteLine("B_" + string_builder)
}
bluetooth.onBluetoothConnected(function () {
    bluetooth_connected = 1
})
bluetooth.onBluetoothDisconnected(function () {
    bluetooth_connected = 0
})
function parse_int_1023_to_b62 (num: number) {
    int_to_b62_char("" + Math.round(Math.map(num, 0, 1023, 0, 61)))
}
function five_boolean_to_base32 (bool: boolean, bool2: boolean, bool3: boolean, bool4: boolean, bool5: boolean) {
    five_boolean_to_base_32_char(false, false, false, false, false, bool, bool2, bool3, bool4, bool5, "0")
    five_boolean_to_base_32_char(false, false, false, false, true, bool, bool2, bool3, bool4, bool5, "1")
    five_boolean_to_base_32_char(false, false, false, true, false, bool, bool2, bool3, bool4, bool5, "2")
    five_boolean_to_base_32_char(false, false, false, true, true, bool, bool2, bool3, bool4, bool5, "3")
    five_boolean_to_base_32_char(false, false, true, false, false, bool, bool2, bool3, bool4, bool5, "4")
    five_boolean_to_base_32_char(false, false, true, false, true, bool, bool2, bool3, bool4, bool5, "5")
    five_boolean_to_base_32_char(false, false, true, true, false, bool, bool2, bool3, bool4, bool5, "6")
    five_boolean_to_base_32_char(false, false, true, true, true, bool, bool2, bool3, bool4, bool5, "7")
    five_boolean_to_base_32_char(false, true, false, false, false, bool, bool2, bool3, bool4, bool5, "8")
    five_boolean_to_base_32_char(false, true, false, false, true, bool, bool2, bool3, bool4, bool5, "9")
    five_boolean_to_base_32_char(false, true, false, true, false, bool, bool2, bool3, bool4, bool5, "A")
    five_boolean_to_base_32_char(false, true, false, true, true, bool, bool2, bool3, bool4, bool5, "B")
    five_boolean_to_base_32_char(false, true, true, false, false, bool, bool2, bool3, bool4, bool5, "C")
    five_boolean_to_base_32_char(false, true, true, false, true, bool, bool2, bool3, bool4, bool5, "D")
    five_boolean_to_base_32_char(false, true, true, true, false, bool, bool2, bool3, bool4, bool5, "E")
    five_boolean_to_base_32_char(false, true, true, true, true, bool, bool2, bool3, bool4, bool5, "F")
    five_boolean_to_base_32_char(true, false, false, false, false, bool, bool2, bool3, bool4, bool5, "G")
    five_boolean_to_base_32_char(true, false, false, false, true, bool, bool2, bool3, bool4, bool5, "H")
    five_boolean_to_base_32_char(true, false, false, true, false, bool, bool2, bool3, bool4, bool5, "I")
    five_boolean_to_base_32_char(true, false, false, true, true, bool, bool2, bool3, bool4, bool5, "J")
    five_boolean_to_base_32_char(true, false, true, false, false, bool, bool2, bool3, bool4, bool5, "K")
    five_boolean_to_base_32_char(true, false, true, false, true, bool, bool2, bool3, bool4, bool5, "L")
    five_boolean_to_base_32_char(true, false, true, true, false, bool, bool2, bool3, bool4, bool5, "M")
    five_boolean_to_base_32_char(true, false, true, true, true, bool, bool2, bool3, bool4, bool5, "N")
    five_boolean_to_base_32_char(true, true, false, false, false, bool, bool2, bool3, bool4, bool5, "O")
    five_boolean_to_base_32_char(true, true, false, false, true, bool, bool2, bool3, bool4, bool5, "P")
    five_boolean_to_base_32_char(true, true, false, true, false, bool, bool2, bool3, bool4, bool5, "Q")
    five_boolean_to_base_32_char(true, true, false, true, true, bool, bool2, bool3, bool4, bool5, "R")
    five_boolean_to_base_32_char(true, true, true, false, false, bool, bool2, bool3, bool4, bool5, "S")
    five_boolean_to_base_32_char(true, true, true, false, true, bool, bool2, bool3, bool4, bool5, "T")
    five_boolean_to_base_32_char(true, true, true, true, false, bool, bool2, bool3, bool4, bool5, "U")
    five_boolean_to_base_32_char(true, true, true, true, true, bool, bool2, bool3, bool4, bool5, "V")
}
function parse_int_255_to_b62 (num: number) {
    int_to_b62_char("" + Math.round(Math.map(num, 0, 255, 0, 61)))
}
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    received_ble = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    if (received_ble == "PING") {
        bluetooth.uartWriteLine("PONG")
    }
    if (received_ble == "?") {
        push_uart()
    }
    if (received_ble == "?5s") {
        time_between_push = 5000
    }
    if (received_ble == "?2s") {
        time_between_push = 2000
    }
    if (received_ble == "?1s") {
        time_between_push = 4000
    }
    if (received_ble == "?500ms") {
        time_between_push = 500
    }
    if (received_ble == "?200ms") {
        time_between_push = 200
    }
    if (received_ble == "?100ms") {
        time_between_push = 100
    }
})
function push_uart_analog () {
    while (list_analog_char.length > 0) {
        list_analog_char.shift()
    }
    parse_int_1023_to_b62(pins.analogReadPin(AnalogPin.P0))
    parse_int_1023_to_b62(pins.analogReadPin(AnalogReadWritePin.P1))
    parse_int_1023_to_b62(pins.analogReadPin(AnalogReadWritePin.P2))
    parse_int_1023_to_b62(pins.analogReadPin(AnalogReadWritePin.P3))
    parse_int_1023_to_b62(pins.analogReadPin(AnalogReadWritePin.P4))
    parse_int_1023_to_b62(pins.analogReadPin(AnalogReadWritePin.P10))
    parse_int_1023_to_b62(input.acceleration(Dimension.X))
    parse_int_1023_to_b62(input.acceleration(Dimension.Y))
    parse_int_1023_to_b62(input.acceleration(Dimension.Z))
    parse_int_1023_to_b62(input.acceleration(Dimension.Strength))
    parse_int_255_to_b62(input.soundLevel())
    parse_int_255_to_b62(input.lightLevel())
    parse_int_360_to_b62(input.compassHeading())
    int_to_b62_char("" + Math.round(input.temperature()))
    string_builder = ""
    for (let value of list_analog_char) {
        string_builder = "" + string_builder + value
    }
    bluetooth.uartWriteLine("A_" + string_builder)
}
function if_value_equals_set_to_b58 (value: string, is_equals: string, set_to: string) {
    if (value == is_equals) {
        list_analog_char.push(set_to)
    }
}
function int_to_b62_char (int_value: string) {
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
}
function five_boolean_to_base_32_char (wb1: boolean, wb2: boolean, wb3: boolean, wb: boolean, wb5: boolean, b1: boolean, b2: boolean, b3: boolean, b4: boolean, b5: boolean, text: string) {
    if (wb1 == b1 && (wb2 == b2 && (wb3 == b3 && (wb == b4 && wb5 == b5)))) {
        list_digit_text.push(text)
    }
}
function push_uart () {
    push_uart_digital()
    push_uart_analog()
}
let received_ble = ""
let bluetooth_connected = 0
let string_builder = ""
let pin_digit_09 = false
let pin_digit_07 = false
let pin_digit_06 = false
let pin_digit_16 = false
let pin_digit_15 = false
let pin_digit_14 = false
let pin_digit_13 = false
let pin_digit_12 = false
let pin_digit_08 = false
let list_digit_text: string[] = []
let list_analog_char: string[] = []
let time_between_push = 0
time_between_push = 200
basic.clearScreen()
led.setBrightness(0)
led.enable(false)
bluetooth.setTransmitPower(7)
list_analog_char = []
list_digit_text = []
basic.forever(function () {
    basic.pause(time_between_push)
    if (bluetooth_connected == 1) {
        push_uart()
    }
})
