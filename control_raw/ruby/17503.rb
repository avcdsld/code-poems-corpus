def journal_lines
      if journal_lines_downloaded?
        @journal_lines

      elsif manual_journal_id =~ GUID_REGEX && @gateway
        # There is a manual_journal_id so we can assume this record was loaded from Xero.
        # Let's attempt to download the journal_line records (if there is a gateway)

        response = @gateway.get_manual_journal(manual_journal_id)
        raise ManualJournalNotFoundError, "Manual Journal with ID #{manual_journal_id} not found in Xero." unless response.success? && response.manual_journal.is_a?(XeroGateway::ManualJournal)

        @journal_lines = response.manual_journal.journal_lines
        @journal_lines_downloaded = true

        @journal_lines

      # Otherwise, this is a new manual journal, so return the journal_lines reference.
      else
        @journal_lines
      end
    end