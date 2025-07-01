function (index) {
                if (index == null) {
                    index = -1;
                }
                return {
                    visited: false,
                    forPole: false,
                    index: index,
                    linkTo: -1
                }
            }