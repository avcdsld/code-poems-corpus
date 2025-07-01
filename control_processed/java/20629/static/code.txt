public void enableUserDefinedRPC() {
        int enabledRpc = scannerParam.getTargetParamsEnabledRPC();
        enabledRpc |= ScannerParam.RPC_USERDEF;
        scannerParam.setTargetParamsEnabledRPC(enabledRpc);
    }