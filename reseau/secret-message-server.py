groupe = 40 + 2 * randint(0, 100)
radio.set_group(groupe)
sprite = images.icon_image(IconNames.RABBIT)


def on_forever():
    radio.send_string("Red1")
    sprite.scroll_image(1, 200)


basic.forever(on_forever)
