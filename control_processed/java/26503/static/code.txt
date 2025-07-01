private File[] accept(File file, final boolean recursive) {
        // Custom filtering rules If you can loop (include subdirectories) or is the end of the file. Class (compiled java class file)
        return file.listFiles(file1 -> (recursive && file1.isDirectory()) || (file1.getName().endsWith(".class")));
    }