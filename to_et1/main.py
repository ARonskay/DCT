import numpy as np


def get_dct_matrix(size):
    """ zwraca macierz size x size (transformacji) DCT """
    dmat = np.zeros((size, size), dtype=np.float64)
    for u in range(size):
        c_u = np.sqrt(1. / size) if u == 0 else np.sqrt(2. / size)
        for v in range(size):
            dmat[u, v] = c_u * np.cos((2 * v + 1) * u * np.pi / (2 * size))
    return dmat


def dct(img_bl, dctmat):
    """ oblicza dct """
    return dctmat @ img_bl @ dctmat.transpose()


def idct(coeffs_bl, dctmat):
    """ oblicza idct """
    return (dctmat.transpose() @ coeffs_bl @ dctmat).round().clip(0, 255)


def dct_image(image, blsize, dctmat=None):
    if dctmat is None:
        dctmat = get_dct_matrix(blsize)
    num_bl_x = image.shape[1] // blsize
    num_bl_y = image.shape[0] // blsize
    dct_coeffs = np.zeros_like(image, dtype=np.float64)
    for blx in range(num_bl_x):
        for bly in range(num_bl_y):
            img_bl = image[bly * blsize:(bly + 1) * blsize, blx * blsize:(blx + 1) * blsize]
            dct_coeffs[bly * blsize:(bly + 1) * blsize, blx * blsize:(blx + 1) * blsize] = dct(img_bl, dctmat)
    return dct_coeffs


def idct_image(coeffs, blsize, dctmat=None):
    if dctmat is None:
        dctmat = get_dct_matrix(blsize)
    num_bl_x = coeffs.shape[1] // blsize
    num_bl_y = coeffs.shape[0] // blsize
    img_rec = np.zeros_like(coeffs, dtype=np.uint8)
    for blx in range(num_bl_x):
        for bly in range(num_bl_y):
            coeffs_bl = coeffs[bly * blsize:(bly + 1) * blsize, blx * blsize:(blx + 1) * blsize]
            img_rec[bly * blsize:(bly + 1) * blsize, blx * blsize:(blx + 1) * blsize] = idct(coeffs_bl, dctmat)
    return img_rec


def select_q_matrix(q_matrix):
    q10 = np.array([[80, 60, 50, 80, 120, 200, 255, 255],
                    [55, 60, 70, 95, 130, 255, 255, 255],
                    [70, 65, 80, 120, 200, 255, 255, 255],
                    [70, 85, 110, 145, 255, 255, 255, 255],
                    [90, 110, 185, 255, 255, 255, 255, 255],
                    [120, 175, 255, 255, 255, 255, 255, 255],
                    [245, 255, 255, 255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255, 255, 255, 255]])

    q50 = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                    [12, 12, 14, 19, 26, 58, 60, 55],
                    [14, 13, 16, 24, 40, 57, 69, 56],
                    [14, 17, 22, 29, 51, 87, 80, 62],
                    [18, 22, 37, 56, 68, 109, 103, 77],
                    [24, 35, 55, 64, 81, 104, 113, 92],
                    [49, 64, 78, 87, 103, 121, 120, 101],
                    [72, 92, 95, 98, 112, 100, 130, 99]])

    q90 = np.array([[3, 2, 2, 3, 5, 8, 10, 12],
                    [2, 2, 3, 4, 5, 12, 12, 11],
                    [3, 3, 3, 5, 8, 11, 14, 11],
                    [3, 3, 4, 6, 10, 17, 16, 12],
                    [4, 4, 7, 11, 14, 22, 21, 15],
                    [5, 7, 11, 13, 16, 12, 23, 18],
                    [10, 13, 16, 17, 21, 24, 24, 21],
                    [14, 18, 19, 20, 22, 20, 20, 20]])

    # macierz sandboxowa do modyfikacji
    qX = np.array([[17, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1]])

    q1 = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]])

    if q_matrix == "q10":
        return q10
    elif q_matrix == "q50":
        return q50
    elif q_matrix == "q90":
        return q90
    elif q_matrix == "q1":
        return q1
    elif q_matrix == "qX":
        return qX
    return np.full((8, 8), int(q_matrix), dtype=int)  # zwraca macierz jednakowych wartości


def quant_operation(small_block, q_matrix, kind):
    """ Funckja pomocnicza do wyboru rodzaju kwantyzacji;  "d" divide, "m" multipy """
    if kind == "d":
        quant_matrix = small_block / q_matrix
    else:
        quant_matrix = small_block * q_matrix
    return quant_matrix


def quant_once(big_matrix, x_blocks, y_blocks, q_matrix, kind):
    """ Jeden proces kwantyzacji """
    """ kind -> "d" divide   "m" multiply """
    quant_matrix = np.zeros_like(big_matrix)
    block_size = len(q_matrix)

    for blx in range(x_blocks):
        for bly in range(y_blocks):
            block = big_matrix[bly * block_size: (bly + 1) * block_size, blx * block_size: (blx + 1) * block_size]
            quant_matrix[bly * block_size: (bly + 1) * block_size, blx * block_size: (blx + 1) * block_size] = \
                np.round_(quant_operation(block, q_matrix, kind))
    return quant_matrix


def quantize_full(dct_coeffs_matrix, quality):  # quality -> podaje sie:  "qXX"
    """ Najwazniejsza funkcja kwantyzujaca, przeprowadza rowniez proces dekwantyzacji """
    q_matrix = select_q_matrix(quality)
    no_x_blocks = dct_coeffs_matrix.shape[1] // len(q_matrix)  # q_matrix jest 8x8 wiec 8
    no_y_blocks = dct_coeffs_matrix.shape[0] // len(q_matrix)
    # block_size wybierany na podstawie macierzy jakości QUALITY
    after_quant_matrix = np.zeros_like(dct_coeffs_matrix, dtype=np.int16)
    quant_temp = quant_once(dct_coeffs_matrix, no_x_blocks, no_y_blocks, q_matrix, "d")
    after_quant_matrix = quant_once(quant_temp, no_x_blocks, no_y_blocks, q_matrix, "m")
    return after_quant_matrix


def choose_coeffs_magn(coeffs, cnt):
    """ Wybiera z danego bloku okresloną liczbę współczynników o największej amplitudzie. """
    abs_coeffs = np.abs(coeffs)  # obliczenie amplitudy (zwracana jest kopia tablicy)
    new_coeffs = np.zeros_like(coeffs)  # utworzenie tablicy wyjściowej - poczatkowo same zera
    for _ in range(cnt):
        # argmax zwraca liczbe, odpowiadajaca pozycji w tablicy flatten
        # unravel_index zwraca tuple ze wspolrzednymi w odniesieniu do tablicy 2d: 'abs_coeffs'
        mat_idx = np.unravel_index(np.argmax(abs_coeffs), abs_coeffs.shape)  # znalezienie indeksu majwiększej wartości
        new_coeffs[mat_idx] = coeffs[mat_idx]  # zapisanie współczynnika w tablicy wyjściowej
        abs_coeffs[mat_idx] = 0  # wyzerowanie w tablicy wejściowej - żeby można było znaleźć kolejny max
    return new_coeffs


def choose_coeffs_area(coeffs, rank):
    """
    Wybiera z danego bloku współczynniki niskoczęstotliwościowe - o rzędzie nie większym niż podany parametr.
    Rząd współczynnika to suma indeksów wiersza i kolumny, czyli:
       0  1  2  3  4  5  6  7
       1  2  3  4  5  6  7  8
       2  3  4  5  6  7  8  9
       3  4  5  6  7  8  9 10
       4  5  6  7  8  9 10 11
       5  6  7  8  9 10 10 12
       6  7  8  9 10 11 12 13
       7  8  9 10 11 12 13 14
    """
    new_coeffs = coeffs.copy()  # skopiowanie tablicy współczynników
    for r in range(coeffs.shape[0]):
        for c in range(coeffs.shape[1]):
            if (r+c) > rank:  # jeśli rząd za duży - wyzerowanie wartości
                new_coeffs[r, c] = 0
    return new_coeffs


def apply_chosen_coeffs(big_matrix, bl_size, param, mode):
    """ zastosowanie funkcji choose_coeefs_magn i area """
    """ param to parametr do wyboru wspolczynnikow amplitudowych lub niskoczestotliwosciowych """
    """ freq <0,14> """
    """ mag <1, 64> """
    """ mode to tryb;  "mag" to amplituda ;  "freq" to czestotliwosc """
    """ funkcja wybiera wspolczynniki z kazdego bloku w calej BIG_MATRIX """
    """ big_matrix to macierz o wymiarach obrazu ze wspolczynnikami """
    num_bl_x = big_matrix.shape[1] // bl_size
    num_bl_y = big_matrix.shape[0] // bl_size
    mtx_res = np.zeros_like(big_matrix)
    mtx_res = np.zeros_like(big_matrix)

    for blx in range(num_bl_x):
        for bly in range(num_bl_y):
            coeffs_bl = big_matrix[bly * bl_size:(bly + 1) * bl_size, blx * bl_size:(blx + 1) * bl_size]
            if mode == "mag":
                chosen_coeffs_bl = choose_coeffs_magn(coeffs_bl, param)
            else:
                chosen_coeffs_bl = choose_coeffs_area(coeffs_bl, param)
            mtx_res[bly*bl_size:(bly+1)*bl_size, blx*bl_size:(blx+1)*bl_size] = chosen_coeffs_bl
    return mtx_res


def modify_quant_matrix(matrix, coordinates, value):   # coordinates to TUPLE z dwoma intami
    """ funkcja do zmiany pol macierzy kwantyzacji  """
    y_idx, x_idx = int(coordinates[0]), int(coordinates[1])
    quant_matrix = matrix
    quant_matrix[y_idx, x_idx] = value
    return quant_matrix


if __name__ == "__main__":
    pass
