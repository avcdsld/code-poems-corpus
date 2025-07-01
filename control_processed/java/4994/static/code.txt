public static Tuple newInstance(int arity) {
		switch (arity) {
			case 0: return Tuple0.INSTANCE;
			case 1: return new Tuple1();
			case 2: return new Tuple2();
			case 3: return new Tuple3();
			case 4: return new Tuple4();
			case 5: return new Tuple5();
			case 6: return new Tuple6();
			case 7: return new Tuple7();
			case 8: return new Tuple8();
			case 9: return new Tuple9();
			case 10: return new Tuple10();
			case 11: return new Tuple11();
			case 12: return new Tuple12();
			case 13: return new Tuple13();
			case 14: return new Tuple14();
			case 15: return new Tuple15();
			case 16: return new Tuple16();
			case 17: return new Tuple17();
			case 18: return new Tuple18();
			case 19: return new Tuple19();
			case 20: return new Tuple20();
			case 21: return new Tuple21();
			case 22: return new Tuple22();
			case 23: return new Tuple23();
			case 24: return new Tuple24();
			case 25: return new Tuple25();
			default: throw new IllegalArgumentException("The tuple arity must be in [0, " + MAX_ARITY + "].");
		}
	}