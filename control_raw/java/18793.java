public int compareTo(Object o) {
        float thisValue = this.value;
        float thatValue = ((FloatWritable) o).value;
        return (thisValue < thatValue ? -1 : (thisValue == thatValue ? 0 : 1));
    }