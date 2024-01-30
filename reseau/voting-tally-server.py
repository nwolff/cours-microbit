"""
Radio monitoring dashboard

Each radio client is represented by a dot on the screen.
Once a client is registered, it will stay at the same pixel location
forever.

 Radio clients can simply send a number(between 0..255) on group 4.
They must transmit the serial number using``radio.setTransmitSerialNumber(true)``

The received number is used to set the LED brightness for that client.

If the radio packet is not received for 10sec, the LED starts blinking.

"""

dead_ping = 20000
lost_ping = 10000


class Client:
    def __init__(self, id, sprite, ping):
        self.id = id
        self.sprite = sprite
        self.ping = ping

clients = [];

# lazy allocate sprite
def getClient(id):
    # needs an id to track radio client's identity
    if not id:
        return None;

    # look for cached clients
    for client in clients:
        if client.id == id:
            return client
    n = clients.length
    if n == 24: # out of pixels
        return None
    client = Client(id=id,
                    sprite = game.createSprite(n % 5, n / 5),
                    ping = input.runningTime()
    }
    clients.append(client)
    return client

# store data received by clients
def on_received_number(n):
    serial_number = radio.receivedPacket(RadioPacketProperty.SerialNumber)
    client = getClient(serial_number)
    if client is None:
        return

    client.ping = input.runningTime()
    client.sprite.setBrightness(Math.max(1, n & 0xff))

radio.onReceivedNumber(on_received_number)


# monitor the sprites and start blinking when no packet is received
def on_forever():
    now = input.runningTime()
    for client in clients:
        last_ping = now - client.ping
        // lost signal starts blinking
        if last_ping > dead_ping:
            client.sprite.setBlink(0)
            client.sprite.setBrightness(0)
        elif last_ping > lost_ping:
            client.sprite.setBlink(500)
        else:
            client.sprite.setBlink(0)
    basic.pause(200)

basic.forever(on_forever)

# setup the radio and start!
radio.setGroup(4)
