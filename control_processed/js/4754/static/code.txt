function (delta) {
            edits.push.apply(edits, delta.edits);
            moves.push.apply(moves, delta.moves);
            queue.push.apply(queue, delta.newElements);
        }