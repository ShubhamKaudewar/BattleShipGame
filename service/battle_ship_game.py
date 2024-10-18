from models.missile import Missile

class BattleShipGame:
    def __init__(self, players, battlefield):
        self.players = players
        self.battlefield = battlefield

    def start_game(self):
        while True:
            for player_id in self.players:
                player = self.players[player_id]
                target = self.players[2] if player_id == 1 else self.players[1]
                target_x, target_y = Missile(self.battlefield, player_id).launch_missile()
                self.battlefield.check_missile_target(player, target, target_x, target_y)

                if target.is_looser():
                    print(f"Congratulation {player_id} you won the war!")
                    return None
