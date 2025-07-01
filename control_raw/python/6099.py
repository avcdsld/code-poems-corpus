def _infer_num_arguments(cls, type_signature: str) -> int:
        """
        Takes a type signature and infers the number of arguments the corresponding function takes.
        Examples:
            e -> 0
            <r,e> -> 1
            <e,<e,t>> -> 2
            <b,<<b,#1>,<#1,b>>> -> 3
        """
        if not "<" in type_signature:
            return 0
        # We need to find the return type from the signature. We do that by removing the outer most
        # angular brackets and traversing the remaining substring till the angular brackets (if any)
        # balance. Once we hit a comma after the angular brackets are balanced, whatever is left
        # after it is the return type.
        type_signature = type_signature[1:-1]
        num_brackets = 0
        char_index = 0
        for char in type_signature:
            if char == '<':
                num_brackets += 1
            elif char == '>':
                num_brackets -= 1
            elif char == ',':
                if num_brackets == 0:
                    break
            char_index += 1
        return_type = type_signature[char_index+1:]
        return 1 + cls._infer_num_arguments(return_type)