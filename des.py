class Info:
    ip = [
        58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7,
    ]  # ip置换

    ip_ = [
        40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25,
    ]

    E = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1,
    ]

    S = [
        [
            0xe, 0x4, 0xd, 0x1, 0x2, 0xf, 0xb, 0x8, 0x3, 0xa, 0x6, 0xc, 0x5, 0x9, 0x0, 0x7,
            0x0, 0xf, 0x7, 0x4, 0xe, 0x2, 0xd, 0x1, 0xa, 0x6, 0xc, 0xb, 0x9, 0x5, 0x3, 0x8,
            0x4, 0x1, 0xe, 0x8, 0xd, 0x6, 0x2, 0xb, 0xf, 0xc, 0x9, 0x7, 0x3, 0xa, 0x5, 0x0,
            0xf, 0xc, 0x8, 0x2, 0x4, 0x9, 0x1, 0x7, 0x5, 0xb, 0x3, 0xe, 0xa, 0x0, 0x6, 0xd,
        ],
        [
            0xf, 0x1, 0x8, 0xe, 0x6, 0xb, 0x3, 0x4, 0x9, 0x7, 0x2, 0xd, 0xc, 0x0, 0x5, 0xa,
            0x3, 0xd, 0x4, 0x7, 0xf, 0x2, 0x8, 0xe, 0xc, 0x0, 0x1, 0xa, 0x6, 0x9, 0xb, 0x5,
            0x0, 0xe, 0x7, 0xb, 0xa, 0x4, 0xd, 0x1, 0x5, 0x8, 0xc, 0x6, 0x9, 0x3, 0x2, 0xf,
            0xd, 0x8, 0xa, 0x1, 0x3, 0xf, 0x4, 0x2, 0xb, 0x6, 0x7, 0xc, 0x0, 0x5, 0xe, 0x9,
        ],
        [
            0xa, 0x0, 0x9, 0xe, 0x6, 0x3, 0xf, 0x5, 0x1, 0xd, 0xc, 0x7, 0xb, 0x4, 0x2, 0x8,
            0xd, 0x7, 0x0, 0x9, 0x3, 0x4, 0x6, 0xa, 0x2, 0x8, 0x5, 0xe, 0xc, 0xb, 0xf, 0x1,
            0xd, 0x6, 0x4, 0x9, 0x8, 0xf, 0x3, 0x0, 0xb, 0x1, 0x2, 0xc, 0x5, 0xa, 0xe, 0x7,
            0x1, 0xa, 0xd, 0x0, 0x6, 0x9, 0x8, 0x7, 0x4, 0xf, 0xe, 0x3, 0xb, 0x5, 0x2, 0xc,
        ],
        [
            0x7, 0xd, 0xe, 0x3, 0x0, 0x6, 0x9, 0xa, 0x1, 0x2, 0x8, 0x5, 0xb, 0xc, 0x4, 0xf,
            0xd, 0x8, 0xb, 0x5, 0x6, 0xf, 0x0, 0x3, 0x4, 0x7, 0x2, 0xc, 0x1, 0xa, 0xe, 0x9,
            0xa, 0x6, 0x9, 0x0, 0xc, 0xb, 0x7, 0xd, 0xf, 0x1, 0x3, 0xe, 0x5, 0x2, 0x8, 0x4,
            0x3, 0xf, 0x0, 0x6, 0xa, 0x1, 0xd, 0x8, 0x9, 0x4, 0x5, 0xb, 0xc, 0x7, 0x2, 0xe,
        ],
        [
            0x2, 0xc, 0x4, 0x1, 0x7, 0xa, 0xb, 0x6, 0x8, 0x5, 0x3, 0xf, 0xd, 0x0, 0xe, 0x9,
            0xe, 0xb, 0x2, 0xc, 0x4, 0x7, 0xd, 0x1, 0x5, 0x0, 0xf, 0xa, 0x3, 0x9, 0x8, 0x6,
            0x4, 0x2, 0x1, 0xb, 0xa, 0xd, 0x7, 0x8, 0xf, 0x9, 0xc, 0x5, 0x6, 0x3, 0x0, 0xe,
            0xb, 0x8, 0xc, 0x7, 0x1, 0xe, 0x2, 0xd, 0x6, 0xf, 0x0, 0x9, 0xa, 0x4, 0x5, 0x3,
        ],
        [
            0xc, 0x1, 0xa, 0xf, 0x9, 0x2, 0x6, 0x8, 0x0, 0xd, 0x3, 0x4, 0xe, 0x7, 0x5, 0xb,
            0xa, 0xf, 0x4, 0x2, 0x7, 0xc, 0x9, 0x5, 0x6, 0x1, 0xd, 0xe, 0x0, 0xb, 0x3, 0x8,
            0x9, 0xe, 0xf, 0x5, 0x2, 0x8, 0xc, 0x3, 0x7, 0x0, 0x4, 0xa, 0x1, 0xd, 0xb, 0x6,
            0x4, 0x3, 0x2, 0xc, 0x9, 0x5, 0xf, 0xa, 0xb, 0xe, 0x1, 0x7, 0x6, 0x0, 0x8, 0xd,
        ],
        [
            0x4, 0xb, 0x2, 0xe, 0xf, 0x0, 0x8, 0xd, 0x3, 0xc, 0x9, 0x7, 0x5, 0xa, 0x6, 0x1,
            0xd, 0x0, 0xb, 0x7, 0x4, 0x9, 0x1, 0xa, 0xe, 0x3, 0x5, 0xc, 0x2, 0xf, 0x8, 0x6,
            0x1, 0x4, 0xb, 0xd, 0xc, 0x3, 0x7, 0xe, 0xa, 0xf, 0x6, 0x8, 0x0, 0x5, 0x9, 0x2,
            0x6, 0xb, 0xd, 0x8, 0x1, 0x4, 0xa, 0x7, 0x9, 0x5, 0x0, 0xf, 0xe, 0x2, 0x3, 0xc,
        ],
        [
            0xd, 0x2, 0x8, 0x4, 0x6, 0xf, 0xb, 0x1, 0xa, 0x9, 0x3, 0xe, 0x5, 0x0, 0xc, 0x7,
            0x1, 0xf, 0xd, 0x8, 0xa, 0x3, 0x7, 0x4, 0xc, 0x5, 0x6, 0xb, 0x0, 0xe, 0x9, 0x2,
            0x7, 0xb, 0x4, 0x1, 0x9, 0xc, 0xe, 0x2, 0x0, 0x6, 0xa, 0xd, 0xf, 0x3, 0x5, 0x8,
            0x2, 0x1, 0xe, 0x7, 0x4, 0xa, 0x8, 0xd, 0xf, 0xc, 0x9, 0x0, 0x3, 0x5, 0x6, 0xb,
        ]]
    P = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25,
    ]
    k1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4,
    ]  # 密钥的K1初始置换
    k2 = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32,
    ]
    k0 = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, ]


def str2bin(string: str) -> list:
    temp = []
    for k in list(bytes(string, 'utf8')):
        temp.extend([int(i) for i in bin(k)[2:].zfill(8)])
    return temp


def p1(bins: list):
    temp = []
    for i in range(0, len(Info.ip)):
        temp.append(bins[Info.ip[i] - 1])
    return temp


def p1_(bins: list):
    temp = []
    for i in range(0, len(Info.ip_)):
        temp.append(bins[Info.ip_[i] - 1])
    return temp


def bin2hex(binary):
    out = ""
    for i in range(0, len(binary), 4):
        strs = ""
        for k in binary[i:i + 4]:
            strs += str(k)

        out += hex(int(strs, 2))[2:]
    return out.upper()


def hex2bin(strs):
    binary = []
    for i in strs:
        binary.extend([int(i) for i in bin(int(i, 16))[2:].zfill(4)])
    return binary


class Key:
    def key_pc(self, binary: list):
        temp = []
        for i in range(0, len(Info.k1)):
            temp.append(binary[Info.k1[i] - 1])
        return temp

    def cycle_key(self, binary: list, round: int):
        temp = []
        number = Info.k0[round - 1]
        length = int(len(binary) / 2)
        left = binary[:length]
        right = binary[length:]

        temp.extend(left[number:])
        temp.extend(left[:number])
        temp.extend(right[number:])
        temp.extend(right[:number])
        return temp

    def key_pc2(self, binary: list):
        temp = []
        for i in range(0, len(Info.k2)):
            temp.append(binary[Info.k2[i] - 1])
        return temp

    # 32bit

    def get_key(self, key):
        alls = []
        key = self.key_pc(key)

        for i in range(1, 17):
            key = self.cycle_key(key, i)
            alls.append(self.key_pc2(key))
        return alls


class Turn:
    def E_encode(self, binary: list):
        temp = []
        for i in range(0, len(Info.E)):
            temp.append(binary[Info.E[i] - 1])
        return temp

    def xor(self, binary_a, binary_b):
        if len(binary_a) == len(binary_b):
            temp = []
            for i in range(0, len(binary_a)):
                temp.append(binary_a[i] ^ binary_b[i])
            return temp

    def P_encode(self, binary: list):
        temp = []
        for i in range(0, len(Info.P)):
            temp.append(binary[Info.P[i] - 1])
        return temp

    def s_encode(self, binary: list):
        if len(binary) == 48:
            temp = []
            for i in range(0, len(binary), 6):
                this_s = Info.S[int(i / 6)]
                work_list = binary[i:i + 6]
                H = int(str(work_list[0]) + str(work_list[5]), 2)
                L = ""
                for i in work_list[1:5]:
                    L += str(i)
                L = int(L, 2)
                number = this_s[H * 16 + L]
                temp.extend([int(i) for i in bin(number)[2:].zfill(4)])
            return temp

    def F(self, bit32, Ki):
        temp = self.E_encode(bit32)
        temp = self.xor(temp, Ki)
        temp = self.s_encode(temp)
        temp = self.P_encode(temp)
        return temp

    def encode(self, L, R, key, round=0):
        if round < 16:
            work_key = key[round]

            work = self.F(R, work_key)
            return self.encode(R, self.xor(L, work), key, round + 1)
        else:
            return L, R


def encode_64b(binary, key):
    binary = p1(binary)
    sub_keys = Key().get_key(key)
    L, R = Turn().encode(binary[:32], binary[32:], sub_keys)
    temp = []
    temp.extend(R)
    temp.extend(L)

    return bin2hex(p1_(temp))


def decode_64b(binary, key):
    binary = p1(binary)
    sub_keys = Key().get_key(key)[::-1]
    turn = Turn()
    L, R = Turn().encode(binary[:32], binary[32:], sub_keys)
    temp = []
    temp.extend(R)
    temp.extend(L)
    temp = bin2hex(p1_(temp))
    strs = ""
    for i in range(0, len(temp), 2):
        if temp[i:i + 2] == "00":
            continue
        strs += chr(int(temp[i:i + 2], 16))
    return strs


def Fillzero(strs):
    need = len(strs) % 8
    if need != 0:
        need = 8 - len(strs) % 8
    return str2bin(strs) + 8 * need * [0]


def encode(strs: str, key: str) -> str:
    binary = Fillzero(strs)
    key = str2bin(key)
    out = ""
    for i in range(0, len(binary), 64):
        out += encode_64b(binary[i:i + 64], key)
    return out


def decode(hexs: str, key: str) -> str:
    key = str2bin(key)
    out = ""
    for i in range(0, len(hexs), 16):
        binary = hex2bin(hexs[i:i + 16])
        out += decode_64b(binary, key)

    return out



print("输入8字节Key:")
inputs_key = input()
while True:
    print("\n输入选项：1.加密明文\t2.解密密文\t3.退出")
    num = input()
    if num == "1":
        print("输入明文:")
        inputs = input()
        c = encode(inputs, inputs_key)
        print("加密后的密文Hex为：", c)
    elif num == "2":
        print("输入密文:")
        inputs = input()
        m = decode(inputs, inputs_key)
        print("解密后的原文为：", m)

    elif num == "3":
        break
    else:
        print("输入有误，重新输入")
