function (err, updatedIdentityCounter) {
                if (err) return next(err);
                // If there are no errors then go ahead and set the document's field to the current count.
                doc[settings.field] = updatedIdentityCounter.count;
                // Continue with default document save functionality.
                next();
              }