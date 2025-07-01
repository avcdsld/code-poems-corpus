def hybrid_forward(self, F, inputs, token_types, valid_length=None, masked_positions=None):
        # pylint: disable=arguments-differ
        # pylint: disable=unused-argument
        """Generate the representation given the inputs.

        This is used in training or fine-tuning a static (hybridized) BERT model.
        """
        outputs = []
        seq_out, attention_out = self._encode_sequence(F, inputs, token_types, valid_length)
        outputs.append(seq_out)

        if self.encoder._output_all_encodings:
            assert isinstance(seq_out, list)
            output = seq_out[-1]
        else:
            output = seq_out

        if attention_out:
            outputs.append(attention_out)

        if self._use_pooler:
            pooled_out = self._apply_pooling(output)
            outputs.append(pooled_out)
            if self._use_classifier:
                next_sentence_classifier_out = self.classifier(pooled_out)
                outputs.append(next_sentence_classifier_out)
        if self._use_decoder:
            assert masked_positions is not None, \
                'masked_positions tensor is required for decoding masked language model'
            decoder_out = self._decode(output, masked_positions)
            outputs.append(decoder_out)
        return tuple(outputs) if len(outputs) > 1 else outputs[0]