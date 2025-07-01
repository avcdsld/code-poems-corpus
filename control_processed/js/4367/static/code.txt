function _moveNext() {
        var $context, $next;

        $context = $currentContext || $("#mrof-container #mrof-list > li.highlight");
        if ($context.length > 0) {
            $next = $context.next();
            if ($next.length === 0) {
                $next = $("#mrof-container #mrof-list > li").first();
            }
            if ($next.length > 0) {
                $currentContext = $next;
                $next.find("a.mroitem").trigger("focus");
            }
        } else {
            //WTF! (Worse than failure). We should not get here.
            $("#mrof-container #mrof-list > li > a.mroitem:visited").last().trigger("focus");
        }
    }