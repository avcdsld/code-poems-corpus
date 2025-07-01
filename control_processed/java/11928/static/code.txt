public final synchronized RunT newBuild() throws IOException {
        try {
            RunT lastBuild = getBuildClass().getConstructor(asJob().getClass()).newInstance(asJob());
            builds.put(lastBuild);
            lastBuild.getPreviousBuild(); // JENKINS-20662: create connection to previous build
            return lastBuild;
        } catch (InvocationTargetException e) {
            LOGGER.log(Level.WARNING, String.format("A new build could not be created in job %s", asJob().getFullName()), e);
            throw handleInvocationTargetException(e);
        } catch (ReflectiveOperationException | IllegalStateException e) {
            LOGGER.log(Level.WARNING, String.format("A new build could not be created in job %s", asJob().getFullName()), e);
            throw new Error(e);
        }
    }