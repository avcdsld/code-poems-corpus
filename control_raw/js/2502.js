function(type, text) {
            var parser = parsers.get(type);

            return parser.parsePage(text)
                .get('content');
        }