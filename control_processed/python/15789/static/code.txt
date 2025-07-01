def install (self, scanner, target, vtarget):
        """ Installs the specified scanner on actual target 'target'.
            vtarget: virtual target from which 'target' was actualized.
        """
        assert isinstance(scanner, Scanner)
        assert isinstance(target, basestring)
        assert isinstance(vtarget, basestring)
        engine = self.manager_.engine()
        engine.set_target_variable(target, "HDRSCAN", scanner.pattern())
        if scanner not in self.exported_scanners_:
            exported_name = "scanner_" + str(self.count_)
            self.count_ = self.count_ + 1
            self.exported_scanners_[scanner] = exported_name
            bjam.import_rule("", exported_name, scanner.process)
        else:
            exported_name = self.exported_scanners_[scanner]

        engine.set_target_variable(target, "HDRRULE", exported_name)

        # scanner reflects difference in properties affecting
        # binding of 'target', which will be known when processing
        # includes for it, will give information on how to
        # interpret quoted includes.
        engine.set_target_variable(target, "HDRGRIST", str(id(scanner)))
        pass