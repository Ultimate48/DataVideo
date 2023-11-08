import base64
import pickle


def extract_binary(file_path):
    name, file_format = file_path.split('.')
    name = name.split('\\')[-1]

    with open(file_path, 'rb') as file:
        data = file.read()

    file_data = {
        "data": data,
        "metadata": {"name": name, "format": file_format}
    }

    binary_data = base64.b64encode(pickle.dumps(file_data))
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)

    return binary_string
