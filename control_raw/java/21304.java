public void setNote(String note) {
       try {
           staticTableHistory.updateNote(historyId, note);
           httpMessageCachedData.setNote(note != null && note.length() > 0);
           notifyEvent(HistoryReferenceEventPublisher.EVENT_NOTE_SET);
       } catch (DatabaseException e) {
           log.error(e.getMessage(), e);
       }
       
   }