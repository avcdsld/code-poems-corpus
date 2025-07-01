def find_emoji(name)
      LOGGER.out("Resolving emoji #{name}")
      emoji.find { |element| element.name == name }
    end