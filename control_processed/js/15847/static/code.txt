function() {
          var self = this;
          $firebaseUtils.trimKeys(self, {});
          self.$value = null;
          return $firebaseUtils.doRemove(self.$ref()).then(function() {
            self.$$notify();
            return self.$ref();
          });
        }