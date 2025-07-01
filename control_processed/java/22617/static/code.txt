public static boolean create(File dest, final boolean isFile, final int retryTimes) {
        if (dest == null) {
            return false;
        }

        int totalRetry = retryTimes;

        if (retryTimes < 0) {
            totalRetry = 1;
        }

        int retry = 0;
        while (retry++ < totalRetry) {
            try {
                if (true == isFile) {
                    if ((true == dest.exists()) || (true == dest.createNewFile())) {
                        return true;
                    }
                } else {
                    FileUtils.forceMkdir(dest);
                    return true;
                }
            } catch (Exception ex) {
                // 本次等待时间
                int wait = (int) Math.pow(retry, retry) * timeWait;
                wait = (wait < timeWait) ? timeWait : wait;

                // 尝试等待
                if (retry == totalRetry) {
                    return false;
                } else {

                    // 记录日志
                    logger.warn(String.format("[%s] create() - retry %s failed : wait [%s] ms , caused by %s",
                                              dest.getAbsolutePath(), retry, wait, ex.getMessage()));
                    try {
                        Thread.sleep(wait);
                    } catch (InterruptedException e) {
                        return false;
                    }
                }
            }
        }

        return false;
    }