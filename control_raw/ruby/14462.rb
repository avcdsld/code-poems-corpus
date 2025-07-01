def add_annotation(*annotations)
            self.Annots ||= []

            annotations.each do |annot|
                annot.solve[:P] = self if self.indirect?
                self.Annots << annot
            end
        end