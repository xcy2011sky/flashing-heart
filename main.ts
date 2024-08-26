input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("" + ("" + "您好".length))
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    basic.showNumber(0)
    basic.showArrow(ArrowNames.North)
    basic.clearScreen()
    images.iconImage(IconNames.Heart).showImage(1, 400)
    basic.showNumber(9)
    images.iconImage(IconNames.Yes).scrollImage(2, 200)
})
basic.forever(function on_forever() {
    basic.showLeds(`
        . # . # .
        . . # . .
        . . # . .
        # . . . #
        . . # . .
        `)
})
