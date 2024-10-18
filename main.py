from models.ship import Ship
from models.player import Player
from models.battlefield import Battlefield
from service.battle_ship_game import BattleShipGame


def init_game(battlefield_size, fleet_count, fleet_details):
    total_ships = {}
    players = {}
    for player_id in range(1, 3):
        ships = []
        for fleet in fleet_details[player_id - 1]:
            ship_id = fleet[0].upper()
            ship = Ship(*fleet)
            total_ships[ship_id] = ship
            ships.append(ship)
        players[player_id] = Player(player_id, ships, active_ships=fleet_count)

    battlefield = Battlefield(ships=total_ships, size=battlefield_size)
    BattleShipGame(players, battlefield).start_game()


def main():
    battlefield_size = int(input("Provide NxN size of grid:"))
    fleet_count = int(input("Provide fleet count:"))

    fleet_details = []
    for player_id in range(1, 3):
        print("Provide fleet details for player:", player_id)
        player_fleet = []
        for fleet in range(fleet_count):
            fleet_detail = input(f"Provide details of ship SH1 0 0 4 for player {player_id}:").split(" ")
            player_fleet.append(fleet_detail)
        fleet_details.append(player_fleet)

    init_game(battlefield_size, fleet_count, fleet_details)


if __name__ == "__main__":
    main()
