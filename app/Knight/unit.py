import random


class KnightsFighting:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: dict,
            weapon: dict,
            potion: dict,
    ) -> None:
        self.name = name
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.power = power
        self.protection = 0
        self.hp = hp
        self.critical_hits = 0
        self.accuracy = random.randint(60, 90) / 100
        self.hits_miss = 0
        self.initial_hp = hp

    def apply_equipment(self) -> None:
        self.power += self.weapon["power"]
        if self.potion is not None:
            self.power += int(self.potion["effect"].get("power", 0))
            self.protection += int(self.potion["effect"].get("protection", 0))
            self.hp += int(self.potion["effect"].get("hp", 0))
        if any("protection" in arm for arm in self.armour):
            self.protection += sum(arm["protection"] for arm in self.armour)

    def attack(self) -> int:
        if random.random() < self.accuracy:
            chance = random.randint(20, 40)
            is_critical = random.random() < (chance / 100)
            damage = self.power
            if is_critical:
                self.critical_hits += 1
                return max(0, damage * 2)
            else:
                return max(0, self.power)
        self.hits_miss += 1
        return 0

    def reset(self) -> any:
        self.hp = self.initial_hp
        self.critical_hits = 0
        self.hits_miss = 0

    def setup_knight(self) -> any:
        knight = KnightsFighting(
            name = self["name"],
            power = self["power"],
            hp = self["hp"],
            armour = self["armour"],
            weapon = self["weapon"],
            potion = self["potion"],
        )
        return knight
