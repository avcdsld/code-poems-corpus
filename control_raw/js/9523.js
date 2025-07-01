function compile(element, attr) {
      // Grab the user template from attr and reset the attribute to null.
      var userTemplate = attr['$mdUserTemplate'];
      attr['$mdUserTemplate'] = null;

      var chipTemplate = getTemplateByQuery('md-chips>md-chip-template');

      var chipRemoveSelector = $mdUtil
        .prefixer()
        .buildList('md-chip-remove')
        .map(function(attr) {
          return 'md-chips>*[' + attr + ']';
        })
        .join(',');

      // Set the chip remove, chip contents and chip input templates. The link function will put
      // them on the scope for transclusion later.
      var chipRemoveTemplate   = getTemplateByQuery(chipRemoveSelector) || templates.remove,
          chipContentsTemplate = chipTemplate || templates.default,
          chipInputTemplate    = getTemplateByQuery('md-chips>md-autocomplete')
              || getTemplateByQuery('md-chips>input')
              || templates.input,
          staticChips = userTemplate.find('md-chip');

      // Warn of malformed template. See #2545
      if (userTemplate[0].querySelector('md-chip-template>*[md-chip-remove]')) {
        $log.warn('invalid placement of md-chip-remove within md-chip-template.');
      }

      function getTemplateByQuery (query) {
        if (!attr.ngModel) return;
        var element = userTemplate[0].querySelector(query);
        return element && element.outerHTML;
      }

      /**
       * Configures controller and transcludes.
       */
      return function postLink(scope, element, attrs, controllers) {
        $mdUtil.initOptionalProperties(scope, attr);

        $mdTheming(element);
        var mdChipsCtrl = controllers[0];
        if (chipTemplate) {
          // Chip editing functionality assumes we are using the default chip template.
          mdChipsCtrl.enableChipEdit = false;
        }

        mdChipsCtrl.chipContentsTemplate = chipContentsTemplate;
        mdChipsCtrl.chipRemoveTemplate   = chipRemoveTemplate;
        mdChipsCtrl.chipInputTemplate    = chipInputTemplate;

        mdChipsCtrl.mdCloseIcon = $$mdSvgRegistry.mdClose;

        element
            .attr({ tabindex: -1 })
            .on('focus', function () { mdChipsCtrl.onFocus(); })
            .on('click', function () {
              if (!mdChipsCtrl.readonly && mdChipsCtrl.selectedChip === -1) {
                mdChipsCtrl.onFocus();
              }
            });

        if (attr.ngModel) {
          mdChipsCtrl.configureNgModel(element.controller('ngModel'));

          // If an `md-transform-chip` attribute was set, tell the controller to use the expression
          // before appending chips.
          if (attrs.mdTransformChip) mdChipsCtrl.useTransformChipExpression();

          // If an `md-on-append` attribute was set, tell the controller to use the expression
          // when appending chips.
          //
          // TODO: Remove this now that 1.0 is long since released
          // DEPRECATED: Will remove in official 1.0 release
          if (attrs.mdOnAppend) mdChipsCtrl.useOnAppendExpression();

          // If an `md-on-add` attribute was set, tell the controller to use the expression
          // when adding chips.
          if (attrs.mdOnAdd) mdChipsCtrl.useOnAddExpression();

          // If an `md-on-remove` attribute was set, tell the controller to use the expression
          // when removing chips.
          if (attrs.mdOnRemove) mdChipsCtrl.useOnRemoveExpression();

          // If an `md-on-select` attribute was set, tell the controller to use the expression
          // when selecting chips.
          if (attrs.mdOnSelect) mdChipsCtrl.useOnSelectExpression();

          // The md-autocomplete and input elements won't be compiled until after this directive
          // is complete (due to their nested nature). Wait a tick before looking for them to
          // configure the controller.
          if (chipInputTemplate !== templates.input) {
            // The autocomplete will not appear until the readonly attribute is not true (i.e.
            // false or undefined), so we have to watch the readonly and then on the next tick
            // after the chip transclusion has run, we can configure the autocomplete and user
            // input.
            scope.$watch('$mdChipsCtrl.readonly', function(readonly) {
              if (!readonly) {

                $mdUtil.nextTick(function(){

                  if (chipInputTemplate.indexOf('<md-autocomplete') === 0) {
                    var autocompleteEl = element.find('md-autocomplete');
                    mdChipsCtrl.configureAutocomplete(autocompleteEl.controller('mdAutocomplete'));
                  }

                  mdChipsCtrl.configureUserInput(element.find('input'));
                });
              }
            });
          }

          // At the next tick, if we find an input, make sure it has the md-input class
          $mdUtil.nextTick(function() {
            var input = element.find('input');

            if (input) {
              mdChipsCtrl.configureInput(input);
              input.toggleClass('md-input', true);
            }
          });
        }

        // Compile with the parent's scope and prepend any static chips to the wrapper.
        if (staticChips.length > 0) {
          var compiledStaticChips = $compile(staticChips.clone())(scope.$parent);
          $timeout(function() { element.find('md-chips-wrap').prepend(compiledStaticChips); });
        }
      };
    }