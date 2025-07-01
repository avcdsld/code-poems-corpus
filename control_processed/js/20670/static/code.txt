function CallResponseCont(flags, csum, args) {
    this.type = CallResponseCont.TypeCode;
    this.flags = flags || 0;
    this.csum = Checksum.objOrType(csum);
    this.args = args || [];
    this.cont = null;
}