class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1:
            return plain_text

        # Khởi tạo các rail rỗng
        rails = ['' for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: xuống, -1: lên

        # Ghi từng ký tự vào đúng rail
        for char in plain_text:
            rails[rail_index] += char
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Ghép các rail lại thành chuỗi mã hóa
        return ''.join(rails)

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1:
            return cipher_text

        # Bước 1: Xác định số ký tự trên từng rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Bước 2: Cắt cipher_text thành từng rail
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Bước 3: Đọc theo đường đi zigzag để giải mã
        result = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            result += rails[rail_index].pop(0)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return result
