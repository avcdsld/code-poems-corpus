def make_output_layers(self):
        """
        Extract the ordering of output layers.
        """
        self.output_layers = []
        # import pytest; pytest.set_trace()
        if hasattr(self.model, 'output_layers'):
            # find corresponding output layers in CoreML model
            # assume output layers are not shared
            # Helper function to recursively extract output layers
            # even if the model has a layer which is a nested model
            def extract_output_layers(keras_model):
                output_layers = []
                for layer in keras_model.output_layers:
                    if hasattr(layer,'output_layers'):
                        output_layers.extend(extract_output_layers(layer))
                    else:
                        output_layers.append(layer)
                return output_layers

            for kl in extract_output_layers(self.model):
                coreml_layers = self.get_coreml_layers(kl)
                if len(coreml_layers) > 0:
                    for cl in coreml_layers:
                        self.output_layers.append(cl)
        elif len(self.model.outputs) > 0:
            for model_output in self.model.outputs:
                for l in self.layer_list:
                    k_layer = self.keras_layer_map[l]
                    in_nodes = k_layer._inbound_nodes if hasattr(k_layer, '_inbound_nodes') else k_layer.inbound_nodes
                    for idx in range(len(in_nodes)):
                        out_tensor = k_layer.get_output_at(idx)
                        if out_tensor == model_output or (out_tensor.name in model_output.name):
                            self.output_layers.append(l)
        if len(self.output_layers) == 0:
            raise ValueError("No outputs can be identified")