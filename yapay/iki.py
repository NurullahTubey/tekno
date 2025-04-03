import numpy as np
import matplotlib.pyplot as plt

# Hiperparametreler
HIPERPARAMETRELER = {
    "boyut": 5,
    "baslangic": (3, 0),
    "bitis": (4, 4),
    "engeller": [(1, 1), (2, 2), (3, 3), (4, 3)],
    "ogrenme_orani": 0.8,
    "indirim_orani": 0.95,
    "epsilon": 1.0,
    "epsilon_azaltma": 0.001,
    "bolum_sayisi": 10,
    "varis_sayisi_siniri": 3,
    "animasyon_duraklama_suresi": 0.1,
}

# Eylemler (yukarı, aşağı, sol, sağ)
EYLEMLER = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def gecerli_konum(konum, boyut, engeller):
    """Verilen konumun labirent içinde geçerli olup olmadığını kontrol eder."""
    return 0 <= konum[0] < boyut and 0 <= konum[1] < boyut and konum not in engeller

def en_kisa_yol(q_tablosu, baslangic, bitis, boyut, engeller):
    """Öğrenilmiş Q-tablosunu kullanarak başlangıçtan bitişe en kısa yolu bulur."""
    konum = baslangic
    yol = [konum]
    while konum != bitis:
        eylem_indeksi = np.argmax(q_tablosu[konum[0], konum[1]])
        yeni_konum = (konum[0] + EYLEMLER[eylem_indeksi][0], konum[1] + EYLEMLER[eylem_indeksi][1])
        if not gecerli_konum(yeni_konum, boyut, engeller):
            break
        konum = yeni_konum
        yol.append(konum)
    return yol

def q_ogrenme_simulasyonu(hiperparametreler):
    """Q-öğrenme simülasyonunu çalıştırır ve sonuçları görselleştirir."""
    boyut = hiperparametreler["boyut"]
    baslangic = hiperparametreler["baslangic"]
    bitis = hiperparametreler["bitis"]
    engeller = hiperparametreler["engeller"]
    ogrenme_orani = hiperparametreler["ogrenme_orani"]
    indirim_orani = hiperparametreler["indirim_orani"]
    epsilon = hiperparametreler["epsilon"]
    epsilon_azaltma = hiperparametreler["epsilon_azaltma"]
    bolum_sayisi = hiperparametreler["bolum_sayisi"]
    varis_sayisi_siniri = hiperparametreler["varis_sayisi_siniri"]
    animasyon_duraklama_suresi = hiperparametreler["animasyon_duraklama_suresi"]

    q_tablosu = np.zeros((boyut, boyut, 4))
    odul_matrisi = np.zeros((boyut, boyut))
    odul_matrisi[bitis] = 100

    plt.figure(figsize=(6, 6))
    yol_genel = []
    varis_gerceklesti = False
    varis_sayisi = 0

    for _ in range(bolum_sayisi):
        konum = baslangic
        yol = [konum]
        while konum != bitis:
            if np.random.rand() < epsilon:
                eylem_indeksi = np.random.randint(4)
            else:
                eylem_indeksi = np.argmax(q_tablosu[konum[0], konum[1]])
            yeni_konum = (konum[0] + EYLEMLER[eylem_indeksi][0], konum[1] + EYLEMLER[eylem_indeksi][1])
            if not gecerli_konum(yeni_konum, boyut, engeller):
                continue
            odul = odul_matrisi[yeni_konum]
            q_tablosu[konum[0], konum[1], eylem_indeksi] = (
                (1 - ogrenme_orani) * q_tablosu[konum[0], konum[1], eylem_indeksi]
                + ogrenme_orani * (odul + indirim_orani * np.max(q_tablosu[yeni_konum[0], yeni_konum[1]]))
            )
            konum = yeni_konum
            yol.append(konum)
            yol_genel.append(konum)

            # Görselleştirme
            plt.clf()
            plt.xticks(np.arange(boyut + 1))
            plt.yticks(np.arange(boyut + 1))
            plt.grid(True)
            for i in range(boyut):
                for j in range(boyut):
                    plt.text(j + 0.5, boyut - 1 - i + 0.5, f"{np.max(q_tablosu[i, j]):.2f}",
                             ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
                    if (i, j) == baslangic:
                        plt.gca().add_patch(plt.Rectangle((j, boyut - 1 - i), 1, 1, facecolor='blue', alpha=0.3))
                    elif (i, j) == bitis:
                        plt.gca().add_patch(plt.Rectangle((j, boyut - 1 - i), 1, 1, facecolor='red', alpha=0.3))
                    elif (i, j) in engeller:
                        plt.gca().add_patch(plt.Rectangle((j, boyut - 1 - i), 1, 1, facecolor='black', alpha=0.5))
                    elif (i, j) in yol_genel:
                        plt.gca().add_patch(plt.Rectangle((j, boyut - 1 - i), 1, 1, facecolor='green', alpha=0.5))
            plt.gca().add_patch(plt.Rectangle((konum[1], boyut - 1 - konum[0]), 1, 1, facecolor='orange', alpha=0.8))
            plt.pause(animasyon_duraklama_suresi)

        if konum == bitis and not varis_gerceklesti:
            varis_gerceklesti = True
            varis_sayisi += 1
            yol_genel = []

        if varis_sayisi == varis_sayisi_siniri:
            break

        epsilon = max(0.1, epsilon - epsilon_azaltma)
        ogrenme_orani = max(0.1, ogrenme_orani - 0.001)

    # En kısa yolun gösterilmesi
    en_kisa_yol_listesi = en_kisa_yol(q_tablosu, baslangic, bitis, boyut, engeller)

    # Yeni görsel oluşturma
    plt.figure(figsize=(6, 6))
    plt.xticks(np.arange(boyut + 1))
    plt.yticks(np.arange(boyut + 1))
    plt.grid(True)
    for i in range(boyut):
        for j in range(boyut):
            plt.text(j + 0.5, boyut - 1 - i + 0.5, f"{np.max(q_tablosu[i, j]):.2f}",
                     ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
            if (i, j) == baslangic:
                plt.gca().add_patch(plt.Rectangle((j, boyut - 1 - i), 1, 1, facecolor='blue', alpha=0.3))
            elif (i, j) == bitis:
                plt.gca().add_patch(plt.Rectangle((j, boyut - 1 - i), 1, 1, facecolor='red', alpha=0.3))
            elif (i, j) in engeller:
                plt.gca().add_patch(plt.Rectangle((j, boyut - 1 - i), 1, 1, facecolor='black', alpha=0.5))
    for konum in en_kisa_yol_listesi:
        plt.gca().add_patch(plt.Rectangle((konum[1], boyut - 1 - konum[0]), 1, 1, facecolor='green', alpha=0.7))
    plt.show()

q_ogrenme_simulasyonu(HIPERPARAMETRELER)