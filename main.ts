bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Heart)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.Square)
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MICROBIT_EVT_ANY, function () {
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.digitalWritePin(DigitalPin.P15, 0)
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_1_DOWN) {
        pins.digitalWritePin(DigitalPin.P11, 1)
        pins.analogWritePin(AnalogPin.P8, Mspeed)
        pins.digitalWritePin(DigitalPin.P9, 0)
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.analogWritePin(AnalogPin.P15, Mspeed)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_2_DOWN) {
        pins.digitalWritePin(DigitalPin.P11, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.analogWritePin(AnalogPin.P9, Mspeed)
        pins.analogWritePin(AnalogPin.P12, Mspeed)
        pins.digitalWritePin(DigitalPin.P15, 0)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_3_DOWN) {
        pins.digitalWritePin(DigitalPin.P11, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.analogWritePin(AnalogPin.P9, Mspeed)
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.analogWritePin(AnalogPin.P15, Mspeed)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_4_DOWN) {
        pins.digitalWritePin(DigitalPin.P11, 0)
        pins.analogWritePin(AnalogPin.P8, Mspeed)
        pins.digitalWritePin(DigitalPin.P9, 0)
        pins.analogWritePin(AnalogPin.P12, Mspeed)
        pins.digitalWritePin(DigitalPin.P15, 0)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_DOWN) {
        Mspeed += -200
        if (Mspeed <= 0) {
            Mspeed = 0
        }
        basic.showString("" + Mspeed)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_DOWN) {
        Mspeed += 200
        if (Mspeed >= 1023) {
            Mspeed = 1023
        }
        basic.showString("" + Mspeed)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_DOWN) {
        basic.showString("C")
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_DOWN) {
        basic.showString("D")
    }
})
let Mspeed = 0
pins.digitalWritePin(DigitalPin.P8, 0)
pins.digitalWritePin(DigitalPin.P9, 0)
pins.digitalWritePin(DigitalPin.P12, 0)
pins.digitalWritePin(DigitalPin.P15, 0)
Mspeed = 150
