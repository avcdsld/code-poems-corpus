def detect_fold_level(self, prev_block, block):
        """
        Detects fold level by looking at the block indentation.

        :param prev_block: previous text block
        :param block: current block to highlight
        """
        text = block.text()
        prev_lvl = TextBlockHelper().get_fold_lvl(prev_block)
        # round down to previous indentation guide to ensure contiguous block
        # fold level evolution.
        indent_len = 0
        if (prev_lvl and prev_block is not None and
           not self.editor.is_comment(prev_block)):
            # ignore commented lines (could have arbitary indentation)
            prev_text = prev_block.text()
            indent_len = (len(prev_text) - len(prev_text.lstrip())) // prev_lvl
        if indent_len == 0:
            indent_len = len(self.editor.indent_chars)

        return (len(text) - len(text.lstrip())) // indent_len