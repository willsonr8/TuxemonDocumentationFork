# SPDX-License-Identifier: GPL-3.0
# Copyright (c) 2014-2023 William Edwards <shadowapex@gmail.com>, Benjamin Bean <superman2k5@gmail.com>
from __future__ import annotations

from tuxemon.event import MapCondition
from tuxemon.event.eventcondition import EventCondition
from tuxemon.session import Session


class VariableSetCondition(EventCondition):
    """
    Check to see if a player game variable exists and has a particular value.

    If the variable does not exist it will return ``False``.

    Script usage:
        .. code-block::

            is variable_set <variable>[:value]

    Script parameters:
        variable: The variable to check.
        value: Optional value to check for.

    """

    name = "variable_set"

    def test(self, session: Session, condition: MapCondition) -> bool:
        """
        Check to see if a player game variable has a particular value.

        Parameters:
            session: The session object
            condition: The map condition object.

        Returns:
            Whether the variable exists and has that value.

        """
        player = session.player
        parameters = condition.parameters
        for param in parameters:
            var = param.split(":")
            key = var[0]
            if len(var) > 1:
                value = var[1]
            else:
                value = None

            exists = key in player.game_variables

            if value is None:
                return exists
            else:
                return exists and player.game_variables[key] == value
        return False
