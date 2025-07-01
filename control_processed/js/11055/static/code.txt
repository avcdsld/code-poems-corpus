function findSafe($context, selector) {
      if (arguments.length === 1) {
        selector = arguments[0];
        $context = self.$el;
      }
      if (!options.nestGuard) {
        return $context.find(selector);
      }
      return $context.find(selector).not($context.find(options.nestGuard).find(selector));
    }