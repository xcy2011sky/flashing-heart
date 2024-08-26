def on_button_pressed_a():
    basic.show_string("" + str((len("您好"))))
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_number(0)
    basic.show_arrow(ArrowNames.NORTH)
    basic.clear_screen()
    images.icon_image(IconNames.HEART).show_image(1, 400)
    basic.show_number(9)
    images.icon_image(IconNames.YES).scroll_image(2, 200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_leds("""
        . # . # .
        . . # . .
        . . # . .
        # . . . #
        . . # . .
        """)
basic.forever(on_forever)
