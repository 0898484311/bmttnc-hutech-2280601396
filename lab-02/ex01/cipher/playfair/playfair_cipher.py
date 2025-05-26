class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        matrix = []
        seen = set()

        for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                seen.add(char)
                matrix.append(char)

        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        i = 0
        prepared_text = ""
        
        # Tạo cặp ký tự không trùng nhau
        while i < len(plain_text):
            a = plain_text[i]
            b = ''
            if i + 1 < len(plain_text):
                b = plain_text[i + 1]
            else:
                b = 'X'
            if a == b:
                prepared_text += a + 'X'
                i += 1
            else:
                prepared_text += a + b
                i += 2
        if len(prepared_text) % 2 != 0:
            prepared_text += 'X'

        encrypted = ''
        for i in range(0, len(prepared_text), 2):
            a = prepared_text[i]
            b = prepared_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                encrypted += matrix[row1][(col1 + 1) % 5]
                encrypted += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted += matrix[(row1 + 1) % 5][col1]
                encrypted += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted += matrix[row1][col2]
                encrypted += matrix[row2][col1]
        return encrypted

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted = ''

        for i in range(0, len(cipher_text), 2):
            a = cipher_text[i]
            b = cipher_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                decrypted += matrix[row1][(col1 - 1) % 5]
                decrypted += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted += matrix[(row1 - 1) % 5][col1]
                decrypted += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted += matrix[row1][col2]
                decrypted += matrix[row2][col1]
        return decrypted
