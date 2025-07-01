function checkError(e) {
    if(e.errno && networkErrors.includes(e.errno)) {
        console.log("we have to reconnect");

        // close port
        client.close();

        // re open client
        client = new ModbusRTU();
        timeoutConnectRef = setTimeout(connect, 1000);
    }
}