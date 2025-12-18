# 🔌 Socket Error Detection Simulator

**Bilgisayar Ağlarında Hata Tespit Yöntemlerini Simüle Eden Python Projesi**

Bu proje, ağ iletişiminde kullanılan çeşitli **hata tespit algoritmalarını** (Error Detection) simüle etmek amacıyla geliştirilmiştir. Proje, socket programlama kullanarak üç bileşen arasında veri iletimi gerçekleştirir ve veri bozulması durumunda hataların nasıl tespit edildiğini gösterir.

---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Mimari](#-mimari)
- [Desteklenen Algoritmalar](#-desteklenen-algoritmalar)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Proje Yapısı](#-proje-yapısı)

---

## 🎯 Proje Hakkında

Bu simülasyon, gerçek dünya ağ iletişimindeki hata tespit mekanizmalarını anlamak için tasarlanmıştır:

1. **Gönderici (Client 1)** → Veriyi seçilen hata tespit yöntemiyle kodlar ve gönderir
2. **Sunucu (Corruptor)** → Veriyi alır, rastgele bozar ve iletir
3. **Alıcı (Client 2)** → Veriyi alır, kontrol bitlerini hesaplar ve hata olup olmadığını tespit eder

---

## 🏗 Mimari

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   CLIENT 1      │         │     SERVER      │         │   CLIENT 2      │
│   (Sender)      │ ──────► │   (Corruptor)   │ ──────► │   (Receiver)    │
│   Port: 5000    │         │   In:5000       │         │   Port: 6000    │
│                 │         │   Out:6000      │         │                 │
│ • Veri girişi   │         │ • Rastgele      │         │ • Hata kontrolü │
│ • Algoritma     │         │   karakter      │         │ • Sonuç         │
│   seçimi        │         │   değiştirme    │         │   gösterimi     │
│ • Kontrol biti  │         │                 │         │                 │
│   hesaplama     │         │                 │         │                 │
└─────────────────┘         └─────────────────┘         └─────────────────┘
```

---

## 🔬 Desteklenen Algoritmalar

| #   | Algoritma             | Açıklama                                                                                   |
| --- | --------------------- | ------------------------------------------------------------------------------------------ |
| 1   | **Even Parity**       | Tek bitlik basit parite kontrolü. Veri bitlerindeki 1'lerin sayısını çift yapar.           |
| 2   | **2D Parity**         | İki boyutlu parite. Hem satır hem sütun bazında parite hesaplar, daha güçlü tespit sağlar. |
| 3   | **CRC-16 CCITT**      | Cyclic Redundancy Check. Polinom bölme tabanlı güçlü hata tespit algoritması.              |
| 4   | **Hamming Code**      | Hem hata tespiti hem de tek bit hata düzeltme yapabilen algoritma.                         |
| 5   | **Internet Checksum** | TCP/IP protokollerinde kullanılan 16-bit checksum algoritması.                             |

---

## ⚙ Kurulum

### Gereksinimler

- Python 3.6+

### Adımlar

```bash
# Repoyu klonlayın
git clone https://github.com/kullanici/SocketErrorDetection.git
cd SocketErrorDetection
```

> 📝 **Not:** Harici bir kütüphane gerektirmez. Sadece Python standart kütüphanesi kullanılmaktadır.

---

## 🚀 Kullanım

Üç ayrı terminal penceresi açın ve sırasıyla çalıştırın:

### 1. Alıcıyı Başlatın (Terminal 1)

```bash
python client2_receiver/client2_receiver.py
```

> Çıktı: `Client 2 waiting...`

### 2. Sunucuyu Başlatın (Terminal 2)

```bash
python server_corruptor/server_corruptor.py
```

> Çıktı: `Server waiting...`

### 3. Göndericiyi Çalıştırın (Terminal 3)

```bash
python client1_sender/client1_sender.py
```

### Örnek Çalışma

**Gönderici (Client 1):**

```
1 - Even Parity
2 - 2D Parity
3 - CRC16
4 - Hamming Code
5 - Internet Checksum

Choose method: 3
Enter text: Hello
Sent Packet: Hello|CRC16|9D13
```

**Sunucu:**

```
Server waiting...
Forwarded: HXllo|CRC16|9D13
```

**Alıcı (Client 2):**

```
Client 2 waiting...
Received Data      : HXllo
Method             : CRC16
Sent Check Bits    : 9D13
Computed Check Bits: 45A2
Status             : DATA CORRUPTED
```

---

## 📁 Proje Yapısı

```
SocketErrorDetection/
│
├── client1_sender/
│   └── client1_sender.py      # Veri gönderici istemci
│
├── client2_receiver/
│   └── client2_receiver.py    # Veri alıcı istemci
│
├── server_corruptor/
│   └── server_corruptor.py    # Veri bozucu sunucu
│
├── common/                    # Ortak modüller
│   ├── __init__.py
│   ├── parity.py              # Even Parity algoritması
│   ├── parity2d.py            # 2D Parity algoritması
│   ├── crc.py                 # CRC-16 CCITT algoritması
│   ├── hamming.py             # Hamming Code algoritması
│   └── checksum.py            # Internet Checksum algoritması
│
└── README.md
```

---

## 📚 Algoritma Detayları

### Even Parity

```python
# Tüm bitlerdeki 1'lerin sayısı çift olacak şekilde parite biti eklenir
ones = sum(bin(b).count("1") for b in data)
parity_bit = ones % 2
```

### CRC-16 CCITT

```python
# Polinom: 0x1021
# Başlangıç değeri: 0xFFFF
# XOR ve shift işlemleriyle 16-bit kontrol değeri üretilir
```

### Internet Checksum

```python
# 16-bit kelimeler toplanır
# Taşmalar eklenir (one's complement)
# Sonuç tersine çevrilir
```

---

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Commit yapın (`git commit -m 'Yeni özellik eklendi'`)
4. Push yapın (`git push origin feature/yeniOzellik`)
5. Pull Request açın

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

## 👨‍💻 Geliştirici

Bilgisayar Ağları dersi projesi kapsamında geliştirilmiştir.

---

<p align="center">
  <i>⭐ Bu proje faydalı olduysa yıldız vermeyi unutmayın!</i>
</p>
