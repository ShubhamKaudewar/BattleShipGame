from models.ship import Ship
from models.player import Player
from models.battlefield import Battlefield
from service.battle_ship_game import BattleShipGame

def init_game():
    # battlefield_size = 10
    # fleet_count = 5

    battlefield_size = int(input("Provide NxN size of grid:"))
    fleet_count = int(input("Provide fleet count:"))
    total_ships = {}
    players = {}
    for player_id in range(1, 3):
        print("Provide fleet details for player:", player_id)
        ships = []
        for fleet in range(fleet_count):
            fleet_details = input("Provide details of ship SH1 0 0 4:").split(" ")
            ship_id = fleet_details[0].upper()
            ship = Ship(*fleet_details)
            total_ships[ship_id] = ship
            ships.append(ship)
        players[player_id] = Player(player_id, ships, active_ships=fleet_count)

    battlefield = Battlefield(ships=total_ships,
                size=battlefield_size)
    BattleShipGame(players, battlefield).start_game()


def main():
    init_game()



if __name__ == "__main__":
    main()