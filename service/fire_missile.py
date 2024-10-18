

class FireMissile:
    def fired_missile(self, battlefield, player_id):
        if player_id == 1:
            return PlayerOneFireMissile().fired_missile(battlefield)
        elif player_id == 2:
            return PlayerTwoFireMissile().fired_missile(battlefield)
        else:
            raise ValueError("Invalid player id")

class PlayerOneFireMissile(FireMissile):
    def fired_missile(self, battlefield):
        from random import choice
        x = choice(range(0, battlefield.size))
        y = choice(range(battlefield.size//2, battlefield.size))
        return x, y

class PlayerTwoFireMissile(FireMissile):
    def fired_missile(self, battlefield):
        from random import choice
        x = choice(range(0, battlefield.size))
        y = choice(range(0, battlefield.size//2))
        return x, y

