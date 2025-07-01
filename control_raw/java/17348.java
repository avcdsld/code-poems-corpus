public SDVariable write(SDVariable flow, int index, SDVariable value){
        return write(flow, intToVar(index), value);
    }