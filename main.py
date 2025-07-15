def on_bluetooth_connected():
    basic.show_icon(IconNames.HEART)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SQUARE)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_mes_dpad_controller_id_microbit_evt():
    global Mspeed
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.digital_write_pin(DigitalPin.P15, 0)
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_DOWN:
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.analog_write_pin(AnalogPin.P5, Mspeed)
        pins.digital_write_pin(DigitalPin.P9, 0)
        pins.digital_write_pin(DigitalPin.P11, 0)
        pins.analog_write_pin(AnalogPin.P15, Mspeed)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_DOWN:
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.digital_write_pin(DigitalPin.P5, 0)
        pins.analog_write_pin(AnalogPin.P9, Mspeed)
        pins.analog_write_pin(AnalogPin.P11, Mspeed)
        pins.digital_write_pin(DigitalPin.P15, 0)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_DOWN:
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.digital_write_pin(DigitalPin.P5, 0)
        pins.analog_write_pin(AnalogPin.P9, 423)
        pins.digital_write_pin(DigitalPin.P11, 0)
        pins.analog_write_pin(AnalogPin.P15, 423)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_DOWN:
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P12, 1)
        pins.analog_write_pin(AnalogPin.P5, 423)
        pins.digital_write_pin(DigitalPin.P9, 0)
        pins.analog_write_pin(AnalogPin.P11, 423)
        pins.digital_write_pin(DigitalPin.P15, 0)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_DOWN:
        Mspeed += -200
        if Mspeed <= 0:
            Mspeed = 0
        basic.show_string("" + str(Mspeed))
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_DOWN:
        Mspeed += 200
        if Mspeed >= 1023:
            Mspeed = 1023
        basic.show_string("" + str(Mspeed))
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_DOWN:
        basic.show_string("C")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_DOWN:
        basic.show_string("D")
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

Mspeed = 0
pins.digital_write_pin(DigitalPin.P5, 0)
pins.digital_write_pin(DigitalPin.P9, 0)
pins.digital_write_pin(DigitalPin.P11, 0)
pins.digital_write_pin(DigitalPin.P15, 0)
Mspeed = 423