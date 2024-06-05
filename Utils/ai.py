"""AI Module
"""

# pylint: skip-file
from __future__ import annotations
from typing import TYPE_CHECKING
from Utils.logger import Logger

if TYPE_CHECKING:
    from Entities import Entity


class AI:
    """
    Utility Class AI Decisions
    """

    def calcbehaviour(_entity: Entity) -> int:
        """Function to calculate AI Behaviour

        Args:
            _entity (entity): Entity for which the calculation should happen

        Returns:
            0 - Flee
            1 - Attack
            2 - Buff
            9 - Entity is Player so we skip
        """

        difficulty = 1  # TODO: Load from Config

        if _entity.isPlayer:
            return 9

        _ai = _entity.ai
        _health = _entity.hp
        _maxhealth = _entity.maxHealth
        Logger.log(f"Entity: {_entity}({_entity.name}) Health: {_health} | AI: {_ai}")

        if difficulty == 1:
            if _health < _maxhealth * 0.2:
                Logger.log(f"Low Health for Entity: {_entity}({_entity.name})")
                return 0
            elif _health < _maxhealth * 0.4:
                Logger.log(f"Entity: {_entity}({_entity.name}) want's to heal")
                return 2
            elif _health > _maxhealth * 0.4:
                Logger.log(f"Entity: {_entity}({_entity.name}) want's to attack")
                return 1
        return 0
