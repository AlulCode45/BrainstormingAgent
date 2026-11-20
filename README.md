# BrainstormingAgent

Workspace terstruktur untuk **Brainstorming Partner & Strategic Analysis Agent** berbasis Antigravity Customizations (`AGENTS.md` + `.agents/skills/`). Dirancang untuk membantu eksplorasi ide, validasi bisnis, penyusunan PRP (*Project Requirements & Plan*), riset pasar, pemodelan keuangan, hingga laporan eksekutif siap cetak (PDF).

---

## Fitur Utama

- **Alur Bertahap dengan Checkpoint**: Analisis berjalan langkah demi langkah; agent merangkum hasil dan meminta persetujuan sebelum lanjut ke tahap berikutnya.
- **Standar Bukti & Asumsi**: Setiap klaim dan angka dilabeli (`Verified`, `Estimate`, `Assumption`, `Unverified`), sumber diberi skor (`A`/`B`/`C`), dan asumsi dicatat di `13-assumption-register.md`.
- **Model Keuangan Terhitung**: Proyeksi 3 skenario (pesimis, dasar, optimis), titik impas (*break-even*), *cash runway*, LTV/CAC, dan sensitivitas harga dihitung lewat skrip Python, bukan tebakan narasi.
- **Riset Pasar & Kompetitor**: Mendukung riset web/browser langsung dengan sitasi URL, matriks fitur-harga, *review mining*, dan kerangka ERRC (*Blue Ocean*).
- **Red-Team & Scorecard Keputusan**: Uji ketahanan ide (*pre-mortem*) dan penilaian Go/No-Go berbobot yang dicatat sebagai ADR (*Architecture/Decision Record*).
- **Export PDF Editorial**: Laporan akhir maupun satu folder PRP lengkap dapat diekspor ke PDF berukuran A4 dengan tipografi rapi, tabel terformat, grafik SVG, dan tanpa *AI slop*.

---

## Prasyarat & Cara Mulai (Quick Start)

### Prasyarat
- **Antigravity** (otomatis membaca `AGENTS.md` dan seluruh skill di `.agents/skills/`).
- **Python 3** (untuk skrip `financial-modeler` dan `export_pdf.py`; tidak memerlukan paket `pip` tambahan).
- **Brave Browser / Google Chrome / Chromium** terpasang di sistem (digunakan oleh `export_pdf.py` dalam mode headless untuk merender PDF).

### Langkah Awal
1. Clone repository ini:
   ```bash
   git clone https://github.com/AlulCode45/BrainstormingAgent.git
   cd BrainstormingAgent
   ```
2. Buka folder `BrainstormingAgent` sebagai workspace di Antigravity.
3. Mulai sesi dengan menceritakan ide, tugas, atau masalah yang ingin dibahas, misalnya:
   - *"Aku mau brainstorm ide SaaS untuk manajemen bengkel..."*
   - *"Bantu validasi ide bisnis ini dan cek kompetitornya."*
   - *"Buatkan PRP lengkap dan arsitektur untuk project aplikasi ini."*
   - *"Hitung proyeksi keuangan 12 bulan dan cek titik impasnya."*
   - *"Export hasil analisa project ini ke PDF."*

---

## Alur Kerja Analisis (Staged Pipeline)

Untuk pembahasan project atau bisnis secara menyeluruh, agent mengikuti alur bertahap berikut dan berhenti di setiap checkpoint untuk konfirmasi:

```text
Ide Mentah
  └─> PRP (00–06)
        └─> Riset Pasar (07)
              └─> Analisa Kompetitor (15)
                    └─> Customer Discovery (14)
                          └─> SWOT (08) -> Peluang (09) -> Manajemen (10)
                                └─> Keuangan Terhitung (11)
                                      └─> Kepatuhan & Legal (16) -> GTM & Risiko (12)
                                            └─> Audit Bukti (13) -> Scorecard Go/No-Go (17)
                                                  └─> Executive Summary (18) & Export PDF
```

---

## Daftar Skill (`.agents/skills/`)

| Skill | Fungsi Utama | Output Utama |
|---|---|---|
| `ideation-facilitator` | Eksplorasi ide (*First Principles*, *SCAMPER*, *How Might We*, *3-Horizon*) | Opsi & arah ide |
| `business-validator` | Validasi cepat (*Lean Canvas*, ICP, monetisasi, eksperimen 48 jam–2 minggu) | Ringkasan validasi |
| `project-scoper` | Pemecahan ide menjadi MVP (*MoSCoW*), arsitektur ringkas, dan *task breakdown* | Scope MVP & tugas |
| `prp-writer` | Penyusunan PRP detail per folder lengkap dengan diagram Mermaid & aset visual | `prps/<project>/00`–`06` |
| `market-researcher` | Riset ukuran pasar (TAM/SAM/SOM), tren, segmen, dan patokan harga via web/browser | `07-market-research.md` |
| `strategy-analyst` | Analisis bertahap: SWOT/TOWS, PESTEL & Five Forces, manajemen, keuangan, GTM | `08`–`12` |
| `evidence-auditor` | Audit sumber (`A`/`B`/`C`), pemisahan fakta vs asumsi, penanda data kedaluwarsa | `13-assumption-register.md` |
| `customer-discovery` | Panduan wawancara, desain survei, *Jobs-to-be-Done*, dan sintesis catatan | `14-customer-discovery.md` |
| `competitor-analyst` | Matriks kompetitor, *review mining*, peta posisi, dan ERRC (*Blue Ocean*) | `15-competitor-analysis.md` |
| `compliance-checker` | Daftar perizinan (OSS/NIB, BPOM, halal, HKI), pajak, UU PDP, dan rantai pasok | `16-compliance-and-legal.md` |
| `financial-modeler` | Perhitungan 3 skenario, *break-even*, *runway*, LTV/CAC, dan sensitivitas harga | `model/inputs.json` & `11` |
| `decision-scorecard` | Red-team otomatis, scorecard Go/No-Go berbobot, perbandingan ide, dan log ADR | `17-scorecard-and-decision.md` |
| `executive-reporter` | Ringkasan eksekutif 1 halaman, grafik konsisten, *pitch outline*, dan export PDF | `18-executive-summary.md` & PDF |
| `devils-advocate` | Uji ketahanan ide (*pre-mortem*, identifikasi asumsi rapuh, mitigasi risiko) | Kritik & mitigasi |
| `idea-logger` | Pengarsipan catatan brainstorming ke folder topik masing-masing | `ideas/<topic-slug>/` |

---

## Struktur Direktori

```text
BrainstormingAgent/
├── AGENTS.md                           # Aturan utama, quality gates, & aturan git
├── README.md                           # Dokumentasi project
├── LICENSE                             # Lisensi repository
├── .gitignore
├── .agents/
│   └── skills/                         # 15 skill modular (masing-masing berisi SKILL.md)
├── templates/                          # Template baku dokumen
│   ├── assumption-register.md
│   ├── changelog.md
│   ├── decision-log-adr.md
│   ├── executive-summary.md
│   └── scorecard.md
├── examples/
│   └── sample-report/                  # Contoh laporan Markdown & hasil export PDF
├── ideas/                              # Catatan brainstorming (wajib dikelompokkan per folder topik)
│   └── <topic-slug>/
│       ├── YYYY-MM-DD-<catatan>.md
│       └── assets/
└── prps/                               # Dokumen PRP & analisa lengkap per project
    ├── INDEX.md                        # Daftar portofolio & status semua project
    └── <project-slug>/
        ├── README.md                   # Indeks navigasi project
        ├── CHANGELOG.md                # Riwayat perubahan versi
        ├── 00-overview.md ... 18-executive-summary.md
        ├── decisions/                  # ADR-NNN-<slug>.md
        ├── model/                      # inputs.json untuk skrip model keuangan
        └── assets/                     # Grafik, ilustrasi, & laporan PDF
```

---

## Menjalankan Skrip Secara Langsung

### 1. Model Keuangan (`financial-modeler`)
Jalankan simulasi skenario dari file `inputs.json`:
```bash
python3 .agents/skills/financial-modeler/scripts/model.py .agents/skills/financial-modeler/scripts/example_inputs.json
```

### 2. Export Laporan ke PDF (`executive-reporter`)
Export satu file Markdown:
```bash
python3 .agents/skills/executive-reporter/scripts/export_pdf.py \
  --input examples/sample-report/sample-executive-report.md \
  --output examples/sample-report/sample-executive-report.pdf \
  --title "Contoh Laporan Analisa Bisnis (Sample)"
```
Atau gabungkan seluruh folder PRP menjadi satu laporan PDF lengkap:
```bash
python3 .agents/skills/executive-reporter/scripts/export_pdf.py \
  --project prps/<project-slug> \
  --output prps/<project-slug>/assets/<project-slug>-report.pdf \
  --title "Nama Project"
```
Lihat contoh hasilnya di [examples/sample-report/sample-executive-report.pdf](examples/sample-report/sample-executive-report.pdf).

---

## Pengembangan & Kontribusi

Siapa pun dapat menyesuaikan atau memperluas workspace ini:

1. **Menambah Skill Baru**:
   - Buat folder `.agents/skills/<nama-skill>/SKILL.md` dengan YAML frontmatter (`name` huruf kecil bertanda hubung, dan `description` yang menjelaskan kapan skill dipanggil).
   - Daftarkan routing-nya di `AGENTS.md` bagian *Skill Routing* dan perbarui tabel di `README.md`.
2. **Menyesuaikan Template**:
   - Edit file di folder `templates/` untuk mengubah struktur *Assumption Register*, *Scorecard*, *ADR*, *Executive Summary*, atau *Changelog*.
3. **Memakai Secara Global (Lintas Project)**:
   - Salin isi `.agents/skills/` ke `~/.gemini/config/skills/` jika ingin skill ini tersedia di seluruh workspace Antigravity pada mesin Anda.
4. **Konvensi Git**:
   - Branch utama adalah `main`. Gunakan pesan commit yang jelas (misalnya `feat:`, `fix:`, `docs:`, `refactor:`).

---

## Lisensi

Lihat file [LICENSE](LICENSE) untuk detail lisensi penggunaan dan distribusi.
