from service.fire_missile import FireMissile

class Missile:
    def __init__(self, battlefield, player_id):
        self.player_id = player_id
        self.battlefield = battlefield

    def launch_missile(self):
        return FireMissile().fired_missile(self.battlefield, self.player_id)