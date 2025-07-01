function(dpad, multiBehavior) {
        var d, dir;
        var winner;

        for (d in dpad.directions) {
            dir = dpad.directions[d];
            dir.active = false;

            if (dir.input.isActive()) {
                if (multiBehavior === "all") {
                    dir.active = true;
                } else {
                    if (!winner) {
                        winner = dir;
                    } else {
                        if (multiBehavior === "first") {
                            if (winner.input.timeDown > dir.input.timeDown) {
                                winner = dir;
                            }
                        }
                        if (multiBehavior === "last") {
                            if (winner.input.timeDown < dir.input.timeDown) {
                                winner = dir;
                            }
                        }
                    }
                }
            }
        }
        // If we picked a winner, set it active
        if (winner) winner.active = true;
    }