function (element) {
            if (!element) {
                throw new ArgumentError(
                    Logger.logMessage(Logger.LEVEL_SEVERE, "OwsServiceProvider", "constructor", "missingDomElement"));
            }

            var children = element.children || element.childNodes;
            for (var c = 0; c < children.length; c++) {
                var child = children[c];

                if (child.localName === "ProviderName") {
                    this.providerName = child.textContent;
                } else if (child.localName === "ProviderSite") {
                    this.providerSiteUrl = child.getAttribute("xlink:href");
                } else if (child.localName === "ServiceContact") {
                    this.serviceContact = OwsServiceProvider.assembleServiceContact(child);
                }
            }
        }