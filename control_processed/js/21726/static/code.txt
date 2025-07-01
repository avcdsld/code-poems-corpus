function (capacity, lowWater) {
            if (!capacity || capacity < 1) {
                throw new ArgumentError(Logger.logMessage(Logger.LEVEL_SEVERE, "MemoryCache", "constructor",
                    "The specified capacity is undefined, zero or negative"));
            }

            if (!lowWater || lowWater >= capacity || lowWater < 0) {
                throw new ArgumentError(Logger.logMessage(Logger.LEVEL_SEVERE, "MemoryCache", "constructor",
                    "The specified low-water value is undefined, greater than or equal to the capacity, or less than 1"));
            }

            // Documented with its property accessor below.
            this._capacity = capacity;

            // Documented with its property accessor below.
            this._lowWater = lowWater;

            /**
             * The size currently used by this cache.
             * @type {Number}
             * @readonly
             */
            this.usedCapacity = 0;

            /**
             * The size currently unused by this cache.
             * @type {Number}
             * @readonly
             */
            this.freeCapacity = capacity;

            // Private. The cache entries.
            this.entries = {};

            // Private. The cache listeners.
            this.listeners = [];
        }