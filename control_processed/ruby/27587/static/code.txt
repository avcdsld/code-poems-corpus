def load_dependencies_to_classpath
      jars = dependencies_classpath.split(File::PATH_SEPARATOR)
      Naether::Java.load_jars(jars)

      jars
    end