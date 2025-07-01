function () {

    var self = this;

    // Modal Cleaning
    if (self.options.modal) {
      $.notyRenderer.setModalCount(-1);
      if ($.notyRenderer.getModalCount() == 0 && !$.noty.queue.length) $('.noty_modal').fadeOut(self.options.animation.fadeSpeed, function () {
        $(this).remove();
      });
    }

    // Layout Cleaning
    $.notyRenderer.setLayoutCountFor(self, -1);
    if ($.notyRenderer.getLayoutCountFor(self) == 0) $(self.options.layout.container.selector).remove();

    // Make sure self.$bar has not been removed before attempting to remove it
    if (typeof self.$bar !== 'undefined' && self.$bar !== null) {

      if (typeof self.options.animation.close == 'string') {
        self.$bar.css('transition', 'all 10ms ease').css('border', 0).css('margin', 0).height(0);
        self.$bar.one('transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd', function () {
          self.$bar.remove();
          self.$bar   = null;
          self.closed = true;

          if (self.options.theme.callback && self.options.theme.callback.onClose) {
            self.options.theme.callback.onClose.apply(self);
          }

          self.handleNext();
        });
      } else {
        self.$bar.remove();
        self.$bar   = null;
        self.closed = true;

        self.handleNext();
      }
    } else {
      self.handleNext();
    }

  }