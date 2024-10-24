from app.Knight.unit import KnightsFighting


def battle(knight1: "KnightsFighting", knight2: "KnightsFighting") -> dict:
    l1, l2 = [], []
    while knight1.hp > 0 and knight2.hp > 0:
        damage_to_knight2 = max(knight1.attack() - knight2.protection, 0)
        knight2.hp -= damage_to_knight2
        l1.append(f"{damage_to_knight2}")
        if knight2.hp <= 0:
            knight2.hp = max(0, knight2.hp)
            break
        damage_to_knight1 = max(knight2.attack() - knight1.protection, 0)
        knight1.hp -= damage_to_knight1
        l2.append(f"{damage_to_knight1}")
        if knight1.hp <= 0:
            knight1.hp = max(0, knight1.hp)
            break
    return {
        "result": {
            f"{knight1.name}: {knight1.hp} hp, "
            f"{knight2.name}: {knight2.hp} hp"
        },
        "crit_hits": {
            knight1.name: knight1.critical_hits,
            knight2.name: knight2.critical_hits,
        },
        "miss": {
            knight1.name: knight1.hits_miss,
            knight2.name: knight2.hits_miss,
        },
        ">>>WINNER<<<": (
            knight1.name if knight2.hp < knight1.hp else knight2.name
        ),
        "HIT_map": {f"{knight1.name}: {l1}, {knight2.name}: {l2}"},
    }

