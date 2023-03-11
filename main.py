def on_button_pressed_a():
    global Target, Menu
    if Menu == "START":
        Target = Target + 5
    else:
        Menu = "START"
        Target = input.compass_heading()
        basic.show_icon(IconNames.HOUSE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Menu
    Menu = "STOP"
    basic.show_icon(IconNames.SKULL)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Target, Menu
    if Menu == "START":
        Target = Target - 5
    else:
        Menu = "START"
        Target = input.compass_heading()
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
Menu = ""
Target = 0
fDelta = 0
Menu = "STOP"
NbIndex = 6
fDelta = 999
Target = 999
Delta = 999
servos.P0.set_angle(90)
EchantDelta = [0, 0, 0, 0, 0, 0]
TabOK = 1
basic.show_icon(IconNames.SKULL)

def on_every_interval():
    global Delta, Menu
    if Menu == "START":
        # basic.show_number(Target)
        Delta = CalcDelta(Target)
        EchantDelta.unshift(Delta)
loops.every_interval(200, on_every_interval)

def on_every_interval2():
    global SommeDelta, index, MoyDelta, Menu
    if Menu == "START":
        # Delta = CalcDelta(Target)
        basic.show_number(Delta)
        SommeDelta = 0
        index = 0
        while index <= NbIndex - 1:
            SommeDelta += EchantDelta[index]
            index += 1
        MoyDelta = Math.round(SommeDelta / NbIndex)
        basic.show_string("" + str(MoyDelta))
        servos.P0.set_angle(90 + MoyDelta)
loops.every_interval(5000, on_every_interval2)
