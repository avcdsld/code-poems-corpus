def convert(self):
        """Converts the mp3's associated with this instance to wav's
        Return:
          wav_directory (os.path): The directory into which the associated wav's were downloaded
        """
        wav_directory = self._pre_convert()
        for mp3_filename in self.mp3_directory.glob('**/*.mp3'):
            wav_filename = path.join(wav_directory, os.path.splitext(os.path.basename(mp3_filename))[0] + ".wav")
            if not path.exists(wav_filename):
                _logger.debug("Converting mp3 file %s to wav file %s" % (mp3_filename, wav_filename))
                transformer = Transformer()
                transformer.convert(samplerate=SAMPLE_RATE, n_channels=N_CHANNELS, bitdepth=BITDEPTH)
                transformer.build(str(mp3_filename), str(wav_filename))
            else:
                _logger.debug("Already converted mp3 file %s to wav file %s" % (mp3_filename, wav_filename))
        return wav_directory