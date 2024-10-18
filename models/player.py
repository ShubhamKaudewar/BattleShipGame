

class Player:
    def __init__(self, player_id, ships, active_ships=0):
        self.player_id = player_id
        self.ships = ships
        self.active_ships = active_ships

    def is_looser(self):
        if self.active_ships == 0:
            return True
        return False
