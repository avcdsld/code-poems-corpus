private String getLines(SlotsLines lines) {
    StringBuilder builder = new StringBuilder();
    for (MiniCapability cap : lines.getLinesType()) {
      String icon = cap.getIcon();
      String version = cap.getVersion();
      builder.append("<p>");
      if (version != null) {
        builder.append("v:").append(version);
      }
      for (TestSlot s : lines.getLine(cap)) {
        builder.append(getSingleSlotHtml(s, icon));
      }
      builder.append("</p>");
    }
    return builder.toString();
  }