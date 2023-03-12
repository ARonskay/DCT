import cv2
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


def test_dct_quantize(q_mat):
    """ Sprawdzenie poprawności obliczania DCT/IDCT. """
    img = cv2.imread("lena_mono.png", cv2.IMREAD_UNCHANGED)
    dct_coeffs = dct_image(img, 8)
    result_of_quant = quantize_full(dct_coeffs, q_mat)
    img_rec = idct_image(result_of_quant, 8)
    cv2.imshow("Poczatkowy", img)
    cv2.imshow("Wynikowy", img_rec)
    psnr_val = cp.calc_psnr(img, img_rec)
    mse_val = cp.calc_mse(img, img_rec)
    ssim_val = cp.calc_ssim(img, img_rec)
    print(f"Macierz: {q_mat}   SSIM: {ssim_val}  PSNR: {psnr_val}  MSE: {mse_val}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_coeffs_choice(q_mat, param, mode):
    """ Sprawdzenie poprawności wyboru wspolczynnikow """
    img = cv2.imread("lena_mono.png", cv2.IMREAD_UNCHANGED)
    # img = cv2.imread("lena_grey_scaled.png", cv2.IMREAD_GRAYSCALE) # bo to niestety obraz 3-skladowy
    dct_coeffs = dct_image(img, 8)
    result_of_quant = quantize_full(dct_coeffs, q_mat)
    result_of_choice = apply_chosen_coeffs(result_of_quant, 8, param, mode)
    img_rec = idct_image(result_of_choice, 8)
    cv2.imshow("Poczatkowy", img)
    # cv2.imshow("Po DCT", dct_coeffs)
    # cv2.imshow("Po kwantyzacji", result_of_quant)
    # cv2.imshow("Po wyborze", result_of_choice)
    cv2.imshow("Wynikowy", img_rec)
    psnr_val = cp.calc_psnr(img, img_rec)
    mse_val = cp.calc_mse(img, img_rec)
    ssim_val = cp.calc_ssim(img, img_rec)
    print(f"Macierz: {q_mat}  Wspolczynniki: {param}  Tryb: {mode}   SSIM: {ssim_val}"
          f"  PSNR: {psnr_val}  MSE: {mse_val}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_change_modify_matrix():
    """ test najwazniejszy """
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
    print("\n\n\Końcowy wyglad")
    print(quantize_matrix)
    print('-----THE END-----')


if __name__ == "__main__":
    # test_dct_quantize('q10')
    test_coeffs_choice("q1", 0, "freq")
    """ q_mat, param, mode """
    """ freq <0,14> lub mag <1, 64> """
    test_coeffs_choice("q1", 1, "mag")
    test_change_modify_matrix()
