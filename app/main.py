from colorama import Fore, Style
from app.Knight_setup.config import KNIGHTS
from app.Knight.unit import KnightsFighting
from app.Knight.battle import battle


def main() -> any:
    knights = {
        "lancelot": KnightsFighting.setup_knight(KNIGHTS["lancelot"]),
        "arthur": KnightsFighting.setup_knight(KNIGHTS["arthur"]),
        "mordred": KnightsFighting.setup_knight(KNIGHTS["mordred"]),
        "red_knight": KnightsFighting.setup_knight(KNIGHTS["red_knight"]),
    }

    for knight in knights.values():
        knight.apply_equipment()

    results = {
        "lancelot vs mordred": battle(
            knights["lancelot"], knights["mordred"]
        ),
        "arthur vs red_knight": battle(
            knights["arthur"], knights["red_knight"]
        ),
    }
    for result in results.items():
        print(Fore.YELLOW + Style.BRIGHT + f"{result}\n")

    winners = []
    for match, result in results.items():
        winners.append(result[">>>WINNER<<<"])
        if len(winners) == 2:
            winner_knight1 = next(
                k for k in knights.values() if k.name == winners[0]
            )
            winner_knight2 = next(
                k for k in knights.values() if k.name == winners[1]
            )
            winner_knight2.reset(), winner_knight1.reset()
            final_battle = battle(winner_knight1, winner_knight2)
            print(
                Fore.YELLOW
                + Style.BRIGHT
                + f"final_battle: {final_battle}"
                + Style.RESET_ALL
            )


if __name__ == "__main__":
    main()
