function oReady(o, callback) {
    !!o && (callback && callback()) || setTimeout(() => oReady(o, callback), 10)
}