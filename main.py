def on_logo_touched():
    global Target
    #Target = input.compass_heading()
    music.play_tone(444, music.beat(BeatFraction.QUARTER))
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_pressed_a():
    global Target, Menu
    if Menu == "START":
        Target = Target - 5
    else:
        Menu = "START"
        basic.show_icon(IconNames.HOUSE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_long_pressed():
    music.play_tone(222, music.beat(BeatFraction.QUARTER))
    input.calibrate_compass()
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_ab():
    global Menu
    Menu = "STOP"
    music.play_tone(444, music.beat(BeatFraction.HALF))
    basic.show_icon(IconNames.SKULL)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Target, Menu
    if Menu == "START":
        Target = Target + 5
    else:
        Menu = "START"
        basic.show_icon(IconNames.HOUSE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def CalcDelta(fTarget: number):
    global fDelta
    if input.compass_heading() - fTarget > 180:
        fDelta = input.compass_heading() - 360 - fTarget
    else:
        fDelta = input.compass_heading() - fTarget
    return fDelta
MoyDelta = 0
index = 0
SommeDelta = 0
Delta = 0
Target = 0
fDelta = 0
Menu = ""
Menu = "STOP"
NbIndex = 4
fDelta = 0
servos.P0.set_angle(90)
EchantDelta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
basic.show_icon(IconNames.SKULL)

def on_every_interval():
    global Target, Delta
    if Menu == "STOP":
        Target = input.compass_heading()
    # basic.show_number(Target)
    Delta = CalcDelta(Target)
    EchantDelta.unshift(Delta)
loops.every_interval(500, on_every_interval)

def on_every_interval2():
    global SommeDelta, index, MoyDelta
    if Menu == "START":
        SommeDelta = 0
        index = 0
        while index <= NbIndex - 1:
            SommeDelta += EchantDelta[index]
            index += 1
        MoyDelta = Math.round(SommeDelta / NbIndex)
        basic.show_string("" + str((MoyDelta)))
        servos.P0.set_angle(90 + MoyDelta)
loops.every_interval(3000, on_every_interval2)
