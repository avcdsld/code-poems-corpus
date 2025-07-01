function addRowWithTime(tablePrinter, eventTime, startTime) {
    tablePrinter.addRow();
    tablePrinter.addCell('t=');
    const tCell = tablePrinter.addCell(eventTime);
    tCell.alignRight = true;
    tablePrinter.addCell(' [st=');
    const stCell = tablePrinter.addCell(eventTime - startTime);
    stCell.alignRight = true;
    tablePrinter.addCell('] ');
  }