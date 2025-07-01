public static DescriptorExtensionList<ListViewColumn, Descriptor<ListViewColumn>> all() {
        return Jenkins.getInstance().<ListViewColumn, Descriptor<ListViewColumn>>getDescriptorList(ListViewColumn.class);
    }