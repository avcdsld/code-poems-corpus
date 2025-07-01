@SuppressWarnings("unchecked")
	public O withForwardedFieldsSecond(String... forwardedFieldsSecond) {
		if (this.udfSemantics == null || this.analyzedUdfSemantics) {
			// extract semantic properties from function annotations
			setSemanticProperties(extractSemanticAnnotationsFromUdf(getFunction().getClass()));
		}

		if (this.udfSemantics == null || this.analyzedUdfSemantics) {
			setSemanticProperties(new DualInputSemanticProperties());
			SemanticPropUtil.getSemanticPropsDualFromString(this.udfSemantics, null, forwardedFieldsSecond,
					null, null, null, null, getInput1Type(), getInput2Type(), getResultType());
		} else {
			if (udfWithForwardedFieldsSecondAnnotation(getFunction().getClass())) {
				// refuse semantic information as it would override the function annotation
				throw new SemanticProperties.InvalidSemanticAnnotationException("Forwarded field information " +
						"has already been added by a function annotation for the second input of this operator. " +
						"Cannot overwrite function annotations.");
			} else {
				SemanticPropUtil.getSemanticPropsDualFromString(this.udfSemantics, null, forwardedFieldsSecond,
						null, null, null, null, getInput1Type(), getInput2Type(), getResultType());
			}
		}

		O returnType = (O) this;
		return returnType;
	}