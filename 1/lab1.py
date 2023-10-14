import cmath

#   aₙ = λ₁·aₙ₋₁ + λ₂aₙ₋₂
#   trazit cemo λ₁ i λ₂ (sustav 2x2 Cramerovim pravilom)

n = int(input("Unesite nenegativan cijeli broj:"))
b_ovi = []
c_ovi = []

for i in range(3):
    b_ovi.append(float(input(f"Unesite vrijednost broja b_{i}:")))

for i in range(3):
    c_ovi.append(float(input(f"Unesite vrijednost broja c_{i}:")))

#   sad imamo sustav oblika
# 
#   b[2] = λ₁·b[1] + λ₂·b[0]
#   c[2] = λ₁·c[1] + λ₂·c[0]

D = b_ovi[1] * c_ovi[0] - b_ovi[0] * c_ovi[1]
Dx = b_ovi[2] * c_ovi[0] - c_ovi[2] * b_ovi[0]
Dy = b_ovi[1] * c_ovi[2] - b_ovi[2] * c_ovi[1]

lambda_1 = Dx / D
lambda_2 = Dy / D

#   sada imamo λ₁ i λ₂
#   imamo konkretnu dvokoracnu rekurziju

diskriminanta = pow(lambda_1, 2) + 4 * lambda_2
x1 = (lambda_1 + cmath.sqrt(diskriminanta)) / 2
x2 = (lambda_1 - cmath.sqrt(diskriminanta)) / 2

rezultat = 0

if (abs(x1 - x2) < 0.00001): 
    #   dvostruka nultocka, dakle rjesenje je μ₁·x₁ⁿ + μ₂·n·x₁ⁿ
    #   μ₁ = b[0] 
    #   μ₂ = (b[1] - μ₁·x₁) / x₁

    mi_1 = b_ovi[0]
    mi_2 = (b_ovi[1] - mi_1 * x1) / x1
    rezultat = mi_1 * pow(x1, n) + mi_2 * n * pow(x1, n)
else:
    #   rjesenje je oblika μ₁·x₁ⁿ + μ₂·x₂ⁿ
    #   rjesavamo sustav 2x2
    #   b[0] = μ₁ + μ₂ => μ₁ = μ₂ - b[0]
    #   b[1] = μ₁·x₁ + μ₂·x₂
    #   ...

    mi_2 = (b_ovi[1] - x1 * b_ovi[0]) / (x2 - x1)
    mi_1 = b_ovi[0] - mi_2
    
    if (mi_1.imag == 0 and mi_2.imag == 0 and x1.imag == 0 and x2.imag == 0):
        rezultat = mi_1.real * pow(x1.real, n) + mi_2.real * pow(x2.real, n)
    else:
        rezultat = mi_1 * pow(x1, n) + mi_2 * pow(x2, n)

print(f"Vrijednost broja b_n: {round(rezultat.real, 4)} + {round(rezultat.imag, 4)}i" if rezultat.imag > 0.00000001 else f"Vrijednost broja b_n: {round(rezultat.real, 4)}")