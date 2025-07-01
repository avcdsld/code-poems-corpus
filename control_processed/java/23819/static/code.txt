public static int getCpuCores() {
        // 找不到文件或者异常，则去物理机的核心数
        int cpu = RpcConfigs.getIntValue(RpcOptions.SYSTEM_CPU_CORES);
        return cpu > 0 ? cpu : Runtime.getRuntime().availableProcessors();
    }