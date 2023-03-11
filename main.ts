input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    
    // Target = input.compass_heading()
    music.playTone(444, music.beat(BeatFraction.Quarter))
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (Menu == "START") {
        Target = Target - 5
    } else {
        Menu = "START"
        basic.showIcon(IconNames.House)
    }
    
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    music.playTone(222, music.beat(BeatFraction.Quarter))
    input.calibrateCompass()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Menu = "STOP"
    music.playTone(444, music.beat(BeatFraction.Half))
    basic.showIcon(IconNames.Skull)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (Menu == "START") {
        Target = Target + 5
    } else {
        Menu = "START"
        basic.showIcon(IconNames.House)
    }
    
})
function CalcDelta(fTarget: number): number {
    
    if (input.compassHeading() - fTarget > 180) {
        fDelta = input.compassHeading() - 360 - fTarget
    } else {
        fDelta = input.compassHeading() - fTarget
    }
    
    return fDelta
}

let MoyDelta = 0
let index = 0
let SommeDelta = 0
let Delta = 0
let Target = 0
let fDelta = 0
let Menu = ""
Menu = "STOP"
let NbIndex = 4
fDelta = 0
servos.P0.setAngle(90)
let EchantDelta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
basic.showIcon(IconNames.Skull)
loops.everyInterval(500, function on_every_interval() {
    
    if (Menu == "STOP") {
        Target = input.compassHeading()
    }
    
    //  basic.show_number(Target)
    Delta = CalcDelta(Target)
    EchantDelta.unshift(Delta)
})
loops.everyInterval(3000, function on_every_interval2() {
    
    if (Menu == "START") {
        SommeDelta = 0
        index = 0
        while (index <= NbIndex - 1) {
            SommeDelta += EchantDelta[index]
            index += 1
        }
        MoyDelta = Math.round(SommeDelta / NbIndex)
        basic.showString("" + ("" + MoyDelta))
        servos.P0.setAngle(90 + MoyDelta)
    }
    
})
