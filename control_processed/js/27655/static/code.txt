function ()
    {
        var stacks = {};
        jQuery.each(jQuery('.jBox-Notice'), function (index, el)
        {
          el = jQuery(el);
          var pos = el.data('jBox-Notice-position');
          if (!stacks[pos]) {
              stacks[pos] = [];
          }
          stacks[pos].push(el);
        });
        for (var pos in stacks) {
            var position = pos.split('-');
            var direction = position[1];
            stacks[pos].reverse();
            var margin = 0;
            for (var i in stacks[pos]) {
                el = stacks[pos][i];
                el.css('margin-' + direction, margin);
                margin += el.outerHeight() + this.options.stackSpacing;
            }
        }
    }