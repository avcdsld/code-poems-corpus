function(t) {

            if (t <= 0) return this.start.clone();
            if (t >= 1) return this.end.clone();

            return this.getSkeletonPoints(t).divider;
        }