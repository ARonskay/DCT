import cv2
import time
from main import dct_image, idct_image, quantize_full, apply_chosen_coeffs, modify_quant_matrix,\
    select_q_matrix
import calc_params as cp


def test_dct_calc():
    """ Sprawdzenie poprawności obliczania DCT/IDCT. """
    img = cv2.imread("lena_mono.png", cv2.IMREAD_UNCHANGED)
    dct_coeffs = dct_image(img, 8)
    img_rec = idct_image(dct_coeffs, 8)
    print(img_rec)
    cv2.imshow("Oryginalny", img)
    cv2.imshow("Wynikowy", img_rec)
    # cv2.imwrite("test.png", img_rec)
    psnr_val = cp.calc_psnr(img, img_rec)
    mse_val = cp.calc_mse(img, img_rec)
    ssim_val = cp.calc_ssim(img, img_rec)
    print(f"SSIM: {ssim_val}  PSNR: {psnr_val}  MSE: {mse_val}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f"{(img == img_rec).all()}")


def test_dct_quantize(q_mat, path_in, *args):
    """ Sprawdzenie poprawności obliczania DCT/IDCT. """
    img = cv2.imread(path_in, cv2.IMREAD_GRAYSCALE)
    dct_coeffs = dct_image(img, 8)
    if q_mat == "q1":
        result_of_quant = dct_coeffs
    else:
        result_of_quant = quantize_full(dct_coeffs, q_mat)
    img_rec = idct_image(result_of_quant, 8)
    cv2.imshow("Poczatkowy", img)
    cv2.imshow("Wynikowy", img_rec)
    if args:
        cv2.imwrite(args[0], img_rec)
    psnr_val = cp.calc_psnr(img, img_rec)
    mse_val = cp.calc_mse(img, img_rec)
    ssim_val = cp.calc_ssim(img, img_rec)
    print(f"Macierz: {q_mat}   SSIM: {ssim_val}  PSNR: {psnr_val}  MSE: {mse_val}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_coeffs_choice(q_mat, param, mode, path_in, *args):
    """ Sprawdzenie poprawności wyboru wspolczynnikow """
    img = cv2.imread(path_in, cv2.IMREAD_UNCHANGED)
    # img = cv2.imread("lena_grey_scaled.png", cv2.IMREAD_GRAYSCALE) # bo to niestety obraz 3-skladowy
    dct_coeffs = dct_image(img, 8)
    if q_mat == "q1":
        result_of_quant = dct_coeffs
    else:
        result_of_quant = quantize_full(dct_coeffs, q_mat)
    result_of_choice = apply_chosen_coeffs(result_of_quant, 8, param, mode)
    img_rec = idct_image(result_of_choice, 8)
    cv2.imshow("Poczatkowy", img)
    # cv2.imshow("Po DCT", dct_coeffs)
    # cv2.imshow("Po kwantyzacji", result_of_quant)
    # cv2.imshow("Po wyborze", result_of_choice)
    cv2.imshow("Wynikowy", img_rec)
    if args:
        cv2.imwrite(args[0], img_rec)
    psnr_val = cp.calc_psnr(img, img_rec)
    mse_val = cp.calc_mse(img, img_rec)
    ssim_val = cp.calc_ssim(img, img_rec)
    print(f"Parametr: {param:2d}  SSIM: {ssim_val}  PSNR: {psnr_val}  MSE: {mse_val}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_change_modify_matrix():
    """ test zmiany macierzy i wspolczynnika """
    go_iterate = True
    q_mat_short = input("Wybierz macierz: ")
    quantize_matrix = select_q_matrix(q_mat_short)
    print(f"Twoja macierz:\n{quantize_matrix}")
    while go_iterate:
        choice = input("Czy chcesz zmienić macierz? y/n ")
        if choice == "n":
            idx_str = input("Podaj wspolrzedne: ")
            idx_list = idx_str.split()
            y_idx, x_idx = int(idx_list[0]), int(idx_list[1])
            print(f"Y: {y_idx} X: {x_idx}")
            val = int(input("Jaka wartosc ma przyjac to pole? "))
            mati = modify_quant_matrix(quantize_matrix, (y_idx, x_idx), val)
            print(f"Zmodyfikowana tablica: \n{mati}")
        else:
            q_mat_short = input("Wybierz macierz: ")
            quantize_matrix = select_q_matrix(q_mat_short)
            print(f"Twoja macierz:\n{quantize_matrix}")
        go_next = input("Modyfikuj dalej? y/n ")
        if go_next == "n":
            go_iterate = False
    print("\n\nKońcowy wyglad")
    print(quantize_matrix)
    print('-----THE END-----')


if __name__ == "__main__":
    start_wall_time = time.time()
    start_cpu_time = time.process_time()

    path_input ="test.PNG"
   # path_input = "szach_mono.jgpg"
    q_mat = "qX"

    ############################################################################
    # path_output_quant = ".\\wyniki_zwykle\\quant.jpg"
    test_dct_quantize(q_mat, path_input)
    ############################################################################

    ############################################################################
    """ mag <1, 64> """
    # for param_m in range(1, 65):
    # param_m = 64
    # path_output_mag = f"TEST{param_m}.jpg"
    # test_coeffs_choice(q_mat, param_m, "mag", path_input, path_output_mag)
    ############################################################################

    ############################################################################
    """ freq <0,14> """
    # for param_f in range(15):
    # # param_f = 14
    # # path_output_freq = f"image.jpg"
    #     test_coeffs_choice(q_mat, param_f, "freq", path_input)
    ############################################################################
    test_dct_quantize(q_mat,path_input)
    # test_change_modify_matrix()

    end_cpu_time = time.process_time()
    end_wall_time = time.time()
    elapsed_wall_time = end_wall_time - start_wall_time
    elapsed_cpu_time = end_cpu_time - start_cpu_time
    print("\n")
    print('Execution Wall time:', elapsed_wall_time, 'seconds')
    print('Execution CPU time:', elapsed_cpu_time, 'seconds')
