

class Battlefield:
    def __init__(self, ships, missiles=None, size=10):
        self.ships = ships
        self.missiles = missiles
        self.size = size

    def check_missile_target(self, player, target, x, y):
        for ship in target.ships:
            if not ship.destroyed:
                console_log = f"Player{player.player_id}’s turn: Missile fired at ({x}, {y}). "
                if ship.x1 <= x <= ship.x2 and ship.y1 <= y <= ship.y2:
                    ship.destroyed = True
                    target.active_ships -= 1
                    console_log += f"Hit. Player{target.player_id}’s ship with id “{ship.id}” destroyed."
                else:
                    console_log += "Miss"
                print(console_log)

