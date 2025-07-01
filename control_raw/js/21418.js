function(cm, operatorArgs, _vim, curStart, curEnd) {
        // If the ending line is past the last line, inclusive, instead of
        // including the trailing \n, include the \n before the starting line
        if (operatorArgs.linewise &&
            curEnd.line > cm.lastLine() && curStart.line > cm.firstLine()) {
          curStart.line--;
          curStart.ch = lineLength(cm, curStart.line);
        }
        vimGlobalState.registerController.pushText(
            operatorArgs.registerName, 'delete', cm.getRange(curStart, curEnd),
            operatorArgs.linewise);
        cm.replaceRange('', curStart, curEnd);
        if (operatorArgs.linewise) {
          cm.setCursor(motions.moveToFirstNonWhiteSpaceCharacter(cm));
        } else {
          cm.setCursor(curStart);
        }
      }