function NatsError(message, code, chainedError) {
    Error.captureStackTrace(this, this.constructor);
    this.name = this.constructor.name;
    this.message = message;
    this.code = code;
    this.chainedError = chainedError;
}