function writeAnchorTag (evt, options, globals, emptyCase) {

    var wholeMatch = evt.getMatches().wholeMatch;
    var text = evt.getMatches().text;
    var id = evt.getMatches().id;
    var url = evt.getMatches().url;
    var title = evt.getMatches().title;
    var target = '';

    if (!title) {
      title = '';
    }
    id = (id) ? id.toLowerCase() : '';

    if (emptyCase) {
      url = '';
    } else if (!url) {
      if (!id) {
        // lower-case and turn embedded newlines into spaces
        id = text.toLowerCase().replace(/ ?\n/g, ' ');
      }
      url = '#' + id;

      if (!showdown.helper.isUndefined(globals.gUrls[id])) {
        url = globals.gUrls[id];
        if (!showdown.helper.isUndefined(globals.gTitles[id])) {
          title = globals.gTitles[id];
        }
      } else {
        return wholeMatch;
      }
    }
    //url = showdown.helper.escapeCharacters(url, '*_:~', false); // replaced line to improve performance
    url = url.replace(showdown.helper.regexes.asteriskDashTildeAndColon, showdown.helper.escapeCharactersCallback);

    if (title !== '' && title !== null) {
      title = title.replace(/"/g, '&quot;');
      //title = showdown.helper.escapeCharacters(title, '*_', false); // replaced line to improve performance
      title = title.replace(showdown.helper.regexes.asteriskDashTildeAndColon, showdown.helper.escapeCharactersCallback);
      title = ' title="' + title + '"';
    }

    // optionLinksInNewWindow only applies
    // to external links. Hash links (#) open in same page
    if (options.openLinksInNewWindow && !/^#/.test(url)) {
      // escaped _
      target = ' target="¨E95Eblank"';
    }

    // Text can be a markdown element, so we run through the appropriate parsers
    text = showdown.subParser('makehtml.codeSpans')(text, options, globals);
    text = showdown.subParser('makehtml.emoji')(text, options, globals);
    text = showdown.subParser('makehtml.underline')(text, options, globals);
    text = showdown.subParser('makehtml.italicsAndBold')(text, options, globals);
    text = showdown.subParser('makehtml.strikethrough')(text, options, globals);
    text = showdown.subParser('makehtml.ellipsis')(text, options, globals);
    text = showdown.subParser('makehtml.hashHTMLSpans')(text, options, globals);

    //evt = createEvent(rgx, evtRootName + '.captureEnd', wholeMatch, text, id, url, title, options, globals);

    var result = '<a href="' + url + '"' + title + target + '>' + text + '</a>';

    //evt = createEvent(rgx, evtRootName + '.beforeHash', wholeMatch, text, id, url, title, options, globals);

    result = showdown.subParser('makehtml.hashHTMLSpans')(result, options, globals);

    return result;
  }