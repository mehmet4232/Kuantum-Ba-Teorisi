import numpy as np
import matplotlib.pyplot as plt

# Başlangıç yoğunluk matrisi (süperpozisyon durumu)
rho_0 = np.array([[0.5, 0.5],
                  [0.5, 0.5]], dtype=complex)

# Hedef yoğunluk matrisi (klasik durum: |0⟩⟨0|)
rho_target = np.array([[1.0, 0.0],
                       [0.0, 0.0]], dtype=complex)

# Simülasyon parametreleri
dt = 0.01      # zaman adımı
T = 5          # toplam süre
steps = int(T / dt)

# Kullanılacak gamma (bağ kuvveti) değerleri
gamma_values = [0.1, 1, 5, 10]

# Zaman aralığı
time = np.linspace(0, T, steps)

# Mesafe ölçüm fonksiyonu (Frobenius normu)
def distance(rho, rho_target):
    return np.linalg.norm(rho - rho_target)

# Simülasyon
plt.figure(figsize=(10, 6))

for gamma in gamma_values:
    rho = rho_0.copy()
    distances = []

    for _ in range(steps):
        # Bağ kuvveti etkisi: dρ/dt = -γ(ρ - ρ_target)
        drho_dt = -gamma * (rho - rho_target)
        rho += drho_dt * dt

        # Mesafeyi ölç
        distances.append(distance(rho, rho_target))

    plt.plot(time, distances, label=f"γ = {gamma}")

# Grafik ayarları
plt.title("Süperpozisyondan Klasik Duruma Geçiş (Bağ Kuvvetine Göre)")
plt.xlabel("Zaman")
plt.ylabel("ρ(t) ile ρ_target Arasındaki Mesafe")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
