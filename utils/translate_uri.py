MAX_LEN_FELT = 31

def str_to_felt(text):
    if len(text) > MAX_LEN_FELT:
        raise Exception("Text length too long to convert to felt.")
    b_text = bytes(text, "UTF-8")
    return int.from_bytes(b_text, "big")

def str_to_felt_array(text):
    # Break string into array of strings that meet felt requirements
    chunks = []
    for i in range(0, len(text), MAX_LEN_FELT):
        str_chunk = text[i:i+MAX_LEN_FELT]
        chunks.append(str_to_felt(str_chunk))
    return chunks


# Create a Felt Array
if __name__ == "__main__":
    text = "https://lh3.googleusercontent.com/fzyCdg7NxBVOQPkwZh2qnI3Ltgfx9LuV8dNpNtm80EQM_LESqyCJRaoZ5EoiX0iLr4sahiQcLRnQQhNqrqzMx3gWueTgGol42gD0=s0"
    felt_array = str_to_felt_array(text)
    print('Felt Array Length: {}'.format(len(felt_array)))
    print('Felt Array: {}'.format(felt_array))