function mixinControllerDefinition(oController, CustomControllerDef, sLocalNameSpace) {
			if (CustomControllerDef instanceof ControllerExtension) {
				applyExtension(oController, CustomControllerDef, sLocalNameSpace);
			} else if (CustomControllerDef.getMetadata && CustomControllerDef.getMetadata().getStereotype() == "controllerextension") {
				//create ControllerExtension instance
				var oControllerExtension = new CustomControllerDef();
				applyExtension(oController, oControllerExtension, sLocalNameSpace);
			} else {
				//apply 'legacy' extension
				var mLifecycleConfig = ControllerExtension.getMetadata().getLifecycleConfiguration();
				for (var sMemberName in CustomControllerDef) {
					if (sMemberName in mLifecycleConfig) {
						ControllerExtension.overrideMethod(sMemberName, oController, CustomControllerDef, oController, mLifecycleConfig[sMemberName].overrideExecution);
					} else {
						//default extension behavior
						ControllerExtension.overrideMethod(sMemberName, oController, CustomControllerDef);
					}
				}
			}
		}