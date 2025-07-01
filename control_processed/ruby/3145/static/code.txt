def update
      filter_docs_with_edit_access!
      copy_visibility = params[:embargoes].values.map { |h| h[:copy_visibility] }
      ActiveFedora::Base.find(batch).each do |curation_concern|
        Hyrax::Actors::EmbargoActor.new(curation_concern).destroy
        # if the concern is a FileSet, set its visibility and skip the copy_visibility_to_files, which is built for Works
        if curation_concern.file_set?
          curation_concern.visibility = curation_concern.to_solr["visibility_after_embargo_ssim"]
          curation_concern.save!
        elsif copy_visibility.include?(curation_concern.id)
          curation_concern.copy_visibility_to_files
        end
      end
      redirect_to embargoes_path, notice: t('.embargo_deactivated')
    end