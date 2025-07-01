public static DescriptorExtensionList<LabelAtomProperty,LabelAtomPropertyDescriptor> all() {
        return Jenkins.getInstance().<LabelAtomProperty,LabelAtomPropertyDescriptor>getDescriptorList(LabelAtomProperty.class);
    }