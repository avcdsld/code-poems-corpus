private static List<String> loadInstantRunDexFile(ApplicationInfo appInfo) {
        List<String> instantRunDexPaths = new ArrayList<>();

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP && appInfo.splitSourceDirs != null) {
            instantRunDexPaths.addAll(Arrays.asList(appInfo.splitSourceDirs));
            Log.i(AndServer.TAG, "InstantRun support was found.");
        } else {
            try {
                // Reflect instant run sdk to find where is the dex file.
                Class pathsByInstantRun = Class.forName("com.android.tools.fd.runtime.Paths");
                Method getDexFileDirectory = pathsByInstantRun.getMethod("getDexFileDirectory", String.class);
                String dexDirectory = (String)getDexFileDirectory.invoke(null, appInfo.packageName);

                File dexFolder = new File(dexDirectory);
                if (dexFolder.exists() && dexFolder.isDirectory()) {
                    File[] dexFiles = dexFolder.listFiles();
                    for (File file : dexFiles) {
                        if (file.exists() && file.isFile() && file.getName().endsWith(".dex")) {
                            instantRunDexPaths.add(file.getAbsolutePath());
                        }
                    }
                    Log.i(AndServer.TAG, "InstantRun support was found.");
                }

            } catch (ClassNotFoundException e) {
                Log.i(AndServer.TAG, "InstantRun support was not found.");
            } catch (Exception e) {
                Log.w(AndServer.TAG, "Finding InstantRun failed.", e);
            }
        }

        return instantRunDexPaths;
    }