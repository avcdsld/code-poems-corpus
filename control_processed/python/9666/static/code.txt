def iter_links(self):
        # type: () -> Iterable[Link]
        """Yields all links in the page"""
        document = html5lib.parse(
            self.content,
            transport_encoding=_get_encoding_from_headers(self.headers),
            namespaceHTMLElements=False,
        )
        base_url = _determine_base_url(document, self.url)
        for anchor in document.findall(".//a"):
            if anchor.get("href"):
                href = anchor.get("href")
                url = _clean_link(urllib_parse.urljoin(base_url, href))
                pyrequire = anchor.get('data-requires-python')
                pyrequire = unescape(pyrequire) if pyrequire else None
                yield Link(url, self.url, requires_python=pyrequire)