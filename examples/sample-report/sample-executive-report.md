> **Catatan**: Dokumen ini adalah contoh format laporan akhir (*sample*) untuk menilai tata letak, tipografi, tabel, dan grafik PDF. Angka di bawah berasal dari simulasi `financial-modeler/scripts/example_inputs.json` dan skenario ilustratif, bukan riset pasar nyata.

## 1. Ringkasan Eksekutif

**Rekomendasi**: Lanjutkan ke fase uji pasar terbatas (30 hari) dengan syarat modal awal dinaikkan menjadi minimal IDR 35.000.000 atau biaya tetap bulanan ditekan di bawah IDR 3.500.000 agar skenario pesimis tetap memiliki *cash buffer*.

| Aspek | Ringkasan | Status Bukti |
|---|---|---|
| Masalah | Konsumen membutuhkan produk dengan harga transparan dan pemesanan ulang yang cepat | [Contoh] |
| Solusi | Penjualan langsung dengan sistem langganan/repeat order bulanan | [Contoh] |
| Harga & Margin | Harga jual IDR 150.000/unit, biaya variabel IDR 60.000/unit (margin kotor 60%) | [Estimate] |
| Ekonomi Unit | LTV IDR 180.000, CAC IDR 25.000, rasio LTV/CAC 7,2x | [Estimate] |
| Titik Impas | Bulan ke-5 pada skenario dasar; tidak tercapai dalam 12 bulan pada skenario pesimis | [Estimate] |
| Keputusan | Go dengan syarat (Skor: 3,7 / 5,0) | [Contoh] |

## 2. Skor Keputusan (Go / No-Go Scorecard)

Penilaian menggunakan bobot standar untuk menguji kelayakan sebelum eksekusi penuh.

| Kriteria | Bobot | Skor (1-5) | Nilai Terbobot | Dasar Penilaian |
|---|---|---|---|---|
| Permintaan Pasar | 20% | 4 | 0,80 | Sinyal permintaan stabil pada segmen target |
| Kualitas Bukti | 15% | 3 | 0,45 | Sebagian asumsi biaya akuisisi belum diuji lapangan |
| Ekonomi Unit | 20% | 4 | 0,80 | Margin kotor 60% dan LTV/CAC di atas ambang sehat (3x) |
| Kelayakan Eksekusi | 15% | 4 | 0,60 | Operasional dapat dijalankan tim kecil pada tahap awal |
| Keunggulan Kompetitif | 10% | 3 | 0,30 | Diferensiasi masih bergantung pada eksekusi layanan |
| Risiko & Kepatuhan | 10% | 4 | 0,40 | Perizinan dasar dan kewajiban pajak UMKM terpetakan |
| Kesiapan Tim | 10% | 4 | 0,40 | Kapasitas tim mencukupi untuk target 90 hari pertama |
| **Total Skor** | **100%** | | **3,75 / 5,0** | **Go dengan syarat** |

## 3. Proyeksi Keuangan (12 Bulan)

Data dihitung menggunakan skrip model keuangan dengan modal awal IDR 30.000.000, biaya tetap IDR 5.000.000/bulan, pertumbuhan dasar 10%/bulan, dan rasio pembelian ulang 2,0x.

| Skenario | Unit Bulan 1 | Break-Even | Kas Terendah (IDR) | Kas Bulan 12 (IDR) | Status Kas |
|---|---|---|---|---|---|
| Pesimis | 36 | Belum tercapai | -2.192.023 | -2.192.023 | Defisit di bulan ke-11 |
| Dasar | 60 | Bulan ke-5 | 26.404.000 | 45.280.172 | Aman |
| Optimis | 84 | Bulan ke-1 | 30.562.400 | 141.787.020 | Aman |

<svg viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Grafik Proyeksi Kas 12 Bulan">
  <rect x="0" y="0" width="640" height="240" fill="#FFFFFF"/>
  <text x="16" y="22" font-family="-apple-system, Helvetica Neue, Arial, sans-serif" font-size="12" font-weight="700" fill="#111317">Proyeksi Saldo Kas 12 Bulan per Skenario (dalam Juta IDR)</text>
  <line x1="56" y1="40" x2="56" y2="195" stroke="#B8C0CC" stroke-width="1"/>
  <line x1="56" y1="168" x2="610" y2="168" stroke="#9CA3AF" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="56" y1="195" x2="610" y2="195" stroke="#B8C0CC" stroke-width="1"/>
  <text x="48" y="48" text-anchor="end" font-size="9" fill="#525866">150</text>
  <text x="48" y="88" text-anchor="end" font-size="9" fill="#525866">100</text>
  <text x="48" y="128" text-anchor="end" font-size="9" fill="#525866">50</text>
  <text x="48" y="171" text-anchor="end" font-size="9" fill="#525866">0</text>
  <text x="48" y="198" text-anchor="end" font-size="9" fill="#525866">-20</text>
  <!-- Optimistic: 30.6M -> 141.8M -->
  <polyline fill="none" stroke="#1B365D" stroke-width="2.2" points="66,143 115,141 164,138 213,134 262,129 311,122 360,114 409,104 458,92 507,78 556,62 605,54"/>
  <!-- Base: 28.9M -> 45.3M -->
  <polyline fill="none" stroke="#4B6A9B" stroke-width="2" points="66,145 115,145 164,146 213,147 262,147 311,146 360,145 409,143 458,140 507,137 556,134 605,132"/>
  <!-- Pessimistic: 26.6M -> -2.2M -->
  <polyline fill="none" stroke="#B91C1C" stroke-width="2" stroke-dasharray="5,3" points="66,147 115,149 164,152 213,154 262,157 311,159 360,161 409,163 458,165 507,167 556,169 605,170"/>
  <text x="66" y="210" font-size="9" fill="#525866">Bln 1</text>
  <text x="311" y="210" font-size="9" fill="#525866">Bln 6</text>
  <text x="585" y="210" font-size="9" fill="#525866">Bln 12</text>
  <line x1="66" y1="226" x2="86" y2="226" stroke="#1B365D" stroke-width="2.2"/>
  <text x="92" y="229" font-size="9" fill="#1A1D21">Optimis</text>
  <line x1="160" y1="226" x2="180" y2="226" stroke="#4B6A9B" stroke-width="2"/>
  <text x="186" y="229" font-size="9" fill="#1A1D21">Dasar</text>
  <line x1="245" y1="226" x2="265" y2="226" stroke="#B91C1C" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="271" y="229" font-size="9" fill="#1A1D21">Pesimis (defisit di Bln 11)</text>
</svg>

### Uji Sensitivitas Harga (Skenario Dasar, Kas Bulan ke-12)

| Perubahan Harga | Kas Bulan 12 (IDR) | Dampak |
|---|---|---|
| -20% | 17.854.172 | Margin menipis, perlu volume lebih tinggi |
| -10% | 31.567.172 | Masih positif namun cadangan kas ketat |
| 0% (Dasar) | 45.280.172 | Titik acuan |
| +10% | 58.993.172 | Cadangan kas naik 30% |
| +20% | 72.706.172 | Tertinggi, perlu uji elastisitas ke pelanggan |

## 4. Risiko Utama & Rencana 30 Hari Pertama

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Volume penjualan di bawah skenario dasar | Kas habis di bulan ke-11 | Terapkan sistem pre-order sebelum produksi massal |
| Biaya akuisisi pelanggan (CAC) lebih tinggi dari IDR 25.000 | Rasio LTV/CAC turun | Fokus pada kanal organik dan rujukan pelanggan awal |
| Asumsi repeat order 2,0x tidak tercapai | Pendapatan berulang meleset | Lakukan wawancara 10 pembeli pertama di minggu ke-3 |

### Langkah Konkret 30 Hari Pertama

- [ ] Minggu 1: Wawancara 10 calon pelanggan untuk menguji asumsi harga IDR 150.000.
- [ ] Minggu 2: Uji penjualan batch kecil (20 unit) untuk mengukur CAC aktual.
- [ ] Minggu 3: Evaluasi margin bersih dan perbarui `inputs.json` dengan data nyata.
- [ ] Minggu 4: Keputusan lanjut ke skala penuh atau penyesuaian harga.
