input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (Menu == "START") {
        Target = Target + 5
    } else {
        Menu = "START"
        Target = input.compassHeading()
        basic.showIcon(IconNames.House)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (Menu == "START") {
        Target = Target - 5
    } else {
        Menu = "START"
        Target = input.compassHeading()
        basic.showIcon(IconNames.House)
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Menu = "STOP"
    basic.showIcon(IconNames.Skull)
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
let Target = 0
let fDelta = 0
let Menu = ""
Menu = "STOP"
let NbIndex = 6
fDelta = 999
Target = 999
let Delta = 999
servos.P0.setAngle(90)
let EchantDelta = [0, 0, 0, 0, 0, 0]
basic.showIcon(IconNames.Skull)
loops.everyInterval(200, function on_every_interval() {
    
    if (Menu == "START") {
        //  basic.show_number(Target)
        Delta = CalcDelta(Target)
        EchantDelta.unshift(Delta)
    }
    
})
loops.everyInterval(5000, function on_every_interval2() {
    
    if (Menu == "START") {
        //  Delta = CalcDelta(Target)
        basic.showNumber(Delta)
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
