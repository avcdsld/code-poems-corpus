function checkSearchField(controller, searchField,
                                                     searchTerm, submitButton,
                                                     timeout) {
  controller.waitThenClick(searchField, timeout);
  controller.type(searchField, searchTerm);

  if (submitButton != undefined) {
    controller.waitThenClick(submitButton, timeout);
  }
}